---
layout: manual
lang: fr
title: "PolyField Server — Manuel"
description: "Aide et manuel d'utilisation de PolyField Server — le serveur de contrôle des concours qui pilote la compétition, les écrans en direct, les anémomètres, les statistiques et les résultats en ligne sur le réseau de votre stade."
---

# PolyField Server

Le serveur de contrôle des concours. Une seule application de bureau fait tourner la compétition sur le réseau de votre stade : elle conserve les épreuves et les athlètes, reçoit les résultats en direct depuis l'application de terrain PolyField, pilote les écrans en direct, enregistre le vent, produit des statistiques et des visuels pour les réseaux sociaux et (en option) publie les résultats en ligne. Fonctionne sur Windows et Mac ; fonctionne sur un réseau local.

[Télécharger depuis polyfield.co.uk](https://www.polyfield.co.uk)

* TOC
{:toc}

## Aperçu    {#overview}

PolyField Server est le cœur d'une compétition de concours. Il tourne sur un seul ordinateur du réseau de votre stade et fait quatre choses à la fois :

- **Conserve la compétition** — les épreuves, les catégories d'âge, les athlètes et chaque essai, le tout stocké localement sur l'ordinateur hôte.
- **Reçoit les résultats** — les officiels mesurent au cercle ou sur la piste d'élan avec l'application de terrain PolyField (sur un appareil Android relié à une station totale EDM, ou saisis à la main), et l'application envoie chaque marque directement au serveur.
- **Pilote les écrans** — il diffuse un ensemble de pages web que n'importe quel écran du réseau ouvre dans un navigateur : un tableau de résultats en direct, les classements des épreuves, un fil pour le speaker et les classements para-athlétisme RAZA.
- **Ajoute l'analyse** — capture du vent, statistiques par épreuve et cartes de chaleur des impacts, visuels pour les réseaux sociaux, et publication optionnelle vers le cloud PolyField.

Tout fonctionne sur le réseau local — aucune connexion internet n'est nécessaire pour faire tourner une compétition, mais elle est requise pour télécharger les listes de départ depuis les fournisseurs de gestion de compétition et pour renvoyer les résultats en temps réel vers leurs systèmes. Une synchronisation est possible après le concours pour envoyer tous les résultats en une fois.

> **Validation positive.** Le serveur n'invente jamais de résultats — chaque marque provient d'un officiel via l'application de terrain. Cela garantit une chaîne claire, de la mesure au cercle jusqu'à ce qui s'affiche sur le tableau.

## Fonctionnement    {#how-it-works}

- Vous faites tourner **une seule instance** de l'application de bureau sur un ordinateur du réseau de la compétition.
- L'**application de terrain** (une par épreuve) se connecte au serveur, télécharge les athlètes de son épreuve et renvoie chaque essai au fur et à mesure de la mesure.
- Chaque **écran** ouvre l'une des pages web du serveur dans un navigateur ; les résultats se mettent à jour instantanément, sans avoir à actualiser.
- L'opérateur travaille depuis le **tableau de bord** de bureau — importer les épreuves, suivre l'avancement, exporter les statistiques et les visuels, et gérer les écrans et les anémomètres. Ceux-ci sont généralement configurés une seule fois au début de la compétition, sans intervention nécessaire pendant la journée.

## Prise en main    {#getting-started}

### 1. Charger une compétition    {#load-a-competition}

Ouvrez l'application ; le **Tableau de bord** est le poste de l'opérateur. Démarrez une compétition de trois façons :

- **Importer depuis OpenTrack ou Athletics.app** — récupérez directement la liste des épreuves et les listes de départ (voir [Importer des épreuves](#importing-events)). C'est la méthode habituelle et elle conserve l'ordre publié des listes de départ.
- **Créer les épreuves à la main** — utilisez *+ Créer une nouvelle épreuve* et ajoutez les athlètes.
- **Nouvelle compétition** — efface les données actuelles pour repartir de zéro.

Une fois chargée, chaque épreuve apparaît sous forme de carte sur le tableau de bord, indiquant son statut (Non commencée, En cours, Terminée).

### 2. Connecter l'application de terrain    {#connect-the-field-app}

Sur chaque appareil de terrain, vérifiez l'adresse du serveur dans l'application de terrain PolyField pour la connecter au serveur. L'officiel sélectionne alors son épreuve, calibre l'EDM sur le cercle ou la piste d'élan, et commence à mesurer. Voir [Les résultats et l'application de terrain](#results-and-the-field-app).

### 3. Ouvrir les écrans    {#open-the-displays}

Sur chaque écran, ouvrez un navigateur à l'adresse du serveur et ajoutez la page voulue — par exemple `http://polyfieldserver.local:8080/tables`. Utilisez **Écrans** sur le tableau de bord pour obtenir des liens en un clic et des QR codes vers chaque écran. Voir [Les écrans](#display-screens).

> **Astuce.** Laissez l'application de bureau sur le tableau de bord et pilotez tout depuis là. Les résultats arrivent automatiquement depuis l'application de terrain pendant que vous surveillez l'avancement et les écrans.

![Fenêtre Écrans — liens et QR codes pour chaque écran](/PolyField-Server/images/displays-popup.png)

## Le tableau de bord    {#the-dashboard}

Le tableau de bord liste chaque épreuve et propose les commandes principales. En haut figurent l'adresse du serveur (avec un sélecteur de réseau sur les machines à plusieurs cartes) et l'état des envois ou de la synchronisation en attente. Les actions clés :

| Commande | Rôle |
|----------|------|
| Nouvelle compétition | Effacer la compétition en cours et repartir de zéro. |
| Créer une nouvelle épreuve | Ajouter une épreuve et ses athlètes à la main. |
| Fusionner les épreuves | Combiner des épreuves (p. ex. deux groupes de la même discipline) en une seule, ou *Fusionner toutes les épreuves identiques* pour combiner d'un coup toutes les paires correspondantes. |
| Écrans | Afficher les liens cliquables et les QR codes de chaque page d'affichage (tableau, classements, speaker, RAZA). |
| Exporter les visuels | Générer les visuels pour les réseaux sociaux, les cartes de chaleur détaillées et les visuels de vent de la compétition (voir [Visuels pour les réseaux sociaux](#social-media-graphics)). |
| Exporter les statistiques | Produire le PDF des statistiques de la compétition (également sur la page Statistiques). |

Sélectionner une épreuve ouvre sa vue **Résultats en direct**, où vous voyez la série de chaque athlète, suivez l'arrivée des essais et consultez le classement.

![Le tableau de bord de PolyField Server](/PolyField-Server/images/dashboard.png)

## Importer des épreuves    {#importing-events}

Utilisez **Lien de compétition** / import pour charger une compétition plutôt que de la saisir :

- **OpenTrack** — connectez-vous et choisissez votre compétition ; le serveur télécharge les concours et leurs inscrits. L'**ordre des listes de départ** publié par OpenTrack est conservé à l'identique.
- **Athletics.app** — saisissez le code du lien de compétition pour créer les épreuves et les athlètes. L'**ordre des listes de départ** publié par Athletics.app est conservé à l'identique.

Les épreuves importées conservent leur numérotation et leurs codes d'origine, afin de correspondre au programme publié et à l'export des résultats.

![Importer une compétition](/PolyField-Server/images/import-opentrack.png)

## Les résultats et l'application de terrain    {#results-and-the-field-app}

Les résultats sont saisis sur le terrain, pas sur le serveur. Chaque épreuve utilise l'application de terrain PolyField sur un appareil Android :

- L'appareil se connecte au serveur et télécharge les athlètes de l'épreuve choisie.
- Pour les lancers et les sauts horizontaux, l'application peut être reliée à une **station totale EDM** ou fonctionner directement sur une station totale PolyField (PolyField APEKS AM02i) ; l'officiel calibre sur le cercle / la piste d'élan / la planche, et chaque marque mesurée (avec sa coordonnée d'impact) est envoyée au serveur. Les marques peuvent aussi être saisies à la main.
- Les **sauts verticaux** (hauteur, perche) sont entièrement pris en charge — les hauteurs, les franchissements (O/X) et la progression de la barre sont enregistrés et envoyés.
- Chaque essai porte son propre horodatage, de sorte que le serveur affiche les résultats dans leur ordre réel et peut produire des statistiques de temps précises.

À mesure que les résultats arrivent, la carte de l'épreuve se met à jour, les classements se recalculent, et tout écran connecté s'actualise instantanément.

![Résultats en direct — tableau des résultats](/PolyField-Server/images/live-results-table.png)

![Résultats en direct — carte de chaleur des impacts](/PolyField-Server/images/live-results-heatmap.png)

## Les écrans    {#display-screens}

Le serveur diffuse quatre pages d'affichage en direct. Chacune est une page web ordinaire — ouvrez-la dans n'importe quel navigateur du réseau ; rien n'est à installer sur l'écran. Toutes se mettent à jour automatiquement : les nouveaux résultats sont poussés dès leur arrivée, avec une interrogation périodique en filet de sécurité, si bien qu'un écran n'a jamais besoin d'être actualisé.

| Page | URL |
|------|-----|
| Tableau de résultats (derniers résultats) | `/` |
| Classements des épreuves (tables) | `/tables` |
| Fil du speaker | `/announcer` |
| Classements RAZA (para-athlétisme) | `/raza` |

### Tableau de résultats    {#display-board}

Un grand tableau des performances les plus récentes, avec l'athlète, l'épreuve, la marque et — pour les lancers — une visualisation de l'impact. Idéal comme écran de résultats principal pour le public.

![Tableau de résultats](/PolyField-Server/images/display-board.png)

### Classements des épreuves    {#event-standings}

Les classements en direct, plusieurs épreuves à la fois, chacun classé avec les surlignages or/argent/bronze. La mise en page s'adapte à la hauteur : elle remplit l'écran, empile davantage d'épreuves sur les écrans hauts ou en mode portrait, et lorsqu'une épreuve compte beaucoup d'athlètes, elle les fait défiler page par page. Les épreuves alternent aussi pour que chaque épreuve du programme passe à l'écran.

![Écran des classements des épreuves](/PolyField-Server/images/display-tables.png)

### Speaker    {#announcer}

Un fil des résultats à mesure qu'ils arrivent — le plus récent en haut, avec la place, l'athlète, le club, l'épreuve et la marque — dimensionné pour être lu d'un coup d'œil depuis un poste de speaker ou de commentaire.

![Fil du speaker](/PolyField-Server/images/display-announcer.png)

### Classements RAZA    {#raza-rankings}

Classements para-athlétisme calculés avec le système de points World Para Athletics (RAZA), afin de comparer sur un même tableau des athlètes de classifications différentes. Une classification et un genre doivent être renseignés pour qu'un score RAZA soit calculé.

![Écran des classements RAZA](/PolyField-Server/images/display-raza.png)

## Anémomètres    {#wind-gauges}

PolyField Server lit les anémomètres via le réseau et enregistre le vent pour toute la journée de compétition. Il prend en charge le **Gill WindSonic 75** et le **PolyField Wind Mini**, et **détecte le type d'anémomètre automatiquement** d'après son flux de données — aucun protocole à choisir. Ajoutez un anémomètre avec son adresse réseau ; dès qu'il émet, le serveur affiche le modèle détecté et commence l'enregistrement.

- Le vent est capturé en continu et stocké par jour, il est donc disponible pour la validité des sauts horizontaux, les statistiques et les visuels de vent.
- La page **Anémomètres** montre chaque appareil en direct et permet d'exporter un visuel de vent de la journée complète.
- Les anémomètres peuvent être masqués de la sélection des athlètes (par exemple un anémomètre général de piste conservé uniquement pour l'historique).

![La page Anémomètres](/PolyField-Server/images/wind-gauges.png)

## Statistiques et cartes de chaleur    {#statistics-and-heatmaps}

La page **Statistiques** transforme les données de la compétition en analyse :

- **Graphiques par épreuve** — performance dans le temps, comparaison tour par tour, taux d'essais mordus et de réussite, et temps entre les essais.
- **Cartes de chaleur des impacts** — pour les lancers, chaque impact tracé dans le secteur, coloré par tour, avec l'angle moyen d'impact par rapport à l'axe central du secteur, l'étendue et la variance.
- **Vent** — moyenne, validité et tendance sur la session pour chaque anémomètre.
- **Exporter les statistiques** — un PDF complet de la compétition avec les graphiques, les cartes de chaleur et les récapitulatifs par épreuve, daté du jour de la compétition.

Les graphiques et les cartes de chaleur s'adaptent au réglage de taille d'affichage afin de rester lisibles sur l'écran de l'opérateur.

![Statistiques — carte de chaleur des impacts d'un lancer](/PolyField-Server/images/statistics-heatmap.png)

## Visuels pour les réseaux sociaux    {#social-media-graphics}

**Exporter les visuels** produit un ensemble d'images carrées (1080 × 1080) prêtes à publier, toutes dans un style PolyField cohérent :

- **Récapitulatif de compétition** — les totaux marquants du concours, avec le plus long lancer et le plus long saut.
- **Cartes par épreuve** — le podium, les conditions de l'épreuve et les totaux. Les cartes de saut vertical montrent la série de franchissements de chaque athlète à sa meilleure hauteur ainsi qu'une répartition du taux de réussite au 1er / 2e / 3e essai ; les cartes de saut horizontal montrent le vent.
- **Cartes de chaleur détaillées** — le nuage complet des impacts pour chaque lancer.
- **Visuels de vent** — la tendance du vent sur la journée complète pour chaque anémomètre, avec la validité et les rafales.

Les visuels ne sont produits que pour les épreuves qui ont eu lieu, et chaque carte porte la date de la compétition et l'identité visuelle PolyField.

![Exemple de carte d'épreuve exportée](/PolyField-Server/images/social-example.png)

![Visuel de vent pour les réseaux sociaux (export)](/PolyField-Server/images/wind-gauges-social.png)

## Résultats en ligne — en test    {#cloud-results}

En option, le serveur publie les résultats vers le cloud PolyField pour que le public puisse suivre en ligne sur [results.polyfield.co.uk](https://results.polyfield.co.uk). Deux choses peuvent être envoyées, chacune activable dans les Réglages :

- **Résultats et cartes de chaleur des athlètes** — des pages individuelles anonymisées pour réduire les informations identifiables conservées avec leurs marques et une carte de chaleur des impacts. Elles s'auto-suppriment après 90 jours.
- **Carte de chaleur globale** — une image agrégée des impacts sur l'ensemble de la compétition. Elle est anonymisée, sans donnée individuelle d'athlète, et conservée indéfiniment.

Les envois sont mis en file d'attente et réessayés, de sorte qu'une brève coupure d'internet ne perd aucune donnée — la compétition elle-même continue de tourner sur le réseau local quoi qu'il arrive.

## Lien de compétition    {#competition-link}

**Lien de compétition** est l'endroit où vous connectez les fournisseurs de gestion de compétition au serveur. Il propose les commandes d'import OpenTrack / Athletics.app pour charger les épreuves.

![Lien de compétition — adresse du serveur et QR code](/PolyField-Server/images/competition-link.png)

## Réglages, taille d'affichage et langue    {#settings}

- **Taille d'affichage** — adapte l'interface de l'opérateur, les graphiques statistiques et les cartes de chaleur à l'écran sur lequel vous faites tourner le serveur.
- **Langue** — l'interface est disponible en anglais, français, espagnol, néerlandais et portugais.
- **Envoi vers le cloud** — active ou désactive la publication des athlètes et des cartes de chaleur.
- **Dossiers** — définit les dossiers utilisés pour l'import des épreuves, les sauvegardes locales sur le PC, et l'export des résultats et des visuels.

![Réglages](/PolyField-Server/images/settings.png)

## Réseau    {#networking}

- L'application diffuse sur le **port 8080** et s'annonce comme `polyfieldserver.local`, si bien que les appareils de terrain et les écrans peuvent utiliser `http://polyfieldserver.local:8080` sans connaître l'adresse IP. Certains appareils Android exigent l'adresse IP complète ; vous pouvez alors utiliser `http://192.168.0.10:8080` en remplaçant 192.168.0.10 par l'adresse du serveur affichée sur le tableau de bord.
- Sur les ordinateurs équipés de plusieurs cartes réseau (fréquent sous Windows), choisissez la bonne carte en haut du tableau de bord afin que la bonne adresse soit annoncée.
- Tous les appareils — applications de terrain et écrans — doivent être sur le même réseau que l'ordinateur hôte.

## Diagnostic    {#diagnostics}

En cas de problème, utilisez le rapport de diagnostic. Il rassemble la compétition en cours (que le support peut rejouer), les journaux et les données de vent du jour dans un seul fichier zip, et pré-remplit un e-mail vers [support@polyfield.co.uk](mailto:support@polyfield.co.uk). Joignez le fichier enregistré avant l'envoi. Le même fichier peut servir à récupérer une compétition s'il faut changer de machine en cours de concours.

![Rapport de diagnostic](/PolyField-Server/images/diagnostics.png)

## Dépannage    {#troubleshooting}

| Symptôme | À vérifier |
|----------|------------|
| Un appareil de terrain ne se connecte pas | Vérifiez qu'il est sur le même réseau, que le port 8080 est accessible et (PC multi-cartes) que la bonne carte réseau est sélectionnée en haut du tableau de bord. Assurez-vous que votre pare-feu ne bloque pas PolyField Server. |
| Un import renvoie 0 épreuve | La compétition source n'a peut-être pas encore d'inscrits, ou une autre compétition est sélectionnée. Vérifiez que les listes de départ ont bien été publiées. |
| Un écran ne se met pas à jour | Les pages se mettent à jour toutes seules ; si l'une est figée, actualisez-la une fois. Vérifiez qu'elle pointe vers l'adresse actuelle du serveur. Les écrans affichent l'heure courante et la mention « LIVE » lorsqu'ils sont connectés, pour aider à vérifier. |
| Un anémomètre n'affiche aucune valeur | Vérifiez l'adresse réseau de l'anémomètre, qu'il est alimenté et qu'il émet ; le modèle est détecté automatiquement dès que des données arrivent. L'anémomètre affiche un statut En ligne / Hors ligne sur le serveur. |
| Le tableau RAZA est vide | Une classification et un genre doivent être renseignés pour qu'un score RAZA soit calculé. |
| Les résultats semblent dans le désordre ou un tour manque | Chaque résultat est horodaté par l'application de terrain ; assurez-vous que les appareils de terrain sont sur la bonne épreuve et à jour. Vérifiez que l'horloge de l'appareil de terrain et du serveur est correcte, elle peut dériver en usage hors ligne prolongé. |

## Téléchargement et support    {#download-and-support}

Téléchargez la dernière version depuis [www.polyfield.co.uk](https://www.polyfield.co.uk) ou la page des versions. L'application vérifie les mises à jour au démarrage et affiche une bannière quand une version plus récente est disponible. Support : [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

## Intégration API {#api-integration}

PolyField Server fournit une **API HTTP + JSON** sur le **port 8080**, sur le **même réseau local** que vos appareils de terrain et vos écrans. C'est la même interface que celle utilisée par l'application de terrain PolyField et les écrans intégrés : tout appareil du réseau local — un tableau d'affichage personnalisé, un tableau de bord de statistiques, une incrustation vidéo pour le streaming, la signalétique propre au stade — peut lire les épreuves, les résultats en direct, les classements, les statistiques et le vent directement depuis le serveur. Les réponses sont en JSON, il n'y a pas d'authentification et le CORS est ouvert : une page web du réseau local peut donc l'appeler directement. La plupart des points d'accès sont des `GET` en lecture seule ; les points d'accès en écriture (`POST /api/v1/results`, `POST /api/v1/athlete/active`, `PUT /api/v1/events/status`) sont utilisés par l'application de terrain.

L'API est **limitée au réseau local par conception** — l'application ne l'expose pas à Internet. **Toute intégration côté WAN ou Internet** (tableaux d'affichage distants, services cloud, second stade) **doit d'abord être discutée avec nous** afin d'être réalisée en toute sécurité, généralement via un VPN ou un proxy inverse contrôlé plutôt qu'en ouvrant le port au monde entier. Contactez [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

**URL de base :** `http://polyfieldserver.local:8080/api/v1` — ou utilisez l'adresse IP du serveur affichée en haut du tableau de bord (p. ex. `http://192.168.0.10:8080/api/v1`).

**JSON Schema :** chaque corps de requête et de réponse est défini dans un seul [fichier JSON Schema (draft 2020-12)](/PolyField-Server/api/polyfield-api.schema.json), sous `$defs`. Chaque point d'accès ci-dessous indique le type de son corps et inclut son schéma ; les types partagés sont décrits dans [Types de données](#api-data-types). Pour valider un corps, référencez sa définition, p. ex. `polyfield-api.schema.json#/$defs/ResultPayload`.

**Conventions**

- Les erreurs renvoient un statut 4xx/5xx avec `{"error": "message"}`. Une méthode non acceptée par un point d'accès renvoie `405`.
- Les horodatages sont au format RFC 3339, p. ex. `2026-06-14T13:42:07.512+01:00`.
- Les performances et les hauteurs sont des chaînes en mètres (`"46.38"`) afin de conserver les zéros finaux ; le vent est une chaîne signée en m/s (`"+1.4"`).
- Les champs facultatifs sont omis lorsqu'ils sont vides. Les tables indexées par tour utilisent des clés texte (`"1"`, `"2"`, …).

| Méthode et chemin | Renvoie |
|---|---|
| [`GET /api/v1/events`](#api-list-events) | Lister toutes les épreuves (résumé). |
| [`GET /api/v1/events/{eventId}`](#api-get-event) | Obtenir une épreuve avec ses athlètes et tous les essais. |
| [`PUT/PATCH /api/v1/events/status`](#api-update-status) | Définir le statut d'une épreuve. |
| [`POST /api/v1/results`](#api-post-results) | Envoyer la série d'un athlète (principale écriture de l'application de terrain). |
| [`POST /api/v1/athlete/active`](#api-post-active) | Signaler l'athlète en cours (sauts horizontaux). |
| [`GET /api/v1/athlete/active/{eventId}`](#api-get-active) | Lire l'athlète en cours dans une épreuve. |
| [`GET /api/v1/display/recent`](#api-display-recent) | Dernières performances (tableau de résultats). |
| [`GET /api/v1/display/standings`](#api-display-standings) | Classements actuels de chaque épreuve ayant des performances. |
| [`GET /api/v1/broadcast/recent`](#api-broadcast-recent) | Les 10 derniers résultats en détail (diffusion / speaker). |
| [`GET /api/v1/raza`](#api-raza) | Classements para-athlétisme RAZA. |
| [`GET /api/v1/statistics/overall`](#api-stats-overall) | Statistiques de l'ensemble de la compétition. |
| [`GET /api/v1/statistics/event/{eventId}`](#api-stats-event) | Statistiques détaillées d'une épreuve. |
| [`GET /api/v1/wind/gauges`](#api-wind-gauges) | Lister les anémomètres et leur dernière mesure. |
| [`GET /api/v1/wind/current`](#api-wind-current) | Vent moyen actuel, sur les dernières secondes. |
| [`GET /api/v1/wind/search`](#api-wind-search) | Vent à un moment passé (journal du jour). |
| [`GET /api/v1/config`](#api-config) | Configuration des écrans. |
| [`GET /api/v1/stream`](#api-stream) | Notifications de mise à jour en direct (Server-Sent Events). |

### `GET /api/v1/events` {#api-list-events}

Lister toutes les épreuves (résumé). Renvoie chaque épreuve chargée sur le serveur sous forme de résumé léger. L'application de terrain s'en sert pour proposer le choix de l'épreuve.

```http
GET /api/v1/events
```

**Réponse — tableau de `EventSummary`:**

- `id` (string)
- `name` (string)
- `type` (string) — Catégorie de l'épreuve. Valeurs connues : "Throws", "Horizontal Jumps", "Vertical Jumps".

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

**Erreurs :**

- `405` — Toute méthode autre que GET.

### `GET /api/v1/events/{eventId}` {#api-get-event}

Obtenir une épreuve avec ses athlètes et tous les essais. Renvoie l'épreuve complète. Utilisé par l'application de terrain pour télécharger la liste de départ et les résultats déjà enregistrés.

- `eventId` (chemin) — ID de l'épreuve, issu de la liste des épreuves (à encoder dans l'URL).

```http
GET /api/v1/events/dt-sw-f07
```

**Réponse — `Event`:**

- `id` (string)
- `name` (string)
- `originalName` (string, facultatif)
- `type` (string) — Catégorie de l'épreuve. Valeurs connues : "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `rules` (EventRules) — Format de compétition d'une épreuve.
- `athletes` (Athlete[])
- `calibrationMetadata` (CalibrationMetadata, facultatif) — Géométrie du terrain relevée lors de l'étalonnage de l'EDM.
- `lastResultTime` (date-time, facultatif)
- `signedOff` (boolean, facultatif)
- `signedOffBy` (string, facultatif)
- `signedOffAt` (date-time, facultatif)
- `evtEventNumber` (string, facultatif)
- `evtRoundNumber` (string, facultatif)
- `evtHeatNumber` (string, facultatif)
- `opentrackUnitId` (string, facultatif)
- `opentrackEventId` (string, facultatif)
- `opentrackEventCode` (string, facultatif)
- `opentrackUrl` (string, facultatif)
- `athleticsAppLinkCode` (string, facultatif)
- `isMerged` (boolean, facultatif)
- `isHidden` (boolean, facultatif)
- `mergedEventId` (string, facultatif)
- `sourceEventIds` (string[], facultatif)
- `sourceEventNames` (string[], facultatif)

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

**Erreurs :**

- `400` — Pas d'ID d'épreuve dans le chemin. `{"error": "Event ID is required"}`
- `404` — Épreuve inconnue. `{"error": "event with ID dt-xx not found"}`

### `PUT / PATCH /api/v1/events/status` {#api-update-status}

Définir le statut d'une épreuve. Fait passer une épreuve entre Not Started, In Progress et Finished. Le serveur passe aussi automatiquement une épreuve à In Progress à la réception de son premier résultat valable.

**Corps de la requête — `EventStatusUpdate`:**

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

**Réponse — `SuccessResponse`:**

- `status` ("success")
- `message` (string, facultatif)

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

**Erreurs :**

- `400` — Champ manquant, épreuve inconnue ou statut invalide. `{"error": "invalid status: Done. Must be one of: Not Started, In Progress, Finished"}`

### `POST /api/v1/results` {#api-post-results}

Envoyer la série d'un athlète (principale écriture de l'application de terrain). Envoie la série **complète** de l'athlète jusqu'ici ; elle remplace ce que le serveur détient pour cet athlète, un nouvel envoi est donc sans risque. Le serveur détermine quels essais sont nouveaux ou modifiés, met à jour les classements et envoie un `update` aux écrans. Les performances sont normalisées : `X`/`FOUL` deviennent `NM`, `PASS`/`-` deviennent `P`. Une performance hors limites est journalisée mais tout de même enregistrée. Si le dossard n'est pas dans l'épreuve, un athlète provisoire est ajouté.

**Corps de la requête — `ResultPayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `series` (Performance[]) — La série complète de l'athlète jusqu'ici. Elle remplace la série enregistrée.
- `heatmapCoordinates` (HeatmapCoordinate[], facultatif)
- `calibrationMetadata` (CalibrationMetadata, facultatif) — Géométrie du terrain relevée lors de l'étalonnage de l'EDM.

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

*Saut horizontal avec vent:*

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

*Saut vertical (un essai par entrée, avec la hauteur de barre):*

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

**Réponse — `SuccessResponse`:**

- `status` ("success")
- `message` (string, facultatif)

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

**Erreurs :**

- `400` — Le corps n'est pas du JSON valide. `{"error": "Invalid request body"}`
- `404` — Épreuve inconnue. `{"error": "event with ID dt-xx not found"}`

### `POST /api/v1/athlete/active` {#api-post-active}

Signaler l'athlète en cours (sauts horizontaux). Signal sans accusé envoyé par l'application de terrain lorsqu'un sauteur devient l'athlète en cours, utilisé par l'affichage de la règle de planche d'appel. Un athlète par épreuve : chaque envoi remplace le précédent. Ce n'est **pas** un résultat.

**Corps de la requête — `ActiveAthletePayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `athleteName` (string, facultatif)
- `board` (number, facultatif) — Distance de la planche d'appel en mètres (0 = planche de longueur).
- `topPerformances` (number[], facultatif) — Meilleures performances valables jusqu'ici, de la meilleure à la moins bonne. Limité à 3.

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

**Réponse — `OkResponse`:**

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

**Erreurs :**

- `400` — JSON invalide, ou eventId / athleteBib manquant. `{"error": "eventId and athleteBib are required"}`

### `GET /api/v1/athlete/active/{eventId}` {#api-get-active}

Lire l'athlète en cours dans une épreuve. Toujours 200 pour qu'un widget puisse interroger simplement ; `active` vaut `null` si aucun athlète n'a été signalé (entre deux athlètes ou après un redémarrage).

- `eventId` (chemin) — ID de l'épreuve.

```http
GET /api/v1/athlete/active/dt-sw-f07
```

**Réponse — `ActiveAthleteResponse`:**

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

*Aucun athlète en cours:*

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

**Erreurs :**

- `400` — Pas d'ID d'épreuve dans le chemin. `{"error": "Event ID is required"}`

### `GET /api/v1/display/recent` {#api-display-recent}

Dernières performances (tableau de résultats). Les performances les plus récentes, de la plus récente à la plus ancienne. Alimente le tableau de résultats sur `/`.

- `limit` (requête) — Nombre de résultats à renvoyer, 1-100. 4 par défaut ; une valeur hors limites revient à 4.

```http
GET /api/v1/display/recent?limit=2
```

**Réponse — `RecentPerformancesResponse`:**

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

Classements actuels de chaque épreuve ayant des performances. Classements de chaque épreuve ayant au moins une performance valable. Alimente l'écran `/tables`. `events` vaut `null` tant qu'aucune épreuve n'a de performance valable.

```http
GET /api/v1/display/standings
```

**Réponse — `EventStandingsResponse`:**

- `events` (EventStandings[]) — Uniquement les épreuves ayant au moins une performance valable. null s'il n'y en a aucune.

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

Les 10 derniers résultats en détail (diffusion / speaker). Jusqu'aux 10 résultats les plus récents, du plus récent au plus ancien, avec assez de détails pour redessiner chacun (lignes de secteur, point d'impact, hauteur de barre et série). Alimente la page `/announcer`.

```http
GET /api/v1/broadcast/recent
```

**Réponse — `DetailedRecentResultsResponse`:**

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

Classements para-athlétisme RAZA. Les athlètes ayant une classification et un sexe, notés avec les points RAZA de World Para Athletics et regroupés par épreuve de référence. Alimente l'écran `/raza`.

```http
GET /api/v1/raza
```

**Réponse — `RazaResponse`:**

- `events` (RazaEventGroup[])
- `total` (integer) — Nombre total d'athlètes classés.

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

Statistiques de l'ensemble de la compétition. Totaux, durées, taux d'essais nuls, essais dans le temps, chronologie des épreuves et zones d'impact par type de lancer.

```http
GET /api/v1/statistics/overall
```

**Réponse — `OverallStatistics`:**

- `totalEvents` (integer)
- `eventsNotStarted` (integer)
- `eventsInProgress` (integer)
- `eventsCompleted` (integer)
- `totalAthletes` (integer)
- `totalAttempts` (integer)
- `totalValidAttempts` (integer)
- `totalFouls` (integer)
- `overallFoulRate` (number) — Pourcentage 0-100.
- `competitionStartTime` (date-time, facultatif)
- `competitionEndTime` (date-time, facultatif)
- `totalDuration` (number) — Minutes.
- `eventsWithOpenTrack` (integer)
- `eventsWithCalibration` (integer)
- `eventsByType` (object) — Nombre d'épreuves par catégorie.
- `attemptsOverTime` (TimeSeriesPoint[])
- `eventTimeline` (EventTimelineItem[])
- `throwHeatmaps` (object, facultatif) — Indexé par code de type de lancer.

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

**Erreurs :**

- `500` — Les statistiques n'ont pas pu être calculées.

### `GET /api/v1/statistics/event/{eventId}` {#api-stats-event}

Statistiques détaillées d'une épreuve. Durées, tours, essais nuls, performances et données de graphiques d'une épreuve. `windStats`, `heatmapStats` et `verticalJumpStats` n'apparaissent que pour le type d'épreuve correspondant. Les tables indexées par tour utilisent le numéro du tour comme clé texte.

- `eventId` (chemin) — ID de l'épreuve.

```http
GET /api/v1/statistics/event/dt-sw-f07
```

**Réponse — `EventStatistics`:**

- `eventId` (string)
- `eventName` (string)
- `eventType` (string) — Catégorie de l'épreuve. Valeurs connues : "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `calibrationTime` (date-time, facultatif)
- `firstAttemptTime` (date-time, facultatif)
- `lastAttemptTime` (date-time, facultatif)
- `setupDuration` (number) — Minutes entre l'étalonnage et le premier essai.
- `competitionDuration` (number) — Minutes entre le premier et le dernier essai.
- `totalEventDuration` (number) — Minutes entre l'étalonnage et le dernier essai.
- `averageTimeBetween` (number) — Secondes entre les essais.
- `roundDurations` (object) — Tour -> minutes.
- `avgTimePerAttemptByRound` (object) — Tour -> minutes moyennes entre les essais.
- `timeBetweenRounds` (object) — Tour -> écart avec le tour suivant (minutes).
- `totalAthletes` (integer)
- `athletesCompleted` (integer)
- `athletesInProgress` (integer)
- `athletesNotStarted` (integer)
- `totalAttempts` (integer)
- `validAttempts` (integer)
- `fouls` (integer)
- `foulRate` (number)
- `winningMark` (string, facultatif)
- `averageMark` (number)
- `medianMark` (number)
- `bestMarkPerRound` (object) — Tour -> meilleure performance.
- `foulRateByRound` (object) — Tour -> taux d'essais nuls.
- `athletesWithZeroFouls` (integer)
- `fastestAthlete` (AthleteTimingInfo, facultatif)
- `slowestAthlete` (AthleteTimingInfo, facultatif)
- `mostConsistent` (AthleteConsistencyInfo, facultatif)
- `windStats` (WindStatistics, facultatif) — Sauts horizontaux uniquement.
- `heatmapStats` (HeatmapStatistics, facultatif) — Lancers avec points d'impact uniquement.
- `verticalJumpStats` (VerticalJumpStatistics, facultatif) — Hauteur et perche uniquement.
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

**Erreurs :**

- `400` — Pas d'ID d'épreuve dans le chemin. `{"error": "Event ID is required"}`
- `404` — Épreuve inconnue. `{"error": "event with ID dt-xx not found"}`

### `GET /api/v1/wind/gauges` {#api-wind-gauges}

Lister les anémomètres et leur dernière mesure.

```http
GET /api/v1/wind/gauges
```

**Réponse — `WindGaugesResponse`:**

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

Vent moyen actuel, sur les dernières secondes.

- `gauge_id` (requête) — Obligatoire. ID de l'anémomètre issu de /wind/gauges.
- `duration` (requête) — Fenêtre de moyenne en secondes, 1-60. 5 par défaut.

```http
GET /api/v1/wind/current?gauge_id=back-pits&duration=5
```

**Réponse — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Vitesse moyenne du vent sur la fenêtre (m/s, + = vent arrière).
- `average_crosswind` (number)
- `readings` (number[]) — Les vitesses individuelles utilisées pour la moyenne.
- `timestamp` (date-time) — Heure de la mesure (RFC 3339, à la seconde près).
- `direction` (integer) — Dernière direction en degrés (0-360).

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

**Erreurs :**

- `400` — gauge_id manquant. `{"error": "gauge_id parameter is required"}`
- `404` — Anémomètre inconnu. `{"error": "Wind gauge not found"}`
- `503` — Anémomètre hors ligne ou aucune mesure dans la fenêtre. `{"error": "Wind gauge is offline"}`

### `GET /api/v1/wind/search` {#api-wind-search}

Vent à un moment passé (journal du jour). Trouve la mesure la plus proche de l'horodatage dans le journal du jour et fait la moyenne des mesures à ±2.5 s autour. Sert à associer le vent à un saut après coup.

- `gauge_id` (requête) — Obligatoire. ID de l'anémomètre.
- `timestamp` (requête) — Obligatoire. Heure RFC 3339, encodée pour l'URL (p. ex. `2026-06-14T14%3A02%3A10Z`).

```http
GET /api/v1/wind/search?gauge_id=back-pits&timestamp=2026-06-14T14%3A02%3A10Z
```

**Réponse — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Vitesse moyenne du vent sur la fenêtre (m/s, + = vent arrière).
- `average_crosswind` (number)
- `readings` (number[]) — Les vitesses individuelles utilisées pour la moyenne.
- `timestamp` (date-time) — Heure de la mesure (RFC 3339, à la seconde près).
- `direction` (integer) — Dernière direction en degrés (0-360).

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

**Erreurs :**

- `400` — gauge_id ou timestamp manquant, ou timestamp non conforme à RFC 3339. `{"error": "Invalid timestamp format (use RFC3339)"}`
- `404` — Anémomètre inconnu. `{"error": "Wind gauge not found"}`
- `503` — Aucune mesure enregistrée aujourd'hui. `{"error": "No wind readings available"}`

### `GET /api/v1/config` {#api-config}

Configuration des écrans. La langue de l'interface choisie dans les Réglages, pour que les écrans sur d'autres appareils l'utilisent aussi.

```http
GET /api/v1/config
```

**Réponse — `ConfigResponse`:**

- `language` (string) — "en", "fr", "es", "nl" ou "pt".

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

Un flux [Server-Sent Events](https://developer.mozilla.org/fr/docs/Web/API/Server-sent_events) (`text/event-stream`). Le serveur envoie `data: update` dès que les résultats, le statut d'une épreuve ou l'athlète en cours changent — rechargez alors le flux que vous affichez. Un commentaire `: ping` toutes les 25 secondes maintient la connexion ouverte. Le message se limite au mot `update` ; il n'a donc pas de JSON Schema.

```text
: connected

data: update

: ping
```

```js
const es = new EventSource('http://polyfieldserver.local:8080/api/v1/stream');
es.onmessage = (e) => { if (e.data === 'update') refresh(); };
```

Conservez une interrogation lente (toutes les 30–60 s) en secours, comme le font les écrans intégrés. Sans le flux, interrogez les flux d'affichage toutes les 1 à 2 secondes ; les statistiques ne doivent être récupérées qu'à la demande.

### Types de données {#api-data-types}

Types utilisés dans plusieurs des corps ci-dessus. Toutes les définitions figurent dans le [schéma téléchargeable](/PolyField-Server/api/polyfield-api.schema.json).

#### Performance {#api-type-performance}

Un essai d'un athlète. Les réponses incluent toujours unit, valid et timestamp.

- `attempt` (integer) — Numéro de l'essai, à partir de 1. Le serveur identifie les modifications par ce numéro.
- `mark` (string) — La performance. Lancers / sauts horizontaux : une distance en mètres ("45.67"), "NM" (essai nul ; "X" et "FOUL" sont acceptés et normalisés en "NM") ou "P" (passe ; "PASS" et "-" acceptés). Sauts verticaux : "O" franchissement, "X" échec, "P" passe.
- `height` (string, facultatif) — Sauts verticaux uniquement : hauteur de barre en mètres ("1.85").
- `unit` (string, facultatif) — Unité de la performance, normalement "m".
- `wind` (string, facultatif) — Mesure du vent en m/s sous forme de chaîne signée ("+1.4", "-0.3"). Sauts horizontaux uniquement.
- `valid` (boolean, facultatif) — true pour une performance / un franchissement valable, false pour un essai nul, un échec ou une passe.
- `coordinates` (HeatmapCoordinate, facultatif) — Point d'impact d'un lancer ou d'un saut.
- `timestamp` (date-time, facultatif) — Moment de l'essai. Rempli avec l'heure de réception par le serveur s'il est omis ou nul.

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

Point d'impact d'un lancer ou d'un saut.

- `x` (number) — X brut du point d'impact dans le repère de l'EDM (m).
- `y` (number) — Y brut du point d'impact dans le repère de l'EDM (m).
- `distance` (number) — Distance mesurée (m).
- `round` (integer)
- `attempt` (integer)
- `valid` (boolean)
- `rx` (number, facultatif) — X du point d'impact après rotation, l'axe central du secteur pointant vers le haut (+Y). Calculé par le serveur ; uniquement pour les lancers valables avec étalonnage des lignes de secteur.
- `ry` (number, facultatif) — Y du point d'impact dans le repère après rotation (voir rx).

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

Géométrie du terrain relevée lors de l'étalonnage de l'EDM.

- `circleType` (string) — Type de cercle / piste d'élan, p. ex. "SHOT", "DISCUS", "HAMMER", "JAVELIN_ARC".
- `circleRadius` (number) — Rayon du cercle en mètres.
- `edmPosition` (Coordinate, facultatif) — Une position X/Y en mètres dans le repère de l'EDM.
- `sectorLines` (SectorLines, facultatif) — Géométrie des lignes de secteur d'un cercle de lancer.
- `timestamp` (string, facultatif) — Moment de l'étalonnage (ISO 8601).
- `calibrationId` (string, facultatif)

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

Géométrie des lignes de secteur d'un cercle de lancer.

- `rightLine` (Coordinate) — Une position X/Y en mètres dans le repère de l'EDM.
- `leftLine` (Coordinate) — Une position X/Y en mètres dans le repère de l'EDM.
- `sectorAngle` (number) — Angle du secteur en degrés (34.92 pour un secteur de lancer standard).

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

Une position X/Y en mètres dans le repère de l'EDM.

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

Un concurrent et sa série.

- `bib` (string)
- `order` (integer) — Ordre de la liste de départ.
- `name` (string)
- `club` (string)
- `ageGroup` (string, facultatif)
- `classification` (string, facultatif) — Classe World Para Athletics, p. ex. "F56".
- `gender` (string, facultatif) — "M" ou "W" (utilisé pour le calcul RAZA).
- `sourceEventId` (string, facultatif)
- `series` (Performance[])
- `heatmapCoordinates` (HeatmapCoordinate[], facultatif)

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

Format de compétition d'une épreuve.

- `attempts` (integer) — Essais par athlète (p. ex. 3, 4 ou 6).
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
- `label` (string, facultatif)

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

Corps renvoyé avec chaque réponse 4xx/5xx de l'API.

- `error` (string) — Message d'erreur lisible.

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
