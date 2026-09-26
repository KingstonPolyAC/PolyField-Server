---

layout: manual

lang: en

title: "PolyField Server — Manual"

description: "Help and user manual for PolyField Server — the field-events control server that runs the competition, live displays, wind gauges, statistics and cloud results over your venue network."

---

  

# PolyField Server

  

The field-events control server. One desktop app runs the competition on your venue network: it holds the events and athletes, receives results live from the PolyField field app, drives the live display screens, records wind, produces statistics and social-media graphics, and (optionally) publishes results to the cloud. Runs on Windows and Mac; works on a local network.

  

[Download from polyfield.co.uk](https://www.polyfield.co.uk)

  

* TOC
{:toc}

  

## Overview

  

PolyField Server is the hub of a field-events competition. It runs on one computer on your venue network and does four things at once:

  

-  **Holds the competition** — the events, age groups, athletes and every attempt, all stored locally on the host computer.

-  **Receives results** — officials measure at the circle or runway with the PolyField field app (on an Android device linked to an EDM total station or entered by hand), and the app posts each mark straight to the server.

-  **Drives the displays** — it serves a set of web pages that any screen on the network opens in a browser: a live results board, event standings, an announcer feed and para-athletics RAZA rankings.

-  **Adds analysis** — wind capture, per-event statistics and landing heatmaps, social-media graphics, and optional publishing to the PolyField cloud.

  

Everything runs on the local network — no internet is required to run a competition but is required to allow start list downloads from competition management providers and upload of real time results back to their systems. A sync is possible post-fixture to upload all results in bulk.

  

>  **Positive validation.** The server never invents results — every mark comes from an official through the field app. That keeps a clear chain from the measurement at the circle to what appears on the board.

  

## How it works

  

- You run **one instance** of the desktop app on a computer on the competition network.

- The **field app** (one per event) connects to the server, downloads the athletes for its event, and posts each attempt back as it is measured.

- Each **display screen** opens one of the server's web pages in a browser; results update instantly with no need to refresh.

- The operator works from the desktop **dashboard** — importing events, monitoring progress, exporting statistics and graphics, and managing displays and wind gauges. These are usually setup once at the start of a competition with no interaction needed through the day.

  

## Getting started

  

### 1. Load a competition

  

Open the app; the **Dashboard** is the operator's home. Start a competition one of three ways:

  

-  **Import from OpenTrack or Athletics.app** — pull the event list and start lists directly (see [Importing events](#importing-events)). This is the usual route and preserves the published start-list order.

-  **Create events manually** — use *+ Create New Event* and add athletes.

-  **New Competition** — clears the current data to start fresh.

  

Once loaded, each event appears as a card on the dashboard showing its status (Not Started, In Progress, Finished).

  

### 2. Connect the field app

  

On each field device verify the server address in the PolyField field app to connect it to the server. The official then selects their event, calibrates the EDM to the circle or runway, and starts measuring. See [Results & the field app](#results--the-field-app).

  

### 3. Open the displays

  

On each display device, open a browser at the server address and add the page you want — for example `http://polyfieldserver.local:8080/tables`. Use **Displays** on the dashboard for one-click links and scannable QR codes to every screen. See [Display screens](#display-screens).

  

>  **Tip.** Leave the desktop app on the dashboard and drive everything from there. Results flow in from the field app automatically while you keep an eye on progress and the screens.

  

![Displays popup — links and QR codes for each screen](/PolyField-Server/images/displays-popup.png)

## The dashboard

  

The dashboard lists every event and gives the main controls. Along the top is the server address (with a network selector on multi-adapter machines) and any pending upload or sync status. The key actions:

  

| Control | What it does |
|---------|--------------|
| New Competition | Clear the current competition and start fresh. |
| Create New Event | Add an event and its athletes by hand. |
| Merge Events | Combine events (e.g. two groups of the same discipline) into one, or *Merge All Same Events* to combine every matching pair at once. |
| Displays | Show clickable links and QR codes for every display page (board, standings, announcer, RAZA). |
| Export Graphics | Generate the social-media graphics, detailed heatmaps and wind graphics for the competition (see [Social-media graphics](#social-media-graphics)). |
| Export Statistics | Produce the competition statistics PDF (also on the Statistics page). |

  

Selecting an event opens its **Live Results** view, where you can see each athlete's series, watch attempts arrive, and review the standing.

  

![The PolyField Server dashboard](/PolyField-Server/images/dashboard.png)

## Importing events

  

Use **Competition Link** / import to bring in a competition rather than typing it:

  

-  **OpenTrack** — sign in and choose your competition; the server downloads the field events and their entries. The **start-list order** published by OpenTrack is preserved exactly.

-  **Athletics.app** — input the competition link code to create the events and athletes. The **start-list order** published by Athletics.app is preserved exactly.

  

Imported events keep their source numbering and codes, so they line up with the published programme and with results export.

  

![Importing a competition](/PolyField-Server/images/import-opentrack.png)

## Results & the field app

  

Results are recorded on the field, not on the server. Each event uses the PolyField field app on an Android device:

  

- The device connects to the server and downloads the athletes for the chosen event.

- For throws and horizontal jumps the app can be paired with an **EDM total station** or run directly on a PolyField Total Station (PolyField APEKS AM02i); the official calibrates to the circle/runway/boards and each measured mark (with landing coordinate) is posted to the server. Marks can also be entered by hand.

-  **Vertical jumps** (high jump, pole vault) are fully supported — heights, clearances (O/X) and the bar progression are recorded and sent.

- Every attempt carries its own timestamp, so the server shows results in the true order they happened and can produce accurate timing statistics.

  

As results arrive the event's card updates, the standings recalculate, and any connected display refreshes instantly.

  

![Live Results — results table](/PolyField-Server/images/live-results-table.png)

![Live Results — landing heatmap](/PolyField-Server/images/live-results-heatmap.png)

## Display screens

  

The server serves four live display pages. Each is a normal web page — open it in any browser on the network; nothing is installed on the display. They all update automatically: new results are pushed the moment they land, with a periodic poll as a safety net, so a screen never needs a manual refresh.

  

| Page | URL |
|------|-----|
| Display board (latest results) | `/` |
| Event standings (tables) | `/tables` |
| Announcer feed | `/announcer` |
| RAZA rankings (para-athletics) | `/raza` |

  

### Display board

  

A big-screen board of the most recent performances, with the athlete, event, mark and — for throws — a landing visualisation. Ideal as the main results screen for spectators.

  

![Display board](/PolyField-Server/images/display-board.png)

### Event standings

  

Live standings, several events at a time, each ranked with gold/silver/bronze highlights. The layout is height-aware: it fills the screen, stacks more events down tall or portrait screens, and where an event has many athletes it rotates through them page by page. Events also rotate so every event on the programme gets screen time.

  

![Event standings display](/PolyField-Server/images/display-tables.png)

### Announcer

  

A running feed of results as they arrive — the newest at the top, with position, athlete, club, event and mark — sized for an announcer or commentary position to read at a glance.

  

![Announcer feed](/PolyField-Server/images/display-announcer.png)

### RAZA rankings

  

Para-athletics rankings scored with the World Para Athletics (RAZA) points system, so athletes across different classifications can be compared on one board. Athletes need a classification and gender set for a RAZA score to be calculated.

  

![RAZA rankings display](/PolyField-Server/images/display-raza.png)

## Wind gauges

  

PolyField Server reads wind gauges over the network and records wind for the whole competition day. It supports the **Gill WindSonic 75** and the **PolyField Wind Mini**, and **detects the gauge type automatically** from its data stream — there is no protocol to choose. Add a gauge with its network address; once it streams, the server shows the detected model and begins logging.

  

- Wind is captured continuously and stored per day, so it is available for horizontal-jump legality, statistics and the wind graphics.

- The **Wind Gauges** page shows each gauge live and lets you export a full-day wind graphic.

- Gauges can be hidden from athlete selection (for example a general track gauge kept only for the record).

  

![The Wind Gauges page](/PolyField-Server/images/wind-gauges.png)

## Statistics & heatmaps

  

The **Statistics** page turns the competition data into analysis:

  

-  **Per-event charts** — performance over time, round-by-round comparison, foul rate and success, and timing between attempts.

-  **Landing heatmaps** — for throwing events, every landing plotted in the sector, coloured by round, with the average landing angle relative to the sector centre line, spread and variance.

-  **Wind** — average, legality and the trend over the session for each gauge.

-  **Export Statistics** — a full competition PDF with the charts, heatmaps and per-event summaries, dated to the day of competition.

  

The charts and heatmaps scale with the display-size setting so they stay readable on the operator screen.

  

![Statistics — landing heatmap for a throwing event](/PolyField-Server/images/statistics-heatmap.png)

## Social-media graphics

  

**Export Graphics** produces a set of square (1080×1080) images ready to post, all in one consistent PolyField style:

  

-  **Competition summary** — headline totals for the meet, with the longest throw and jump.

-  **Per-event cards** — the top three, event conditions and totals. Vertical-jump cards show each athlete's clearance series at their best height and a 1st/2nd/3rd-attempt success-rate breakdown; horizontal-jump cards show the wind.

-  **Detailed heatmaps** — the full landing scatter for each throwing event.

-  **Wind graphics** — the full-day wind trend for each gauge, with legality and gusts.

  

Graphics are produced only for events that have run, and every card carries the competition date and PolyField branding.

  

![Example exported event card](/PolyField-Server/images/social-example.png)

![Wind-gauge social graphic (exported)](/PolyField-Server/images/wind-gauges-social.png)

## Cloud results - In Trial

  

Optionally, the server publishes results to the PolyField cloud so spectators can follow along online at [results.polyfield.co.uk](https://results.polyfield.co.uk). Two things can be uploaded, each toggled in Settings:

  

-  **Athlete results & heatmaps** — individual athlete pages anonymised to reduce identifiable information stored with their marks and a landing heatmap. These will auto-delete after 90 days. 

-  **Global heatmap** — an aggregated landing picture across the competition. This is anonymised with no athlete individual data, it is held indefinitely. 

  

Uploads are queued and retried, so a brief loss of internet does not lose data — the competition itself keeps running on the local network regardless.

  

## Competition link

  

**Competition Link** is where you connect competition management providers to the server. The OpenTrack / Athletics.app import controls for loading the events.

  

![Competition Link — server address and QR code](/PolyField-Server/images/competition-link.png)

## Settings, display size & language

  

-  **Display size** — scales the operator interface, statistics charts and heatmaps to suit the screen you run the server on.

-  **Language** — the interface is available in English, French, Spanish, Dutch and Portuguese.

-  **Cloud upload** — enable or disable athlete and heatmap publishing.

-  **Directories** — set the folders used for event import, setting local PC backup folders, result and graphics export.

  

![Settings](/PolyField-Server/images/settings.png)

## Networking

  

- The app serves on **port 8080** and advertises `polyfieldserver.local`, so field devices and displays can use `http://polyfieldserver.local:8080` without the IP address. Some android devices require the full IP Address so you can also use `http://192.168.0.10:8080` replacing the 192.168.0.10 with the advertised server address in the Dashboard.

- On computers with more than one network adapter (common on Windows), pick the correct adapter at the top of the dashboard so the right address is advertised.

- All devices — field apps and displays — must be on the same network as the host computer.

  

## Diagnostics

  

If something goes wrong, use the diagnostic report. It bundles the current competition (which support can replay), the logs, and the day's wind data into a single zip, and pre-fills an email to [support@polyfield.co.uk](mailto:support@polyfield.co.uk). Attach the saved file before sending. The same bundle can be used to recover a competition if a machine has to be swapped mid-meet.

  

![Diagnostic report](/PolyField-Server/images/diagnostics.png)

## Troubleshooting

  

| Symptom | Check |
|---------|-------|
| A field device can't connect | Confirm it is on the same network, port 8080 is reachable, and (multi-adapter PCs) the right network adapter is selected at the top of the dashboard. Ensure your firewall is not blocking the PolyField Server|
| An import returns 0 events | The source competition may have no entries yet, or a different competition is selected. Re-check the competition to ensure start lists have been published. |
| A display isn't updating | The pages update themselves; if one is stale, reload it once. Confirm it is pointed at the current server address. The screens show a current time and "LIVE" text when connected to help verify.|
| A wind gauge shows no reading | Check the gauge's network address and that it is powered and streaming; the model is detected automatically once data arrives. The wind gauge will show Online or Offline status on the Server.|
| RAZA board is empty | Athletes need a classification and gender set for a RAZA score to be calculated. |
| Results look out of order or a round is missing | Each result is timestamped by the field app; make sure the field devices are on the correct event and up to date. Verify the clock on the field device and server is correct, this can drift if used offline without an update. |

  

## Download & support

  

Download the latest version from [www.polyfield.co.uk](https://www.polyfield.co.uk) or the releases page. The app checks for updates on start-up and shows a banner when a newer version is available. Support: [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

## API integration {#api-integration}

PolyField Server serves an **HTTP + JSON API** on **port 8080**, on the **same local network** as your field devices and displays. It's the same interface the PolyField field app and the built-in display screens use, so anything on the LAN — a custom scoreboard, a stats dashboard, a stream overlay, a venue's own signage — can read events, live results, standings, statistics and wind straight from the server. Responses are JSON, there is no authentication, and CORS is open, so a browser page on the LAN can call it directly. Most endpoints are read-only `GET`s; the write endpoints (`POST /api/v1/results`, `POST /api/v1/athlete/active`, `PUT /api/v1/events/status`) are used by the field app.

The API is **LAN-only by design** — the app does not expose it to the internet. **Any WAN- or internet-facing integration** (remote scoreboards, cloud services, a second venue) **should be discussed with us first** so it's done safely, typically over a VPN or a controlled reverse proxy rather than by opening the port to the world. Contact [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

**Base URL:** `http://polyfieldserver.local:8080/api/v1` — or use the server's IP address shown at the top of the dashboard (e.g. `http://192.168.0.10:8080/api/v1`).

**JSON Schema:** every request and response body is defined in one [JSON Schema (draft 2020-12) file](/PolyField-Server/api/polyfield-api.schema.json), under `$defs`. Each endpoint below names its body type and includes its schema; shared types are under [Data types](#api-data-types). To validate a body, reference its definition, e.g. `polyfield-api.schema.json#/$defs/ResultPayload`.

**Conventions**

- Errors return a 4xx/5xx status with `{"error": "message"}`. A method an endpoint doesn't accept returns `405`.
- Times are RFC 3339, e.g. `2026-06-14T13:42:07.512+01:00`.
- Marks and heights are strings in metres (`"46.38"`) so trailing zeros survive; wind is a signed string in m/s (`"+1.4"`).
- Optional fields are left out when empty. Maps keyed by round use string keys (`"1"`, `"2"`, …).

| Method & path | Returns |
|---|---|
| [`GET /api/v1/events`](#api-list-events) | List all events (summary). |
| [`GET /api/v1/events/{eventId}`](#api-get-event) | Get one event with its athletes and every attempt. |
| [`PUT/PATCH /api/v1/events/status`](#api-update-status) | Set an event's status. |
| [`POST /api/v1/results`](#api-post-results) | Send an athlete's series (the field app's main write). |
| [`POST /api/v1/athlete/active`](#api-post-active) | Signal who is up now (horizontal jumps). |
| [`GET /api/v1/athlete/active/{eventId}`](#api-get-active) | Read who is up now in an event. |
| [`GET /api/v1/display/recent`](#api-display-recent) | Latest performances (display board). |
| [`GET /api/v1/display/standings`](#api-display-standings) | Current standings for every event with marks. |
| [`GET /api/v1/broadcast/recent`](#api-broadcast-recent) | Last 10 results in full detail (broadcast / announcer). |
| [`GET /api/v1/raza`](#api-raza) | RAZA para-athletics rankings. |
| [`GET /api/v1/statistics/overall`](#api-stats-overall) | Competition-wide statistics. |
| [`GET /api/v1/statistics/event/{eventId}`](#api-stats-event) | Detailed statistics for one event. |
| [`GET /api/v1/wind/gauges`](#api-wind-gauges) | List wind gauges and their latest reading. |
| [`GET /api/v1/wind/current`](#api-wind-current) | Average wind now, over the last few seconds. |
| [`GET /api/v1/wind/search`](#api-wind-search) | Wind at a past moment (today's log). |
| [`GET /api/v1/config`](#api-config) | Display configuration. |
| [`GET /api/v1/stream`](#api-stream) | Live update notifications (Server-Sent Events). |

### `GET /api/v1/events` {#api-list-events}

List all events (summary). Returns every event loaded on the server as a lightweight summary. The field app uses this to offer the event picker.

```http
GET /api/v1/events
```

**Response — array of `EventSummary`:**

- `id` (string)
- `name` (string)
- `type` (string) — Event category. Known values: "Throws", "Horizontal Jumps", "Vertical Jumps".

```json
[
  { "id": "dt-sw-f07", "name": "Discus SW", "type": "Throws" },
  { "id": "lj-u17m-f03", "name": "Long Jump U17M", "type": "Horizontal Jumps" },
  { "id": "hj-u15g-f11", "name": "High Jump U15G", "type": "Vertical Jumps" }
]
```

<details markdown="1"><summary>JSON Schema — <code>array of EventSummary</code></summary>

```json
{
  "type": "array",
  "items": {
    "$ref": "#/$defs/EventSummary"
  }
}
```

</details>

**Errors:**

- `405` — Any method other than GET.

### `GET /api/v1/events/{eventId}` {#api-get-event}

Get one event with its athletes and every attempt. Returns the full event. Used by the field app to download the start list and any results already recorded.

- `eventId` (path) — Event ID from the event list (URL-encode it).

```http
GET /api/v1/events/dt-sw-f07
```

**Response — `Event`:**

- `id` (string)
- `name` (string)
- `originalName` (string, optional)
- `type` (string) — Event category. Known values: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `rules` (EventRules) — Competition format for an event.
- `athletes` (Athlete[])
- `calibrationMetadata` (CalibrationMetadata, optional) — Field geometry captured when the EDM was calibrated.
- `lastResultTime` (date-time, optional)
- `signedOff` (boolean, optional)
- `signedOffBy` (string, optional)
- `signedOffAt` (date-time, optional)
- `evtEventNumber` (string, optional)
- `evtRoundNumber` (string, optional)
- `evtHeatNumber` (string, optional)
- `opentrackUnitId` (string, optional)
- `opentrackEventId` (string, optional)
- `opentrackEventCode` (string, optional)
- `opentrackUrl` (string, optional)
- `athleticsAppLinkCode` (string, optional)
- `isMerged` (boolean, optional)
- `isHidden` (boolean, optional)
- `mergedEventId` (string, optional)
- `sourceEventIds` (string[], optional)
- `sourceEventNames` (string[], optional)

```json
{
  "id": "dt-sw-f07",
  "name": "Discus SW",
  "type": "Throws",
  "status": "In Progress",
  "rules": { "attempts": 6, "cutEnabled": true, "cutQualifiers": 8, "reorderAfterCut": true, "cutPerAgeGroup": false },
  "athletes": [
    {
      "bib": "214",
      "order": 1,
      "name": "Jane Smith",
      "club": "Kingston & Poly AC",
      "ageGroup": "SW",
      "series": [
        {
          "attempt": 1,
          "mark": "44.62",
          "unit": "m",
          "valid": true,
          "coordinates": { "x": 5.83, "y": 44.51, "distance": 44.62, "round": 1, "attempt": 1, "valid": true, "rx": 1.12, "ry": 44.61 },
          "timestamp": "2026-06-14T13:31:02.118+01:00"
        },
        {
          "attempt": 2,
          "mark": "46.38",
          "unit": "m",
          "valid": true,
          "coordinates": { "x": 7.1, "y": 46.02, "distance": 46.38, "round": 2, "attempt": 2, "valid": true, "rx": 1.95, "ry": 46.34 },
          "timestamp": "2026-06-14T13:38:44.907+01:00"
        },
        { "attempt": 3, "mark": "NM", "unit": "m", "valid": false, "timestamp": "2026-06-14T13:42:07.512+01:00" }
      ],
      "heatmapCoordinates": [
        { "x": 5.83, "y": 44.51, "distance": 44.62, "round": 1, "attempt": 1, "valid": true, "rx": 1.12, "ry": 44.61 },
        { "x": 7.1, "y": 46.02, "distance": 46.38, "round": 2, "attempt": 2, "valid": true, "rx": 1.95, "ry": 46.34 }
      ]
    },
    {
      "bib": "309",
      "order": 2,
      "name": "Amira Okafor",
      "club": "Herne Hill Harriers",
      "ageGroup": "SW",
      "series": []
    }
  ],
  "calibrationMetadata": {
    "circleType": "DISCUS",
    "circleRadius": 1.25,
    "edmPosition": { "x": -12.4, "y": 3.1 },
    "sectorLines": {
      "rightLine": { "x": 18.21, "y": 36.9 },
      "leftLine": { "x": -6.42, "y": 40.6 },
      "sectorAngle": 34.92
    },
    "timestamp": "2026-06-14T13:05:11Z",
    "calibrationId": "cal-1718366711"
  },
  "lastResultTime": "2026-06-14T13:38:44.907+01:00",
  "opentrackEventId": "F07",
  "opentrackEventCode": "DT"
}
```

<details markdown="1"><summary>JSON Schema — <code>Event</code></summary>

```json
{
  "type": "object",
  "description": "A full event: rules, athletes and every attempt. Optional fields are omitted when empty.",
  "properties": {
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "originalName": {
      "type": "string"
    },
    "type": {
      "type": "string",
      "description": "Event category. Known values: \"Throws\", \"Horizontal Jumps\", \"Vertical Jumps\".",
      "examples": [
        "Throws",
        "Horizontal Jumps",
        "Vertical Jumps"
      ]
    },
    "status": {
      "type": "string",
      "enum": [
        "Not Started",
        "In Progress",
        "Finished"
      ]
    },
    "rules": {
      "$ref": "#/$defs/EventRules"
    },
    "athletes": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/Athlete"
      }
    },
    "calibrationMetadata": {
      "$ref": "#/$defs/CalibrationMetadata"
    },
    "lastResultTime": {
      "type": "string",
      "format": "date-time"
    },
    "signedOff": {
      "type": "boolean"
    },
    "signedOffBy": {
      "type": "string"
    },
    "signedOffAt": {
      "type": "string",
      "format": "date-time"
    },
    "evtEventNumber": {
      "type": "string"
    },
    "evtRoundNumber": {
      "type": "string"
    },
    "evtHeatNumber": {
      "type": "string"
    },
    "opentrackUnitId": {
      "type": "string"
    },
    "opentrackEventId": {
      "type": "string"
    },
    "opentrackEventCode": {
      "type": "string"
    },
    "opentrackUrl": {
      "type": "string"
    },
    "athleticsAppLinkCode": {
      "type": "string"
    },
    "isMerged": {
      "type": "boolean"
    },
    "isHidden": {
      "type": "boolean"
    },
    "mergedEventId": {
      "type": "string"
    },
    "sourceEventIds": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "sourceEventNames": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "id",
    "name",
    "type",
    "status",
    "rules",
    "athletes"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — No event ID in the path. `{"error": "Event ID is required"}`
- `404` — Unknown event. `{"error": "event with ID dt-xx not found"}`

### `PUT / PATCH /api/v1/events/status` {#api-update-status}

Set an event's status. Moves an event between Not Started, In Progress and Finished. The server also moves an event to In Progress automatically when its first valid result arrives.

**Request body — `EventStatusUpdate`:**

- `eventId` (string)
- `status` ("Not Started" / "In Progress" / "Finished")

```http
PUT /api/v1/events/status HTTP/1.1
Content-Type: application/json

{ "eventId": "dt-sw-f07", "status": "Finished" }
```

<details markdown="1"><summary>JSON Schema — <code>EventStatusUpdate</code></summary>

```json
{
  "type": "object",
  "description": "Body of PUT/PATCH /api/v1/events/status.",
  "properties": {
    "eventId": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": [
        "Not Started",
        "In Progress",
        "Finished"
      ]
    }
  },
  "required": [
    "eventId",
    "status"
  ],
  "additionalProperties": false
}
```

</details>

**Response — `SuccessResponse`:**

- `status` ("success")
- `message` (string, optional)

```json
{ "status": "success", "message": "Event status updated successfully" }
```

<details markdown="1"><summary>JSON Schema — <code>SuccessResponse</code></summary>

```json
{
  "type": "object",
  "description": "Acknowledgement for a successful write.",
  "properties": {
    "status": {
      "const": "success"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "status"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — Missing field, unknown event or invalid status. `{"error": "invalid status: Done. Must be one of: Not Started, In Progress, Finished"}`

### `POST /api/v1/results` {#api-post-results}

Send an athlete's series (the field app's main write). Posts the athlete's **complete** series so far; it replaces what the server holds for that athlete, so resending is safe. The server works out which attempts are new or changed, updates standings and pushes an `update` to the displays. Marks are normalised: `X`/`FOUL` become `NM`, `PASS`/`-` become `P`. An out-of-range mark is logged but still stored. If the bib is not in the event a placeholder athlete is added.

**Request body — `ResultPayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `series` (Performance[]) — The athlete's complete series so far. It replaces the stored series.
- `heatmapCoordinates` (HeatmapCoordinate[], optional)
- `calibrationMetadata` (CalibrationMetadata, optional) — Field geometry captured when the EDM was calibrated.

```http
POST /api/v1/results HTTP/1.1
Content-Type: application/json

{
  "eventId": "dt-sw-f07",
  "athleteBib": "214",
  "series": [
    {
      "attempt": 1,
      "mark": "44.62",
      "unit": "m",
      "valid": true,
      "coordinates": { "x": 5.83, "y": 44.51, "distance": 44.62, "round": 1, "attempt": 1, "valid": true, "rx": 1.12, "ry": 44.61 },
      "timestamp": "2026-06-14T13:31:02.118+01:00"
    },
    {
      "attempt": 2,
      "mark": "46.38",
      "unit": "m",
      "valid": true,
      "coordinates": { "x": 7.1, "y": 46.02, "distance": 46.38, "round": 2, "attempt": 2, "valid": true, "rx": 1.95, "ry": 46.34 },
      "timestamp": "2026-06-14T13:38:44.907+01:00"
    },
    { "attempt": 3, "mark": "NM", "unit": "m", "valid": false, "timestamp": "2026-06-14T13:42:07.512+01:00" }
  ],
  "heatmapCoordinates": [
    { "x": 5.83, "y": 44.51, "distance": 44.62, "round": 1, "attempt": 1, "valid": true, "rx": 1.12, "ry": 44.61 },
    { "x": 7.1, "y": 46.02, "distance": 46.38, "round": 2, "attempt": 2, "valid": true, "rx": 1.95, "ry": 46.34 }
  ],
  "calibrationMetadata": {
    "circleType": "DISCUS",
    "circleRadius": 1.25,
    "edmPosition": { "x": -12.4, "y": 3.1 },
    "sectorLines": {
      "rightLine": { "x": 18.21, "y": 36.9 },
      "leftLine": { "x": -6.42, "y": 40.6 },
      "sectorAngle": 34.92
    },
    "timestamp": "2026-06-14T13:05:11Z",
    "calibrationId": "cal-1718366711"
  }
}
```

*Horizontal jump with wind:*

```json
{
  "eventId": "lj-u17m-f03",
  "athleteBib": "1187",
  "series": [
    { "attempt": 1, "mark": "5.84", "unit": "m", "wind": "+1.4", "valid": true, "timestamp": "2026-06-14T14:02:10Z" },
    { "attempt": 2, "mark": "NM", "unit": "m", "wind": "+0.8", "valid": false, "timestamp": "2026-06-14T14:11:37Z" }
  ]
}
```

*Vertical jump (one attempt per entry, with bar height):*

```json
{
  "eventId": "hj-u15g-f11",
  "athleteBib": "742",
  "series": [
    { "attempt": 1, "mark": "O", "height": "1.60", "unit": "m", "valid": true, "timestamp": "2026-06-14T15:01:00Z" },
    { "attempt": 2, "mark": "X", "height": "1.65", "unit": "m", "valid": false, "timestamp": "2026-06-14T15:09:12Z" },
    { "attempt": 3, "mark": "O", "height": "1.65", "unit": "m", "valid": true, "timestamp": "2026-06-14T15:14:40Z" }
  ]
}
```

<details markdown="1"><summary>JSON Schema — <code>ResultPayload</code></summary>

```json
{
  "type": "object",
  "description": "Body of POST /api/v1/results.",
  "properties": {
    "eventId": {
      "type": "string"
    },
    "athleteBib": {
      "type": "string"
    },
    "series": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/Performance"
      },
      "description": "The athlete's complete series so far. It replaces the stored series."
    },
    "heatmapCoordinates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/HeatmapCoordinate"
      }
    },
    "calibrationMetadata": {
      "$ref": "#/$defs/CalibrationMetadata"
    }
  },
  "required": [
    "eventId",
    "athleteBib",
    "series"
  ],
  "additionalProperties": false
}
```

</details>

**Response — `SuccessResponse`:**

- `status` ("success")
- `message` (string, optional)

```json
{ "status": "success" }
```

<details markdown="1"><summary>JSON Schema — <code>SuccessResponse</code></summary>

```json
{
  "type": "object",
  "description": "Acknowledgement for a successful write.",
  "properties": {
    "status": {
      "const": "success"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "status"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — Body is not valid JSON. `{"error": "Invalid request body"}`
- `404` — Unknown event. `{"error": "event with ID dt-xx not found"}`

### `POST /api/v1/athlete/active` {#api-post-active}

Signal who is up now (horizontal jumps). Fire-and-forget signal from the field app when a jumper becomes the current athlete, used by the take-off-board ruler display. One athlete per event: each post overwrites the last. It is **not** a result.

**Request body — `ActiveAthletePayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `athleteName` (string, optional)
- `board` (number, optional) — Take-off board distance in metres (0 = long-jump board).
- `topPerformances` (number[], optional) — Best legal marks so far, best first. Truncated to 3.

```http
POST /api/v1/athlete/active HTTP/1.1
Content-Type: application/json

{
  "eventId": "lj-u17m-f03",
  "athleteBib": "1187",
  "athleteName": "Tom Reid",
  "board": 0,
  "topPerformances": [5.84, 5.61]
}
```

<details markdown="1"><summary>JSON Schema — <code>ActiveAthletePayload</code></summary>

```json
{
  "type": "object",
  "description": "Body of POST /api/v1/athlete/active.",
  "properties": {
    "eventId": {
      "type": "string"
    },
    "athleteBib": {
      "type": "string"
    },
    "athleteName": {
      "type": "string"
    },
    "board": {
      "type": "number",
      "description": "Take-off board distance in metres (0 = long-jump board)."
    },
    "topPerformances": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "description": "Best legal marks so far, best first. Truncated to 3."
    }
  },
  "required": [
    "eventId",
    "athleteBib"
  ],
  "additionalProperties": false
}
```

</details>

**Response — `OkResponse`:**

- `status` ("ok")

```json
{ "status": "ok" }
```

<details markdown="1"><summary>JSON Schema — <code>OkResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "status": {
      "const": "ok"
    }
  },
  "required": [
    "status"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — Invalid JSON, or eventId / athleteBib missing. `{"error": "eventId and athleteBib are required"}`

### `GET /api/v1/athlete/active/{eventId}` {#api-get-active}

Read who is up now in an event. Always 200 so a widget can poll simply; `active` is `null` when nobody has been signalled (between athletes or after a restart).

- `eventId` (path) — Event ID.

```http
GET /api/v1/athlete/active/dt-sw-f07
```

**Response — `ActiveAthleteResponse`:**

- `active` (None)

```json
{
  "active": {
    "eventId": "lj-u17m-f03",
    "athleteBib": "1187",
    "athleteName": "Tom Reid",
    "board": 0,
    "topPerformances": [5.84, 5.61],
    "updatedAt": "2026-06-14T14:15:03.201+01:00"
  }
}
```

*Nobody up:*

```json
{ "active": null }
```

<details markdown="1"><summary>JSON Schema — <code>ActiveAthleteResponse</code></summary>

```json
{
  "type": "object",
  "description": "Response of GET /api/v1/athlete/active/{eventId}. active is null when nobody is signalled.",
  "properties": {
    "active": {
      "oneOf": [
        {
          "$ref": "#/$defs/ActiveAthlete"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "active"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — No event ID in the path. `{"error": "Event ID is required"}`

### `GET /api/v1/display/recent` {#api-display-recent}

Latest performances (display board). The most recent performances, newest first. Feeds the display board at `/`.

- `limit` (query) — How many to return, 1-100. Default 4; out-of-range values fall back to 4.

```http
GET /api/v1/display/recent?limit=2
```

**Response — `RecentPerformancesResponse`:**

- `performances` (RecentPerformance[])

```json
{
  "performances": [
    {
      "eventId": "dt-sw-f07",
      "eventName": "Discus SW",
      "eventType": "Throws",
      "athleteBib": "214",
      "athleteName": "Jane Smith",
      "athleteClub": "Kingston & Poly AC",
      "attempt": 2,
      "mark": "46.38",
      "bestMark": "46.38",
      "unit": "m",
      "valid": true,
      "position": 1,
      "timestamp": "2026-06-14T13:38:44.907+01:00",
      "hasHeatmap": true,
      "coordinates": [
        { "x": 5.83, "y": 44.51, "distance": 44.62, "round": 1, "attempt": 1, "valid": true, "rx": 1.12, "ry": 44.61 },
        { "x": 7.1, "y": 46.02, "distance": 46.38, "round": 2, "attempt": 2, "valid": true, "rx": 1.95, "ry": 46.34 }
      ]
    },
    {
      "eventId": "lj-u17m-f03",
      "eventName": "Long Jump U17M",
      "eventType": "Horizontal Jumps",
      "athleteBib": "1187",
      "athleteName": "Tom Reid",
      "athleteClub": "Blackheath & Bromley",
      "attempt": 1,
      "mark": "5.84",
      "bestMark": "5.84",
      "unit": "m",
      "wind": "+1.4",
      "valid": true,
      "position": 3,
      "timestamp": "2026-06-14T14:02:10Z",
      "hasHeatmap": false
    }
  ]
}
```

<details markdown="1"><summary>JSON Schema — <code>RecentPerformancesResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "performances": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/RecentPerformance"
      }
    }
  },
  "required": [
    "performances"
  ],
  "additionalProperties": false
}
```

</details>

### `GET /api/v1/display/standings` {#api-display-standings}

Current standings for every event with marks. Ranked standings for each event that has at least one valid mark. Feeds the `/tables` display. `events` is `null` when no event has a valid mark yet.

```http
GET /api/v1/display/standings
```

**Response — `EventStandingsResponse`:**

- `events` (EventStandings[]) — Only events with at least one valid mark. null when there are none.

```json
{
  "events": [
    {
      "id": "dt-sw-f07",
      "name": "Discus SW",
      "type": "Throws",
      "athletes": [
        { "position": 1, "name": "Jane Smith", "club": "Kingston & Poly AC", "bestMark": "46.38", "unit": "m" },
        { "position": 2, "name": "Amira Okafor", "club": "Herne Hill Harriers", "bestMark": "41.02", "unit": "m" }
      ]
    },
    {
      "id": "hj-u15g-f11",
      "name": "High Jump U15G",
      "type": "Vertical Jumps",
      "athletes": [
        { "position": 1, "name": "Ella Brooks", "club": "Kingston & Poly AC", "bestMark": "1.65", "unit": "m", "attempts": "XO" }
      ]
    }
  ]
}
```

<details markdown="1"><summary>JSON Schema — <code>EventStandingsResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "events": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/EventStandings"
      },
      "description": "Only events with at least one valid mark. null when there are none."
    }
  },
  "required": [
    "events"
  ],
  "additionalProperties": false
}
```

</details>

### `GET /api/v1/broadcast/recent` {#api-broadcast-recent}

Last 10 results in full detail (broadcast / announcer). Up to the 10 most recent results, newest first, with enough detail to redraw each one (sector lines, landing point, bar height and series). Feeds the `/announcer` page.

```http
GET /api/v1/broadcast/recent
```

**Response — `DetailedRecentResultsResponse`:**

- `results` (DetailedRecentResult[])

```json
{
  "results": [
    {
      "eventId": "hj-u15g-f11",
      "eventName": "High Jump U15G",
      "eventType": "Vertical Jumps",
      "athleteBib": "742",
      "athleteName": "Ella Brooks",
      "athleteClub": "Kingston & Poly AC",
      "athleteBest": "1.65",
      "attempt": 3,
      "mark": "O",
      "height": "1.65",
      "attemptsAtHeight": "XO",
      "unit": "m",
      "valid": true,
      "timestamp": "2026-06-14T15:14:40Z"
    },
    {
      "eventId": "dt-sw-f07",
      "eventName": "Discus SW",
      "eventType": "Throws",
      "athleteBib": "214",
      "athleteName": "Jane Smith",
      "athleteClub": "Kingston & Poly AC",
      "athleteBest": "46.38",
      "attempt": 2,
      "mark": "46.38",
      "unit": "m",
      "valid": true,
      "timestamp": "2026-06-14T13:38:44.907+01:00",
      "sectorLines": {
        "rightLine": { "x": 18.21, "y": 36.9 },
        "leftLine": { "x": -6.42, "y": 40.6 },
        "sectorAngle": 34.92
      },
      "coordinates": { "x": 7.1, "y": 46.02, "distance": 46.38, "round": 2, "attempt": 2, "valid": true, "rx": 1.95, "ry": 46.34 }
    }
  ]
}
```

<details markdown="1"><summary>JSON Schema — <code>DetailedRecentResultsResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "results": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/DetailedRecentResult"
      }
    }
  },
  "required": [
    "results"
  ],
  "additionalProperties": false
}
```

</details>

### `GET /api/v1/raza` {#api-raza}

RAZA para-athletics rankings. Athletes with a classification and gender, scored with World Para Athletics RAZA points and grouped by canonical event. Feeds the `/raza` display.

```http
GET /api/v1/raza
```

**Response — `RazaResponse`:**

- `events` (RazaEventGroup[])
- `total` (integer) — Total number of ranked athletes.

```json
{
  "events": [
    {
      "event": "Shot Put",
      "rows": [
        {
          "position": 1,
          "bib": "51",
          "name": "Sam Patel",
          "club": "Kingston & Poly AC",
          "classification": "F56",
          "gender": "M",
          "sourceEvent": "Shot Put Para",
          "mark": "9.12",
          "unit": "m",
          "razaScore": 912
        },
        {
          "position": 2,
          "bib": "58",
          "name": "Leah Ward",
          "club": "Windsor Slough Eton & Hounslow",
          "classification": "F37",
          "gender": "W",
          "sourceEvent": "Shot Put Para",
          "mark": "8.40",
          "unit": "m",
          "razaScore": 861
        }
      ]
    }
  ],
  "total": 2
}
```

<details markdown="1"><summary>JSON Schema — <code>RazaResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "events": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/RazaEventGroup"
      }
    },
    "total": {
      "type": "integer",
      "description": "Total number of ranked athletes."
    }
  },
  "required": [
    "events",
    "total"
  ],
  "additionalProperties": false
}
```

</details>

### `GET /api/v1/statistics/overall` {#api-stats-overall}

Competition-wide statistics. Totals, timings, foul rate, attempts over time, event timeline and per-throw-type landing buckets.

```http
GET /api/v1/statistics/overall
```

**Response — `OverallStatistics`:**

- `totalEvents` (integer)
- `eventsNotStarted` (integer)
- `eventsInProgress` (integer)
- `eventsCompleted` (integer)
- `totalAthletes` (integer)
- `totalAttempts` (integer)
- `totalValidAttempts` (integer)
- `totalFouls` (integer)
- `overallFoulRate` (number) — Percentage 0-100.
- `competitionStartTime` (date-time, optional)
- `competitionEndTime` (date-time, optional)
- `totalDuration` (number) — Minutes.
- `eventsWithOpenTrack` (integer)
- `eventsWithCalibration` (integer)
- `eventsByType` (object) — Event count per category.
- `attemptsOverTime` (TimeSeriesPoint[])
- `eventTimeline` (EventTimelineItem[])
- `throwHeatmaps` (object, optional) — Keyed by throw type code.

```json
{
  "totalEvents": 12,
  "eventsNotStarted": 3,
  "eventsInProgress": 2,
  "eventsCompleted": 7,
  "totalAthletes": 148,
  "totalAttempts": 612,
  "totalValidAttempts": 471,
  "totalFouls": 141,
  "overallFoulRate": 23.04,
  "competitionStartTime": "2026-06-14T10:02:31+01:00",
  "competitionEndTime": "2026-06-14T15:14:40+01:00",
  "totalDuration": 312.15,
  "eventsWithOpenTrack": 12,
  "eventsWithCalibration": 5,
  "eventsByType": { "Throws": 5, "Horizontal Jumps": 4, "Vertical Jumps": 3 },
  "attemptsOverTime": [
    { "timestamp": "2026-06-14T10:00:00+01:00", "value": 38, "label": "10:00" },
    { "timestamp": "2026-06-14T11:00:00+01:00", "value": 96, "label": "11:00" }
  ],
  "eventTimeline": [
    {
      "eventId": "dt-sw-f07",
      "eventName": "Discus SW",
      "startTime": "2026-06-14T13:05:11+01:00",
      "endTime": "2026-06-14T14:10:02+01:00",
      "duration": 64.85
    }
  ],
  "throwHeatmaps": {
    "DT": {
      "throwType": "DT",
      "buckets": [[1, 4, 3, 0], [2, 9, 7, 1], [0, 3, 2, 0]],
      "maxCount": 9,
      "totalThrows": 32
    }
  }
}
```

<details markdown="1"><summary>JSON Schema — <code>OverallStatistics</code></summary>

```json
{
  "type": "object",
  "description": "Competition-wide statistics.",
  "properties": {
    "totalEvents": {
      "type": "integer"
    },
    "eventsNotStarted": {
      "type": "integer"
    },
    "eventsInProgress": {
      "type": "integer"
    },
    "eventsCompleted": {
      "type": "integer"
    },
    "totalAthletes": {
      "type": "integer"
    },
    "totalAttempts": {
      "type": "integer"
    },
    "totalValidAttempts": {
      "type": "integer"
    },
    "totalFouls": {
      "type": "integer"
    },
    "overallFoulRate": {
      "type": "number",
      "description": "Percentage 0-100."
    },
    "competitionStartTime": {
      "type": "string",
      "format": "date-time"
    },
    "competitionEndTime": {
      "type": "string",
      "format": "date-time"
    },
    "totalDuration": {
      "type": "number",
      "description": "Minutes."
    },
    "eventsWithOpenTrack": {
      "type": "integer"
    },
    "eventsWithCalibration": {
      "type": "integer"
    },
    "eventsByType": {
      "type": [
        "object",
        "null"
      ],
      "description": "Event count per category.",
      "additionalProperties": {
        "type": "integer"
      }
    },
    "attemptsOverTime": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/TimeSeriesPoint"
      }
    },
    "eventTimeline": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/EventTimelineItem"
      }
    },
    "throwHeatmaps": {
      "type": [
        "object",
        "null"
      ],
      "description": "Keyed by throw type code.",
      "additionalProperties": {
        "$ref": "#/$defs/ThrowHeatmapData"
      }
    }
  },
  "required": [
    "totalEvents",
    "eventsNotStarted",
    "eventsInProgress",
    "eventsCompleted",
    "totalAthletes",
    "totalAttempts",
    "totalValidAttempts",
    "totalFouls",
    "overallFoulRate",
    "totalDuration",
    "eventsWithOpenTrack",
    "eventsWithCalibration",
    "eventsByType",
    "attemptsOverTime",
    "eventTimeline"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `500` — Statistics could not be calculated.

### `GET /api/v1/statistics/event/{eventId}` {#api-stats-event}

Detailed statistics for one event. Timing, rounds, fouls, marks and chart data for one event. `windStats`, `heatmapStats` and `verticalJumpStats` appear only for the matching event type. Round-keyed maps use the round number as a string key.

- `eventId` (path) — Event ID.

```http
GET /api/v1/statistics/event/dt-sw-f07
```

**Response — `EventStatistics`:**

- `eventId` (string)
- `eventName` (string)
- `eventType` (string) — Event category. Known values: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `calibrationTime` (date-time, optional)
- `firstAttemptTime` (date-time, optional)
- `lastAttemptTime` (date-time, optional)
- `setupDuration` (number) — Minutes from calibration to first attempt.
- `competitionDuration` (number) — Minutes from first to last attempt.
- `totalEventDuration` (number) — Minutes from calibration to last attempt.
- `averageTimeBetween` (number) — Seconds between attempts.
- `roundDurations` (object) — Round -> minutes.
- `avgTimePerAttemptByRound` (object) — Round -> average minutes between attempts.
- `timeBetweenRounds` (object) — Round -> gap to the next round (minutes).
- `totalAthletes` (integer)
- `athletesCompleted` (integer)
- `athletesInProgress` (integer)
- `athletesNotStarted` (integer)
- `totalAttempts` (integer)
- `validAttempts` (integer)
- `fouls` (integer)
- `foulRate` (number)
- `winningMark` (string, optional)
- `averageMark` (number)
- `medianMark` (number)
- `bestMarkPerRound` (object) — Round -> best mark.
- `foulRateByRound` (object) — Round -> foul rate.
- `athletesWithZeroFouls` (integer)
- `fastestAthlete` (AthleteTimingInfo, optional)
- `slowestAthlete` (AthleteTimingInfo, optional)
- `mostConsistent` (AthleteConsistencyInfo, optional)
- `windStats` (WindStatistics, optional) — Horizontal jumps only.
- `heatmapStats` (HeatmapStatistics, optional) — Throws with landing coordinates only.
- `verticalJumpStats` (VerticalJumpStatistics, optional) — High jump / pole vault only.
- `performanceOverTime` (PerformancePoint[])
- `roundComparison` (RoundComparisonPoint[])
- `athleteRankings` (AthleteRankingPoint[])

```json
{
  "eventId": "dt-sw-f07",
  "eventName": "Discus SW",
  "eventType": "Throws",
  "status": "Finished",
  "calibrationTime": "2026-06-14T13:05:11+01:00",
  "firstAttemptTime": "2026-06-14T13:31:02+01:00",
  "lastAttemptTime": "2026-06-14T14:10:02+01:00",
  "setupDuration": 25.85,
  "competitionDuration": 39.0,
  "totalEventDuration": 64.85,
  "averageTimeBetween": 58.5,
  "roundDurations": { "1": 7.2, "2": 6.8 },
  "avgTimePerAttemptByRound": { "1": 0.9, "2": 0.85 },
  "timeBetweenRounds": { "1": 1.5 },
  "totalAthletes": 8,
  "athletesCompleted": 8,
  "athletesInProgress": 0,
  "athletesNotStarted": 0,
  "totalAttempts": 40,
  "validAttempts": 29,
  "fouls": 11,
  "foulRate": 27.5,
  "winningMark": "46.38",
  "averageMark": 38.71,
  "medianMark": 38.2,
  "bestMarkPerRound": { "1": "44.62", "2": "46.38" },
  "foulRateByRound": { "1": 25.0, "2": 30.0 },
  "athletesWithZeroFouls": 2,
  "fastestAthlete": { "bib": "309", "name": "Amira Okafor", "competitionTime": 31.2, "averageTimeBetween": 49.1 },
  "mostConsistent": { "bib": "214", "name": "Jane Smith", "standardDeviation": 0.84, "averageMark": 45.4, "bestMark": 46.38 },
  "heatmapStats": {
    "attemptsLeft": 12,
    "attemptsRight": 17,
    "leftBiasPercent": 41.4,
    "averageLandingAngle": 2.3,
    "averageLandingSide": "Right",
    "sectorFouls": 4,
    "sectorFoulRate": 10.0
  },
  "performanceOverTime": [
    { "timestamp": "2026-06-14T13:31:02+01:00", "athleteName": "Jane Smith", "mark": 44.62, "valid": true, "round": 1, "attempt": 1 }
  ],
  "roundComparison": [{"round": 1, "averageMark": 37.9, "bestMark": 44.62, "foulRate": 25.0, "totalAttempts": 8}],
  "athleteRankings": [
    { "bib": "214", "name": "Jane Smith", "bestMark": 46.38, "averageMark": 45.4, "foulRate": 20.0, "consistency": 0.84 }
  ]
}
```

<details markdown="1"><summary>JSON Schema — <code>EventStatistics</code></summary>

```json
{
  "type": "object",
  "description": "Detailed statistics for one event.",
  "properties": {
    "eventId": {
      "type": "string"
    },
    "eventName": {
      "type": "string"
    },
    "eventType": {
      "type": "string",
      "description": "Event category. Known values: \"Throws\", \"Horizontal Jumps\", \"Vertical Jumps\".",
      "examples": [
        "Throws",
        "Horizontal Jumps",
        "Vertical Jumps"
      ]
    },
    "status": {
      "type": "string",
      "enum": [
        "Not Started",
        "In Progress",
        "Finished"
      ]
    },
    "calibrationTime": {
      "type": "string",
      "format": "date-time"
    },
    "firstAttemptTime": {
      "type": "string",
      "format": "date-time"
    },
    "lastAttemptTime": {
      "type": "string",
      "format": "date-time"
    },
    "setupDuration": {
      "type": "number",
      "description": "Minutes from calibration to first attempt."
    },
    "competitionDuration": {
      "type": "number",
      "description": "Minutes from first to last attempt."
    },
    "totalEventDuration": {
      "type": "number",
      "description": "Minutes from calibration to last attempt."
    },
    "averageTimeBetween": {
      "type": "number",
      "description": "Seconds between attempts."
    },
    "roundDurations": {
      "type": [
        "object",
        "null"
      ],
      "description": "Round -> minutes.",
      "propertyNames": {
        "pattern": "^[0-9]+$"
      },
      "additionalProperties": {
        "type": "number"
      }
    },
    "avgTimePerAttemptByRound": {
      "type": [
        "object",
        "null"
      ],
      "description": "Round -> average minutes between attempts.",
      "propertyNames": {
        "pattern": "^[0-9]+$"
      },
      "additionalProperties": {
        "type": "number"
      }
    },
    "timeBetweenRounds": {
      "type": [
        "object",
        "null"
      ],
      "description": "Round -> gap to the next round (minutes).",
      "propertyNames": {
        "pattern": "^[0-9]+$"
      },
      "additionalProperties": {
        "type": "number"
      }
    },
    "totalAthletes": {
      "type": "integer"
    },
    "athletesCompleted": {
      "type": "integer"
    },
    "athletesInProgress": {
      "type": "integer"
    },
    "athletesNotStarted": {
      "type": "integer"
    },
    "totalAttempts": {
      "type": "integer"
    },
    "validAttempts": {
      "type": "integer"
    },
    "fouls": {
      "type": "integer"
    },
    "foulRate": {
      "type": "number"
    },
    "winningMark": {
      "type": "string"
    },
    "averageMark": {
      "type": "number"
    },
    "medianMark": {
      "type": "number"
    },
    "bestMarkPerRound": {
      "type": [
        "object",
        "null"
      ],
      "description": "Round -> best mark.",
      "propertyNames": {
        "pattern": "^[0-9]+$"
      },
      "additionalProperties": {
        "type": "string"
      }
    },
    "foulRateByRound": {
      "type": [
        "object",
        "null"
      ],
      "description": "Round -> foul rate.",
      "propertyNames": {
        "pattern": "^[0-9]+$"
      },
      "additionalProperties": {
        "type": "number"
      }
    },
    "athletesWithZeroFouls": {
      "type": "integer"
    },
    "fastestAthlete": {
      "$ref": "#/$defs/AthleteTimingInfo"
    },
    "slowestAthlete": {
      "$ref": "#/$defs/AthleteTimingInfo"
    },
    "mostConsistent": {
      "$ref": "#/$defs/AthleteConsistencyInfo"
    },
    "windStats": {
      "$ref": "#/$defs/WindStatistics",
      "description": "Horizontal jumps only."
    },
    "heatmapStats": {
      "$ref": "#/$defs/HeatmapStatistics",
      "description": "Throws with landing coordinates only."
    },
    "verticalJumpStats": {
      "$ref": "#/$defs/VerticalJumpStatistics",
      "description": "High jump / pole vault only."
    },
    "performanceOverTime": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/PerformancePoint"
      }
    },
    "roundComparison": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/RoundComparisonPoint"
      }
    },
    "athleteRankings": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/AthleteRankingPoint"
      }
    }
  },
  "required": [
    "eventId",
    "eventName",
    "eventType",
    "status",
    "setupDuration",
    "competitionDuration",
    "totalEventDuration",
    "averageTimeBetween",
    "roundDurations",
    "avgTimePerAttemptByRound",
    "timeBetweenRounds",
    "totalAthletes",
    "athletesCompleted",
    "athletesInProgress",
    "athletesNotStarted",
    "totalAttempts",
    "validAttempts",
    "fouls",
    "foulRate",
    "averageMark",
    "medianMark",
    "bestMarkPerRound",
    "foulRateByRound",
    "athletesWithZeroFouls",
    "performanceOverTime",
    "roundComparison",
    "athleteRankings"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — No event ID in the path. `{"error": "Event ID is required"}`
- `404` — Unknown event. `{"error": "event with ID dt-xx not found"}`

### `GET /api/v1/wind/gauges` {#api-wind-gauges}

List wind gauges and their latest reading.

```http
GET /api/v1/wind/gauges
```

**Response — `WindGaugesResponse`:**

- `gauges` (WindGauge[])

```json
{
  "gauges": [
    {
      "id": "back-pits",
      "name": "Back Pits",
      "online": true,
      "last_reading": 1.3,
      "last_crosswind": -0.4,
      "last_update": "2026-06-14T14:15:02.004+01:00",
      "hidden": false,
      "connection_type": "network",
      "ip_address": "192.168.0.51",
      "port": 10001,
      "protocol": "tcp",
      "detected_type": "gill"
    },
    {
      "id": "track",
      "name": "Track",
      "online": false,
      "last_update": "2026-06-14T09:58:40+01:00",
      "hidden": true,
      "connection_type": "network",
      "ip_address": "",
      "port": 10003,
      "protocol": "udp"
    }
  ]
}
```

<details markdown="1"><summary>JSON Schema — <code>WindGaugesResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "gauges": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/WindGauge"
      }
    }
  },
  "required": [
    "gauges"
  ],
  "additionalProperties": false
}
```

</details>

### `GET /api/v1/wind/current` {#api-wind-current}

Average wind now, over the last few seconds.

- `gauge_id` (query) — Required. Gauge ID from /wind/gauges.
- `duration` (query) — Averaging window in seconds, 1-60. Default 5.

```http
GET /api/v1/wind/current?gauge_id=back-pits&duration=5
```

**Response — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Average wind speed over the window (m/s, + = tailwind).
- `average_crosswind` (number)
- `readings` (number[]) — The individual speeds that were averaged.
- `timestamp` (date-time) — Reading time (RFC 3339, second precision).
- `direction` (integer) — Latest direction in degrees (0-360).

```json
{
  "gauge_id": "back-pits",
  "average_speed": 1.32,
  "average_crosswind": -0.38,
  "readings": [1.2, 1.4, 1.3, 1.3, 1.4],
  "timestamp": "2026-06-14T14:15:03+01:00",
  "direction": 184
}
```

<details markdown="1"><summary>JSON Schema — <code>WindReadingResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "gauge_id": {
      "type": "string"
    },
    "average_speed": {
      "type": "number",
      "description": "Average wind speed over the window (m/s, + = tailwind)."
    },
    "average_crosswind": {
      "type": "number"
    },
    "readings": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "description": "The individual speeds that were averaged."
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Reading time (RFC 3339, second precision)."
    },
    "direction": {
      "type": "integer",
      "description": "Latest direction in degrees (0-360)."
    }
  },
  "required": [
    "gauge_id",
    "average_speed",
    "average_crosswind",
    "readings",
    "timestamp",
    "direction"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — gauge_id missing. `{"error": "gauge_id parameter is required"}`
- `404` — Unknown gauge. `{"error": "Wind gauge not found"}`
- `503` — Gauge offline or no readings in the window. `{"error": "Wind gauge is offline"}`

### `GET /api/v1/wind/search` {#api-wind-search}

Wind at a past moment (today's log). Finds the reading nearest the timestamp in today's stored log and averages the readings within ±2.5 s of it. Used to attach wind to a jump after the fact.

- `gauge_id` (query) — Required. Gauge ID.
- `timestamp` (query) — Required. RFC 3339 time, URL-encoded (e.g. `2026-06-14T14%3A02%3A10Z`).

```http
GET /api/v1/wind/search?gauge_id=back-pits&timestamp=2026-06-14T14%3A02%3A10Z
```

**Response — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Average wind speed over the window (m/s, + = tailwind).
- `average_crosswind` (number)
- `readings` (number[]) — The individual speeds that were averaged.
- `timestamp` (date-time) — Reading time (RFC 3339, second precision).
- `direction` (integer) — Latest direction in degrees (0-360).

```json
{
  "gauge_id": "back-pits",
  "average_speed": 1.4,
  "average_crosswind": -0.38,
  "readings": [1.3, 1.5, 1.4],
  "timestamp": "2026-06-14T14:02:10Z",
  "direction": 184
}
```

<details markdown="1"><summary>JSON Schema — <code>WindReadingResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "gauge_id": {
      "type": "string"
    },
    "average_speed": {
      "type": "number",
      "description": "Average wind speed over the window (m/s, + = tailwind)."
    },
    "average_crosswind": {
      "type": "number"
    },
    "readings": {
      "type": "array",
      "items": {
        "type": "number"
      },
      "description": "The individual speeds that were averaged."
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "Reading time (RFC 3339, second precision)."
    },
    "direction": {
      "type": "integer",
      "description": "Latest direction in degrees (0-360)."
    }
  },
  "required": [
    "gauge_id",
    "average_speed",
    "average_crosswind",
    "readings",
    "timestamp",
    "direction"
  ],
  "additionalProperties": false
}
```

</details>

**Errors:**

- `400` — gauge_id or timestamp missing, or timestamp not RFC 3339. `{"error": "Invalid timestamp format (use RFC3339)"}`
- `404` — Unknown gauge. `{"error": "Wind gauge not found"}`
- `503` — No readings stored today. `{"error": "No wind readings available"}`

### `GET /api/v1/config` {#api-config}

Display configuration. The interface language chosen in Settings, so display pages on other devices can match it.

```http
GET /api/v1/config
```

**Response — `ConfigResponse`:**

- `language` (string) — "en", "fr", "es", "nl" or "pt".

```json
{ "language": "en" }
```

<details markdown="1"><summary>JSON Schema — <code>ConfigResponse</code></summary>

```json
{
  "type": "object",
  "properties": {
    "language": {
      "type": "string",
      "description": "\"en\", \"fr\", \"es\", \"nl\" or \"pt\"."
    }
  },
  "required": [
    "language"
  ],
  "additionalProperties": false
}
```

</details>

### `GET /api/v1/stream` {#api-stream}

A [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) stream (`text/event-stream`). The server sends `data: update` whenever results, event status or the active athlete change — refetch whichever feed you show. A `: ping` comment every 25 seconds keeps the connection open. The message is just the word `update`, so it has no JSON Schema.

```text
: connected

data: update

: ping
```

```js
const es = new EventSource('http://polyfieldserver.local:8080/api/v1/stream');
es.onmessage = (e) => { if (e.data === 'update') refresh(); };
```

Keep a slow poll (every 30–60 s) as a fallback, as the built-in display pages do. Without the stream, poll the display feeds every 1–2 seconds; statistics only need fetching on demand.

### Data types {#api-data-types}

Types used inside several bodies above. All definitions are in the [downloadable schema](/PolyField-Server/api/polyfield-api.schema.json).

#### Performance {#api-type-performance}

One attempt by an athlete. Responses always include unit, valid and timestamp.

- `attempt` (integer) — Attempt number, 1-based. The server keys changes on this.
- `mark` (string) — The mark. Throws / horizontal jumps: a distance in metres ("45.67"), "NM" (foul; "X" and "FOUL" are accepted and normalised to "NM") or "P" (pass; "PASS" and "-" accepted). Vertical jumps: "O" clearance, "X" failure, "P" pass.
- `height` (string, optional) — Vertical jumps only: bar height in metres ("1.85").
- `unit` (string, optional) — Unit of the mark, normally "m".
- `wind` (string, optional) — Wind reading in m/s as a signed string ("+1.4", "-0.3"). Horizontal jumps only.
- `valid` (boolean, optional) — true for a valid mark / clearance, false for a foul, failure or pass.
- `coordinates` (HeatmapCoordinate, optional) — A throw/jump landing position.
- `timestamp` (date-time, optional) — When the attempt happened. Filled with the server receipt time if omitted or zero.

<details markdown="1"><summary>JSON Schema — <code>Performance</code></summary>

```json
{
  "type": "object",
  "description": "One attempt by an athlete. Responses always include unit, valid and timestamp.",
  "properties": {
    "attempt": {
      "type": "integer",
      "description": "Attempt number, 1-based. The server keys changes on this."
    },
    "mark": {
      "type": "string",
      "description": "The mark. Throws / horizontal jumps: a distance in metres (\"45.67\"), \"NM\" (foul; \"X\" and \"FOUL\" are accepted and normalised to \"NM\") or \"P\" (pass; \"PASS\" and \"-\" accepted). Vertical jumps: \"O\" clearance, \"X\" failure, \"P\" pass."
    },
    "height": {
      "type": "string",
      "description": "Vertical jumps only: bar height in metres (\"1.85\")."
    },
    "unit": {
      "type": "string",
      "description": "Unit of the mark, normally \"m\"."
    },
    "wind": {
      "type": "string",
      "description": "Wind reading in m/s as a signed string (\"+1.4\", \"-0.3\"). Horizontal jumps only."
    },
    "valid": {
      "type": "boolean",
      "description": "true for a valid mark / clearance, false for a foul, failure or pass."
    },
    "coordinates": {
      "$ref": "#/$defs/HeatmapCoordinate"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "When the attempt happened. Filled with the server receipt time if omitted or zero."
    }
  },
  "required": [
    "attempt",
    "mark"
  ],
  "additionalProperties": false
}
```

</details>

#### HeatmapCoordinate {#api-type-heatmapcoordinate}

A throw/jump landing position.

- `x` (number) — Raw landing X in the EDM frame (m).
- `y` (number) — Raw landing Y in the EDM frame (m).
- `distance` (number) — Measured distance (m).
- `round` (integer)
- `attempt` (integer)
- `valid` (boolean)
- `rx` (number, optional) — Landing X rotated so the sector centre line points up (+Y). Server-computed; only for valid throws with sector calibration.
- `ry` (number, optional) — Landing Y in the rotated frame (see rx).

<details markdown="1"><summary>JSON Schema — <code>HeatmapCoordinate</code></summary>

```json
{
  "type": "object",
  "description": "A throw/jump landing position.",
  "properties": {
    "x": {
      "type": "number",
      "description": "Raw landing X in the EDM frame (m)."
    },
    "y": {
      "type": "number",
      "description": "Raw landing Y in the EDM frame (m)."
    },
    "distance": {
      "type": "number",
      "description": "Measured distance (m)."
    },
    "round": {
      "type": "integer"
    },
    "attempt": {
      "type": "integer"
    },
    "valid": {
      "type": "boolean"
    },
    "rx": {
      "type": "number",
      "description": "Landing X rotated so the sector centre line points up (+Y). Server-computed; only for valid throws with sector calibration."
    },
    "ry": {
      "type": "number",
      "description": "Landing Y in the rotated frame (see rx)."
    }
  },
  "required": [
    "x",
    "y",
    "distance",
    "round",
    "attempt",
    "valid"
  ],
  "additionalProperties": false
}
```

</details>

#### CalibrationMetadata {#api-type-calibrationmetadata}

Field geometry captured when the EDM was calibrated.

- `circleType` (string) — Circle / runway type, e.g. "SHOT", "DISCUS", "HAMMER", "JAVELIN_ARC".
- `circleRadius` (number) — Circle radius in metres.
- `edmPosition` (Coordinate, optional) — An X/Y position in metres in the EDM frame.
- `sectorLines` (SectorLines, optional) — Sector-line geometry for a throwing circle.
- `timestamp` (string, optional) — When the calibration was taken (ISO 8601).
- `calibrationId` (string, optional)

<details markdown="1"><summary>JSON Schema — <code>CalibrationMetadata</code></summary>

```json
{
  "type": "object",
  "description": "Field geometry captured when the EDM was calibrated.",
  "properties": {
    "circleType": {
      "type": "string",
      "description": "Circle / runway type, e.g. \"SHOT\", \"DISCUS\", \"HAMMER\", \"JAVELIN_ARC\"."
    },
    "circleRadius": {
      "type": "number",
      "description": "Circle radius in metres."
    },
    "edmPosition": {
      "$ref": "#/$defs/Coordinate"
    },
    "sectorLines": {
      "$ref": "#/$defs/SectorLines"
    },
    "timestamp": {
      "type": "string",
      "description": "When the calibration was taken (ISO 8601)."
    },
    "calibrationId": {
      "type": "string"
    }
  },
  "required": [
    "circleType",
    "circleRadius"
  ],
  "additionalProperties": false
}
```

</details>

#### SectorLines {#api-type-sectorlines}

Sector-line geometry for a throwing circle.

- `rightLine` (Coordinate) — An X/Y position in metres in the EDM frame.
- `leftLine` (Coordinate) — An X/Y position in metres in the EDM frame.
- `sectorAngle` (number) — Sector angle in degrees (34.92 for a standard throws sector).

<details markdown="1"><summary>JSON Schema — <code>SectorLines</code></summary>

```json
{
  "type": "object",
  "description": "Sector-line geometry for a throwing circle.",
  "properties": {
    "rightLine": {
      "$ref": "#/$defs/Coordinate"
    },
    "leftLine": {
      "$ref": "#/$defs/Coordinate"
    },
    "sectorAngle": {
      "type": "number",
      "description": "Sector angle in degrees (34.92 for a standard throws sector)."
    }
  },
  "required": [
    "rightLine",
    "leftLine",
    "sectorAngle"
  ],
  "additionalProperties": false
}
```

</details>

#### Coordinate {#api-type-coordinate}

An X/Y position in metres in the EDM frame.

- `x` (number)
- `y` (number)

<details markdown="1"><summary>JSON Schema — <code>Coordinate</code></summary>

```json
{
  "type": "object",
  "description": "An X/Y position in metres in the EDM frame.",
  "properties": {
    "x": {
      "type": "number"
    },
    "y": {
      "type": "number"
    }
  },
  "required": [
    "x",
    "y"
  ],
  "additionalProperties": false
}
```

</details>

#### Athlete {#api-type-athlete}

A competitor and their series.

- `bib` (string)
- `order` (integer) — Start-list order.
- `name` (string)
- `club` (string)
- `ageGroup` (string, optional)
- `classification` (string, optional) — World Para Athletics class, e.g. "F56".
- `gender` (string, optional) — "M" or "W" (used for RAZA scoring).
- `sourceEventId` (string, optional)
- `series` (Performance[])
- `heatmapCoordinates` (HeatmapCoordinate[], optional)

<details markdown="1"><summary>JSON Schema — <code>Athlete</code></summary>

```json
{
  "type": "object",
  "description": "A competitor and their series.",
  "properties": {
    "bib": {
      "type": "string"
    },
    "order": {
      "type": "integer",
      "description": "Start-list order."
    },
    "name": {
      "type": "string"
    },
    "club": {
      "type": "string"
    },
    "ageGroup": {
      "type": "string"
    },
    "classification": {
      "type": "string",
      "description": "World Para Athletics class, e.g. \"F56\"."
    },
    "gender": {
      "type": "string",
      "description": "\"M\" or \"W\" (used for RAZA scoring)."
    },
    "sourceEventId": {
      "type": "string"
    },
    "series": {
      "type": [
        "array",
        "null"
      ],
      "items": {
        "$ref": "#/$defs/Performance"
      }
    },
    "heatmapCoordinates": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/HeatmapCoordinate"
      }
    }
  },
  "required": [
    "bib",
    "order",
    "name",
    "club",
    "series"
  ],
  "additionalProperties": false
}
```

</details>

#### EventRules {#api-type-eventrules}

Competition format for an event.

- `attempts` (integer) — Attempts per athlete (e.g. 3, 4 or 6).
- `cutEnabled` (boolean)
- `cutQualifiers` (integer)
- `reorderAfterCut` (boolean)
- `cutPerAgeGroup` (boolean)

<details markdown="1"><summary>JSON Schema — <code>EventRules</code></summary>

```json
{
  "type": "object",
  "description": "Competition format for an event.",
  "properties": {
    "attempts": {
      "type": "integer",
      "description": "Attempts per athlete (e.g. 3, 4 or 6)."
    },
    "cutEnabled": {
      "type": "boolean"
    },
    "cutQualifiers": {
      "type": "integer"
    },
    "reorderAfterCut": {
      "type": "boolean"
    },
    "cutPerAgeGroup": {
      "type": "boolean"
    }
  },
  "required": [
    "attempts",
    "cutEnabled",
    "cutQualifiers",
    "reorderAfterCut",
    "cutPerAgeGroup"
  ],
  "additionalProperties": false
}
```

</details>

#### TimeSeriesPoint {#api-type-timeseriespoint}



- `timestamp` (date-time)
- `value` (number)
- `label` (string, optional)

<details markdown="1"><summary>JSON Schema — <code>TimeSeriesPoint</code></summary>

```json
{
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "value": {
      "type": "number"
    },
    "label": {
      "type": "string"
    }
  },
  "required": [
    "timestamp",
    "value"
  ],
  "additionalProperties": false
}
```

</details>

#### Error {#api-type-error}

Body returned with every 4xx/5xx response from the API.

- `error` (string) — Human-readable error message.

<details markdown="1"><summary>JSON Schema — <code>Error</code></summary>

```json
{
  "type": "object",
  "description": "Body returned with every 4xx/5xx response from the API.",
  "properties": {
    "error": {
      "type": "string",
      "description": "Human-readable error message."
    }
  },
  "required": [
    "error"
  ],
  "additionalProperties": false
}
```

</details>
