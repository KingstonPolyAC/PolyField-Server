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

![Vue Résultats en direct d'une épreuve](/PolyField-Server/images/live-results.png)

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
- **Langue** — l'interface est disponible en anglais, français, espagnol et néerlandais.
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
