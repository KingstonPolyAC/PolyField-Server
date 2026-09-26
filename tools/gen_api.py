#!/usr/bin/env python3
"""Generate api/polyfield-api.schema.json and the "API integration" section of
every language's manual (index.md, fr/, es/, nl/, pt/): everything from the
heading carrying {#api-integration} to the end of the page.

Prose is translated through tools/api_i18n.json ("ui" templates plus a "text"
map keyed by the English string); JSON examples and schemas are the same in
every language. The script stops and lists any string missing a translation.

The schema mirrors the Go structs in polyfield-control-server (models.go,
server.go, active_athlete.go, raza.go). Update the definitions and examples
here when the API changes, then run:

    pip install jsonschema
    python3 tools/gen_api.py

Every example is validated against the schema before anything is written.
"""
import json, os, re, sys, copy
from jsonschema import Draft202012Validator
from jsonschema.validators import validator_for

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = "https://kingstonpolyac.github.io/PolyField-Server/api/polyfield-api.schema.json"

def ref(n): return {"$ref": f"#/$defs/{n}"}
def arr(x, nullable=False):
    s = {"type": ["array", "null"] if nullable else "array", "items": x}
    return s
S = {"type": "string"}
I = {"type": "integer"}
N = {"type": "number"}
B = {"type": "boolean"}
DT = {"type": "string", "format": "date-time"}
def d(schema, desc):
    s = dict(schema); s["description"] = desc; return s
def obj(props, required=(), desc=None, extra=False):
    s = {"type": "object"}
    if desc: s["description"] = desc
    s["properties"] = props
    if required: s["required"] = list(required)
    s["additionalProperties"] = extra
    return s
def intmap(v, desc):
    return {"type": ["object", "null"], "description": desc,
            "propertyNames": {"pattern": "^[0-9]+$"}, "additionalProperties": v}
def strmap(v, desc):
    return {"type": ["object", "null"], "description": desc, "additionalProperties": v}

EVENT_TYPE = d(S, 'Event category. Known values: "Throws", "Horizontal Jumps", "Vertical Jumps".')
EVENT_TYPE["examples"] = ["Throws", "Horizontal Jumps", "Vertical Jumps"]
STATUS = {"type": "string", "enum": ["Not Started", "In Progress", "Finished"]}

defs = {
  "Error": obj({"error": d(S, "Human-readable error message.")}, ["error"],
               "Body returned with every 4xx/5xx response from the API."),
  "SuccessResponse": obj({"status": {"const": "success"},
                          "message": S}, ["status"], "Acknowledgement for a successful write."),
  "EventSummary": obj({"id": S, "name": S, "type": EVENT_TYPE}, ["id", "name", "type"],
                      "Lightweight event entry used in the event list."),
  "EventRules": obj({"attempts": d(I, "Attempts per athlete (e.g. 3, 4 or 6)."),
                     "cutEnabled": B, "cutQualifiers": I, "reorderAfterCut": B, "cutPerAgeGroup": B},
                    ["attempts", "cutEnabled", "cutQualifiers", "reorderAfterCut", "cutPerAgeGroup"],
                    "Competition format for an event."),
  "Coordinate": obj({"x": N, "y": N}, ["x", "y"], "An X/Y position in metres in the EDM frame."),
  "SectorLines": obj({"rightLine": ref("Coordinate"), "leftLine": ref("Coordinate"),
                      "sectorAngle": d(N, "Sector angle in degrees (34.92 for a standard throws sector).")},
                     ["rightLine", "leftLine", "sectorAngle"], "Sector-line geometry for a throwing circle."),
  "CalibrationMetadata": obj({
      "circleType": d(S, 'Circle / runway type, e.g. "SHOT", "DISCUS", "HAMMER", "JAVELIN_ARC".'),
      "circleRadius": d(N, "Circle radius in metres."),
      "edmPosition": ref("Coordinate"), "sectorLines": ref("SectorLines"),
      "timestamp": d(S, "When the calibration was taken (ISO 8601)."), "calibrationId": S},
      ["circleType", "circleRadius"], "Field geometry captured when the EDM was calibrated."),
  "HeatmapCoordinate": obj({
      "x": d(N, "Raw landing X in the EDM frame (m)."), "y": d(N, "Raw landing Y in the EDM frame (m)."),
      "distance": d(N, "Measured distance (m)."), "round": I, "attempt": I, "valid": B,
      "rx": d(N, "Landing X rotated so the sector centre line points up (+Y). Server-computed; only for valid throws with sector calibration."),
      "ry": d(N, "Landing Y in the rotated frame (see rx).")},
      ["x", "y", "distance", "round", "attempt", "valid"], "A throw/jump landing position."),
  "Performance": obj({
      "attempt": d(I, "Attempt number, 1-based. The server keys changes on this."),
      "mark": d(S, 'The mark. Throws / horizontal jumps: a distance in metres ("45.67"), "NM" (foul; "X" and "FOUL" are accepted and normalised to "NM") or "P" (pass; "PASS" and "-" accepted). Vertical jumps: "O" clearance, "X" failure, "P" pass.'),
      "height": d(S, 'Vertical jumps only: bar height in metres ("1.85").'),
      "unit": d(S, 'Unit of the mark, normally "m".'),
      "wind": d(S, 'Wind reading in m/s as a signed string ("+1.4", "-0.3"). Horizontal jumps only.'),
      "valid": d(B, "true for a valid mark / clearance, false for a foul, failure or pass."),
      "coordinates": ref("HeatmapCoordinate"),
      "timestamp": d(DT, "When the attempt happened. Filled with the server receipt time if omitted or zero.")},
      ["attempt", "mark"], "One attempt by an athlete. Responses always include unit, valid and timestamp."),
  "Athlete": obj({
      "bib": S, "order": d(I, "Start-list order."), "name": S, "club": S,
      "ageGroup": S, "classification": d(S, 'World Para Athletics class, e.g. "F56".'),
      "gender": d(S, '"M" or "W" (used for RAZA scoring).'), "sourceEventId": S,
      "series": arr(ref("Performance"), nullable=True),
      "heatmapCoordinates": arr(ref("HeatmapCoordinate"))},
      ["bib", "order", "name", "club", "series"], "A competitor and their series."),
  "Event": obj({
      "id": S, "name": S, "originalName": S, "type": EVENT_TYPE, "status": STATUS,
      "rules": ref("EventRules"), "athletes": arr(ref("Athlete"), nullable=True),
      "calibrationMetadata": ref("CalibrationMetadata"),
      "lastResultTime": DT,
      "signedOff": B, "signedOffBy": S, "signedOffAt": DT,
      "evtEventNumber": S, "evtRoundNumber": S, "evtHeatNumber": S,
      "opentrackUnitId": S, "opentrackEventId": S, "opentrackEventCode": S, "opentrackUrl": S,
      "athleticsAppLinkCode": S,
      "isMerged": B, "isHidden": B, "mergedEventId": S,
      "sourceEventIds": arr(S), "sourceEventNames": arr(S)},
      ["id", "name", "type", "status", "rules", "athletes"],
      "A full event: rules, athletes and every attempt. Optional fields are omitted when empty."),
  "ResultPayload": obj({
      "eventId": S, "athleteBib": S,
      "series": d(arr(ref("Performance")), "The athlete's complete series so far. It replaces the stored series."),
      "heatmapCoordinates": arr(ref("HeatmapCoordinate")),
      "calibrationMetadata": ref("CalibrationMetadata")},
      ["eventId", "athleteBib", "series"], "Body of POST /api/v1/results."),
  "EventStatusUpdate": obj({"eventId": S, "status": STATUS}, ["eventId", "status"],
                           "Body of PUT/PATCH /api/v1/events/status."),
  "ActiveAthletePayload": obj({
      "eventId": S, "athleteBib": S, "athleteName": S,
      "board": d(N, "Take-off board distance in metres (0 = long-jump board)."),
      "topPerformances": d(arr(N), "Best legal marks so far, best first. Truncated to 3.")},
      ["eventId", "athleteBib"], "Body of POST /api/v1/athlete/active."),
  "ActiveAthlete": obj({
      "eventId": S, "athleteBib": S, "athleteName": S, "board": N,
      "topPerformances": arr(N), "updatedAt": d(DT, "Server receipt time.")},
      ["eventId", "athleteBib", "athleteName", "board", "topPerformances", "updatedAt"],
      "The athlete currently up in an event."),
  "ActiveAthleteResponse": obj({"active": {"oneOf": [ref("ActiveAthlete"), {"type": "null"}]}}, ["active"],
      "Response of GET /api/v1/athlete/active/{eventId}. active is null when nobody is signalled."),
  "OkResponse": obj({"status": {"const": "ok"}}, ["status"]),
  "RecentPerformance": obj({
      "eventId": S, "eventName": S, "eventType": EVENT_TYPE, "athleteBib": S, "athleteName": S,
      "athleteClub": S, "attempt": I, "mark": S, "bestMark": S, "unit": S, "wind": S, "valid": B,
      "position": d(I, "Athlete's current position in the event."), "timestamp": DT,
      "hasHeatmap": B, "coordinates": arr(ref("HeatmapCoordinate"))},
      ["eventId", "eventName", "eventType", "athleteBib", "athleteName", "athleteClub", "attempt",
       "mark", "unit", "valid", "position", "timestamp", "hasHeatmap"],
      "One performance on the display board."),
  "RecentPerformancesResponse": obj({"performances": arr(ref("RecentPerformance"))}, ["performances"]),
  "DetailedRecentResult": obj({
      "eventId": S, "eventName": S, "eventType": EVENT_TYPE, "athleteBib": S, "athleteName": S,
      "athleteClub": S, "athleteBest": d(S, "Best mark/height so far."), "attempt": I, "mark": S,
      "height": S, "attemptsAtHeight": d(S, 'Vertical jumps: series at this height, e.g. "XO".'),
      "unit": S, "wind": S, "valid": B, "timestamp": DT,
      "sectorLines": ref("SectorLines"), "coordinates": ref("HeatmapCoordinate")},
      ["eventId", "eventName", "eventType", "athleteBib", "athleteName", "athleteClub", "athleteBest",
       "attempt", "mark", "unit", "valid", "timestamp"],
      "A result with everything needed to redraw it (broadcast / graphics)."),
  "DetailedRecentResultsResponse": obj({"results": arr(ref("DetailedRecentResult"))}, ["results"]),
  "AthleteStanding": obj({
      "position": I, "name": S, "club": S, "bestMark": S, "unit": S, "wind": S,
      "attempts": d(S, 'Vertical jumps: series at the best height, e.g. "XXO".')},
      ["position", "name", "club", "bestMark", "unit"]),
  "EventStandings": obj({"id": S, "name": S, "type": EVENT_TYPE, "athletes": arr(ref("AthleteStanding"))},
                        ["id", "name", "type", "athletes"]),
  "EventStandingsResponse": obj({"events": d(arr(ref("EventStandings"), nullable=True),
                                             "Only events with at least one valid mark. null when there are none.")},
                                ["events"]),
  "RazaRow": obj({
      "position": I, "bib": S, "name": S, "club": S, "classification": S, "gender": S,
      "sourceEvent": d(S, "Event name in the session the mark came from."),
      "mark": S, "unit": S, "razaScore": d(I, "World Para Athletics RAZA points.")},
      ["position", "bib", "name", "club", "classification", "gender", "sourceEvent", "mark", "unit", "razaScore"]),
  "RazaEventGroup": obj({"event": d(S, 'Canonical event, e.g. "Shot Put", "Long Jump".'),
                         "rows": arr(ref("RazaRow"), nullable=True)}, ["event", "rows"]),
  "RazaResponse": obj({"events": arr(ref("RazaEventGroup"), nullable=True),
                       "total": d(I, "Total number of ranked athletes.")}, ["events", "total"]),
  "TimeSeriesPoint": obj({"timestamp": DT, "value": N, "label": S}, ["timestamp", "value"]),
  "EventTimelineItem": obj({"eventId": S, "eventName": S, "startTime": DT, "endTime": DT,
                            "duration": d(N, "Minutes.")}, ["eventId", "eventName", "duration"]),
  "ThrowHeatmapData": obj({"throwType": d(S, '"HT", "DT", "JT" or "SP".'),
                           "buckets": d(arr(arr(I)), "3x4 grid: [distance zone][sector-width zone] counts."),
                           "maxCount": I, "totalThrows": I},
                          ["throwType", "buckets", "maxCount", "totalThrows"]),
  "OverallStatistics": obj({
      "totalEvents": I, "eventsNotStarted": I, "eventsInProgress": I, "eventsCompleted": I,
      "totalAthletes": I, "totalAttempts": I, "totalValidAttempts": I, "totalFouls": I,
      "overallFoulRate": d(N, "Percentage 0-100."),
      "competitionStartTime": DT, "competitionEndTime": DT,
      "totalDuration": d(N, "Minutes."), "eventsWithOpenTrack": I, "eventsWithCalibration": I,
      "eventsByType": strmap(I, "Event count per category."),
      "attemptsOverTime": arr(ref("TimeSeriesPoint"), nullable=True),
      "eventTimeline": arr(ref("EventTimelineItem"), nullable=True),
      "throwHeatmaps": strmap(ref("ThrowHeatmapData"), "Keyed by throw type code.")},
      ["totalEvents", "eventsNotStarted", "eventsInProgress", "eventsCompleted", "totalAthletes",
       "totalAttempts", "totalValidAttempts", "totalFouls", "overallFoulRate", "totalDuration",
       "eventsWithOpenTrack", "eventsWithCalibration", "eventsByType", "attemptsOverTime", "eventTimeline"],
      "Competition-wide statistics."),
  "AthleteTimingInfo": obj({"bib": S, "name": S, "competitionTime": d(N, "Minutes."),
                            "averageTimeBetween": d(N, "Seconds.")},
                           ["bib", "name", "competitionTime", "averageTimeBetween"]),
  "AthleteConsistencyInfo": obj({"bib": S, "name": S, "standardDeviation": N, "averageMark": N, "bestMark": N},
                                ["bib", "name", "standardDeviation", "averageMark", "bestMark"]),
  "WindStatistics": obj({
      "averageWind": N, "maxWind": N, "minWind": N,
      "legalAttempts": d(I, "Attempts with wind <= +2.0 m/s."),
      "windAssistedAttempts": d(I, "Attempts with wind > +2.0 m/s."),
      "bestLegalMark": S, "windByRound": intmap(N, "Round number -> average wind."),
      "windOverTime": arr(ref("TimeSeriesPoint"), nullable=True)},
      ["averageWind", "maxWind", "minWind", "legalAttempts", "windAssistedAttempts", "windByRound", "windOverTime"]),
  "HeatmapStatistics": obj({
      "attemptsLeft": I, "attemptsRight": I, "leftBiasPercent": N,
      "averageLandingAngle": d(N, "Degrees from the sector centre line."),
      "averageLandingSide": {"type": "string", "enum": ["Left", "Right", "Centre"]},
      "sectorFouls": I, "sectorFoulRate": N},
      ["attemptsLeft", "attemptsRight", "leftBiasPercent", "averageLandingAngle", "averageLandingSide",
       "sectorFouls", "sectorFoulRate"]),
  "HeightProgressionPoint": obj({"height": d(N, "Bar height (m)."), "attemptsAtHeight": I, "cleared": B},
                                ["height", "attemptsAtHeight", "cleared"]),
  "VerticalJumpStatistics": obj({
      "totalHeights": I, "startingHeight": S, "winningHeight": S, "averageIncrement": N,
      "successRateByHeight": strmap(N, "Height -> success rate."),
      "athletesPerHeight": strmap(I, "Height -> athletes attempting."),
      "mostCommonElimHeight": S,
      "heightProgression": arr(ref("HeightProgressionPoint"), nullable=True)},
      ["totalHeights", "startingHeight", "winningHeight", "averageIncrement", "successRateByHeight",
       "athletesPerHeight", "heightProgression"]),
  "PerformancePoint": obj({"timestamp": DT, "athleteName": S, "mark": N, "valid": B, "round": I, "attempt": I},
                          ["timestamp", "athleteName", "mark", "valid", "round", "attempt"]),
  "RoundComparisonPoint": obj({"round": I, "averageMark": N, "bestMark": N, "foulRate": N, "totalAttempts": I},
                              ["round", "averageMark", "bestMark", "foulRate", "totalAttempts"]),
  "AthleteRankingPoint": obj({"bib": S, "name": S, "bestMark": N, "averageMark": N, "foulRate": N,
                              "consistency": d(N, "Standard deviation; lower is better.")},
                             ["bib", "name", "bestMark", "averageMark", "foulRate", "consistency"]),
  "EventStatistics": obj({
      "eventId": S, "eventName": S, "eventType": EVENT_TYPE, "status": STATUS,
      "calibrationTime": DT, "firstAttemptTime": DT, "lastAttemptTime": DT,
      "setupDuration": d(N, "Minutes from calibration to first attempt."),
      "competitionDuration": d(N, "Minutes from first to last attempt."),
      "totalEventDuration": d(N, "Minutes from calibration to last attempt."),
      "averageTimeBetween": d(N, "Seconds between attempts."),
      "roundDurations": intmap(N, "Round -> minutes."),
      "avgTimePerAttemptByRound": intmap(N, "Round -> average minutes between attempts."),
      "timeBetweenRounds": intmap(N, "Round -> gap to the next round (minutes)."),
      "totalAthletes": I, "athletesCompleted": I, "athletesInProgress": I, "athletesNotStarted": I,
      "totalAttempts": I, "validAttempts": I, "fouls": I, "foulRate": N, "winningMark": S,
      "averageMark": N, "medianMark": N, "bestMarkPerRound": intmap(S, "Round -> best mark."),
      "foulRateByRound": intmap(N, "Round -> foul rate."), "athletesWithZeroFouls": I,
      "fastestAthlete": ref("AthleteTimingInfo"), "slowestAthlete": ref("AthleteTimingInfo"),
      "mostConsistent": ref("AthleteConsistencyInfo"),
      "windStats": d(ref("WindStatistics"), "Horizontal jumps only."),
      "heatmapStats": d(ref("HeatmapStatistics"), "Throws with landing coordinates only."),
      "verticalJumpStats": d(ref("VerticalJumpStatistics"), "High jump / pole vault only."),
      "performanceOverTime": arr(ref("PerformancePoint"), nullable=True),
      "roundComparison": arr(ref("RoundComparisonPoint"), nullable=True),
      "athleteRankings": arr(ref("AthleteRankingPoint"), nullable=True)},
      ["eventId", "eventName", "eventType", "status", "setupDuration", "competitionDuration",
       "totalEventDuration", "averageTimeBetween", "roundDurations", "avgTimePerAttemptByRound",
       "timeBetweenRounds", "totalAthletes", "athletesCompleted", "athletesInProgress", "athletesNotStarted",
       "totalAttempts", "validAttempts", "fouls", "foulRate", "averageMark", "medianMark", "bestMarkPerRound",
       "foulRateByRound", "athletesWithZeroFouls", "performanceOverTime", "roundComparison", "athleteRankings"],
      "Detailed statistics for one event."),
  "WindGauge": obj({
      "id": S, "name": S, "online": B,
      "last_reading": d(N, "Most recent wind speed along the runway (m/s)."),
      "last_crosswind": d(N, "Most recent crosswind (m/s)."),
      "last_update": DT, "hidden": d(B, "Hidden from athlete/event selection."),
      "connection_type": d(S, '"network" or "simulated".'), "ip_address": S, "port": I,
      "protocol": d(S, '"tcp" or "udp".'),
      "detected_type": d(S, 'Auto-detected data format: "gill" (Gill WindSonic) or "hd-wsd" (PolyField Wind Mini).')},
      ["id", "name", "online", "last_update", "hidden", "connection_type", "ip_address", "port", "protocol"]),
  "WindGaugesResponse": obj({"gauges": arr(ref("WindGauge"))}, ["gauges"]),
  "WindReadingResponse": obj({
      "gauge_id": S, "average_speed": d(N, "Average wind speed over the window (m/s, + = tailwind)."),
      "average_crosswind": N, "readings": d(arr(N), "The individual speeds that were averaged."),
      "timestamp": d(DT, "Reading time (RFC 3339, second precision)."),
      "direction": d(I, "Latest direction in degrees (0-360).")},
      ["gauge_id", "average_speed", "average_crosswind", "readings", "timestamp", "direction"]),
  "ConfigResponse": obj({"language": d(S, '"en", "fr", "es", "nl" or "pt".')}, ["language"]),
}

schema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": BASE,
  "title": "PolyField Server local API (v1)",
  "description": "Request and response bodies for the PolyField Server HTTP API served on port 8080 under /api/v1. Each endpoint's body is one of the definitions in $defs.",
  "$defs": defs,
}

# ---------------------------------------------------------------- examples
T0 = "2026-06-14T13:42:07.512+01:00"
calib = {"circleType": "DISCUS", "circleRadius": 1.25, "edmPosition": {"x": -12.4, "y": 3.1},
         "sectorLines": {"rightLine": {"x": 18.21, "y": 36.9}, "leftLine": {"x": -6.42, "y": 40.6}, "sectorAngle": 34.92},
         "timestamp": "2026-06-14T13:05:11Z", "calibrationId": "cal-1718366711"}
coord1 = {"x": 5.83, "y": 44.51, "distance": 44.62, "round": 1, "attempt": 1, "valid": True, "rx": 1.12, "ry": 44.61}
coord2 = {"x": 7.10, "y": 46.02, "distance": 46.38, "round": 2, "attempt": 2, "valid": True, "rx": 1.95, "ry": 46.34}
series = [
  {"attempt": 1, "mark": "44.62", "unit": "m", "valid": True, "coordinates": coord1, "timestamp": "2026-06-14T13:31:02.118+01:00"},
  {"attempt": 2, "mark": "46.38", "unit": "m", "valid": True, "coordinates": coord2, "timestamp": "2026-06-14T13:38:44.907+01:00"},
  {"attempt": 3, "mark": "NM", "unit": "m", "valid": False, "timestamp": T0},
]
event_full = {
  "id": "dt-sw-f07", "name": "Discus SW", "type": "Throws", "status": "In Progress",
  "rules": {"attempts": 6, "cutEnabled": True, "cutQualifiers": 8, "reorderAfterCut": True, "cutPerAgeGroup": False},
  "athletes": [
    {"bib": "214", "order": 1, "name": "Jane Smith", "club": "Kingston & Poly AC", "ageGroup": "SW",
     "series": series, "heatmapCoordinates": [coord1, coord2]},
    {"bib": "309", "order": 2, "name": "Amira Okafor", "club": "Herne Hill Harriers", "ageGroup": "SW",
     "series": []},
  ],
  "calibrationMetadata": calib,
  "lastResultTime": "2026-06-14T13:38:44.907+01:00",
  "opentrackEventId": "F07", "opentrackEventCode": "DT",
}
result_payload = {"eventId": "dt-sw-f07", "athleteBib": "214", "series": series,
                  "heatmapCoordinates": [coord1, coord2], "calibrationMetadata": calib}
lj_series = [
  {"attempt": 1, "mark": "5.84", "unit": "m", "wind": "+1.4", "valid": True, "timestamp": "2026-06-14T14:02:10Z"},
  {"attempt": 2, "mark": "NM", "unit": "m", "wind": "+0.8", "valid": False, "timestamp": "2026-06-14T14:11:37Z"},
]
hj_series = [
  {"attempt": 1, "mark": "O", "height": "1.60", "unit": "m", "valid": True, "timestamp": "2026-06-14T15:01:00Z"},
  {"attempt": 2, "mark": "X", "height": "1.65", "unit": "m", "valid": False, "timestamp": "2026-06-14T15:09:12Z"},
  {"attempt": 3, "mark": "O", "height": "1.65", "unit": "m", "valid": True, "timestamp": "2026-06-14T15:14:40Z"},
]
err = lambda m: {"error": m}

EP = []
def ep(**k): EP.append(k)

ep(id="list-events", method="GET", path="/api/v1/events",
   summary="List all events (summary).",
   desc="Returns every event loaded on the server as a lightweight summary. The field app uses this to offer the event picker.",
   response=("array of EventSummary", {"type": "array", "items": ref("EventSummary")},
             [{"id": "dt-sw-f07", "name": "Discus SW", "type": "Throws"},
              {"id": "lj-u17m-f03", "name": "Long Jump U17M", "type": "Horizontal Jumps"},
              {"id": "hj-u15g-f11", "name": "High Jump U15G", "type": "Vertical Jumps"}]),
   errors=[("405", "Any method other than GET.")])

ep(id="get-event", method="GET", path="/api/v1/events/{eventId}",
   summary="Get one event with its athletes and every attempt.",
   desc="Returns the full event. Used by the field app to download the start list and any results already recorded.",
   params=[("eventId", "path", "Event ID from the event list (URL-encode it).")],
   response=("Event", ref("Event"), event_full),
   errors=[("400", "No event ID in the path.", err("Event ID is required")),
           ("404", "Unknown event.", err("event with ID dt-xx not found"))])

ep(id="update-status", method="PUT or PATCH", path="/api/v1/events/status",
   summary="Set an event's status.",
   desc="Moves an event between Not Started, In Progress and Finished. The server also moves an event to In Progress automatically when its first valid result arrives.",
   request=("EventStatusUpdate", ref("EventStatusUpdate"), {"eventId": "dt-sw-f07", "status": "Finished"}),
   response=("SuccessResponse", ref("SuccessResponse"), {"status": "success", "message": "Event status updated successfully"}),
   errors=[("400", "Missing field, unknown event or invalid status.",
            err("invalid status: Done. Must be one of: Not Started, In Progress, Finished"))])

ep(id="post-results", method="POST", path="/api/v1/results",
   summary="Send an athlete's series (the field app's main write).",
   desc="Posts the athlete's **complete** series so far; it replaces what the server holds for that athlete, so resending is safe. The server works out which attempts are new or changed, updates standings and pushes an `update` to the displays. Marks are normalised: `X`/`FOUL` become `NM`, `PASS`/`-` become `P`. An out-of-range mark is logged but still stored. If the bib is not in the event a placeholder athlete is added.",
   request=("ResultPayload", ref("ResultPayload"), result_payload),
   extra_examples=[
     ("Horizontal jump with wind", "ResultPayload", {"eventId": "lj-u17m-f03", "athleteBib": "1187", "series": lj_series}),
     ("Vertical jump (one attempt per entry, with bar height)", "ResultPayload",
      {"eventId": "hj-u15g-f11", "athleteBib": "742", "series": hj_series}),
   ],
   response=("SuccessResponse", ref("SuccessResponse"), {"status": "success"}),
   errors=[("400", "Body is not valid JSON.", err("Invalid request body")),
           ("404", "Unknown event.", err("event with ID dt-xx not found"))])

ep(id="post-active", method="POST", path="/api/v1/athlete/active",
   summary="Signal who is up now (horizontal jumps).",
   desc="Fire-and-forget signal from the field app when a jumper becomes the current athlete, used by the take-off-board ruler display. One athlete per event: each post overwrites the last. It is **not** a result.",
   request=("ActiveAthletePayload", ref("ActiveAthletePayload"),
            {"eventId": "lj-u17m-f03", "athleteBib": "1187", "athleteName": "Tom Reid", "board": 0,
             "topPerformances": [5.84, 5.61]}),
   response=("OkResponse", ref("OkResponse"), {"status": "ok"}),
   errors=[("400", "Invalid JSON, or eventId / athleteBib missing.", err("eventId and athleteBib are required"))])

ep(id="get-active", method="GET", path="/api/v1/athlete/active/{eventId}",
   summary="Read who is up now in an event.",
   desc="Always 200 so a widget can poll simply; `active` is `null` when nobody has been signalled (between athletes or after a restart).",
   params=[("eventId", "path", "Event ID.")],
   response=("ActiveAthleteResponse", ref("ActiveAthleteResponse"),
             {"active": {"eventId": "lj-u17m-f03", "athleteBib": "1187", "athleteName": "Tom Reid", "board": 0,
                         "topPerformances": [5.84, 5.61], "updatedAt": "2026-06-14T14:15:03.201+01:00"}}),
   extra_examples=[("Nobody up", "ActiveAthleteResponse", {"active": None})],
   errors=[("400", "No event ID in the path.", err("Event ID is required"))])

ep(id="display-recent", method="GET", path="/api/v1/display/recent",
   summary="Latest performances (display board).",
   desc="The most recent performances, newest first. Feeds the display board at `/`.",
   params=[("limit", "query", "How many to return, 1-100. Default 4; out-of-range values fall back to 4.")],
   response=("RecentPerformancesResponse", ref("RecentPerformancesResponse"),
             {"performances": [
               {"eventId": "dt-sw-f07", "eventName": "Discus SW", "eventType": "Throws", "athleteBib": "214",
                "athleteName": "Jane Smith", "athleteClub": "Kingston & Poly AC", "attempt": 2, "mark": "46.38",
                "bestMark": "46.38", "unit": "m", "valid": True, "position": 1,
                "timestamp": "2026-06-14T13:38:44.907+01:00", "hasHeatmap": True, "coordinates": [coord1, coord2]},
               {"eventId": "lj-u17m-f03", "eventName": "Long Jump U17M", "eventType": "Horizontal Jumps",
                "athleteBib": "1187", "athleteName": "Tom Reid", "athleteClub": "Blackheath & Bromley",
                "attempt": 1, "mark": "5.84", "bestMark": "5.84", "unit": "m", "wind": "+1.4", "valid": True,
                "position": 3, "timestamp": "2026-06-14T14:02:10Z", "hasHeatmap": False}]}),
   example_url="/api/v1/display/recent?limit=2")

ep(id="display-standings", method="GET", path="/api/v1/display/standings",
   summary="Current standings for every event with marks.",
   desc="Ranked standings for each event that has at least one valid mark. Feeds the `/tables` display. `events` is `null` when no event has a valid mark yet.",
   response=("EventStandingsResponse", ref("EventStandingsResponse"),
             {"events": [
               {"id": "dt-sw-f07", "name": "Discus SW", "type": "Throws", "athletes": [
                 {"position": 1, "name": "Jane Smith", "club": "Kingston & Poly AC", "bestMark": "46.38", "unit": "m"},
                 {"position": 2, "name": "Amira Okafor", "club": "Herne Hill Harriers", "bestMark": "41.02", "unit": "m"}]},
               {"id": "hj-u15g-f11", "name": "High Jump U15G", "type": "Vertical Jumps", "athletes": [
                 {"position": 1, "name": "Ella Brooks", "club": "Kingston & Poly AC", "bestMark": "1.65",
                  "unit": "m", "attempts": "XO"}]}]}))

ep(id="broadcast-recent", method="GET", path="/api/v1/broadcast/recent",
   summary="Last 10 results in full detail (broadcast / announcer).",
   desc="Up to the 10 most recent results, newest first, with enough detail to redraw each one (sector lines, landing point, bar height and series). Feeds the `/announcer` page.",
   response=("DetailedRecentResultsResponse", ref("DetailedRecentResultsResponse"),
             {"results": [
               {"eventId": "hj-u15g-f11", "eventName": "High Jump U15G", "eventType": "Vertical Jumps",
                "athleteBib": "742", "athleteName": "Ella Brooks", "athleteClub": "Kingston & Poly AC",
                "athleteBest": "1.65", "attempt": 3, "mark": "O", "height": "1.65", "attemptsAtHeight": "XO",
                "unit": "m", "valid": True, "timestamp": "2026-06-14T15:14:40Z"},
               {"eventId": "dt-sw-f07", "eventName": "Discus SW", "eventType": "Throws", "athleteBib": "214",
                "athleteName": "Jane Smith", "athleteClub": "Kingston & Poly AC", "athleteBest": "46.38",
                "attempt": 2, "mark": "46.38", "unit": "m", "valid": True,
                "timestamp": "2026-06-14T13:38:44.907+01:00", "sectorLines": calib["sectorLines"],
                "coordinates": coord2}]}))

ep(id="raza", method="GET", path="/api/v1/raza",
   summary="RAZA para-athletics rankings.",
   desc="Athletes with a classification and gender, scored with World Para Athletics RAZA points and grouped by canonical event. Feeds the `/raza` display.",
   response=("RazaResponse", ref("RazaResponse"),
             {"events": [{"event": "Shot Put", "rows": [
               {"position": 1, "bib": "51", "name": "Sam Patel", "club": "Kingston & Poly AC", "classification": "F56",
                "gender": "M", "sourceEvent": "Shot Put Para", "mark": "9.12", "unit": "m", "razaScore": 912},
               {"position": 2, "bib": "58", "name": "Leah Ward", "club": "Windsor Slough Eton & Hounslow",
                "classification": "F37", "gender": "W", "sourceEvent": "Shot Put Para", "mark": "8.40",
                "unit": "m", "razaScore": 861}]}], "total": 2}))

ep(id="stats-overall", method="GET", path="/api/v1/statistics/overall",
   summary="Competition-wide statistics.",
   desc="Totals, timings, foul rate, attempts over time, event timeline and per-throw-type landing buckets.",
   response=("OverallStatistics", ref("OverallStatistics"),
             {"totalEvents": 12, "eventsNotStarted": 3, "eventsInProgress": 2, "eventsCompleted": 7,
              "totalAthletes": 148, "totalAttempts": 612, "totalValidAttempts": 471, "totalFouls": 141,
              "overallFoulRate": 23.04, "competitionStartTime": "2026-06-14T10:02:31+01:00",
              "competitionEndTime": "2026-06-14T15:14:40+01:00", "totalDuration": 312.15,
              "eventsWithOpenTrack": 12, "eventsWithCalibration": 5,
              "eventsByType": {"Throws": 5, "Horizontal Jumps": 4, "Vertical Jumps": 3},
              "attemptsOverTime": [{"timestamp": "2026-06-14T10:00:00+01:00", "value": 38, "label": "10:00"},
                                   {"timestamp": "2026-06-14T11:00:00+01:00", "value": 96, "label": "11:00"}],
              "eventTimeline": [{"eventId": "dt-sw-f07", "eventName": "Discus SW",
                                 "startTime": "2026-06-14T13:05:11+01:00", "endTime": "2026-06-14T14:10:02+01:00",
                                 "duration": 64.85}],
              "throwHeatmaps": {"DT": {"throwType": "DT", "buckets": [[1, 4, 3, 0], [2, 9, 7, 1], [0, 3, 2, 0]],
                                       "maxCount": 9, "totalThrows": 32}}}),
   errors=[("500", "Statistics could not be calculated.")])

ep(id="stats-event", method="GET", path="/api/v1/statistics/event/{eventId}",
   summary="Detailed statistics for one event.",
   desc="Timing, rounds, fouls, marks and chart data for one event. `windStats`, `heatmapStats` and `verticalJumpStats` appear only for the matching event type. Round-keyed maps use the round number as a string key.",
   params=[("eventId", "path", "Event ID.")],
   response=("EventStatistics", ref("EventStatistics"),
             {"eventId": "dt-sw-f07", "eventName": "Discus SW", "eventType": "Throws", "status": "Finished",
              "calibrationTime": "2026-06-14T13:05:11+01:00", "firstAttemptTime": "2026-06-14T13:31:02+01:00",
              "lastAttemptTime": "2026-06-14T14:10:02+01:00", "setupDuration": 25.85, "competitionDuration": 39.0,
              "totalEventDuration": 64.85, "averageTimeBetween": 58.5,
              "roundDurations": {"1": 7.2, "2": 6.8}, "avgTimePerAttemptByRound": {"1": 0.9, "2": 0.85},
              "timeBetweenRounds": {"1": 1.5},
              "totalAthletes": 8, "athletesCompleted": 8, "athletesInProgress": 0, "athletesNotStarted": 0,
              "totalAttempts": 40, "validAttempts": 29, "fouls": 11, "foulRate": 27.5, "winningMark": "46.38",
              "averageMark": 38.71, "medianMark": 38.2, "bestMarkPerRound": {"1": "44.62", "2": "46.38"},
              "foulRateByRound": {"1": 25.0, "2": 30.0}, "athletesWithZeroFouls": 2,
              "fastestAthlete": {"bib": "309", "name": "Amira Okafor", "competitionTime": 31.2, "averageTimeBetween": 49.1},
              "mostConsistent": {"bib": "214", "name": "Jane Smith", "standardDeviation": 0.84,
                                 "averageMark": 45.4, "bestMark": 46.38},
              "heatmapStats": {"attemptsLeft": 12, "attemptsRight": 17, "leftBiasPercent": 41.4,
                               "averageLandingAngle": 2.3, "averageLandingSide": "Right",
                               "sectorFouls": 4, "sectorFoulRate": 10.0},
              "performanceOverTime": [{"timestamp": "2026-06-14T13:31:02+01:00", "athleteName": "Jane Smith",
                                       "mark": 44.62, "valid": True, "round": 1, "attempt": 1}],
              "roundComparison": [{"round": 1, "averageMark": 37.9, "bestMark": 44.62, "foulRate": 25.0, "totalAttempts": 8}],
              "athleteRankings": [{"bib": "214", "name": "Jane Smith", "bestMark": 46.38, "averageMark": 45.4,
                                   "foulRate": 20.0, "consistency": 0.84}]}),
   errors=[("400", "No event ID in the path.", err("Event ID is required")),
           ("404", "Unknown event.", err("event with ID dt-xx not found"))])

gauge = {"id": "back-pits", "name": "Back Pits", "online": True, "last_reading": 1.3, "last_crosswind": -0.4,
         "last_update": "2026-06-14T14:15:02.004+01:00", "hidden": False, "connection_type": "network",
         "ip_address": "192.168.0.51", "port": 10001, "protocol": "tcp", "detected_type": "gill"}
ep(id="wind-gauges", method="GET", path="/api/v1/wind/gauges",
   summary="List wind gauges and their latest reading.",
   response=("WindGaugesResponse", ref("WindGaugesResponse"),
             {"gauges": [gauge, {"id": "track", "name": "Track", "online": False,
                                 "last_update": "2026-06-14T09:58:40+01:00", "hidden": True,
                                 "connection_type": "network", "ip_address": "", "port": 10003, "protocol": "udp"}]}))

wind_resp = {"gauge_id": "back-pits", "average_speed": 1.32, "average_crosswind": -0.38,
             "readings": [1.2, 1.4, 1.3, 1.3, 1.4], "timestamp": "2026-06-14T14:15:03+01:00", "direction": 184}
ep(id="wind-current", method="GET", path="/api/v1/wind/current",
   summary="Average wind now, over the last few seconds.",
   params=[("gauge_id", "query", "Required. Gauge ID from /wind/gauges."),
           ("duration", "query", "Averaging window in seconds, 1-60. Default 5.")],
   example_url="/api/v1/wind/current?gauge_id=back-pits&duration=5",
   response=("WindReadingResponse", ref("WindReadingResponse"), wind_resp),
   errors=[("400", "gauge_id missing.", err("gauge_id parameter is required")),
           ("404", "Unknown gauge.", err("Wind gauge not found")),
           ("503", "Gauge offline or no readings in the window.", err("Wind gauge is offline"))])

ep(id="wind-search", method="GET", path="/api/v1/wind/search",
   summary="Wind at a past moment (today's log).",
   desc="Finds the reading nearest the timestamp in today's stored log and averages the readings within ±2.5 s of it. Used to attach wind to a jump after the fact.",
   params=[("gauge_id", "query", "Required. Gauge ID."),
           ("timestamp", "query", "Required. RFC 3339 time, URL-encoded (e.g. `2026-06-14T14%3A02%3A10Z`).")],
   example_url="/api/v1/wind/search?gauge_id=back-pits&timestamp=2026-06-14T14%3A02%3A10Z",
   response=("WindReadingResponse", ref("WindReadingResponse"),
             dict(wind_resp, average_speed=1.4, readings=[1.3, 1.5, 1.4], timestamp="2026-06-14T14:02:10Z")),
   errors=[("400", "gauge_id or timestamp missing, or timestamp not RFC 3339.", err("Invalid timestamp format (use RFC3339)")),
           ("404", "Unknown gauge.", err("Wind gauge not found")),
           ("503", "No readings stored today.", err("No wind readings available"))])

ep(id="config", method="GET", path="/api/v1/config",
   summary="Display configuration.",
   desc="The interface language chosen in Settings, so display pages on other devices can match it.",
   response=("ConfigResponse", ref("ConfigResponse"), {"language": "en"}))

# ---------------------------------------------------------------- validate
Validator = validator_for(schema)
Validator.check_schema(schema)
def check(sub, inst, label):
    s = dict(sub); s["$defs"] = defs
    errs = list(Draft202012Validator(s, format_checker=Draft202012Validator.FORMAT_CHECKER).iter_errors(inst))
    if errs:
        for e in errs: print(label, list(e.absolute_path), e.message)
        sys.exit(1)
for e in EP:
    for key in ("request", "response"):
        if key in e: check(e[key][1], e[key][2], e["id"] + " " + key)
    for (lbl, name, ex) in e.get("extra_examples", []): check(ref(name), ex, e["id"] + " " + lbl)
    for er in e.get("errors", []):
        if len(er) > 2: check(ref("Error"), er[2], e["id"] + " error")
print("all examples valid")

# ---------------------------------------------------------------- write
os.makedirs(os.path.join(OUT, "api"), exist_ok=True)
with open(os.path.join(OUT, "api", "polyfield-api.schema.json"), "w") as f:
    json.dump(schema, f, indent=2, ensure_ascii=False); f.write("\n")

def js(x, ind=0, width=96):
    """Pretty JSON that keeps short objects/arrays on one line (Track-manual style)."""
    one = json.dumps(x, ensure_ascii=False, separators=(", ", ": "))
    flat = isinstance(x, dict) and all(not isinstance(v, (dict, list)) for v in x.values())
    if not isinstance(x, (dict, list)) or len(one) + ind <= width or (flat and len(one) + ind <= 140):
        return one.replace("{", "{ ", 1)[:-1] + " }" if isinstance(x, dict) and x else one
    pad = " " * (ind + 2)
    if isinstance(x, dict):
        items = [f'{pad}{json.dumps(k)}: {js(v, ind + 2, width)}' for k, v in x.items()]
        return "{\n" + ",\n".join(items) + "\n" + " " * ind + "}"
    items = [pad + js(v, ind + 2, width) for v in x]
    return "[\n" + ",\n".join(items) + "\n" + " " * ind + "]"
def jsschema(x): return json.dumps(x, indent=2, ensure_ascii=False)
def schema_block(name, sub):
    body = defs[name] if sub.get("$ref") == f"#/$defs/{name}" else sub
    return f'<details markdown="1"><summary>JSON Schema — <code>{name}</code></summary>\n\n```json\n{jsschema(body)}\n```\n\n</details>\n'

def tname(s):
    """Short type label for a property schema."""
    if "$ref" in s: return s["$ref"].split("/")[-1]
    if "const" in s: return json.dumps(s["const"])
    if "enum" in s: return " / ".join(json.dumps(v) for v in s["enum"])
    t = s.get("type")
    if isinstance(t, list): t = [x for x in t if x != "null"][0]
    if t == "array": return tname(s["items"]) + "[]"
    if t == "object": return "object"
    if s.get("format") == "date-time": return "date-time"
    return t

I18N = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "api_i18n.json")))
MISSING = set()

def tr(lang, text):
    """Translate an English prose string; English passes through."""
    if lang == "en" or not text: return text
    t = I18N[lang]["text"].get(text)
    if t is None: MISSING.add((lang, text)); return text
    return t

def fields(lang, name):
    """Markdown bullet list of a definition's fields, like the Track manual."""
    ui = I18N[lang]["ui"]
    dfn = defs[name]; req = set(dfn.get("required", []))
    out = []
    for k, v in dfn["properties"].items():
        desc = v.get("description", "")
        if "$ref" in v and not desc: desc = defs[tname(v)].get("description", "")
        desc = tr(lang, desc)
        opt = "" if k in req else ", " + ui["optional"]
        out.append(f"- `{k}` ({tname(v)}{opt}){' — ' + desc if desc else ''}")
    return "\n".join(out) + "\n"

def build(lang):
    ui = I18N[lang]["ui"]
    L = [ui["intro"].rstrip() + "\n\n", f'| {ui["th_method"]} | {ui["th_returns"]} |\n|---|---|\n']
    for e in EP:
        L.append(f'| [`{e["method"].replace(" or ", "/")} {e["path"]}`](#api-{e["id"]}) | {tr(lang, e["summary"])} |\n')
    L.append(f'| [`GET /api/v1/stream`](#api-stream) | {ui["stream_summary"]} |\n')

    for e in EP:
        method = e["method"].split(" ")[0]
        L.append(f'\n### `{e["method"].replace(" or ", " / ")} {e["path"]}` {{#api-{e["id"]}}}\n\n{tr(lang, e["summary"])}')
        if e.get("desc"): L.append(" " + tr(lang, e["desc"]))
        L.append("\n")
        if e.get("params"):
            L.append("\n" + "\n".join(f"- `{p[0]}` ({tr(lang, p[1])}) — {tr(lang, p[2])}" for p in e["params"]) + "\n")
        url = e.get("example_url", e["path"].replace("{eventId}", "dt-sw-f07"))
        if "request" in e:
            name, sub, ex = e["request"]
            L.append(f'\n**{ui["request_body"]} — `{name}`:**\n\n{fields(lang, name)}\n```http\n{method} {url} HTTP/1.1\nContent-Type: application/json\n\n{js(ex)}\n```\n')
            for (lbl, n2, ex2) in e.get("extra_examples", []):
                if n2 == name: L.append(f"\n*{tr(lang, lbl)}:*\n\n```json\n{js(ex2)}\n```\n")
            L.append("\n" + schema_block(name, sub))
        else:
            L.append(f"\n```http\n{method} {url}\n```\n")
        name, sub, ex = e["response"]
        if name.startswith("array of"):
            item = name.split(" ")[-1]
            L.append(f'\n**{ui["response_array"].format(item=f"`{item}`")}:**\n\n{fields(lang, item)}')
        else:
            L.append(f'\n**{ui["response"]} — `{name}`:**\n\n{fields(lang, name)}')
        L.append(f"\n```json\n{js(ex)}\n```\n")
        for (lbl, n2, ex2) in e.get("extra_examples", []):
            if n2 == name and not ("request" in e and n2 == e["request"][0]):
                L.append(f"\n*{tr(lang, lbl)}:*\n\n```json\n{js(ex2)}\n```\n")
        L.append("\n")
        if name.startswith("array of"):
            L.append(f'<details markdown="1"><summary>JSON Schema — <code>{name}</code></summary>\n\n```json\n{jsschema(sub)}\n```\n\n</details>\n')
        else:
            L.append(schema_block(name, sub))
        if e.get("errors"):
            L.append(f'\n**{ui["errors"]}**\n\n' + "\n".join(
                f"- `{er[0]}` — {tr(lang, er[1])}" + (f" `{json.dumps(er[2], ensure_ascii=False)}`" if len(er) > 2 else "")
                for er in e["errors"]) + "\n")

    L.append("\n" + ui["stream"].rstrip() + "\n\n" + ui["types_intro"].rstrip() + "\n")
    for n in ["Performance", "HeatmapCoordinate", "CalibrationMetadata", "SectorLines", "Coordinate",
              "Athlete", "EventRules", "TimeSeriesPoint", "Error"]:
        L.append(f"\n#### {n} {{#api-type-{n.lower()}}}\n\n{tr(lang, defs[n].get('description', ''))}\n\n{fields(lang, n)}\n{schema_block(n, ref(n))}")
    return "".join(L).rstrip() + "\n"

PAGES = {"en": "index.md", "fr": "fr/index.md", "es": "es/index.md", "nl": "nl/index.md", "pt": "pt/index.md"}
out = {lang: build(lang) for lang in PAGES if lang in I18N}
if MISSING:
    for lang, text in sorted(MISSING): print("MISSING", lang, json.dumps(text, ensure_ascii=False))
    sys.exit(1)
for lang, section in out.items():
    path = os.path.join(OUT, PAGES[lang])
    man = open(path).read()
    # The section runs from its heading (any language) to the end of the page.
    m = re.search(r"^## .*\{#api-integration\}", man, re.M)
    man = (man[:m.start()] if m else man.rstrip() + "\n\n") + section
    open(path, "w").write(man)
    print("written", PAGES[lang])
