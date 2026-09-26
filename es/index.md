---
layout: manual
lang: es
title: "PolyField Server — Manual"
description: "Ayuda y manual de usuario de PolyField Server — el servidor de control de concursos que gestiona la competición, las pantallas en directo, los anemómetros, las estadísticas y los resultados en línea a través de la red de su instalación."
---

# PolyField Server

El servidor de control de concursos. Una sola aplicación de escritorio gestiona la competición en la red de su instalación: guarda las pruebas y los atletas, recibe los resultados en directo desde la aplicación de campo PolyField, controla las pantallas en directo, registra el viento, genera estadísticas y gráficos para redes sociales y (opcionalmente) publica los resultados en línea. Funciona en Windows y Mac; funciona en una red local.

[Descargar desde polyfield.co.uk](https://www.polyfield.co.uk)

* TOC
{:toc}

## Resumen    {#overview}

PolyField Server es el centro de una competición de concursos. Se ejecuta en un único ordenador de la red de su instalación y hace cuatro cosas a la vez:

- **Guarda la competición** — las pruebas, las categorías de edad, los atletas y cada intento, todo almacenado localmente en el ordenador anfitrión.
- **Recibe los resultados** — los jueces miden en el círculo o en el pasillo con la aplicación de campo PolyField (en un dispositivo Android conectado a una estación total EDM, o introducidos a mano), y la aplicación envía cada marca directamente al servidor.
- **Controla las pantallas** — sirve un conjunto de páginas web que cualquier pantalla de la red abre en un navegador: un marcador de resultados en directo, las clasificaciones de las pruebas, un canal para el locutor y las clasificaciones de para-atletismo RAZA.
- **Añade análisis** — captura de viento, estadísticas por prueba y mapas de calor de caídas, gráficos para redes sociales y publicación opcional a la nube de PolyField.

Todo funciona en la red local — no se necesita internet para gestionar una competición, pero sí para descargar las listas de salida desde los proveedores de gestión de competiciones y para enviar los resultados en tiempo real de vuelta a sus sistemas. Es posible una sincronización posterior al concurso para enviar todos los resultados de una vez.

> **Validación positiva.** El servidor nunca inventa resultados — cada marca procede de un juez a través de la aplicación de campo. Esto mantiene una cadena clara, desde la medición en el círculo hasta lo que aparece en el marcador.

## Cómo funciona    {#how-it-works}

- Se ejecuta **una sola instancia** de la aplicación de escritorio en un ordenador de la red de la competición.
- La **aplicación de campo** (una por prueba) se conecta al servidor, descarga los atletas de su prueba y devuelve cada intento a medida que se mide.
- Cada **pantalla** abre una de las páginas web del servidor en un navegador; los resultados se actualizan al instante, sin necesidad de refrescar.
- El operador trabaja desde el **panel** de escritorio — importar pruebas, seguir el avance, exportar estadísticas y gráficos, y gestionar pantallas y anemómetros. Normalmente se configuran una sola vez al inicio de la competición, sin necesidad de intervenir durante la jornada.

## Primeros pasos    {#getting-started}

### 1. Cargar una competición    {#load-a-competition}

Abra la aplicación; el **Panel** es el puesto del operador. Inicie una competición de tres formas:

- **Importar desde OpenTrack o Athletics.app** — obtenga directamente la lista de pruebas y las listas de salida (véase [Importar pruebas](#importing-events)). Es la vía habitual y conserva el orden publicado de las listas de salida.
- **Crear las pruebas a mano** — use *+ Crear nueva prueba* y añada los atletas.
- **Nueva competición** — borra los datos actuales para empezar de cero.

Una vez cargada, cada prueba aparece como una tarjeta en el panel que muestra su estado (No iniciada, En curso, Finalizada).

### 2. Conectar la aplicación de campo    {#connect-the-field-app}

En cada dispositivo de campo, verifique la dirección del servidor en la aplicación de campo PolyField para conectarla al servidor. El juez selecciona entonces su prueba, calibra el EDM en el círculo o el pasillo y empieza a medir. Véase [Los resultados y la aplicación de campo](#results-and-the-field-app).

### 3. Abrir las pantallas    {#open-the-displays}

En cada pantalla, abra un navegador en la dirección del servidor y añada la página que desee — por ejemplo `http://polyfieldserver.local:8080/tables`. Use **Pantallas** en el panel para obtener enlaces con un clic y códigos QR a cada pantalla. Véase [Las pantallas](#display-screens).

> **Consejo.** Deje la aplicación de escritorio en el panel y gestione todo desde ahí. Los resultados llegan automáticamente desde la aplicación de campo mientras vigila el avance y las pantallas.

![Ventana Pantallas — enlaces y códigos QR de cada pantalla](/PolyField-Server/images/displays-popup.png)

## El panel    {#the-dashboard}

El panel enumera cada prueba y ofrece los controles principales. En la parte superior figuran la dirección del servidor (con un selector de red en máquinas con varias tarjetas) y el estado de los envíos o la sincronización pendientes. Las acciones clave:

| Control | Qué hace |
|---------|----------|
| Nueva competición | Borrar la competición actual y empezar de cero. |
| Crear nueva prueba | Añadir una prueba y sus atletas a mano. |
| Combinar pruebas | Combinar pruebas (p. ej. dos grupos de la misma disciplina) en una sola, o *Combinar todas las pruebas iguales* para combinar de una vez todas las parejas coincidentes. |
| Pantallas | Mostrar enlaces en los que se puede pulsar y códigos QR de cada página de pantalla (marcador, clasificaciones, locutor, RAZA). |
| Exportar gráficos | Generar los gráficos para redes sociales, los mapas de calor detallados y los gráficos de viento de la competición (véase [Gráficos para redes sociales](#social-media-graphics)). |
| Exportar estadísticas | Generar el PDF de estadísticas de la competición (también en la página de Estadísticas). |

Seleccionar una prueba abre su vista de **Resultados en directo**, donde ve la serie de cada atleta, sigue la llegada de los intentos y consulta la clasificación.

![El panel de PolyField Server](/PolyField-Server/images/dashboard.png)

## Importar pruebas    {#importing-events}

Use **Enlace de competición** / importar para cargar una competición en lugar de escribirla:

- **OpenTrack** — inicie sesión y elija su competición; el servidor descarga los concursos y sus inscritos. El **orden de las listas de salida** publicado por OpenTrack se conserva de forma idéntica.
- **Athletics.app** — introduzca el código del enlace de competición para crear las pruebas y los atletas. El **orden de las listas de salida** publicado por Athletics.app se conserva de forma idéntica.

Las pruebas importadas conservan su numeración y sus códigos de origen, de modo que coinciden con el programa publicado y con la exportación de resultados.

![Importar una competición](/PolyField-Server/images/import-opentrack.png)

## Los resultados y la aplicación de campo    {#results-and-the-field-app}

Los resultados se registran en el campo, no en el servidor. Cada prueba usa la aplicación de campo PolyField en un dispositivo Android:

- El dispositivo se conecta al servidor y descarga los atletas de la prueba elegida.
- Para lanzamientos y saltos horizontales, la aplicación puede conectarse a una **estación total EDM** o funcionar directamente en una estación total PolyField (PolyField APEKS AM02i); el juez calibra en el círculo / el pasillo / la tabla, y cada marca medida (con su coordenada de caída) se envía al servidor. Las marcas también pueden introducirse a mano.
- Los **saltos verticales** (altura, pértiga) son totalmente compatibles — las alturas, los intentos (O/X) y la progresión del listón se registran y se envían.
- Cada intento lleva su propia marca de tiempo, de modo que el servidor muestra los resultados en su orden real y puede generar estadísticas de tiempo precisas.

A medida que llegan los resultados, la tarjeta de la prueba se actualiza, las clasificaciones se recalculan y cualquier pantalla conectada se actualiza al instante.

![Resultados en directo — tabla de resultados](/PolyField-Server/images/live-results-table.png)

![Resultados en directo — mapa de calor de caídas](/PolyField-Server/images/live-results-heatmap.png)

## Las pantallas    {#display-screens}

El servidor sirve cuatro páginas de pantalla en directo. Cada una es una página web normal — ábrala en cualquier navegador de la red; no se instala nada en la pantalla. Todas se actualizan automáticamente: los nuevos resultados se envían en el momento en que llegan, con un sondeo periódico como red de seguridad, de modo que una pantalla nunca necesita refrescarse.

| Página | URL |
|--------|-----|
| Marcador de resultados (últimos resultados) | `/` |
| Clasificaciones de pruebas (tablas) | `/tables` |
| Canal del locutor | `/announcer` |
| Clasificaciones RAZA (para-atletismo) | `/raza` |

### Marcador de resultados    {#display-board}

Un gran marcador de las actuaciones más recientes, con el atleta, la prueba, la marca y — para lanzamientos — una visualización de la caída. Ideal como pantalla principal de resultados para el público.

![Marcador de resultados](/PolyField-Server/images/display-board.png)

### Clasificaciones de pruebas    {#event-standings}

Las clasificaciones en directo, varias pruebas a la vez, cada una ordenada con resaltados oro/plata/bronce. El diseño se adapta a la altura: llena la pantalla, apila más pruebas en pantallas altas o en modo vertical, y cuando una prueba tiene muchos atletas los recorre página a página. Las pruebas también van rotando para que cada prueba del programa aparezca en pantalla.

![Pantalla de clasificaciones de pruebas](/PolyField-Server/images/display-tables.png)

### Locutor    {#announcer}

Un canal de resultados a medida que llegan — el más reciente arriba, con el puesto, el atleta, el club, la prueba y la marca — dimensionado para leerse de un vistazo desde un puesto de locutor o de comentarios.

![Canal del locutor](/PolyField-Server/images/display-announcer.png)

### Clasificaciones RAZA    {#raza-rankings}

Clasificaciones de para-atletismo calculadas con el sistema de puntos World Para Athletics (RAZA), para comparar en un mismo marcador a atletas de clasificaciones distintas. Debe estar definida una clasificación y un género para que se calcule una puntuación RAZA.

![Pantalla de clasificaciones RAZA](/PolyField-Server/images/display-raza.png)

## Anemómetros    {#wind-gauges}

PolyField Server lee los anemómetros a través de la red y registra el viento durante toda la jornada de competición. Es compatible con el **Gill WindSonic 75** y el **PolyField Wind Mini**, y **detecta el tipo de anemómetro automáticamente** a partir de su flujo de datos — no hay ningún protocolo que elegir. Añada un anemómetro con su dirección de red; en cuanto emite, el servidor muestra el modelo detectado y empieza a registrar.

- El viento se captura de forma continua y se almacena por día, por lo que está disponible para la validez de los saltos horizontales, las estadísticas y los gráficos de viento.
- La página **Anemómetros** muestra cada aparato en directo y permite exportar un gráfico de viento de la jornada completa.
- Los anemómetros pueden ocultarse de la selección de atletas (por ejemplo, un anemómetro general de pista que se conserva solo para el registro).

![La página de Anemómetros](/PolyField-Server/images/wind-gauges.png)

## Estadísticas y mapas de calor    {#statistics-and-heatmaps}

La página **Estadísticas** convierte los datos de la competición en análisis:

- **Gráficos por prueba** — rendimiento a lo largo del tiempo, comparación ronda a ronda, tasa de nulos y de aciertos, y tiempo entre intentos.
- **Mapas de calor de caídas** — para lanzamientos, cada caída trazada en el sector, coloreada por ronda, con el ángulo medio de caída respecto al eje central del sector, la dispersión y la varianza.
- **Viento** — media, validez y tendencia durante la sesión para cada anemómetro.
- **Exportar estadísticas** — un PDF completo de la competición con los gráficos, los mapas de calor y los resúmenes por prueba, fechado el día de la competición.

Los gráficos y los mapas de calor se adaptan al ajuste de tamaño de pantalla para que sigan siendo legibles en la pantalla del operador.

![Estadísticas — mapa de calor de caídas de un lanzamiento](/PolyField-Server/images/statistics-heatmap.png)

## Gráficos para redes sociales    {#social-media-graphics}

**Exportar gráficos** genera un conjunto de imágenes cuadradas (1080 × 1080) listas para publicar, todas con un estilo PolyField coherente:

- **Resumen de la competición** — los totales destacados del concurso, con el lanzamiento y el salto más largos.
- **Tarjetas por prueba** — el podio, las condiciones de la prueba y los totales. Las tarjetas de salto vertical muestran la serie de intentos de cada atleta en su mejor altura y un desglose de la tasa de acierto en el 1.º / 2.º / 3.º intento; las tarjetas de salto horizontal muestran el viento.
- **Mapas de calor detallados** — la nube completa de caídas de cada lanzamiento.
- **Gráficos de viento** — la tendencia del viento de la jornada completa para cada anemómetro, con la validez y las rachas.

Los gráficos solo se generan para las pruebas que se han disputado, y cada tarjeta lleva la fecha de la competición y la identidad visual de PolyField.

![Ejemplo de tarjeta de prueba exportada](/PolyField-Server/images/social-example.png)

![Gráfico de viento para redes sociales (exportado)](/PolyField-Server/images/wind-gauges-social.png)

## Resultados en línea — en pruebas    {#cloud-results}

Opcionalmente, el servidor publica los resultados en la nube de PolyField para que el público pueda seguirlos en línea en [results.polyfield.co.uk](https://results.polyfield.co.uk). Se pueden enviar dos cosas, cada una activable en los Ajustes:

- **Resultados y mapas de calor de atletas** — páginas individuales anonimizadas para reducir la información identificable almacenada junto con sus marcas y un mapa de calor de caídas. Se autoeliminan a los 90 días.
- **Mapa de calor global** — una imagen agregada de las caídas de toda la competición. Está anonimizada, sin datos individuales de atletas, y se conserva de forma indefinida.

Los envíos se ponen en cola y se reintentan, de modo que una breve pérdida de internet no pierde datos — la competición en sí sigue funcionando en la red local en cualquier caso.

## Enlace de competición    {#competition-link}

**Enlace de competición** es donde conecta los proveedores de gestión de competiciones al servidor. Ofrece los controles de importación de OpenTrack / Athletics.app para cargar las pruebas.

![Enlace de competición — dirección del servidor y código QR](/PolyField-Server/images/competition-link.png)

## Ajustes, tamaño de pantalla e idioma    {#settings}

- **Tamaño de pantalla** — adapta la interfaz del operador, los gráficos estadísticos y los mapas de calor a la pantalla en la que ejecuta el servidor.
- **Idioma** — la interfaz está disponible en inglés, francés, español, neerlandés y portugués.
- **Envío a la nube** — activa o desactiva la publicación de atletas y mapas de calor.
- **Carpetas** — define las carpetas usadas para la importación de pruebas, las copias de seguridad locales en el PC, y la exportación de resultados y gráficos.

![Ajustes](/PolyField-Server/images/settings.png)

## Red    {#networking}

- La aplicación sirve en el **puerto 8080** y se anuncia como `polyfieldserver.local`, de modo que los dispositivos de campo y las pantallas pueden usar `http://polyfieldserver.local:8080` sin conocer la dirección IP. Algunos dispositivos Android requieren la dirección IP completa; en ese caso puede usar `http://192.168.0.10:8080` sustituyendo 192.168.0.10 por la dirección del servidor que se muestra en el panel.
- En ordenadores con más de una tarjeta de red (frecuente en Windows), elija la tarjeta correcta en la parte superior del panel para que se anuncie la dirección adecuada.
- Todos los dispositivos — aplicaciones de campo y pantallas — deben estar en la misma red que el ordenador anfitrión.

## Diagnóstico    {#diagnostics}

Si algo va mal, use el informe de diagnóstico. Reúne la competición actual (que el soporte puede reproducir), los registros y los datos de viento del día en un único archivo zip, y rellena previamente un correo a [support@polyfield.co.uk](mailto:support@polyfield.co.uk). Adjunte el archivo guardado antes de enviarlo. El mismo archivo puede servir para recuperar una competición si hay que cambiar de máquina a mitad del concurso.

![Informe de diagnóstico](/PolyField-Server/images/diagnostics.png)

## Solución de problemas    {#troubleshooting}

| Síntoma | Qué comprobar |
|---------|---------------|
| Un dispositivo de campo no se conecta | Compruebe que está en la misma red, que el puerto 8080 es accesible y (PC con varias tarjetas) que está seleccionada la tarjeta de red correcta en la parte superior del panel. Asegúrese de que su cortafuegos no bloquee PolyField Server. |
| Una importación devuelve 0 pruebas | Puede que la competición de origen aún no tenga inscritos, o que esté seleccionada otra competición. Compruebe que las listas de salida se han publicado. |
| Una pantalla no se actualiza | Las páginas se actualizan solas; si una se queda congelada, refrésquela una vez. Compruebe que apunta a la dirección actual del servidor. Las pantallas muestran la hora actual y el texto «LIVE» cuando están conectadas, para ayudar a verificarlo. |
| Un anemómetro no muestra ninguna lectura | Compruebe la dirección de red del anemómetro, que está encendido y emitiendo; el modelo se detecta automáticamente en cuanto llegan datos. El anemómetro muestra un estado En línea / Sin conexión en el servidor. |
| El marcador RAZA está vacío | Debe estar definida una clasificación y un género para que se calcule una puntuación RAZA. |
| Los resultados parecen desordenados o falta una ronda | Cada resultado lleva la marca de tiempo de la aplicación de campo; asegúrese de que los dispositivos de campo están en la prueba correcta y actualizados. Verifique que el reloj del dispositivo de campo y del servidor es correcto; puede desviarse con un uso sin conexión prolongado. |

## Descarga y soporte    {#download-and-support}

Descargue la última versión desde [www.polyfield.co.uk](https://www.polyfield.co.uk) o la página de versiones. La aplicación busca actualizaciones al iniciarse y muestra un aviso cuando hay una versión más reciente disponible. Soporte: [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

## Integración mediante API {#api-integration}

PolyField Server ofrece una **API HTTP + JSON** en el **puerto 8080**, en la **misma red local** que sus dispositivos de campo y sus pantallas. Es la misma interfaz que usan la aplicación de campo PolyField y las pantallas integradas, así que cualquier dispositivo de la red local — un marcador personalizado, un panel de estadísticas, una superposición para streaming, la señalización propia de una instalación — puede leer las pruebas, los resultados en directo, las clasificaciones, las estadísticas y el viento directamente del servidor. Las respuestas son JSON, no hay autenticación y CORS está abierto, por lo que una página web de la red local puede llamarla directamente. La mayoría de los endpoints son `GET` de solo lectura; los endpoints de escritura (`POST /api/v1/results`, `POST /api/v1/athlete/active`, `PUT /api/v1/events/status`) los usa la aplicación de campo.

La API es **solo para la red local por diseño** — la aplicación no la expone a Internet. **Cualquier integración orientada a la WAN o a Internet** (marcadores remotos, servicios en la nube, una segunda instalación) **debe consultarse primero con nosotros** para hacerla de forma segura, normalmente mediante una VPN o un proxy inverso controlado en lugar de abrir el puerto al mundo. Contacte con [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

**URL base:** `http://polyfieldserver.local:8080/api/v1` — o use la dirección IP del servidor que aparece en la parte superior del panel (p. ej. `http://192.168.0.10:8080/api/v1`).

**JSON Schema:** cada cuerpo de petición y de respuesta está definido en un único [archivo JSON Schema (draft 2020-12)](/PolyField-Server/api/polyfield-api.schema.json), bajo `$defs`. Cada endpoint indica a continuación el tipo de su cuerpo e incluye su esquema; los tipos compartidos están en [Tipos de datos](#api-data-types). Para validar un cuerpo, haga referencia a su definición, p. ej. `polyfield-api.schema.json#/$defs/ResultPayload`.

**Convenciones**

- Los errores devuelven un estado 4xx/5xx con `{"error": "message"}`. Un método que un endpoint no acepta devuelve `405`.
- Las horas están en formato RFC 3339, p. ej. `2026-06-14T13:42:07.512+01:00`.
- Las marcas y las alturas son cadenas en metros (`"46.38"`) para conservar los ceros finales; el viento es una cadena con signo en m/s (`"+1.4"`).
- Los campos opcionales se omiten cuando están vacíos. Los mapas indexados por ronda usan claves de texto (`"1"`, `"2"`, …).

| Método y ruta | Devuelve |
|---|---|
| [`GET /api/v1/events`](#api-list-events) | Listar todas las pruebas (resumen). |
| [`GET /api/v1/events/{eventId}`](#api-get-event) | Obtener una prueba con sus atletas y todos los intentos. |
| [`PUT/PATCH /api/v1/events/status`](#api-update-status) | Establecer el estado de una prueba. |
| [`POST /api/v1/results`](#api-post-results) | Enviar la serie de un atleta (la escritura principal de la aplicación de campo). |
| [`POST /api/v1/athlete/active`](#api-post-active) | Señalar quién está en curso (saltos horizontales). |
| [`GET /api/v1/athlete/active/{eventId}`](#api-get-active) | Leer quién está en curso en una prueba. |
| [`GET /api/v1/display/recent`](#api-display-recent) | Últimas actuaciones (marcador de resultados). |
| [`GET /api/v1/display/standings`](#api-display-standings) | Clasificaciones actuales de cada prueba con marcas. |
| [`GET /api/v1/broadcast/recent`](#api-broadcast-recent) | Los últimos 10 resultados con todo detalle (retransmisión / locutor). |
| [`GET /api/v1/raza`](#api-raza) | Clasificaciones RAZA de para-atletismo. |
| [`GET /api/v1/statistics/overall`](#api-stats-overall) | Estadísticas de toda la competición. |
| [`GET /api/v1/statistics/event/{eventId}`](#api-stats-event) | Estadísticas detalladas de una prueba. |
| [`GET /api/v1/wind/gauges`](#api-wind-gauges) | Listar los anemómetros y su última lectura. |
| [`GET /api/v1/wind/current`](#api-wind-current) | Viento medio actual, en los últimos segundos. |
| [`GET /api/v1/wind/search`](#api-wind-search) | Viento en un momento pasado (registro de hoy). |
| [`GET /api/v1/config`](#api-config) | Configuración de las pantallas. |
| [`GET /api/v1/stream`](#api-stream) | Notificaciones de actualización en directo (Server-Sent Events). |

### `GET /api/v1/events` {#api-list-events}

Listar todas las pruebas (resumen). Devuelve cada prueba cargada en el servidor como un resumen ligero. La aplicación de campo lo usa para ofrecer el selector de pruebas.

```http
GET /api/v1/events
```

**Respuesta — array de `EventSummary`:**

- `id` (string)
- `name` (string)
- `type` (string) — Categoría de la prueba. Valores conocidos: "Throws", "Horizontal Jumps", "Vertical Jumps".

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

**Errores:**

- `405` — Cualquier método distinto de GET.

### `GET /api/v1/events/{eventId}` {#api-get-event}

Obtener una prueba con sus atletas y todos los intentos. Devuelve la prueba completa. La usa la aplicación de campo para descargar la lista de salida y los resultados ya registrados.

- `eventId` (ruta) — ID de la prueba, de la lista de pruebas (codifíquelo para la URL).

```http
GET /api/v1/events/dt-sw-f07
```

**Respuesta — `Event`:**

- `id` (string)
- `name` (string)
- `originalName` (string, opcional)
- `type` (string) — Categoría de la prueba. Valores conocidos: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `rules` (EventRules) — Formato de competición de una prueba.
- `athletes` (Athlete[])
- `calibrationMetadata` (CalibrationMetadata, opcional) — Geometría del campo tomada al calibrar el EDM.
- `lastResultTime` (date-time, opcional)
- `signedOff` (boolean, opcional)
- `signedOffBy` (string, opcional)
- `signedOffAt` (date-time, opcional)
- `evtEventNumber` (string, opcional)
- `evtRoundNumber` (string, opcional)
- `evtHeatNumber` (string, opcional)
- `opentrackUnitId` (string, opcional)
- `opentrackEventId` (string, opcional)
- `opentrackEventCode` (string, opcional)
- `opentrackUrl` (string, opcional)
- `athleticsAppLinkCode` (string, opcional)
- `isMerged` (boolean, opcional)
- `isHidden` (boolean, opcional)
- `mergedEventId` (string, opcional)
- `sourceEventIds` (string[], opcional)
- `sourceEventNames` (string[], opcional)

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

**Errores:**

- `400` — No hay ID de prueba en la ruta. `{"error": "Event ID is required"}`
- `404` — Prueba desconocida. `{"error": "event with ID dt-xx not found"}`

### `PUT / PATCH /api/v1/events/status` {#api-update-status}

Establecer el estado de una prueba. Cambia una prueba entre Not Started, In Progress y Finished. El servidor también pasa una prueba a In Progress automáticamente cuando llega su primer resultado válido.

**Cuerpo de la petición — `EventStatusUpdate`:**

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

**Respuesta — `SuccessResponse`:**

- `status` ("success")
- `message` (string, opcional)

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

**Errores:**

- `400` — Falta un campo, prueba desconocida o estado no válido. `{"error": "invalid status: Done. Must be one of: Not Started, In Progress, Finished"}`

### `POST /api/v1/results` {#api-post-results}

Enviar la serie de un atleta (la escritura principal de la aplicación de campo). Envía la serie **completa** del atleta hasta el momento; sustituye lo que el servidor tiene para ese atleta, así que reenviarla es seguro. El servidor determina qué intentos son nuevos o han cambiado, actualiza las clasificaciones y envía un `update` a las pantallas. Las marcas se normalizan: `X`/`FOUL` pasan a `NM`, `PASS`/`-` pasan a `P`. Una marca fuera de rango se registra en el log pero se guarda igualmente. Si el dorsal no está en la prueba, se añade un atleta provisional.

**Cuerpo de la petición — `ResultPayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `series` (Performance[]) — La serie completa del atleta hasta el momento. Sustituye la serie guardada.
- `heatmapCoordinates` (HeatmapCoordinate[], opcional)
- `calibrationMetadata` (CalibrationMetadata, opcional) — Geometría del campo tomada al calibrar el EDM.

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

*Salto horizontal con viento:*

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

*Salto vertical (un intento por entrada, con la altura del listón):*

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

**Respuesta — `SuccessResponse`:**

- `status` ("success")
- `message` (string, opcional)

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

**Errores:**

- `400` — El cuerpo no es JSON válido. `{"error": "Invalid request body"}`
- `404` — Prueba desconocida. `{"error": "event with ID dt-xx not found"}`

### `POST /api/v1/athlete/active` {#api-post-active}

Señalar quién está en curso (saltos horizontales). Señal sin confirmación que envía la aplicación de campo cuando un saltador pasa a ser el atleta en curso; la usa la pantalla de regla de la tabla de batida. Un atleta por prueba: cada envío sustituye al anterior. **No** es un resultado.

**Cuerpo de la petición — `ActiveAthletePayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `athleteName` (string, opcional)
- `board` (number, opcional) — Distancia de la tabla de batida en metros (0 = tabla de longitud).
- `topPerformances` (number[], opcional) — Mejores marcas válidas hasta ahora, de mejor a peor. Máximo 3.

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

**Respuesta — `OkResponse`:**

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

**Errores:**

- `400` — JSON no válido, o falta eventId / athleteBib. `{"error": "eventId and athleteBib are required"}`

### `GET /api/v1/athlete/active/{eventId}` {#api-get-active}

Leer quién está en curso en una prueba. Siempre 200 para que un widget pueda consultar de forma sencilla; `active` es `null` cuando no se ha señalado a nadie (entre atletas o tras un reinicio).

- `eventId` (ruta) — ID de la prueba.

```http
GET /api/v1/athlete/active/dt-sw-f07
```

**Respuesta — `ActiveAthleteResponse`:**

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

*Nadie en curso:*

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

**Errores:**

- `400` — No hay ID de prueba en la ruta. `{"error": "Event ID is required"}`

### `GET /api/v1/display/recent` {#api-display-recent}

Últimas actuaciones (marcador de resultados). Las actuaciones más recientes, de la más reciente a la más antigua. Alimenta el marcador de resultados en `/`.

- `limit` (consulta) — Cuántos devolver, 1-100. Por defecto 4; los valores fuera de rango vuelven a 4.

```http
GET /api/v1/display/recent?limit=2
```

**Respuesta — `RecentPerformancesResponse`:**

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

Clasificaciones actuales de cada prueba con marcas. Clasificación de cada prueba con al menos una marca válida. Alimenta la pantalla `/tables`. `events` es `null` mientras ninguna prueba tenga una marca válida.

```http
GET /api/v1/display/standings
```

**Respuesta — `EventStandingsResponse`:**

- `events` (EventStandings[]) — Solo las pruebas con al menos una marca válida. null si no hay ninguna.

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

Los últimos 10 resultados con todo detalle (retransmisión / locutor). Hasta los 10 resultados más recientes, del más reciente al más antiguo, con detalle suficiente para redibujar cada uno (líneas del sector, punto de caída, altura del listón y serie). Alimenta la página `/announcer`.

```http
GET /api/v1/broadcast/recent
```

**Respuesta — `DetailedRecentResultsResponse`:**

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

Clasificaciones RAZA de para-atletismo. Atletas con clasificación y sexo, puntuados con los puntos RAZA de World Para Athletics y agrupados por prueba de referencia. Alimenta la pantalla `/raza`.

```http
GET /api/v1/raza
```

**Respuesta — `RazaResponse`:**

- `events` (RazaEventGroup[])
- `total` (integer) — Número total de atletas clasificados.

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

Estadísticas de toda la competición. Totales, tiempos, tasa de nulos, intentos a lo largo del tiempo, cronología de pruebas y zonas de caída por tipo de lanzamiento.

```http
GET /api/v1/statistics/overall
```

**Respuesta — `OverallStatistics`:**

- `totalEvents` (integer)
- `eventsNotStarted` (integer)
- `eventsInProgress` (integer)
- `eventsCompleted` (integer)
- `totalAthletes` (integer)
- `totalAttempts` (integer)
- `totalValidAttempts` (integer)
- `totalFouls` (integer)
- `overallFoulRate` (number) — Porcentaje 0-100.
- `competitionStartTime` (date-time, opcional)
- `competitionEndTime` (date-time, opcional)
- `totalDuration` (number) — Minutos.
- `eventsWithOpenTrack` (integer)
- `eventsWithCalibration` (integer)
- `eventsByType` (object) — Número de pruebas por categoría.
- `attemptsOverTime` (TimeSeriesPoint[])
- `eventTimeline` (EventTimelineItem[])
- `throwHeatmaps` (object, opcional) — Indexado por código de tipo de lanzamiento.

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

**Errores:**

- `500` — No se han podido calcular las estadísticas.

### `GET /api/v1/statistics/event/{eventId}` {#api-stats-event}

Estadísticas detalladas de una prueba. Tiempos, rondas, nulos, marcas y datos de gráficos de una prueba. `windStats`, `heatmapStats` y `verticalJumpStats` solo aparecen para el tipo de prueba correspondiente. Los mapas indexados por ronda usan el número de ronda como clave de texto.

- `eventId` (ruta) — ID de la prueba.

```http
GET /api/v1/statistics/event/dt-sw-f07
```

**Respuesta — `EventStatistics`:**

- `eventId` (string)
- `eventName` (string)
- `eventType` (string) — Categoría de la prueba. Valores conocidos: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `calibrationTime` (date-time, opcional)
- `firstAttemptTime` (date-time, opcional)
- `lastAttemptTime` (date-time, opcional)
- `setupDuration` (number) — Minutos desde la calibración hasta el primer intento.
- `competitionDuration` (number) — Minutos desde el primer hasta el último intento.
- `totalEventDuration` (number) — Minutos desde la calibración hasta el último intento.
- `averageTimeBetween` (number) — Segundos entre intentos.
- `roundDurations` (object) — Ronda -> minutos.
- `avgTimePerAttemptByRound` (object) — Ronda -> minutos medios entre intentos.
- `timeBetweenRounds` (object) — Ronda -> intervalo hasta la siguiente ronda (minutos).
- `totalAthletes` (integer)
- `athletesCompleted` (integer)
- `athletesInProgress` (integer)
- `athletesNotStarted` (integer)
- `totalAttempts` (integer)
- `validAttempts` (integer)
- `fouls` (integer)
- `foulRate` (number)
- `winningMark` (string, opcional)
- `averageMark` (number)
- `medianMark` (number)
- `bestMarkPerRound` (object) — Ronda -> mejor marca.
- `foulRateByRound` (object) — Ronda -> tasa de nulos.
- `athletesWithZeroFouls` (integer)
- `fastestAthlete` (AthleteTimingInfo, opcional)
- `slowestAthlete` (AthleteTimingInfo, opcional)
- `mostConsistent` (AthleteConsistencyInfo, opcional)
- `windStats` (WindStatistics, opcional) — Solo saltos horizontales.
- `heatmapStats` (HeatmapStatistics, opcional) — Solo lanzamientos con coordenadas de caída.
- `verticalJumpStats` (VerticalJumpStatistics, opcional) — Solo salto de altura / pértiga.
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

**Errores:**

- `400` — No hay ID de prueba en la ruta. `{"error": "Event ID is required"}`
- `404` — Prueba desconocida. `{"error": "event with ID dt-xx not found"}`

### `GET /api/v1/wind/gauges` {#api-wind-gauges}

Listar los anemómetros y su última lectura.

```http
GET /api/v1/wind/gauges
```

**Respuesta — `WindGaugesResponse`:**

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

Viento medio actual, en los últimos segundos.

- `gauge_id` (consulta) — Obligatorio. ID del anemómetro de /wind/gauges.
- `duration` (consulta) — Ventana de promedio en segundos, 1-60. Por defecto 5.

```http
GET /api/v1/wind/current?gauge_id=back-pits&duration=5
```

**Respuesta — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Velocidad media del viento en la ventana (m/s, + = viento a favor).
- `average_crosswind` (number)
- `readings` (number[]) — Las velocidades individuales que se promediaron.
- `timestamp` (date-time) — Hora de la lectura (RFC 3339, precisión de segundos).
- `direction` (integer) — Última dirección en grados (0-360).

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

**Errores:**

- `400` — Falta gauge_id. `{"error": "gauge_id parameter is required"}`
- `404` — Anemómetro desconocido. `{"error": "Wind gauge not found"}`
- `503` — Anemómetro desconectado o sin lecturas en la ventana. `{"error": "Wind gauge is offline"}`

### `GET /api/v1/wind/search` {#api-wind-search}

Viento en un momento pasado (registro de hoy). Busca la lectura más cercana a la hora indicada en el registro de hoy y promedia las lecturas a ±2.5 s de ella. Sirve para asignar el viento a un salto a posteriori.

- `gauge_id` (consulta) — Obligatorio. ID del anemómetro.
- `timestamp` (consulta) — Obligatorio. Hora RFC 3339, codificada para la URL (p. ej. `2026-06-14T14%3A02%3A10Z`).

```http
GET /api/v1/wind/search?gauge_id=back-pits&timestamp=2026-06-14T14%3A02%3A10Z
```

**Respuesta — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Velocidad media del viento en la ventana (m/s, + = viento a favor).
- `average_crosswind` (number)
- `readings` (number[]) — Las velocidades individuales que se promediaron.
- `timestamp` (date-time) — Hora de la lectura (RFC 3339, precisión de segundos).
- `direction` (integer) — Última dirección en grados (0-360).

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

**Errores:**

- `400` — Falta gauge_id o timestamp, o timestamp no es RFC 3339. `{"error": "Invalid timestamp format (use RFC3339)"}`
- `404` — Anemómetro desconocido. `{"error": "Wind gauge not found"}`
- `503` — No hay lecturas guardadas hoy. `{"error": "No wind readings available"}`

### `GET /api/v1/config` {#api-config}

Configuración de las pantallas. El idioma de la interfaz elegido en Ajustes, para que las pantallas de otros dispositivos lo usen también.

```http
GET /api/v1/config
```

**Respuesta — `ConfigResponse`:**

- `language` (string) — "en", "fr", "es", "nl" o "pt".

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

Un flujo [Server-Sent Events](https://developer.mozilla.org/es/docs/Web/API/Server-sent_events) (`text/event-stream`). El servidor envía `data: update` cada vez que cambian los resultados, el estado de una prueba o el atleta en curso — vuelva a pedir entonces el feed que muestre. Un comentario `: ping` cada 25 segundos mantiene la conexión abierta. El mensaje es solo la palabra `update`, por lo que no tiene JSON Schema.

```text
: connected

data: update

: ping
```

```js
const es = new EventSource('http://polyfieldserver.local:8080/api/v1/stream');
es.onmessage = (e) => { if (e.data === 'update') refresh(); };
```

Mantenga una consulta lenta (cada 30–60 s) como respaldo, como hacen las pantallas integradas. Sin el flujo, consulte los feeds de pantalla cada 1–2 segundos; las estadísticas solo hace falta pedirlas bajo demanda.

### Tipos de datos {#api-data-types}

Tipos usados dentro de varios de los cuerpos anteriores. Todas las definiciones están en el [esquema descargable](/PolyField-Server/api/polyfield-api.schema.json).

#### Performance {#api-type-performance}

Un intento de un atleta. Las respuestas siempre incluyen unit, valid y timestamp.

- `attempt` (integer) — Número de intento, empezando en 1. El servidor identifica los cambios por este número.
- `mark` (string) — La marca. Lanzamientos / saltos horizontales: una distancia en metros ("45.67"), "NM" (nulo; se aceptan "X" y "FOUL", que se normalizan a "NM") o "P" (pase; se aceptan "PASS" y "-"). Saltos verticales: "O" superado, "X" fallo, "P" pase.
- `height` (string, opcional) — Solo saltos verticales: altura del listón en metros ("1.85").
- `unit` (string, opcional) — Unidad de la marca, normalmente "m".
- `wind` (string, opcional) — Lectura del viento en m/s como cadena con signo ("+1.4", "-0.3"). Solo saltos horizontales.
- `valid` (boolean, opcional) — true para una marca / un listón superado válido, false para un nulo, un fallo o un pase.
- `coordinates` (HeatmapCoordinate, opcional) — Punto de caída de un lanzamiento o salto.
- `timestamp` (date-time, opcional) — Cuándo se hizo el intento. Si se omite o es cero, se usa la hora de recepción en el servidor.

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

Punto de caída de un lanzamiento o salto.

- `x` (number) — X bruta del punto de caída en el sistema del EDM (m).
- `y` (number) — Y bruta del punto de caída en el sistema del EDM (m).
- `distance` (number) — Distancia medida (m).
- `round` (integer)
- `attempt` (integer)
- `valid` (boolean)
- `rx` (number, opcional) — X del punto de caída girado para que la línea central del sector apunte hacia arriba (+Y). Calculado por el servidor; solo para lanzamientos válidos con calibración de las líneas del sector.
- `ry` (number, opcional) — Y del punto de caída en el sistema girado (ver rx).

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

Geometría del campo tomada al calibrar el EDM.

- `circleType` (string) — Tipo de círculo / pasillo, p. ej. "SHOT", "DISCUS", "HAMMER", "JAVELIN_ARC".
- `circleRadius` (number) — Radio del círculo en metros.
- `edmPosition` (Coordinate, opcional) — Una posición X/Y en metros en el sistema de referencia del EDM.
- `sectorLines` (SectorLines, opcional) — Geometría de las líneas del sector de un círculo de lanzamiento.
- `timestamp` (string, opcional) — Cuándo se hizo la calibración (ISO 8601).
- `calibrationId` (string, opcional)

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

Geometría de las líneas del sector de un círculo de lanzamiento.

- `rightLine` (Coordinate) — Una posición X/Y en metros en el sistema de referencia del EDM.
- `leftLine` (Coordinate) — Una posición X/Y en metros en el sistema de referencia del EDM.
- `sectorAngle` (number) — Ángulo del sector en grados (34.92 para un sector de lanzamientos estándar).

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

Una posición X/Y en metros en el sistema de referencia del EDM.

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

Un competidor y su serie.

- `bib` (string)
- `order` (integer) — Orden en la lista de salida.
- `name` (string)
- `club` (string)
- `ageGroup` (string, opcional)
- `classification` (string, opcional) — Clase de World Para Athletics, p. ej. "F56".
- `gender` (string, opcional) — "M" o "W" (se usa para la puntuación RAZA).
- `sourceEventId` (string, opcional)
- `series` (Performance[])
- `heatmapCoordinates` (HeatmapCoordinate[], opcional)

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

Formato de competición de una prueba.

- `attempts` (integer) — Intentos por atleta (p. ej. 3, 4 o 6).
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
- `label` (string, opcional)

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

Cuerpo devuelto con cada respuesta 4xx/5xx de la API.

- `error` (string) — Mensaje de error legible.

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
