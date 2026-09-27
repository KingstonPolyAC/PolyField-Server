---
layout: manual
lang: en
title: "PolyField Server — API reference"
description: "HTTP API reference for PolyField Server: every endpoint with request and response examples and JSON Schema."
---

# API reference

PolyField Server exposes a small HTTP API on the venue network. The PolyField field app, the display screens and any third-party tool (scoreboards, graphics, broadcast overlays) all use the same endpoints. This page lists every endpoint with a request and response example and the JSON Schema of each body.

[← Back to the manual](/PolyField-Server/) · [Download the full JSON Schema](/PolyField-Server/api/polyfield-api.schema.json)

* TOC
{:toc}

## Conventions

- **Base URL** — `http://polyfieldserver.local:8080` (or the server's IP address, e.g. `http://192.168.0.10:8080`). All API paths start with `/api/v1`.
- **Format** — requests and responses are JSON (`Content-Type: application/json`), UTF-8. The only exception is the live update stream, which is Server-Sent Events.
- **Authentication** — none. The API is meant for the local competition network only; keep the server off public networks.
- **CORS** — every response allows any origin (`Access-Control-Allow-Origin: *`), so browser pages on other hosts can call the API.
- **Methods** — each endpoint accepts only the method(s) shown; anything else returns `405` with an error body.
- **Errors** — every error is `{"error": "message"}` with a 4xx/5xx status (schema: `Error`).
- **Times** — RFC 3339 / ISO 8601 date-times, e.g. `2026-06-14T13:42:07.512+01:00`.
- **Marks** — marks and heights are strings in metres (`"46.38"`), so trailing zeros survive. Wind is a signed string in m/s (`"+1.4"`).
- **Optional fields** — fields not in a schema's `required` list are left out of the response when empty. Lists that are empty may come back as `null` where the schema says `["array", "null"]`.
- **Maps keyed by round** — JSON object keys are always strings, so round numbers appear as `"1"`, `"2"`, …

### The JSON Schema

All bodies are defined once in a single [JSON Schema (draft 2020-12)](/PolyField-Server/api/polyfield-api.schema.json) file, under `$defs`. Each endpoint below names the definition it uses and shows it in a collapsible block. To validate a body, reference the definition directly, for example `https://kingstonpolyac.github.io/PolyField-Server/api/polyfield-api.schema.json#/$defs/ResultPayload`. Shared objects such as `Performance`, `Athlete` and `HeatmapCoordinate` are listed under [Shared definitions](#shared-definitions).

## Endpoint summary

| Method | Path | Purpose | Body schema |
|--------|------|---------|-------------|
| GET | [`/api/v1/events`](#list-events) | List all events (summary). | out: `array of EventSummary` |
| GET | [`/api/v1/events/{eventId}`](#get-event) | Get one event with its athletes and every attempt. | out: `Event` |
| PUT or PATCH | [`/api/v1/events/status`](#update-status) | Set an event's status. | in: `EventStatusUpdate`<br>out: `SuccessResponse` |
| POST | [`/api/v1/results`](#post-results) | Send an athlete's series (the field app's main write). | in: `ResultPayload`<br>out: `SuccessResponse` |
| POST | [`/api/v1/athlete/active`](#post-active) | Signal who is up now (horizontal jumps). | in: `ActiveAthletePayload`<br>out: `OkResponse` |
| GET | [`/api/v1/athlete/active/{eventId}`](#get-active) | Read who is up now in an event. | out: `ActiveAthleteResponse` |
| GET | [`/api/v1/display/recent`](#display-recent) | Latest performances (display board). | out: `RecentPerformancesResponse` |
| GET | [`/api/v1/display/standings`](#display-standings) | Current standings for every event with marks. | out: `EventStandingsResponse` |
| GET | [`/api/v1/broadcast/recent`](#broadcast-recent) | Last 10 results in full detail (broadcast / announcer). | out: `DetailedRecentResultsResponse` |
| GET | [`/api/v1/raza`](#raza) | RAZA para-athletics rankings. | out: `RazaResponse` |
| GET | [`/api/v1/statistics/overall`](#stats-overall) | Competition-wide statistics. | out: `OverallStatistics` |
| GET | [`/api/v1/statistics/event/{eventId}`](#stats-event) | Detailed statistics for one event. | out: `EventStatistics` |
| GET | [`/api/v1/wind/gauges`](#wind-gauges) | List wind gauges and their latest reading. | out: `WindGaugesResponse` |
| GET | [`/api/v1/wind/current`](#wind-current) | Average wind now, over the last few seconds. | out: `WindReadingResponse` |
| GET | [`/api/v1/wind/search`](#wind-search) | Wind at a past moment (today's log). | out: `WindReadingResponse` |
| GET | [`/api/v1/config`](#config) | Display configuration. | out: `ConfigResponse` |
| GET | [`/api/v1/stream`](#stream) | Live update notifications (Server-Sent Events). | text/event-stream |

## Events & results

### GET /api/v1/events
{: #list-events}

List all events (summary). Returns every event loaded on the server as a lightweight summary. The field app uses this to offer the event picker.

**Request**

```http
GET /api/v1/events HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `array of EventSummary`

```json
[
  {
    "id": "dt-sw-f07",
    "name": "Discus SW",
    "type": "Throws"
  },
  {
    "id": "lj-u17m-f03",
    "name": "Long Jump U17M",
    "type": "Horizontal Jumps"
  },
  {
    "id": "hj-u15g-f11",
    "name": "High Jump U15G",
    "type": "Vertical Jumps"
  }
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 405 | Any method other than GET. |  |

### GET /api/v1/events/{eventId}
{: #get-event}

Get one event with its athletes and every attempt. Returns the full event. Used by the field app to download the start list and any results already recorded.

| Parameter | In | Description |
|-----------|----|-------------|
| `eventId` | path | Event ID from the event list (URL-encode it). |

**Request**

```http
GET /api/v1/events/dt-sw-f07 HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `Event`

```json
{
  "id": "dt-sw-f07",
  "name": "Discus SW",
  "type": "Throws",
  "status": "In Progress",
  "rules": {
    "attempts": 6,
    "cutEnabled": true,
    "cutQualifiers": 8,
    "reorderAfterCut": true,
    "cutPerAgeGroup": false
  },
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
          "coordinates": {
            "x": 5.83,
            "y": 44.51,
            "distance": 44.62,
            "round": 1,
            "attempt": 1,
            "valid": true,
            "rx": 1.12,
            "ry": 44.61
          },
          "timestamp": "2026-06-14T13:31:02.118+01:00"
        },
        {
          "attempt": 2,
          "mark": "46.38",
          "unit": "m",
          "valid": true,
          "coordinates": {
            "x": 7.1,
            "y": 46.02,
            "distance": 46.38,
            "round": 2,
            "attempt": 2,
            "valid": true,
            "rx": 1.95,
            "ry": 46.34
          },
          "timestamp": "2026-06-14T13:38:44.907+01:00"
        },
        {
          "attempt": 3,
          "mark": "NM",
          "unit": "m",
          "valid": false,
          "timestamp": "2026-06-14T13:42:07.512+01:00"
        }
      ],
      "heatmapCoordinates": [
        {
          "x": 5.83,
          "y": 44.51,
          "distance": 44.62,
          "round": 1,
          "attempt": 1,
          "valid": true,
          "rx": 1.12,
          "ry": 44.61
        },
        {
          "x": 7.1,
          "y": 46.02,
          "distance": 46.38,
          "round": 2,
          "attempt": 2,
          "valid": true,
          "rx": 1.95,
          "ry": 46.34
        }
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
    "edmPosition": {
      "x": -12.4,
      "y": 3.1
    },
    "sectorLines": {
      "rightLine": {
        "x": 18.21,
        "y": 36.9
      },
      "leftLine": {
        "x": -6.42,
        "y": 40.6
      },
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | No event ID in the path. | `{"error": "Event ID is required"}` |
| 404 | Unknown event. | `{"error": "event with ID dt-xx not found"}` |

### PUT or PATCH /api/v1/events/status
{: #update-status}

Set an event's status. Moves an event between Not Started, In Progress and Finished. The server also moves an event to In Progress automatically when its first valid result arrives.

**Request** — body: `EventStatusUpdate`

```http
PUT /api/v1/events/status HTTP/1.1
Host: polyfieldserver.local:8080
Content-Type: application/json

{
  "eventId": "dt-sw-f07",
  "status": "Finished"
}
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

**Response** `200 OK` — body: `SuccessResponse`

```json
{
  "status": "success",
  "message": "Event status updated successfully"
}
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | Missing field, unknown event or invalid status. | `{"error": "invalid status: Done. Must be one of: Not Started, In Progress, Finished"}` |

### POST /api/v1/results
{: #post-results}

Send an athlete's series (the field app's main write). Posts the athlete's **complete** series so far; it replaces what the server holds for that athlete, so resending is safe. The server works out which attempts are new or changed, updates standings and pushes an `update` to the displays. Marks are normalised: `X`/`FOUL` become `NM`, `PASS`/`-` become `P`. An out-of-range mark is logged but still stored. If the bib is not in the event a placeholder athlete is added.

**Request** — body: `ResultPayload`

```http
POST /api/v1/results HTTP/1.1
Host: polyfieldserver.local:8080
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
      "coordinates": {
        "x": 5.83,
        "y": 44.51,
        "distance": 44.62,
        "round": 1,
        "attempt": 1,
        "valid": true,
        "rx": 1.12,
        "ry": 44.61
      },
      "timestamp": "2026-06-14T13:31:02.118+01:00"
    },
    {
      "attempt": 2,
      "mark": "46.38",
      "unit": "m",
      "valid": true,
      "coordinates": {
        "x": 7.1,
        "y": 46.02,
        "distance": 46.38,
        "round": 2,
        "attempt": 2,
        "valid": true,
        "rx": 1.95,
        "ry": 46.34
      },
      "timestamp": "2026-06-14T13:38:44.907+01:00"
    },
    {
      "attempt": 3,
      "mark": "NM",
      "unit": "m",
      "valid": false,
      "timestamp": "2026-06-14T13:42:07.512+01:00"
    }
  ],
  "heatmapCoordinates": [
    {
      "x": 5.83,
      "y": 44.51,
      "distance": 44.62,
      "round": 1,
      "attempt": 1,
      "valid": true,
      "rx": 1.12,
      "ry": 44.61
    },
    {
      "x": 7.1,
      "y": 46.02,
      "distance": 46.38,
      "round": 2,
      "attempt": 2,
      "valid": true,
      "rx": 1.95,
      "ry": 46.34
    }
  ],
  "calibrationMetadata": {
    "circleType": "DISCUS",
    "circleRadius": 1.25,
    "edmPosition": {
      "x": -12.4,
      "y": 3.1
    },
    "sectorLines": {
      "rightLine": {
        "x": 18.21,
        "y": 36.9
      },
      "leftLine": {
        "x": -6.42,
        "y": 40.6
      },
      "sectorAngle": 34.92
    },
    "timestamp": "2026-06-14T13:05:11Z",
    "calibrationId": "cal-1718366711"
  }
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

*Example — Horizontal jump with wind:*

```json
{
  "eventId": "lj-u17m-f03",
  "athleteBib": "1187",
  "series": [
    {
      "attempt": 1,
      "mark": "5.84",
      "unit": "m",
      "wind": "+1.4",
      "valid": true,
      "timestamp": "2026-06-14T14:02:10Z"
    },
    {
      "attempt": 2,
      "mark": "NM",
      "unit": "m",
      "wind": "+0.8",
      "valid": false,
      "timestamp": "2026-06-14T14:11:37Z"
    }
  ]
}
```

*Example — Vertical jump (one attempt per entry, with bar height):*

```json
{
  "eventId": "hj-u15g-f11",
  "athleteBib": "742",
  "series": [
    {
      "attempt": 1,
      "mark": "O",
      "height": "1.60",
      "unit": "m",
      "valid": true,
      "timestamp": "2026-06-14T15:01:00Z"
    },
    {
      "attempt": 2,
      "mark": "X",
      "height": "1.65",
      "unit": "m",
      "valid": false,
      "timestamp": "2026-06-14T15:09:12Z"
    },
    {
      "attempt": 3,
      "mark": "O",
      "height": "1.65",
      "unit": "m",
      "valid": true,
      "timestamp": "2026-06-14T15:14:40Z"
    }
  ]
}
```

**Response** `200 OK` — body: `SuccessResponse`

```json
{
  "status": "success"
}
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | Body is not valid JSON. | `{"error": "Invalid request body"}` |
| 404 | Unknown event. | `{"error": "event with ID dt-xx not found"}` |

### POST /api/v1/athlete/active
{: #post-active}

Signal who is up now (horizontal jumps). Fire-and-forget signal from the field app when a jumper becomes the current athlete, used by the take-off-board ruler display. One athlete per event: each post overwrites the last. It is **not** a result.

**Request** — body: `ActiveAthletePayload`

```http
POST /api/v1/athlete/active HTTP/1.1
Host: polyfieldserver.local:8080
Content-Type: application/json

{
  "eventId": "lj-u17m-f03",
  "athleteBib": "1187",
  "athleteName": "Tom Reid",
  "board": 0,
  "topPerformances": [
    5.84,
    5.61
  ]
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

**Response** `200 OK` — body: `OkResponse`

```json
{
  "status": "ok"
}
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | Invalid JSON, or eventId / athleteBib missing. | `{"error": "eventId and athleteBib are required"}` |

### GET /api/v1/athlete/active/{eventId}
{: #get-active}

Read who is up now in an event. Always 200 so a widget can poll simply; `active` is `null` when nobody has been signalled (between athletes or after a restart).

| Parameter | In | Description |
|-----------|----|-------------|
| `eventId` | path | Event ID. |

**Request**

```http
GET /api/v1/athlete/active/dt-sw-f07 HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `ActiveAthleteResponse`

```json
{
  "active": {
    "eventId": "lj-u17m-f03",
    "athleteBib": "1187",
    "athleteName": "Tom Reid",
    "board": 0,
    "topPerformances": [
      5.84,
      5.61
    ],
    "updatedAt": "2026-06-14T14:15:03.201+01:00"
  }
}
```

*Example — Nobody up:*

```json
{
  "active": null
}
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | No event ID in the path. | `{"error": "Event ID is required"}` |

## Display feeds

### GET /api/v1/display/recent
{: #display-recent}

Latest performances (display board). The most recent performances, newest first. Feeds the display board at `/`.

| Parameter | In | Description |
|-----------|----|-------------|
| `limit` | query | How many to return, 1-100. Default 4; out-of-range values fall back to 4. |

**Request**

```http
GET /api/v1/display/recent?limit=2 HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `RecentPerformancesResponse`

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
        {
          "x": 5.83,
          "y": 44.51,
          "distance": 44.62,
          "round": 1,
          "attempt": 1,
          "valid": true,
          "rx": 1.12,
          "ry": 44.61
        },
        {
          "x": 7.1,
          "y": 46.02,
          "distance": 46.38,
          "round": 2,
          "attempt": 2,
          "valid": true,
          "rx": 1.95,
          "ry": 46.34
        }
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

### GET /api/v1/display/standings
{: #display-standings}

Current standings for every event with marks. Ranked standings for each event that has at least one valid mark. Feeds the `/tables` display. `events` is `null` when no event has a valid mark yet.

**Request**

```http
GET /api/v1/display/standings HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `EventStandingsResponse`

```json
{
  "events": [
    {
      "id": "dt-sw-f07",
      "name": "Discus SW",
      "type": "Throws",
      "athletes": [
        {
          "position": 1,
          "name": "Jane Smith",
          "club": "Kingston & Poly AC",
          "bestMark": "46.38",
          "unit": "m"
        },
        {
          "position": 2,
          "name": "Amira Okafor",
          "club": "Herne Hill Harriers",
          "bestMark": "41.02",
          "unit": "m"
        }
      ]
    },
    {
      "id": "hj-u15g-f11",
      "name": "High Jump U15G",
      "type": "Vertical Jumps",
      "athletes": [
        {
          "position": 1,
          "name": "Ella Brooks",
          "club": "Kingston & Poly AC",
          "bestMark": "1.65",
          "unit": "m",
          "attempts": "XO"
        }
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

### GET /api/v1/broadcast/recent
{: #broadcast-recent}

Last 10 results in full detail (broadcast / announcer). Up to the 10 most recent results, newest first, with enough detail to redraw each one (sector lines, landing point, bar height and series). Feeds the `/announcer` page.

**Request**

```http
GET /api/v1/broadcast/recent HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `DetailedRecentResultsResponse`

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
        "rightLine": {
          "x": 18.21,
          "y": 36.9
        },
        "leftLine": {
          "x": -6.42,
          "y": 40.6
        },
        "sectorAngle": 34.92
      },
      "coordinates": {
        "x": 7.1,
        "y": 46.02,
        "distance": 46.38,
        "round": 2,
        "attempt": 2,
        "valid": true,
        "rx": 1.95,
        "ry": 46.34
      }
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

### GET /api/v1/raza
{: #raza}

RAZA para-athletics rankings. Athletes with a classification and gender, scored with World Para Athletics RAZA points and grouped by canonical event. Feeds the `/raza` display.

**Request**

```http
GET /api/v1/raza HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `RazaResponse`

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

### GET /api/v1/config
{: #config}

Display configuration. The interface language chosen in Settings, so display pages on other devices can match it.

**Request**

```http
GET /api/v1/config HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `ConfigResponse`

```json
{
  "language": "en"
}
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

## Statistics

### GET /api/v1/statistics/overall
{: #stats-overall}

Competition-wide statistics. Totals, timings, foul rate, attempts over time, event timeline and per-throw-type landing buckets.

**Request**

```http
GET /api/v1/statistics/overall HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `OverallStatistics`

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
  "eventsByType": {
    "Throws": 5,
    "Horizontal Jumps": 4,
    "Vertical Jumps": 3
  },
  "attemptsOverTime": [
    {
      "timestamp": "2026-06-14T10:00:00+01:00",
      "value": 38,
      "label": "10:00"
    },
    {
      "timestamp": "2026-06-14T11:00:00+01:00",
      "value": 96,
      "label": "11:00"
    }
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
      "buckets": [
        [
          1,
          4,
          3,
          0
        ],
        [
          2,
          9,
          7,
          1
        ],
        [
          0,
          3,
          2,
          0
        ]
      ],
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 500 | Statistics could not be calculated. |  |

### GET /api/v1/statistics/event/{eventId}
{: #stats-event}

Detailed statistics for one event. Timing, rounds, fouls, marks and chart data for one event. `windStats`, `heatmapStats` and `verticalJumpStats` appear only for the matching event type. Round-keyed maps use the round number as a string key.

| Parameter | In | Description |
|-----------|----|-------------|
| `eventId` | path | Event ID. |

**Request**

```http
GET /api/v1/statistics/event/dt-sw-f07 HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `EventStatistics`

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
  "roundDurations": {
    "1": 7.2,
    "2": 6.8
  },
  "avgTimePerAttemptByRound": {
    "1": 0.9,
    "2": 0.85
  },
  "timeBetweenRounds": {
    "1": 1.5
  },
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
  "bestMarkPerRound": {
    "1": "44.62",
    "2": "46.38"
  },
  "foulRateByRound": {
    "1": 25.0,
    "2": 30.0
  },
  "athletesWithZeroFouls": 2,
  "fastestAthlete": {
    "bib": "309",
    "name": "Amira Okafor",
    "competitionTime": 31.2,
    "averageTimeBetween": 49.1
  },
  "mostConsistent": {
    "bib": "214",
    "name": "Jane Smith",
    "standardDeviation": 0.84,
    "averageMark": 45.4,
    "bestMark": 46.38
  },
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
    {
      "timestamp": "2026-06-14T13:31:02+01:00",
      "athleteName": "Jane Smith",
      "mark": 44.62,
      "valid": true,
      "round": 1,
      "attempt": 1
    }
  ],
  "roundComparison": [
    {
      "round": 1,
      "averageMark": 37.9,
      "bestMark": 44.62,
      "foulRate": 25.0,
      "totalAttempts": 8
    }
  ],
  "athleteRankings": [
    {
      "bib": "214",
      "name": "Jane Smith",
      "bestMark": 46.38,
      "averageMark": 45.4,
      "foulRate": 20.0,
      "consistency": 0.84
    }
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | No event ID in the path. | `{"error": "Event ID is required"}` |
| 404 | Unknown event. | `{"error": "event with ID dt-xx not found"}` |

## Wind

### GET /api/v1/wind/gauges
{: #wind-gauges}

List wind gauges and their latest reading.

**Request**

```http
GET /api/v1/wind/gauges HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `WindGaugesResponse`

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

### GET /api/v1/wind/current
{: #wind-current}

Average wind now, over the last few seconds.

| Parameter | In | Description |
|-----------|----|-------------|
| `gauge_id` | query | Required. Gauge ID from /wind/gauges. |
| `duration` | query | Averaging window in seconds, 1-60. Default 5. |

**Request**

```http
GET /api/v1/wind/current?gauge_id=back-pits&duration=5 HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `WindReadingResponse`

```json
{
  "gauge_id": "back-pits",
  "average_speed": 1.32,
  "average_crosswind": -0.38,
  "readings": [
    1.2,
    1.4,
    1.3,
    1.3,
    1.4
  ],
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | gauge_id missing. | `{"error": "gauge_id parameter is required"}` |
| 404 | Unknown gauge. | `{"error": "Wind gauge not found"}` |
| 503 | Gauge offline or no readings in the window. | `{"error": "Wind gauge is offline"}` |

### GET /api/v1/wind/search
{: #wind-search}

Wind at a past moment (today's log). Finds the reading nearest the timestamp in today's stored log and averages the readings within ±2.5 s of it. Used to attach wind to a jump after the fact.

| Parameter | In | Description |
|-----------|----|-------------|
| `gauge_id` | query | Required. Gauge ID. |
| `timestamp` | query | Required. RFC 3339 time, URL-encoded (e.g. `2026-06-14T14%3A02%3A10Z`). |

**Request**

```http
GET /api/v1/wind/search?gauge_id=back-pits&timestamp=2026-06-14T14%3A02%3A10Z HTTP/1.1
Host: polyfieldserver.local:8080
```

**Response** `200 OK` — body: `WindReadingResponse`

```json
{
  "gauge_id": "back-pits",
  "average_speed": 1.4,
  "average_crosswind": -0.38,
  "readings": [
    1.3,
    1.5,
    1.4
  ],
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

**Errors** (body: `Error`)

| Status | When | Example |
|--------|------|---------|
| 400 | gauge_id or timestamp missing, or timestamp not RFC 3339. | `{"error": "Invalid timestamp format (use RFC3339)"}` |
| 404 | Unknown gauge. | `{"error": "Wind gauge not found"}` |
| 503 | No readings stored today. | `{"error": "No wind readings available"}` |

## Live updates

### GET /api/v1/stream
{: #stream}

A [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) stream (`Content-Type: text/event-stream`). The server sends a `data: update` message whenever results, event status or the active athlete change; on receiving it, refetch whichever feed you display. A comment line (`: ping`) is sent every 25 seconds to keep the connection open. The message carries no data beyond the word `update`, so there is no JSON Schema for it.

```text
: connected

data: update

: ping

data: update
```

```js
const es = new EventSource('http://polyfieldserver.local:8080/api/v1/stream');
es.onmessage = (e) => { if (e.data === 'update') refresh(); };
```

Keep a slow poll (every 30–60 s) as a fallback, as the built-in display pages do, in case the connection drops.

## Display pages and static files

These routes return HTML or assets rather than JSON. They are listed for completeness; see [Display screens](/PolyField-Server/#display-screens) in the manual.

| Path | Returns |
|------|---------|
| `/` | Display board (HTML) |
| `/tables` | Event standings (HTML) |
| `/announcer` | Announcer feed (HTML) |
| `/raza` | RAZA rankings (HTML) |
| `/heatmap.js` | Heatmap drawing script used by the display pages |
| `/display-i18n.js` | Display-page translations |
| `/polyfield-logo.png` | PolyField logo |

## Shared definitions

Objects used inside several endpoint bodies. Every other definition is shown with its endpoint above; all of them are in the [downloadable schema](/PolyField-Server/api/polyfield-api.schema.json).

### Error

Body returned with every 4xx/5xx response from the API.

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

### Performance

One attempt by an athlete. Responses always include unit, valid and timestamp.

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

### HeatmapCoordinate

A throw/jump landing position.

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

### CalibrationMetadata

Field geometry captured when the EDM was calibrated.

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

### SectorLines

Sector-line geometry for a throwing circle.

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

### Coordinate

An X/Y position in metres in the EDM frame.

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

### Athlete

A competitor and their series.

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

### EventRules

Competition format for an event.

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

### TimeSeriesPoint



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
