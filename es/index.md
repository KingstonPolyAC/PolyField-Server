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
- **Idioma** — la interfaz está disponible en inglés, francés, español y neerlandés.
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
