---
layout: manual
lang: nl
title: "PolyField Server — Handleiding"
description: "Help en gebruikershandleiding voor PolyField Server — de besturingsserver voor technische nummers die de wedstrijd, de live-schermen, de windmeters, de statistieken en de online-uitslagen over het netwerk van uw accommodatie verzorgt."
---

# PolyField Server

De besturingsserver voor technische nummers. Eén desktop-app draait de wedstrijd op het netwerk van uw accommodatie: hij bewaart de onderdelen en de atleten, ontvangt de uitslagen live vanuit de PolyField-veldapp, stuurt de live-schermen aan, registreert de wind, maakt statistieken en socialmediabeelden en publiceert (optioneel) de uitslagen online. Werkt op Windows en Mac; werkt op een lokaal netwerk.

[Downloaden via polyfield.co.uk](https://www.polyfield.co.uk)

* TOC
{:toc}

## Overzicht    {#overview}

PolyField Server is het hart van een wedstrijd met technische nummers. Hij draait op één computer op het netwerk van uw accommodatie en doet vier dingen tegelijk:

- **Bewaart de wedstrijd** — de onderdelen, leeftijdscategorieën, atleten en elke poging, allemaal lokaal opgeslagen op de hostcomputer.
- **Ontvangt de uitslagen** — officials meten bij de ring of aanloop met de PolyField-veldapp (op een Android-toestel gekoppeld aan een EDM-totaalstation, of handmatig ingevoerd), en de app stuurt elke prestatie rechtstreeks naar de server.
- **Stuurt de schermen aan** — hij levert een reeks webpagina's die elk scherm op het netwerk in een browser opent: een live-uitslagenbord, de standen per onderdeel, een feed voor de speaker en de para-atletiek RAZA-ranglijsten.
- **Voegt analyse toe** — windregistratie, statistieken per onderdeel en heatmaps van de landingen, socialmediabeelden en optionele publicatie naar de PolyField-cloud.

Alles werkt op het lokale netwerk — er is geen internet nodig om een wedstrijd te draaien, maar het is wel vereist om startlijsten te downloaden van aanbieders van wedstrijdbeheer en om real-time-uitslagen terug te sturen naar hun systemen. Na afloop is een synchronisatie mogelijk om alle uitslagen in één keer te versturen.

> **Positieve validatie.** De server verzint nooit uitslagen — elke prestatie komt van een official via de veldapp. Zo blijft er een duidelijke keten van de meting bij de ring tot wat op het bord verschijnt.

## Hoe het werkt    {#how-it-works}

- U draait **één exemplaar** van de desktop-app op een computer op het wedstrijdnetwerk.
- De **veldapp** (één per onderdeel) maakt verbinding met de server, downloadt de atleten van zijn onderdeel en stuurt elke poging terug zodra die is gemeten.
- Elk **scherm** opent een van de webpagina's van de server in een browser; de uitslagen worden meteen bijgewerkt, zonder te hoeven vernieuwen.
- De operator werkt vanuit het desktop-**dashboard** — onderdelen importeren, de voortgang volgen, statistieken en beelden exporteren en schermen en windmeters beheren. Die worden meestal één keer aan het begin van de wedstrijd ingesteld, zonder dat er gedurende de dag iets hoeft te gebeuren.

## Aan de slag    {#getting-started}

### 1. Een wedstrijd laden    {#load-a-competition}

Open de app; het **Dashboard** is de werkplek van de operator. Start een wedstrijd op een van drie manieren:

- **Importeren uit OpenTrack of Athletics.app** — haal de onderdelenlijst en de startlijsten rechtstreeks op (zie [Onderdelen importeren](#importing-events)). Dit is de gebruikelijke route en behoudt de gepubliceerde volgorde van de startlijsten.
- **Onderdelen handmatig aanmaken** — gebruik *+ Nieuw onderdeel aanmaken* en voeg de atleten toe.
- **Nieuwe wedstrijd** — wist de huidige gegevens om opnieuw te beginnen.

Zodra ze geladen is, verschijnt elk onderdeel als een kaart op het dashboard met de status (Niet gestart, Bezig, Afgerond).

### 2. De veldapp verbinden    {#connect-the-field-app}

Controleer op elk veldtoestel het serveradres in de PolyField-veldapp om het met de server te verbinden. De official kiest vervolgens zijn onderdeel, kalibreert de EDM op de ring of aanloop en begint te meten. Zie [De uitslagen en de veldapp](#results-and-the-field-app).

### 3. De schermen openen    {#open-the-displays}

Open op elk scherm een browser op het serveradres en voeg de gewenste pagina toe — bijvoorbeeld `http://polyfieldserver.local:8080/tables`. Gebruik **Schermen** op het dashboard voor koppelingen met één klik en scanbare QR-codes naar elk scherm. Zie [De schermen](#display-screens).

> **Tip.** Laat de desktop-app op het dashboard staan en stuur alles van daaruit aan. De uitslagen komen automatisch binnen vanuit de veldapp terwijl u de voortgang en de schermen in de gaten houdt.

![Venster Schermen — koppelingen en QR-codes voor elk scherm](/PolyField-Server/images/displays-popup.png)

## Het dashboard    {#the-dashboard}

Het dashboard toont elk onderdeel en biedt de belangrijkste bedieningsknoppen. Bovenaan staan het serveradres (met een netwerkkeuze op machines met meerdere kaarten) en de status van wachtende uploads of synchronisatie. De belangrijkste acties:

| Knop | Wat die doet |
|------|--------------|
| Nieuwe wedstrijd | De huidige wedstrijd wissen en opnieuw beginnen. |
| Nieuw onderdeel aanmaken | Een onderdeel en de atleten handmatig toevoegen. |
| Onderdelen samenvoegen | Onderdelen (bijv. twee groepen van dezelfde discipline) tot één samenvoegen, of *Alle gelijke onderdelen samenvoegen* om in één keer alle overeenkomende paren samen te voegen. |
| Schermen | Aanklikbare koppelingen en QR-codes van elke schermpagina tonen (bord, standen, speaker, RAZA). |
| Beelden exporteren | De socialmediabeelden, gedetailleerde heatmaps en windbeelden van de wedstrijd genereren (zie [Socialmediabeelden](#social-media-graphics)). |
| Statistieken exporteren | De statistiek-PDF van de wedstrijd maken (ook op de pagina Statistieken). |

Een onderdeel selecteren opent de weergave **Live-uitslagen**, waar u de serie van elke atleet ziet, de pogingen ziet binnenkomen en de stand bekijkt.

![Het dashboard van PolyField Server](/PolyField-Server/images/dashboard.png)

## Onderdelen importeren    {#importing-events}

Gebruik **Wedstrijdkoppeling** / importeren om een wedstrijd te laden in plaats van hem in te typen:

- **OpenTrack** — meld u aan en kies uw wedstrijd; de server downloadt de onderdelen en hun inschrijvingen. De **volgorde van de startlijsten** die OpenTrack publiceert wordt exact behouden.
- **Athletics.app** — voer de code van de wedstrijdkoppeling in om de onderdelen en de atleten aan te maken. De **volgorde van de startlijsten** die Athletics.app publiceert wordt exact behouden.

Geïmporteerde onderdelen behouden hun oorspronkelijke nummering en codes, zodat ze aansluiten op het gepubliceerde programma en op de uitslagenexport.

![Een wedstrijd importeren](/PolyField-Server/images/import-opentrack.png)

## De uitslagen en de veldapp    {#results-and-the-field-app}

Uitslagen worden op het veld geregistreerd, niet op de server. Elk onderdeel gebruikt de PolyField-veldapp op een Android-toestel:

- Het toestel maakt verbinding met de server en downloadt de atleten van het gekozen onderdeel.
- Voor werp- en horizontale springnummers kan de app worden gekoppeld aan een **EDM-totaalstation** of rechtstreeks draaien op een PolyField-totaalstation (PolyField APEKS AM02i); de official kalibreert op de ring / aanloop / balk, en elke gemeten prestatie (met landingscoördinaat) wordt naar de server gestuurd. Prestaties kunnen ook handmatig worden ingevoerd.
- **Verticale springnummers** (hoogspringen, polsstokhoogspringen) worden volledig ondersteund — de hoogtes, de pogingen (O/X) en het verloop van de lat worden geregistreerd en verstuurd.
- Elke poging heeft een eigen tijdstempel, zodat de server de uitslagen in hun werkelijke volgorde toont en nauwkeurige tijdstatistieken kan maken.

Naarmate de uitslagen binnenkomen, wordt de kaart van het onderdeel bijgewerkt, worden de standen opnieuw berekend en wordt elk verbonden scherm meteen ververst.

![Live-uitslagen — resultatentabel](/PolyField-Server/images/live-results-table.png)

![Live-uitslagen — landingsheatmap](/PolyField-Server/images/live-results-heatmap.png)

## De schermen    {#display-screens}

De server levert vier live-schermpagina's. Elk is een gewone webpagina — open die in elke browser op het netwerk; er wordt niets op het scherm geïnstalleerd. Ze werken allemaal automatisch bij: nieuwe uitslagen worden meteen verstuurd zodra ze binnenkomen, met een periodieke controle als vangnet, zodat een scherm nooit hoeft te worden ververst.

| Pagina | URL |
|--------|-----|
| Uitslagenbord (laatste uitslagen) | `/` |
| Standen per onderdeel (tabellen) | `/tables` |
| Speakerfeed | `/announcer` |
| RAZA-ranglijsten (para-atletiek) | `/raza` |

### Uitslagenbord    {#display-board}

Een groot bord met de meest recente prestaties, met de atleet, het onderdeel, de prestatie en — voor werpnummers — een weergave van de landing. Ideaal als hoofd-uitslagenscherm voor het publiek.

![Uitslagenbord](/PolyField-Server/images/display-board.png)

### Standen per onderdeel    {#event-standings}

De live-standen, meerdere onderdelen tegelijk, elk gerangschikt met goud/zilver/brons-accenten. De opmaak past zich aan de hoogte aan: hij vult het scherm, stapelt meer onderdelen op hoge of staande schermen, en wanneer een onderdeel veel atleten heeft, doorloopt hij ze pagina voor pagina. De onderdelen wisselen elkaar ook af zodat elk onderdeel van het programma in beeld komt.

![Scherm met standen per onderdeel](/PolyField-Server/images/display-tables.png)

### Speaker    {#announcer}

Een feed van uitslagen zodra ze binnenkomen — de nieuwste bovenaan, met de plaats, de atleet, de club, het onderdeel en de prestatie — geschikt om in één oogopslag te lezen vanaf een speaker- of commentaarpositie.

![Speakerfeed](/PolyField-Server/images/display-announcer.png)

### RAZA-ranglijsten    {#raza-rankings}

Para-atletiekranglijsten berekend met het puntensysteem van World Para Athletics (RAZA), zodat atleten uit verschillende klassen op één bord vergeleken kunnen worden. Er moet een klasse en een geslacht zijn ingesteld voordat er een RAZA-score wordt berekend.

![Scherm met RAZA-ranglijsten](/PolyField-Server/images/display-raza.png)

## Windmeters    {#wind-gauges}

PolyField Server leest windmeters via het netwerk en registreert de wind voor de hele wedstrijddag. Hij ondersteunt de **Gill WindSonic 75** en de **PolyField Wind Mini** en **herkent het type windmeter automatisch** aan de hand van zijn datastroom — er is geen protocol te kiezen. Voeg een windmeter toe met zijn netwerkadres; zodra hij zendt, toont de server het herkende model en begint te registreren.

- De wind wordt continu vastgelegd en per dag opgeslagen, zodat hij beschikbaar is voor de geldigheid van horizontale springnummers, de statistieken en de windbeelden.
- De pagina **Windmeters** toont elke meter live en laat u een windbeeld van de hele dag exporteren.
- Windmeters kunnen worden verborgen voor de atletenselectie (bijvoorbeeld een algemene baanwindmeter die alleen voor de registratie wordt bewaard).

![De pagina Windmeters](/PolyField-Server/images/wind-gauges.png)

## Statistieken en heatmaps    {#statistics-and-heatmaps}

De pagina **Statistieken** zet de wedstrijdgegevens om in analyse:

- **Grafieken per onderdeel** — prestatie in de tijd, vergelijking ronde voor ronde, percentage ongeldige en geldige pogingen, en tijd tussen pogingen.
- **Landingsheatmaps** — voor werpnummers wordt elke landing in de sector uitgezet, gekleurd per ronde, met de gemiddelde landingshoek ten opzichte van de middellijn van de sector, de spreiding en de variantie.
- **Wind** — gemiddelde, geldigheid en het verloop over de sessie voor elke windmeter.
- **Statistieken exporteren** — een volledige wedstrijd-PDF met de grafieken, heatmaps en samenvattingen per onderdeel, gedateerd op de wedstrijddag.

De grafieken en heatmaps schalen mee met de instelling voor weergavegrootte, zodat ze leesbaar blijven op het scherm van de operator.

![Statistieken — landingsheatmap van een werpnummer](/PolyField-Server/images/statistics-heatmap.png)

## Socialmediabeelden    {#social-media-graphics}

**Beelden exporteren** maakt een reeks vierkante afbeeldingen (1080 × 1080) die klaar zijn om te posten, allemaal in een consistente PolyField-stijl:

- **Wedstrijdsamenvatting** — de opvallende totalen van de wedstrijd, met de verste worp en de verste sprong.
- **Kaarten per onderdeel** — het podium, de omstandigheden van het onderdeel en de totalen. De kaarten voor verticaal springen tonen de serie pogingen van elke atleet op zijn beste hoogte en een verdeling van het slaagpercentage bij de 1e / 2e / 3e poging; de kaarten voor horizontaal springen tonen de wind.
- **Gedetailleerde heatmaps** — de volledige spreiding van de landingen van elk werpnummer.
- **Windbeelden** — het windverloop van de hele dag voor elke windmeter, met de geldigheid en de windstoten.

Beelden worden alleen gemaakt voor onderdelen die zijn verwerkt, en elke kaart draagt de wedstrijddatum en de PolyField-huisstijl.

![Voorbeeld van een geëxporteerde onderdeelkaart](/PolyField-Server/images/social-example.png)

![Windbeeld voor social media (geëxporteerd)](/PolyField-Server/images/wind-gauges-social.png)

## Online-uitslagen — in test    {#cloud-results}

Optioneel publiceert de server de uitslagen naar de PolyField-cloud zodat het publiek online kan meekijken op [results.polyfield.co.uk](https://results.polyfield.co.uk). Er kunnen twee dingen worden verstuurd, elk in te schakelen in de Instellingen:

- **Atletenuitslagen en heatmaps** — individuele pagina's die geanonimiseerd zijn om minder herleidbare informatie op te slaan bij hun prestaties, met een landingsheatmap. Deze worden na 90 dagen automatisch verwijderd.
- **Globale heatmap** — een samengevoegd beeld van de landingen over de hele wedstrijd. Dit is geanonimiseerd, zonder individuele atletengegevens, en wordt onbeperkt bewaard.

Uploads worden in de wachtrij gezet en opnieuw geprobeerd, zodat een korte internetonderbreking geen gegevens verliest — de wedstrijd zelf blijft hoe dan ook op het lokale netwerk draaien.

## Wedstrijdkoppeling    {#competition-link}

**Wedstrijdkoppeling** is waar u de aanbieders van wedstrijdbeheer met de server verbindt. Het biedt de import-bediening voor OpenTrack / Athletics.app om de onderdelen te laden.

![Wedstrijdkoppeling — serveradres en QR-code](/PolyField-Server/images/competition-link.png)

## Instellingen, weergavegrootte en taal    {#settings}

- **Weergavegrootte** — schaalt de operatorinterface, de statistiekgrafieken en de heatmaps naar het scherm waarop u de server draait.
- **Taal** — de interface is beschikbaar in het Engels, Frans, Spaans, Nederlands en Portugees.
- **Cloud-upload** — schakelt het publiceren van atleten en heatmaps in of uit.
- **Mappen** — stelt de mappen in voor het importeren van onderdelen, lokale back-ups op de pc, en het exporteren van uitslagen en beelden.

![Instellingen](/PolyField-Server/images/settings.png)

## Netwerk    {#networking}

- De app draait op **poort 8080** en meldt zich als `polyfieldserver.local`, zodat veldtoestellen en schermen `http://polyfieldserver.local:8080` kunnen gebruiken zonder het IP-adres te kennen. Sommige Android-toestellen vereisen het volledige IP-adres; dan kunt u `http://192.168.0.10:8080` gebruiken, waarbij u 192.168.0.10 vervangt door het serveradres dat op het dashboard wordt getoond.
- Op computers met meer dan één netwerkkaart (gebruikelijk op Windows) kiest u de juiste kaart bovenaan het dashboard, zodat het juiste adres wordt aangekondigd.
- Alle toestellen — veldapps en schermen — moeten op hetzelfde netwerk zitten als de hostcomputer.

## Diagnostiek    {#diagnostics}

Als er iets misgaat, gebruik dan het diagnoserapport. Het bundelt de huidige wedstrijd (die de support kan afspelen), de logboeken en de windgegevens van de dag in één zip-bestand, en vult vooraf een e-mail in naar [support@polyfield.co.uk](mailto:support@polyfield.co.uk). Voeg het opgeslagen bestand toe voordat u verzendt. Hetzelfde bestand kan dienen om een wedstrijd te herstellen als er halverwege van machine gewisseld moet worden.

![Diagnoserapport](/PolyField-Server/images/diagnostics.png)

## Problemen oplossen    {#troubleshooting}

| Symptoom | Wat te controleren |
|----------|--------------------|
| Een veldtoestel maakt geen verbinding | Controleer of het op hetzelfde netwerk zit, of poort 8080 bereikbaar is en (pc's met meerdere kaarten) of de juiste netwerkkaart bovenaan het dashboard is gekozen. Zorg dat uw firewall PolyField Server niet blokkeert. |
| Een import levert 0 onderdelen op | De bronwedstrijd heeft misschien nog geen inschrijvingen, of er is een andere wedstrijd geselecteerd. Controleer of de startlijsten zijn gepubliceerd. |
| Een scherm werkt niet bij | De pagina's werken zichzelf bij; als er een blijft hangen, ververs die dan één keer. Controleer of hij naar het huidige serveradres wijst. De schermen tonen de huidige tijd en de tekst «LIVE» wanneer ze verbonden zijn, om dit te helpen controleren. |
| Een windmeter toont geen meting | Controleer het netwerkadres van de windmeter en of hij aanstaat en zendt; het model wordt automatisch herkend zodra er data binnenkomt. De windmeter toont een status Online / Offline op de server. |
| Het RAZA-bord is leeg | Er moet een klasse en een geslacht zijn ingesteld voordat er een RAZA-score wordt berekend. |
| De uitslagen lijken door elkaar te staan of een ronde ontbreekt | Elke uitslag krijgt een tijdstempel van de veldapp; zorg dat de veldtoestellen op het juiste onderdeel staan en bijgewerkt zijn. Controleer of de klok van het veldtoestel en de server klopt; die kan afwijken bij langdurig offline gebruik. |

## Downloaden en support    {#download-and-support}

Download de nieuwste versie via [www.polyfield.co.uk](https://www.polyfield.co.uk) of de releasepagina. De app controleert bij het opstarten op updates en toont een melding wanneer er een nieuwere versie beschikbaar is. Support: [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

## API-integratie {#api-integration}

PolyField Server biedt een **HTTP + JSON-API** op **poort 8080**, op **hetzelfde lokale netwerk** als uw veldapparaten en schermen. Het is dezelfde interface die de PolyField-veldapp en de ingebouwde schermen gebruiken, dus alles op het lokale netwerk — een eigen scorebord, een statistiekendashboard, een streamingoverlay, de eigen bewegwijzering van een accommodatie — kan onderdelen, live uitslagen, standen, statistieken en wind rechtstreeks van de server lezen. Antwoorden zijn JSON, er is geen authenticatie en CORS staat open, zodat een webpagina op het lokale netwerk de API direct kan aanroepen. De meeste endpoints zijn alleen-lezen `GET`s; de schrijf-endpoints (`POST /api/v1/results`, `POST /api/v1/athlete/active`, `PUT /api/v1/events/status`) worden door de veldapp gebruikt.

De API is **bewust alleen voor het lokale netwerk** — de app stelt hem niet bloot aan internet. **Elke integratie via WAN of internet** (externe scoreborden, clouddiensten, een tweede accommodatie) **moet eerst met ons besproken worden** zodat het veilig gebeurt, meestal via een VPN of een beheerde reverse proxy in plaats van de poort voor de hele wereld open te zetten. Neem contact op via [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

**Basis-URL:** `http://polyfieldserver.local:8080/api/v1` — of gebruik het IP-adres van de server dat bovenaan het dashboard staat (bijv. `http://192.168.0.10:8080/api/v1`).

**JSON Schema:** elke request- en response-body is gedefinieerd in één [JSON Schema-bestand (draft 2020-12)](/PolyField-Server/api/polyfield-api.schema.json), onder `$defs`. Bij elk endpoint hieronder staat het type van de body met het bijbehorende schema; gedeelde typen staan onder [Datatypen](#api-data-types). Verwijs om een body te valideren naar de definitie ervan, bijv. `polyfield-api.schema.json#/$defs/ResultPayload`.

**Conventies**

- Fouten geven een 4xx/5xx-status met `{"error": "message"}`. Een methode die een endpoint niet accepteert geeft `405`.
- Tijden zijn RFC 3339, bijv. `2026-06-14T13:42:07.512+01:00`.
- Prestaties en hoogtes zijn strings in meters (`"46.38"`) zodat nullen aan het eind behouden blijven; wind is een string met teken in m/s (`"+1.4"`).
- Optionele velden worden weggelaten als ze leeg zijn. Maps per ronde gebruiken tekstsleutels (`"1"`, `"2"`, …).

| Methode en pad | Geeft terug |
|---|---|
| [`GET /api/v1/events`](#api-list-events) | Alle onderdelen weergeven (overzicht). |
| [`GET /api/v1/events/{eventId}`](#api-get-event) | Eén onderdeel ophalen met de atleten en alle pogingen. |
| [`PUT/PATCH /api/v1/events/status`](#api-update-status) | De status van een onderdeel instellen. |
| [`POST /api/v1/results`](#api-post-results) | De serie van een atleet versturen (de belangrijkste schrijfactie van de veldapp). |
| [`POST /api/v1/athlete/active`](#api-post-active) | Melden wie er nu aan de beurt is (horizontale sprongen). |
| [`GET /api/v1/athlete/active/{eventId}`](#api-get-active) | Opvragen wie er nu aan de beurt is in een onderdeel. |
| [`GET /api/v1/display/recent`](#api-display-recent) | Laatste prestaties (uitslagenbord). |
| [`GET /api/v1/display/standings`](#api-display-standings) | Huidige standen voor elk onderdeel met prestaties. |
| [`GET /api/v1/broadcast/recent`](#api-broadcast-recent) | De laatste 10 uitslagen met alle details (uitzending / speaker). |
| [`GET /api/v1/raza`](#api-raza) | RAZA-ranglijsten voor para-atletiek. |
| [`GET /api/v1/statistics/overall`](#api-stats-overall) | Statistieken over de hele wedstrijd. |
| [`GET /api/v1/statistics/event/{eventId}`](#api-stats-event) | Gedetailleerde statistieken voor één onderdeel. |
| [`GET /api/v1/wind/gauges`](#api-wind-gauges) | Windmeters met hun laatste meting weergeven. |
| [`GET /api/v1/wind/current`](#api-wind-current) | Gemiddelde wind nu, over de laatste seconden. |
| [`GET /api/v1/wind/search`](#api-wind-search) | Wind op een eerder moment (logboek van vandaag). |
| [`GET /api/v1/config`](#api-config) | Schermconfiguratie. |
| [`GET /api/v1/stream`](#api-stream) | Live updatemeldingen (Server-Sent Events). |

### `GET /api/v1/events` {#api-list-events}

Alle onderdelen weergeven (overzicht). Geeft elk onderdeel dat op de server is geladen als beknopt overzicht. De veldapp gebruikt dit voor de keuze van het onderdeel.

```http
GET /api/v1/events
```

**Response — array van `EventSummary`:**

- `id` (string)
- `name` (string)
- `type` (string) — Categorie van het onderdeel. Bekende waarden: "Throws", "Horizontal Jumps", "Vertical Jumps".

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

**Fouten:**

- `405` — Elke methode behalve GET.

### `GET /api/v1/events/{eventId}` {#api-get-event}

Eén onderdeel ophalen met de atleten en alle pogingen. Geeft het volledige onderdeel. De veldapp gebruikt dit om de startlijst en eventuele al vastgelegde uitslagen te downloaden.

- `eventId` (pad) — Onderdeel-ID uit de lijst met onderdelen (URL-coderen).

```http
GET /api/v1/events/dt-sw-f07
```

**Response — `Event`:**

- `id` (string)
- `name` (string)
- `originalName` (string, optioneel)
- `type` (string) — Categorie van het onderdeel. Bekende waarden: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `rules` (EventRules) — Wedstrijdformat van een onderdeel.
- `athletes` (Athlete[])
- `calibrationMetadata` (CalibrationMetadata, optioneel) — Veldgeometrie vastgelegd bij het kalibreren van de EDM.
- `lastResultTime` (date-time, optioneel)
- `signedOff` (boolean, optioneel)
- `signedOffBy` (string, optioneel)
- `signedOffAt` (date-time, optioneel)
- `evtEventNumber` (string, optioneel)
- `evtRoundNumber` (string, optioneel)
- `evtHeatNumber` (string, optioneel)
- `opentrackUnitId` (string, optioneel)
- `opentrackEventId` (string, optioneel)
- `opentrackEventCode` (string, optioneel)
- `opentrackUrl` (string, optioneel)
- `athleticsAppLinkCode` (string, optioneel)
- `isMerged` (boolean, optioneel)
- `isHidden` (boolean, optioneel)
- `mergedEventId` (string, optioneel)
- `sourceEventIds` (string[], optioneel)
- `sourceEventNames` (string[], optioneel)

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

**Fouten:**

- `400` — Geen onderdeel-ID in het pad. `{"error": "Event ID is required"}`
- `404` — Onbekend onderdeel. `{"error": "event with ID dt-xx not found"}`

### `PUT / PATCH /api/v1/events/status` {#api-update-status}

De status van een onderdeel instellen. Zet een onderdeel op Not Started, In Progress of Finished. De server zet een onderdeel ook automatisch op In Progress zodra de eerste geldige uitslag binnenkomt.

**Request-body — `EventStatusUpdate`:**

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
- `message` (string, optioneel)

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

**Fouten:**

- `400` — Ontbrekend veld, onbekend onderdeel of ongeldige status. `{"error": "invalid status: Done. Must be one of: Not Started, In Progress, Finished"}`

### `POST /api/v1/results` {#api-post-results}

De serie van een atleet versturen (de belangrijkste schrijfactie van de veldapp). Stuurt de **volledige** serie van de atleet tot nu toe; die vervangt wat de server voor die atleet heeft, dus opnieuw versturen is veilig. De server bepaalt welke pogingen nieuw of gewijzigd zijn, werkt de standen bij en stuurt een `update` naar de schermen. Prestaties worden genormaliseerd: `X`/`FOUL` worden `NM`, `PASS`/`-` worden `P`. Een prestatie buiten het bereik wordt gelogd maar toch opgeslagen. Staat het startnummer niet in het onderdeel, dan wordt een tijdelijke atleet toegevoegd.

**Request-body — `ResultPayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `series` (Performance[]) — De volledige serie van de atleet tot nu toe. Vervangt de opgeslagen serie.
- `heatmapCoordinates` (HeatmapCoordinate[], optioneel)
- `calibrationMetadata` (CalibrationMetadata, optioneel) — Veldgeometrie vastgelegd bij het kalibreren van de EDM.

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

*Horizontale sprong met wind:*

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

*Verticale sprong (één poging per regel, met lathoogte):*

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
- `message` (string, optioneel)

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

**Fouten:**

- `400` — Body is geen geldige JSON. `{"error": "Invalid request body"}`
- `404` — Onbekend onderdeel. `{"error": "event with ID dt-xx not found"}`

### `POST /api/v1/athlete/active` {#api-post-active}

Melden wie er nu aan de beurt is (horizontale sprongen). Signaal zonder bevestiging vanuit de veldapp wanneer een springer de huidige atleet wordt, gebruikt door de afzetbalk-liniaal op het scherm. Eén atleet per onderdeel: elke melding overschrijft de vorige. Het is **geen** uitslag.

**Request-body — `ActiveAthletePayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `athleteName` (string, optioneel)
- `board` (number, optioneel) — Afstand van de afzetbalk in meters (0 = verspringbalk).
- `topPerformances` (number[], optioneel) — Beste geldige prestaties tot nu toe, beste eerst. Maximaal 3.

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

**Fouten:**

- `400` — Ongeldige JSON, of eventId / athleteBib ontbreekt. `{"error": "eventId and athleteBib are required"}`

### `GET /api/v1/athlete/active/{eventId}` {#api-get-active}

Opvragen wie er nu aan de beurt is in een onderdeel. Altijd 200 zodat een widget eenvoudig kan peilen; `active` is `null` als er niemand is gemeld (tussen atleten of na een herstart).

- `eventId` (pad) — Onderdeel-ID.

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

*Niemand aan de beurt:*

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

**Fouten:**

- `400` — Geen onderdeel-ID in het pad. `{"error": "Event ID is required"}`

### `GET /api/v1/display/recent` {#api-display-recent}

Laatste prestaties (uitslagenbord). De meest recente prestaties, nieuwste eerst. Voedt het uitslagenbord op `/`.

- `limit` (query) — Hoeveel terug te geven, 1-100. Standaard 4; waarden buiten het bereik vallen terug op 4.

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

Huidige standen voor elk onderdeel met prestaties. Gerangschikte standen voor elk onderdeel met minstens één geldige prestatie. Voedt het scherm `/tables`. `events` is `null` zolang geen onderdeel een geldige prestatie heeft.

```http
GET /api/v1/display/standings
```

**Response — `EventStandingsResponse`:**

- `events` (EventStandings[]) — Alleen onderdelen met minstens één geldige prestatie. null als die er niet zijn.

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

De laatste 10 uitslagen met alle details (uitzending / speaker). Tot de 10 meest recente uitslagen, nieuwste eerst, met genoeg detail om elke uitslag opnieuw te tekenen (sectorlijnen, landingspunt, lathoogte en serie). Voedt de pagina `/announcer`.

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

RAZA-ranglijsten voor para-atletiek. Atleten met een classificatie en geslacht, gescoord met RAZA-punten van World Para Athletics en gegroepeerd per standaardonderdeel. Voedt het scherm `/raza`.

```http
GET /api/v1/raza
```

**Response — `RazaResponse`:**

- `events` (RazaEventGroup[])
- `total` (integer) — Totaal aantal gerangschikte atleten.

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

Statistieken over de hele wedstrijd. Totalen, tijden, percentage ongeldige pogingen, pogingen in de tijd, tijdlijn van onderdelen en landingsvakken per werponderdeel.

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
- `competitionStartTime` (date-time, optioneel)
- `competitionEndTime` (date-time, optioneel)
- `totalDuration` (number) — Minuten.
- `eventsWithOpenTrack` (integer)
- `eventsWithCalibration` (integer)
- `eventsByType` (object) — Aantal onderdelen per categorie.
- `attemptsOverTime` (TimeSeriesPoint[])
- `eventTimeline` (EventTimelineItem[])
- `throwHeatmaps` (object, optioneel) — Per werponderdeelcode.

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

**Fouten:**

- `500` — De statistieken konden niet worden berekend.

### `GET /api/v1/statistics/event/{eventId}` {#api-stats-event}

Gedetailleerde statistieken voor één onderdeel. Tijden, rondes, ongeldige pogingen, prestaties en grafiekgegevens voor één onderdeel. `windStats`, `heatmapStats` en `verticalJumpStats` verschijnen alleen bij het bijbehorende type onderdeel. Maps per ronde gebruiken het rondenummer als tekstsleutel.

- `eventId` (pad) — Onderdeel-ID.

```http
GET /api/v1/statistics/event/dt-sw-f07
```

**Response — `EventStatistics`:**

- `eventId` (string)
- `eventName` (string)
- `eventType` (string) — Categorie van het onderdeel. Bekende waarden: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `calibrationTime` (date-time, optioneel)
- `firstAttemptTime` (date-time, optioneel)
- `lastAttemptTime` (date-time, optioneel)
- `setupDuration` (number) — Minuten van kalibratie tot eerste poging.
- `competitionDuration` (number) — Minuten van eerste tot laatste poging.
- `totalEventDuration` (number) — Minuten van kalibratie tot laatste poging.
- `averageTimeBetween` (number) — Seconden tussen pogingen.
- `roundDurations` (object) — Ronde -> minuten.
- `avgTimePerAttemptByRound` (object) — Ronde -> gemiddeld aantal minuten tussen pogingen.
- `timeBetweenRounds` (object) — Ronde -> tijd tot de volgende ronde (minuten).
- `totalAthletes` (integer)
- `athletesCompleted` (integer)
- `athletesInProgress` (integer)
- `athletesNotStarted` (integer)
- `totalAttempts` (integer)
- `validAttempts` (integer)
- `fouls` (integer)
- `foulRate` (number)
- `winningMark` (string, optioneel)
- `averageMark` (number)
- `medianMark` (number)
- `bestMarkPerRound` (object) — Ronde -> beste prestatie.
- `foulRateByRound` (object) — Ronde -> percentage ongeldige pogingen.
- `athletesWithZeroFouls` (integer)
- `fastestAthlete` (AthleteTimingInfo, optioneel)
- `slowestAthlete` (AthleteTimingInfo, optioneel)
- `mostConsistent` (AthleteConsistencyInfo, optioneel)
- `windStats` (WindStatistics, optioneel) — Alleen horizontale sprongen.
- `heatmapStats` (HeatmapStatistics, optioneel) — Alleen worpen met landingscoördinaten.
- `verticalJumpStats` (VerticalJumpStatistics, optioneel) — Alleen hoogspringen / polsstokhoogspringen.
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

**Fouten:**

- `400` — Geen onderdeel-ID in het pad. `{"error": "Event ID is required"}`
- `404` — Onbekend onderdeel. `{"error": "event with ID dt-xx not found"}`

### `GET /api/v1/wind/gauges` {#api-wind-gauges}

Windmeters met hun laatste meting weergeven.

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

Gemiddelde wind nu, over de laatste seconden.

- `gauge_id` (query) — Verplicht. Windmeter-ID uit /wind/gauges.
- `duration` (query) — Middelingsvenster in seconden, 1-60. Standaard 5.

```http
GET /api/v1/wind/current?gauge_id=back-pits&duration=5
```

**Response — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Gemiddelde windsnelheid over het venster (m/s, + = rugwind).
- `average_crosswind` (number)
- `readings` (number[]) — De afzonderlijke snelheden die gemiddeld zijn.
- `timestamp` (date-time) — Tijd van de meting (RFC 3339, op de seconde).
- `direction` (integer) — Laatste richting in graden (0-360).

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

**Fouten:**

- `400` — gauge_id ontbreekt. `{"error": "gauge_id parameter is required"}`
- `404` — Onbekende windmeter. `{"error": "Wind gauge not found"}`
- `503` — Windmeter offline of geen metingen in het venster. `{"error": "Wind gauge is offline"}`

### `GET /api/v1/wind/search` {#api-wind-search}

Wind op een eerder moment (logboek van vandaag). Zoekt de meting die het dichtst bij het tijdstip ligt in het logboek van vandaag en middelt de metingen binnen ±2.5 s daarvan. Wordt gebruikt om achteraf wind aan een sprong te koppelen.

- `gauge_id` (query) — Verplicht. Windmeter-ID.
- `timestamp` (query) — Verplicht. RFC 3339-tijd, URL-gecodeerd (bijv. `2026-06-14T14%3A02%3A10Z`).

```http
GET /api/v1/wind/search?gauge_id=back-pits&timestamp=2026-06-14T14%3A02%3A10Z
```

**Response — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Gemiddelde windsnelheid over het venster (m/s, + = rugwind).
- `average_crosswind` (number)
- `readings` (number[]) — De afzonderlijke snelheden die gemiddeld zijn.
- `timestamp` (date-time) — Tijd van de meting (RFC 3339, op de seconde).
- `direction` (integer) — Laatste richting in graden (0-360).

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

**Fouten:**

- `400` — gauge_id of timestamp ontbreekt, of timestamp is geen RFC 3339. `{"error": "Invalid timestamp format (use RFC3339)"}`
- `404` — Onbekende windmeter. `{"error": "Wind gauge not found"}`
- `503` — Vandaag geen metingen opgeslagen. `{"error": "No wind readings available"}`

### `GET /api/v1/config` {#api-config}

Schermconfiguratie. De interfacetaal die in Instellingen is gekozen, zodat schermen op andere apparaten dezelfde taal gebruiken.

```http
GET /api/v1/config
```

**Response — `ConfigResponse`:**

- `language` (string) — "en", "fr", "es", "nl" of "pt".

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

Een [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)-stream (`text/event-stream`). De server stuurt `data: update` zodra uitslagen, de status van een onderdeel of de actieve atleet veranderen — haal dan de feed die u toont opnieuw op. Een `: ping`-commentaar elke 25 seconden houdt de verbinding open. Het bericht is alleen het woord `update`, dus er is geen JSON Schema voor.

```text
: connected

data: update

: ping
```

```js
const es = new EventSource('http://polyfieldserver.local:8080/api/v1/stream');
es.onmessage = (e) => { if (e.data === 'update') refresh(); };
```

Houd een trage peiling (elke 30–60 s) aan als terugval, zoals de ingebouwde schermen doen. Zonder de stream peilt u de schermfeeds elke 1–2 seconden; statistieken hoeft u alleen op verzoek op te halen.

### Datatypen {#api-data-types}

Typen die in meerdere bodies hierboven worden gebruikt. Alle definities staan in het [downloadbare schema](/PolyField-Server/api/polyfield-api.schema.json).

#### Performance {#api-type-performance}

Eén poging van een atleet. Responses bevatten altijd unit, valid en timestamp.

- `attempt` (integer) — Pogingnummer, vanaf 1. De server herkent wijzigingen aan dit nummer.
- `mark` (string) — De prestatie. Werpen / horizontale sprongen: een afstand in meters ("45.67"), "NM" (ongeldig; "X" en "FOUL" worden geaccepteerd en genormaliseerd naar "NM") of "P" (pas; "PASS" en "-" geaccepteerd). Verticale sprongen: "O" geslaagd, "X" mislukt, "P" pas.
- `height` (string, optioneel) — Alleen verticale sprongen: lathoogte in meters ("1.85").
- `unit` (string, optioneel) — Eenheid van de prestatie, normaal "m".
- `wind` (string, optioneel) — Windmeting in m/s als string met teken ("+1.4", "-0.3"). Alleen horizontale sprongen.
- `valid` (boolean, optioneel) — true voor een geldige prestatie / geslaagde hoogte, false voor een ongeldige poging, mislukte poging of pas.
- `coordinates` (HeatmapCoordinate, optioneel) — Landingspositie van een worp of sprong.
- `timestamp` (date-time, optioneel) — Wanneer de poging plaatsvond. Wordt ingevuld met de ontvangsttijd van de server als het ontbreekt of nul is.

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

Landingspositie van een worp of sprong.

- `x` (number) — Ruwe landings-X in het assenstelsel van de EDM (m).
- `y` (number) — Ruwe landings-Y in het assenstelsel van de EDM (m).
- `distance` (number) — Gemeten afstand (m).
- `round` (integer)
- `attempt` (integer)
- `valid` (boolean)
- `rx` (number, optioneel) — Landings-X gedraaid zodat de middenlijn van de sector naar boven (+Y) wijst. Door de server berekend; alleen voor geldige worpen met kalibratie van de sectorlijnen.
- `ry` (number, optioneel) — Landings-Y in het gedraaide assenstelsel (zie rx).

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

Veldgeometrie vastgelegd bij het kalibreren van de EDM.

- `circleType` (string) — Type ring / aanloop, bijv. "SHOT", "DISCUS", "HAMMER", "JAVELIN_ARC".
- `circleRadius` (number) — Straal van de ring in meters.
- `edmPosition` (Coordinate, optioneel) — Een X/Y-positie in meters in het assenstelsel van de EDM.
- `sectorLines` (SectorLines, optioneel) — Geometrie van de sectorlijnen van een werpring.
- `timestamp` (string, optioneel) — Wanneer de kalibratie is gedaan (ISO 8601).
- `calibrationId` (string, optioneel)

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

Geometrie van de sectorlijnen van een werpring.

- `rightLine` (Coordinate) — Een X/Y-positie in meters in het assenstelsel van de EDM.
- `leftLine` (Coordinate) — Een X/Y-positie in meters in het assenstelsel van de EDM.
- `sectorAngle` (number) — Sectorhoek in graden (34.92 voor een standaard werpsector).

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

Een X/Y-positie in meters in het assenstelsel van de EDM.

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

Een deelnemer en diens serie.

- `bib` (string)
- `order` (integer) — Volgorde op de startlijst.
- `name` (string)
- `club` (string)
- `ageGroup` (string, optioneel)
- `classification` (string, optioneel) — Klasse van World Para Athletics, bijv. "F56".
- `gender` (string, optioneel) — "M" of "W" (gebruikt voor de RAZA-score).
- `sourceEventId` (string, optioneel)
- `series` (Performance[])
- `heatmapCoordinates` (HeatmapCoordinate[], optioneel)

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

Wedstrijdformat van een onderdeel.

- `attempts` (integer) — Pogingen per atleet (bijv. 3, 4 of 6).
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
- `label` (string, optioneel)

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

Body die bij elke 4xx/5xx-response van de API wordt teruggegeven.

- `error` (string) — Leesbare foutmelding.

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
