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
- **Taal** — de interface is beschikbaar in het Engels, Frans, Spaans en Nederlands.
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
