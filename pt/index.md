---
layout: manual
lang: pt
title: "PolyField Server — Manual"
description: "Ajuda e manual do utilizador do PolyField Server — o servidor de controlo de provas de campo que gere a competição, os ecrãs em direto, os anemómetros, as estatísticas e os resultados na nuvem através da rede do recinto."
---

# PolyField Server

O servidor de controlo de provas de campo. Uma aplicação de ambiente de trabalho gere a competição na rede do seu recinto: guarda as provas e os atletas, recebe resultados em direto da aplicação de campo PolyField, comanda os ecrãs de apresentação em direto, regista o vento, produz estatísticas e visuais para redes sociais e (opcionalmente) publica resultados na nuvem. Funciona em Windows e Mac; opera numa rede local.

[Transferir a partir de polyfield.co.uk](https://www.polyfield.co.uk)

* TOC
{:toc}

## Visão geral    {#overview}

O PolyField Server é o centro de uma competição de provas de campo. Corre num único computador na rede do recinto e faz quatro coisas em simultâneo:

- **Guarda a competição** — as provas, os escalões etários, os atletas e cada tentativa, tudo armazenado localmente no computador anfitrião.
- **Recebe resultados** — os oficiais medem no círculo ou na pista de balanço com a aplicação de campo PolyField (num dispositivo Android ligado a uma estação total EDM, ou introduzidos à mão), e a aplicação envia cada marca diretamente para o servidor.
- **Comanda os ecrãs** — disponibiliza um conjunto de páginas web que qualquer ecrã na rede abre num navegador: um painel de resultados em direto, os classificações das provas, um fluxo para o locutor e as classificações de para-atletismo RAZA.
- **Acrescenta análise** — captura de vento, estatísticas por prova e mapas de calor das quedas, visuais para redes sociais e publicação opcional na nuvem PolyField.

Tudo funciona na rede local — não é necessária ligação à Internet para gerir uma competição, mas é necessária para transferir as listas de partida dos fornecedores de gestão de competições e para reenviar os resultados em tempo real para os seus sistemas. É possível uma sincronização após o concurso para enviar todos os resultados de uma só vez.

> **Validação positiva.** O servidor nunca inventa resultados — cada marca provém de um oficial através da aplicação de campo. Isto garante uma cadeia clara, da medição no círculo até ao que aparece no painel.

## Como funciona    {#how-it-works}

- Executa **uma instância** da aplicação de ambiente de trabalho num computador da rede da competição.
- A **aplicação de campo** (uma por prova) liga-se ao servidor, transfere os atletas da sua prova e envia cada tentativa à medida que é medida.
- Cada **ecrã de apresentação** abre uma das páginas web do servidor num navegador; os resultados atualizam-se instantaneamente, sem necessidade de recarregar.
- O operador trabalha a partir do **painel** de ambiente de trabalho — importando provas, acompanhando o progresso, exportando estatísticas e visuais e gerindo ecrãs e anemómetros. Geralmente são configurados uma vez no início da competição, sem necessidade de interação ao longo do dia.

## Primeiros passos    {#getting-started}

### 1. Carregar uma competição    {#load-a-competition}

Abra a aplicação; o **Painel** é a base do operador. Inicie uma competição de uma de três formas:

- **Importar do OpenTrack ou do Athletics.app** — obtenha a lista de provas e as listas de partida diretamente (ver [Importar provas](#importing-events)). Este é o caminho habitual e preserva a ordem publicada da lista de partida.
- **Criar provas manualmente** — utilize *+ Criar Nova Prova* e adicione atletas.
- **Nova Competição** — limpa os dados atuais para começar de novo.

Depois de carregada, cada prova surge como um cartão no painel, mostrando o seu estado (Não Iniciada, Em Curso, Terminada).

### 2. Ligar a aplicação de campo    {#connect-the-field-app}

Em cada dispositivo de campo, verifique o endereço do servidor na aplicação de campo PolyField para o ligar ao servidor. O oficial seleciona então a sua prova, calibra o EDM ao círculo ou à pista de balanço e começa a medir. Ver [Resultados e a aplicação de campo](#results-and-the-field-app).

### 3. Abrir os ecrãs    {#open-the-displays}

Em cada dispositivo de apresentação, abra um navegador no endereço do servidor e adicione a página que pretende — por exemplo `http://polyfieldserver.local:8080/tables`. Utilize **Ecrãs** no painel para obter ligações num clique e códigos QR de leitura rápida para cada ecrã. Ver [Ecrãs de apresentação](#display-screens).

> **Dica.** Deixe a aplicação de ambiente de trabalho no painel e comande tudo a partir daí. Os resultados chegam automaticamente da aplicação de campo enquanto acompanha o progresso e os ecrãs.

![Janela Ecrãs — ligações e códigos QR para cada ecrã](/PolyField-Server/images/displays-popup.png)

## O painel    {#the-dashboard}

O painel lista todas as provas e disponibiliza os controlos principais. No topo está o endereço do servidor (com um seletor de rede em máquinas com vários adaptadores) e qualquer estado pendente de envio ou sincronização. As ações principais:

| Controlo | O que faz |
|---------|--------------|
| Nova Competição | Limpar a competição atual e começar de novo. |
| Criar Nova Prova | Adicionar uma prova e os seus atletas manualmente. |
| Combinar Provas | Combinar provas (ex.: dois grupos da mesma disciplina) numa só, ou *Combinar Todas as Provas Iguais* para combinar todos os pares correspondentes de uma vez. |
| Ecrãs | Mostrar ligações clicáveis e códigos QR para cada página de apresentação (painel, classificações, locutor, RAZA). |
| Exportar Gráficos | Gerar os visuais para redes sociais, mapas de calor detalhados e gráficos de vento da competição (ver [Visuais para redes sociais](#social-media-graphics)). |
| Exportar Estatísticas | Produzir o PDF de estatísticas da competição (também na página Estatísticas). |

Ao selecionar uma prova abre-se a sua vista de **Resultados em Direto**, onde pode ver a série de cada atleta, acompanhar a chegada das tentativas e rever a classificação.

![O painel do PolyField Server](/PolyField-Server/images/dashboard.png)

## Importar provas    {#importing-events}

Utilize **Ligação à Competição** / importar para trazer uma competição em vez de a digitar:

- **OpenTrack** — inicie sessão e escolha a sua competição; o servidor transfere as provas de campo e as respetivas inscrições. A **ordem da lista de partida** publicada pelo OpenTrack é preservada exatamente.
- **Athletics.app** — introduza o código de ligação da competição para criar as provas e os atletas. A **ordem da lista de partida** publicada pelo Athletics.app é preservada exatamente.

As provas importadas mantêm a numeração e os códigos de origem, pelo que ficam alinhadas com o programa publicado e com a exportação de resultados.

![Importar uma competição](/PolyField-Server/images/import-opentrack.png)

## Resultados e a aplicação de campo    {#results-and-the-field-app}

Os resultados são registados no campo, não no servidor. Cada prova utiliza a aplicação de campo PolyField num dispositivo Android:

- O dispositivo liga-se ao servidor e transfere os atletas da prova escolhida.
- Para lançamentos e saltos horizontais, a aplicação pode ser emparelhada com uma **estação total EDM** ou correr diretamente numa PolyField Total Station (PolyField APEKS AM02i); o oficial calibra ao círculo/pista/tábuas e cada marca medida (com a coordenada de queda) é enviada para o servidor. As marcas também podem ser introduzidas à mão.
- Os **saltos verticais** (salto em altura, salto com vara) são totalmente suportados — as alturas, as transposições (O/X) e a progressão da fasquia são registadas e enviadas.
- Cada tentativa tem a sua própria marca temporal, pelo que o servidor mostra os resultados pela verdadeira ordem em que ocorreram e pode produzir estatísticas de tempo rigorosas.

À medida que os resultados chegam, o cartão da prova atualiza-se, as classificações são recalculadas e qualquer ecrã ligado atualiza-se instantaneamente.

![Resultados em Direto — tabela de resultados](/PolyField-Server/images/live-results-table.png)

![Resultados em Direto — mapa de calor das quedas](/PolyField-Server/images/live-results-heatmap.png)

## Ecrãs de apresentação    {#display-screens}

O servidor disponibiliza quatro páginas de apresentação em direto. Cada uma é uma página web normal — abra-a em qualquer navegador na rede; nada é instalado no ecrã. Todas se atualizam automaticamente: os novos resultados são enviados no momento em que chegam, com uma sondagem periódica como rede de segurança, pelo que um ecrã nunca precisa de ser recarregado manualmente.

| Página | URL |
|------|-----|
| Painel de resultados (últimos resultados) | `/` |
| Classificações das provas (tabelas) | `/tables` |
| Fluxo do locutor | `/announcer` |
| Classificações RAZA (para-atletismo) | `/raza` |

### Painel de resultados    {#display-board}

Um painel de grande ecrã com os desempenhos mais recentes, com o atleta, a prova, a marca e — para lançamentos — uma visualização da queda. Ideal como ecrã principal de resultados para os espetadores.

![Painel de resultados](/PolyField-Server/images/display-board.png)

### Classificações das provas    {#event-standings}

Classificações em direto, várias provas de cada vez, cada uma ordenada com destaques de ouro/prata/bronze. O esquema adapta-se à altura: preenche o ecrã, empilha mais provas em ecrãs altos ou verticais e, quando uma prova tem muitos atletas, percorre-os página a página. As provas também rodam para que todas as provas do programa tenham tempo de ecrã.

![Ecrã de classificações das provas](/PolyField-Server/images/display-tables.png)

### Locutor    {#announcer}

Um fluxo contínuo de resultados à medida que chegam — o mais recente no topo, com posição, atleta, clube, prova e marca — dimensionado para um locutor ou posição de comentário ler num relance.

![Fluxo do locutor](/PolyField-Server/images/display-announcer.png)

### Classificações RAZA    {#raza-rankings}

Classificações de para-atletismo pontuadas com o sistema de pontos World Para Athletics (RAZA), para que atletas de diferentes classificações possam ser comparados num só painel. Os atletas precisam de uma classificação e de género definidos para que uma pontuação RAZA seja calculada.

![Ecrã de classificações RAZA](/PolyField-Server/images/display-raza.png)

## Anemómetros    {#wind-gauges}

O PolyField Server lê anemómetros através da rede e regista o vento durante todo o dia de competição. Suporta o **Gill WindSonic 75** e o **PolyField Wind Mini**, e **deteta automaticamente o tipo de anemómetro** a partir do seu fluxo de dados — não há protocolo a escolher. Adicione um anemómetro com o seu endereço de rede; assim que transmitir, o servidor mostra o modelo detetado e começa a registar.

- O vento é captado continuamente e guardado por dia, ficando disponível para a legalidade dos saltos horizontais, as estatísticas e os gráficos de vento.
- A página **Anemómetros** mostra cada anemómetro em direto e permite exportar um gráfico de vento de dia completo.
- Os anemómetros podem ser ocultados da seleção de atletas (por exemplo, um anemómetro geral de pista mantido apenas para registo).

![A página Anemómetros](/PolyField-Server/images/wind-gauges.png)

## Estatísticas e mapas de calor    {#statistics-and-heatmaps}

A página **Estatísticas** transforma os dados da competição em análise:

- **Gráficos por prova** — desempenho ao longo do tempo, comparação ronda a ronda, taxa de nulos e de sucesso e tempo entre tentativas.
- **Mapas de calor das quedas** — para provas de lançamento, cada queda representada no setor, colorida por ronda, com o ângulo médio de queda relativo à linha central do setor, dispersão e variância.
- **Vento** — média, legalidade e a tendência ao longo da sessão para cada anemómetro.
- **Exportar Estatísticas** — um PDF completo da competição com os gráficos, mapas de calor e resumos por prova, datado do dia da competição.

Os gráficos e mapas de calor ajustam-se à definição de tamanho de apresentação, mantendo-se legíveis no ecrã do operador.

![Estatísticas — mapa de calor das quedas de uma prova de lançamento](/PolyField-Server/images/statistics-heatmap.png)

## Visuais para redes sociais    {#social-media-graphics}

**Exportar Gráficos** produz um conjunto de imagens quadradas (1080×1080) prontas a publicar, todas num estilo PolyField consistente:

- **Resumo da competição** — totais principais do encontro, com o lançamento e o salto mais longos.
- **Cartões por prova** — os três primeiros, as condições e os totais da prova. Os cartões de salto vertical mostram a série de transposições de cada atleta na sua melhor altura e uma repartição da taxa de sucesso à 1.ª/2.ª/3.ª tentativa; os cartões de salto horizontal mostram o vento.
- **Mapas de calor detalhados** — a dispersão completa das quedas de cada prova de lançamento.
- **Gráficos de vento** — a tendência do vento de dia completo para cada anemómetro, com legalidade e rajadas.

Os visuais são produzidos apenas para as provas que decorreram, e cada cartão inclui a data da competição e a identidade visual PolyField.

![Exemplo de cartão de prova exportado](/PolyField-Server/images/social-example.png)

![Gráfico de vento para redes sociais (exportado)](/PolyField-Server/images/wind-gauges-social.png)

## Resultados na nuvem - Em Teste    {#cloud-results}

Opcionalmente, o servidor publica os resultados na nuvem PolyField para que os espetadores possam acompanhar online em [results.polyfield.co.uk](https://results.polyfield.co.uk). Podem ser enviados dois elementos, cada um alternável nas Definições:

- **Resultados e mapas de calor dos atletas** — páginas individuais de atletas anonimizadas para reduzir a informação identificável guardada com as suas marcas, e um mapa de calor das quedas. Estas serão eliminadas automaticamente após 90 dias.
- **Mapa de calor global** — uma imagem agregada das quedas de toda a competição. É anonimizada, sem dados individuais dos atletas, e é mantida indefinidamente.

Os envios são colocados em fila e repetidos, pelo que uma breve perda de Internet não perde dados — a própria competição continua a funcionar na rede local independentemente disso.

## Ligação à competição    {#competition-link}

**Ligação à Competição** é onde liga os fornecedores de gestão de competições ao servidor. Os controlos de importação do OpenTrack / Athletics.app para carregar as provas.

![Ligação à Competição — endereço do servidor e código QR](/PolyField-Server/images/competition-link.png)

## Definições, tamanho de apresentação e idioma    {#settings}

- **Tamanho de apresentação** — ajusta a interface do operador, os gráficos de estatísticas e os mapas de calor ao ecrã em que corre o servidor.
- **Idioma** — a interface está disponível em inglês, francês, espanhol, neerlandês e português.
- **Envio para a nuvem** — ative ou desative a publicação de atletas e de mapas de calor.
- **Diretorias** — defina as pastas usadas para a importação de provas, as pastas de cópia de segurança no PC local e a exportação de resultados e visuais.

![Definições](/PolyField-Server/images/settings.png)

## Rede    {#networking}

- A aplicação serve na **porta 8080** e anuncia `polyfieldserver.local`, pelo que os dispositivos de campo e os ecrãs podem usar `http://polyfieldserver.local:8080` sem o endereço IP. Alguns dispositivos Android exigem o endereço IP completo, pelo que também pode usar `http://192.168.0.10:8080`, substituindo 192.168.0.10 pelo endereço do servidor anunciado no Painel.
- Em computadores com mais do que um adaptador de rede (comum no Windows), escolha o adaptador correto no topo do painel para que o endereço certo seja anunciado.
- Todos os dispositivos — aplicações de campo e ecrãs — devem estar na mesma rede que o computador anfitrião.

## Diagnóstico    {#diagnostics}

Se algo correr mal, utilize o relatório de diagnóstico. Ele reúne a competição atual (que o apoio pode reproduzir), os registos e os dados de vento do dia num único ficheiro zip, e preenche previamente um e-mail para [support@polyfield.co.uk](mailto:support@polyfield.co.uk). Anexe o ficheiro guardado antes de enviar. O mesmo pacote pode ser usado para recuperar uma competição se for necessário trocar de máquina a meio do encontro.

![Relatório de diagnóstico](/PolyField-Server/images/diagnostics.png)

## Resolução de problemas    {#troubleshooting}

| Sintoma | Verificar |
|---------|-------|
| Um dispositivo de campo não consegue ligar-se | Confirme que está na mesma rede, que a porta 8080 é acessível e (em PCs com vários adaptadores) que o adaptador de rede correto está selecionado no topo do painel. Certifique-se de que a firewall não está a bloquear o PolyField Server. |
| Uma importação devolve 0 provas | A competição de origem pode ainda não ter inscrições, ou está selecionada uma competição diferente. Reverifique a competição para garantir que as listas de partida foram publicadas. |
| Um ecrã não está a atualizar | As páginas atualizam-se sozinhas; se uma estiver desatualizada, recarregue-a uma vez. Confirme que aponta para o endereço atual do servidor. Os ecrãs mostram a hora atual e o texto "LIVE" quando ligados, para ajudar a verificar. |
| Um anemómetro não mostra leitura | Verifique o endereço de rede do anemómetro e se está ligado e a transmitir; o modelo é detetado automaticamente assim que os dados chegam. O anemómetro mostrará o estado Ligado ou Desligado no servidor. |
| O painel RAZA está vazio | Os atletas precisam de uma classificação e de género definidos para que uma pontuação RAZA seja calculada. |
| Os resultados parecem fora de ordem ou falta uma ronda | Cada resultado é marcado temporalmente pela aplicação de campo; certifique-se de que os dispositivos de campo estão na prova correta e atualizados. Verifique se o relógio do dispositivo de campo e do servidor está correto, pois pode desviar-se se usado offline sem atualização. |

## Transferência e apoio    {#download-and-support}

Transfira a versão mais recente em [www.polyfield.co.uk](https://www.polyfield.co.uk) ou na página de versões. A aplicação verifica se há atualizações no arranque e mostra um aviso quando está disponível uma versão mais recente. Apoio: [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

## Integração via API {#api-integration}

O PolyField Server serve uma **API HTTP + JSON** na **porta 8080**, na **mesma rede local** dos seus dispositivos de campo e ecrãs. É a mesma interface que a aplicação de campo PolyField e os ecrãs integrados usam, pelo que qualquer coisa na LAN — um quadro de resultados personalizado, um painel de estatísticas, uma sobreposição de streaming, a sinalização própria de um recinto — pode ler as provas, os resultados ao vivo, as classificações, as estatísticas e o vento diretamente do servidor. As respostas são JSON, não há autenticação e o CORS está aberto, pelo que uma página de browser na LAN pode chamá-la diretamente. A maioria dos endpoints são `GET` só de leitura; os endpoints de escrita (`POST /api/v1/results`, `POST /api/v1/athlete/active`, `PUT /api/v1/events/status`) são usados pela aplicação de campo.

A API é **apenas para LAN por conceção** — a aplicação não a expõe à internet. **Qualquer integração voltada para a WAN ou a internet** (quadros de resultados remotos, serviços na nuvem, um segundo recinto) **deve ser discutida connosco primeiro** para ser feita em segurança, normalmente através de uma VPN ou de um proxy inverso controlado, em vez de abrir a porta ao mundo. Contacte [support@polyfield.co.uk](mailto:support@polyfield.co.uk).

**URL base:** `http://polyfieldserver.local:8080/api/v1` — ou use o endereço IP do servidor mostrado no topo do painel (p. ex. `http://192.168.0.10:8080/api/v1`).

**JSON Schema:** cada corpo de pedido e de resposta está definido num único [ficheiro JSON Schema (draft 2020-12)](/PolyField-Server/api/polyfield-api.schema.json), em `$defs`. Cada endpoint abaixo indica o tipo do seu corpo e inclui o respetivo esquema; os tipos partilhados estão em [Tipos de dados](#api-data-types). Para validar um corpo, referencie a sua definição, p. ex. `polyfield-api.schema.json#/$defs/ResultPayload`.

**Convenções**

- Os erros devolvem um estado 4xx/5xx com `{"error": "message"}`. Um método que um endpoint não aceita devolve `405`.
- As horas estão em RFC 3339, p. ex. `2026-06-14T13:42:07.512+01:00`.
- Marcas e alturas são strings em metros (`"46.38"`) para manter os zeros finais; o vento é uma string com sinal em m/s (`"+1.4"`).
- Os campos opcionais são omitidos quando vazios. Os mapas indexados por ronda usam chaves de texto (`"1"`, `"2"`, …).

| Método e caminho | Devolve |
|---|---|
| [`GET /api/v1/events`](#api-list-events) | Listar todas as provas (resumo). |
| [`GET /api/v1/events/{eventId}`](#api-get-event) | Obter uma prova com os seus atletas e todos os ensaios. |
| [`PUT/PATCH /api/v1/events/status`](#api-update-status) | Definir o estado de uma prova. |
| [`POST /api/v1/results`](#api-post-results) | Enviar a série de um atleta (a principal escrita da aplicação de campo). |
| [`POST /api/v1/athlete/active`](#api-post-active) | Sinalizar quem está em prova agora (saltos horizontais). |
| [`GET /api/v1/athlete/active/{eventId}`](#api-get-active) | Ler quem está em prova agora numa prova. |
| [`GET /api/v1/display/recent`](#api-display-recent) | Últimas marcas (painel de resultados). |
| [`GET /api/v1/display/standings`](#api-display-standings) | Classificações atuais de cada prova com marcas. |
| [`GET /api/v1/broadcast/recent`](#api-broadcast-recent) | Os últimos 10 resultados com todo o detalhe (transmissão / locutor). |
| [`GET /api/v1/raza`](#api-raza) | Classificações RAZA de para-atletismo. |
| [`GET /api/v1/statistics/overall`](#api-stats-overall) | Estatísticas de toda a competição. |
| [`GET /api/v1/statistics/event/{eventId}`](#api-stats-event) | Estatísticas detalhadas de uma prova. |
| [`GET /api/v1/wind/gauges`](#api-wind-gauges) | Listar os anemómetros e a sua última leitura. |
| [`GET /api/v1/wind/current`](#api-wind-current) | Vento médio agora, nos últimos segundos. |
| [`GET /api/v1/wind/search`](#api-wind-search) | Vento num momento passado (registo de hoje). |
| [`GET /api/v1/config`](#api-config) | Configuração dos ecrãs. |
| [`GET /api/v1/stream`](#api-stream) | Notificações de atualização ao vivo (Server-Sent Events). |

### `GET /api/v1/events` {#api-list-events}

Listar todas as provas (resumo). Devolve cada prova carregada no servidor como um resumo leve. A aplicação de campo usa-o para apresentar a escolha da prova.

```http
GET /api/v1/events
```

**Resposta — array de `EventSummary`:**

- `id` (string)
- `name` (string)
- `type` (string) — Categoria da prova. Valores conhecidos: "Throws", "Horizontal Jumps", "Vertical Jumps".

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

**Erros:**

- `405` — Qualquer método que não seja GET.

### `GET /api/v1/events/{eventId}` {#api-get-event}

Obter uma prova com os seus atletas e todos os ensaios. Devolve a prova completa. Usado pela aplicação de campo para transferir a lista de partida e os resultados já registados.

- `eventId` (caminho) — ID da prova, da lista de provas (codifique-o para o URL).

```http
GET /api/v1/events/dt-sw-f07
```

**Resposta — `Event`:**

- `id` (string)
- `name` (string)
- `originalName` (string, opcional)
- `type` (string) — Categoria da prova. Valores conhecidos: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `rules` (EventRules) — Formato de competição de uma prova.
- `athletes` (Athlete[])
- `calibrationMetadata` (CalibrationMetadata, opcional) — Geometria do campo registada ao calibrar o EDM.
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

**Erros:**

- `400` — Sem ID da prova no caminho. `{"error": "Event ID is required"}`
- `404` — Prova desconhecida. `{"error": "event with ID dt-xx not found"}`

### `PUT / PATCH /api/v1/events/status` {#api-update-status}

Definir o estado de uma prova. Muda uma prova entre Not Started, In Progress e Finished. O servidor também passa uma prova para In Progress automaticamente quando chega o seu primeiro resultado válido.

**Corpo do pedido — `EventStatusUpdate`:**

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

**Resposta — `SuccessResponse`:**

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

**Erros:**

- `400` — Campo em falta, prova desconhecida ou estado inválido. `{"error": "invalid status: Done. Must be one of: Not Started, In Progress, Finished"}`

### `POST /api/v1/results` {#api-post-results}

Enviar a série de um atleta (a principal escrita da aplicação de campo). Envia a série **completa** do atleta até agora; substitui o que o servidor tem para esse atleta, pelo que reenviar é seguro. O servidor determina que ensaios são novos ou foram alterados, atualiza as classificações e envia um `update` para os ecrãs. As marcas são normalizadas: `X`/`FOUL` passam a `NM`, `PASS`/`-` passam a `P`. Uma marca fora do intervalo fica registada no log, mas é guardada na mesma. Se o dorsal não estiver na prova, é adicionado um atleta provisório.

**Corpo do pedido — `ResultPayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `series` (Performance[]) — A série completa do atleta até agora. Substitui a série guardada.
- `heatmapCoordinates` (HeatmapCoordinate[], opcional)
- `calibrationMetadata` (CalibrationMetadata, opcional) — Geometria do campo registada ao calibrar o EDM.

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

*Salto horizontal com vento:*

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

*Salto vertical (um ensaio por entrada, com a altura da fasquia):*

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

**Resposta — `SuccessResponse`:**

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

**Erros:**

- `400` — O corpo não é JSON válido. `{"error": "Invalid request body"}`
- `404` — Prova desconhecida. `{"error": "event with ID dt-xx not found"}`

### `POST /api/v1/athlete/active` {#api-post-active}

Sinalizar quem está em prova agora (saltos horizontais). Sinal sem confirmação enviado pela aplicação de campo quando um saltador passa a ser o atleta ativo, usado pelo ecrã da régua da tábua de chamada. Um atleta por prova: cada envio substitui o anterior. **Não** é um resultado.

**Corpo do pedido — `ActiveAthletePayload`:**

- `eventId` (string)
- `athleteBib` (string)
- `athleteName` (string, opcional)
- `board` (number, opcional) — Distância da tábua de chamada em metros (0 = tábua do comprimento).
- `topPerformances` (number[], opcional) — Melhores marcas válidas até agora, da melhor para a pior. Máximo 3.

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

**Resposta — `OkResponse`:**

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

**Erros:**

- `400` — JSON inválido, ou falta eventId / athleteBib. `{"error": "eventId and athleteBib are required"}`

### `GET /api/v1/athlete/active/{eventId}` {#api-get-active}

Ler quem está em prova agora numa prova. Sempre 200 para que um widget possa sondar de forma simples; `active` é `null` quando ninguém foi sinalizado (entre atletas ou após um reinício).

- `eventId` (caminho) — ID da prova.

```http
GET /api/v1/athlete/active/dt-sw-f07
```

**Resposta — `ActiveAthleteResponse`:**

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

*Ninguém em prova:*

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

**Erros:**

- `400` — Sem ID da prova no caminho. `{"error": "Event ID is required"}`

### `GET /api/v1/display/recent` {#api-display-recent}

Últimas marcas (painel de resultados). As marcas mais recentes, da mais recente para a mais antiga. Alimenta o painel de resultados em `/`.

- `limit` (consulta) — Quantos devolver, 1-100. Predefinição 4; valores fora do intervalo voltam a 4.

```http
GET /api/v1/display/recent?limit=2
```

**Resposta — `RecentPerformancesResponse`:**

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

Classificações atuais de cada prova com marcas. Classificações de cada prova com pelo menos uma marca válida. Alimenta o ecrã `/tables`. `events` é `null` enquanto nenhuma prova tiver uma marca válida.

```http
GET /api/v1/display/standings
```

**Resposta — `EventStandingsResponse`:**

- `events` (EventStandings[]) — Apenas provas com pelo menos uma marca válida. null quando não há nenhuma.

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

Os últimos 10 resultados com todo o detalhe (transmissão / locutor). Até aos 10 resultados mais recentes, do mais recente para o mais antigo, com detalhe suficiente para redesenhar cada um (linhas do setor, ponto de queda, altura da fasquia e série). Alimenta a página `/announcer`.

```http
GET /api/v1/broadcast/recent
```

**Resposta — `DetailedRecentResultsResponse`:**

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

Classificações RAZA de para-atletismo. Atletas com classificação e género, pontuados com os pontos RAZA da World Para Athletics e agrupados por prova de referência. Alimenta o ecrã `/raza`.

```http
GET /api/v1/raza
```

**Resposta — `RazaResponse`:**

- `events` (RazaEventGroup[])
- `total` (integer) — Número total de atletas classificados.

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

Estatísticas de toda a competição. Totais, tempos, taxa de nulos, ensaios ao longo do tempo, cronologia das provas e zonas de queda por tipo de lançamento.

```http
GET /api/v1/statistics/overall
```

**Resposta — `OverallStatistics`:**

- `totalEvents` (integer)
- `eventsNotStarted` (integer)
- `eventsInProgress` (integer)
- `eventsCompleted` (integer)
- `totalAthletes` (integer)
- `totalAttempts` (integer)
- `totalValidAttempts` (integer)
- `totalFouls` (integer)
- `overallFoulRate` (number) — Percentagem 0-100.
- `competitionStartTime` (date-time, opcional)
- `competitionEndTime` (date-time, opcional)
- `totalDuration` (number) — Minutos.
- `eventsWithOpenTrack` (integer)
- `eventsWithCalibration` (integer)
- `eventsByType` (object) — Número de provas por categoria.
- `attemptsOverTime` (TimeSeriesPoint[])
- `eventTimeline` (EventTimelineItem[])
- `throwHeatmaps` (object, opcional) — Indexado pelo código do tipo de lançamento.

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

**Erros:**

- `500` — Não foi possível calcular as estatísticas.

### `GET /api/v1/statistics/event/{eventId}` {#api-stats-event}

Estatísticas detalhadas de uma prova. Tempos, rondas, nulos, marcas e dados de gráficos de uma prova. `windStats`, `heatmapStats` e `verticalJumpStats` só aparecem para o tipo de prova correspondente. Os mapas indexados por ronda usam o número da ronda como chave de texto.

- `eventId` (caminho) — ID da prova.

```http
GET /api/v1/statistics/event/dt-sw-f07
```

**Resposta — `EventStatistics`:**

- `eventId` (string)
- `eventName` (string)
- `eventType` (string) — Categoria da prova. Valores conhecidos: "Throws", "Horizontal Jumps", "Vertical Jumps".
- `status` ("Not Started" / "In Progress" / "Finished")
- `calibrationTime` (date-time, opcional)
- `firstAttemptTime` (date-time, opcional)
- `lastAttemptTime` (date-time, opcional)
- `setupDuration` (number) — Minutos da calibração até ao primeiro ensaio.
- `competitionDuration` (number) — Minutos do primeiro ao último ensaio.
- `totalEventDuration` (number) — Minutos da calibração até ao último ensaio.
- `averageTimeBetween` (number) — Segundos entre ensaios.
- `roundDurations` (object) — Ronda -> minutos.
- `avgTimePerAttemptByRound` (object) — Ronda -> minutos médios entre ensaios.
- `timeBetweenRounds` (object) — Ronda -> intervalo até à ronda seguinte (minutos).
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
- `bestMarkPerRound` (object) — Ronda -> melhor marca.
- `foulRateByRound` (object) — Ronda -> taxa de nulos.
- `athletesWithZeroFouls` (integer)
- `fastestAthlete` (AthleteTimingInfo, opcional)
- `slowestAthlete` (AthleteTimingInfo, opcional)
- `mostConsistent` (AthleteConsistencyInfo, opcional)
- `windStats` (WindStatistics, opcional) — Apenas saltos horizontais.
- `heatmapStats` (HeatmapStatistics, opcional) — Apenas lançamentos com coordenadas de queda.
- `verticalJumpStats` (VerticalJumpStatistics, opcional) — Apenas salto em altura / salto com vara.
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

**Erros:**

- `400` — Sem ID da prova no caminho. `{"error": "Event ID is required"}`
- `404` — Prova desconhecida. `{"error": "event with ID dt-xx not found"}`

### `GET /api/v1/wind/gauges` {#api-wind-gauges}

Listar os anemómetros e a sua última leitura.

```http
GET /api/v1/wind/gauges
```

**Resposta — `WindGaugesResponse`:**

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

Vento médio agora, nos últimos segundos.

- `gauge_id` (consulta) — Obrigatório. ID do anemómetro de /wind/gauges.
- `duration` (consulta) — Janela de média em segundos, 1-60. Predefinição 5.

```http
GET /api/v1/wind/current?gauge_id=back-pits&duration=5
```

**Resposta — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Velocidade média do vento na janela (m/s, + = vento a favor).
- `average_crosswind` (number)
- `readings` (number[]) — As velocidades individuais usadas na média.
- `timestamp` (date-time) — Hora da leitura (RFC 3339, precisão ao segundo).
- `direction` (integer) — Última direção em graus (0-360).

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

**Erros:**

- `400` — Falta gauge_id. `{"error": "gauge_id parameter is required"}`
- `404` — Anemómetro desconhecido. `{"error": "Wind gauge not found"}`
- `503` — Anemómetro offline ou sem leituras na janela. `{"error": "Wind gauge is offline"}`

### `GET /api/v1/wind/search` {#api-wind-search}

Vento num momento passado (registo de hoje). Encontra a leitura mais próxima da hora indicada no registo de hoje e faz a média das leituras a ±2.5 s dela. Serve para associar o vento a um salto posteriormente.

- `gauge_id` (consulta) — Obrigatório. ID do anemómetro.
- `timestamp` (consulta) — Obrigatório. Hora RFC 3339, codificada para o URL (p. ex. `2026-06-14T14%3A02%3A10Z`).

```http
GET /api/v1/wind/search?gauge_id=back-pits&timestamp=2026-06-14T14%3A02%3A10Z
```

**Resposta — `WindReadingResponse`:**

- `gauge_id` (string)
- `average_speed` (number) — Velocidade média do vento na janela (m/s, + = vento a favor).
- `average_crosswind` (number)
- `readings` (number[]) — As velocidades individuais usadas na média.
- `timestamp` (date-time) — Hora da leitura (RFC 3339, precisão ao segundo).
- `direction` (integer) — Última direção em graus (0-360).

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

**Erros:**

- `400` — Falta gauge_id ou timestamp, ou timestamp não é RFC 3339. `{"error": "Invalid timestamp format (use RFC3339)"}`
- `404` — Anemómetro desconhecido. `{"error": "Wind gauge not found"}`
- `503` — Nenhuma leitura guardada hoje. `{"error": "No wind readings available"}`

### `GET /api/v1/config` {#api-config}

Configuração dos ecrãs. O idioma da interface escolhido nas Definições, para que os ecrãs noutros dispositivos o usem também.

```http
GET /api/v1/config
```

**Resposta — `ConfigResponse`:**

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

Um fluxo [Server-Sent Events](https://developer.mozilla.org/pt-PT/docs/Web/API/Server-sent_events) (`text/event-stream`). O servidor envia `data: update` sempre que os resultados, o estado de uma prova ou o atleta ativo mudam — volte então a pedir o feed que mostra. Um comentário `: ping` a cada 25 segundos mantém a ligação aberta. A mensagem é apenas a palavra `update`, pelo que não tem JSON Schema.

```text
: connected

data: update

: ping
```

```js
const es = new EventSource('http://polyfieldserver.local:8080/api/v1/stream');
es.onmessage = (e) => { if (e.data === 'update') refresh(); };
```

Mantenha uma sondagem lenta (a cada 30–60 s) como alternativa, como fazem os ecrãs integrados. Sem o fluxo, sonde os feeds dos ecrãs a cada 1–2 segundos; as estatísticas só precisam de ser obtidas a pedido.

### Tipos de dados {#api-data-types}

Tipos usados em vários dos corpos acima. Todas as definições estão no [esquema para transferir](/PolyField-Server/api/polyfield-api.schema.json).

#### Performance {#api-type-performance}

Um ensaio de um atleta. As respostas incluem sempre unit, valid e timestamp.

- `attempt` (integer) — Número do ensaio, a partir de 1. O servidor identifica as alterações por este número.
- `mark` (string) — A marca. Lançamentos / saltos horizontais: uma distância em metros ("45.67"), "NM" (nulo; "X" e "FOUL" são aceites e normalizados para "NM") ou "P" (passagem; "PASS" e "-" aceites). Saltos verticais: "O" transposição, "X" falha, "P" passagem.
- `height` (string, opcional) — Apenas saltos verticais: altura da fasquia em metros ("1.85").
- `unit` (string, opcional) — Unidade da marca, normalmente "m".
- `wind` (string, opcional) — Leitura do vento em m/s como string com sinal ("+1.4", "-0.3"). Apenas saltos horizontais.
- `valid` (boolean, opcional) — true para uma marca / transposição válida, false para um nulo, uma falha ou uma passagem.
- `coordinates` (HeatmapCoordinate, opcional) — Posição de queda de um lançamento ou salto.
- `timestamp` (date-time, opcional) — Quando o ensaio aconteceu. Preenchido com a hora de receção no servidor se for omitido ou zero.

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

Posição de queda de um lançamento ou salto.

- `x` (number) — X bruto da queda no referencial do EDM (m).
- `y` (number) — Y bruto da queda no referencial do EDM (m).
- `distance` (number) — Distância medida (m).
- `round` (integer)
- `attempt` (integer)
- `valid` (boolean)
- `rx` (number, opcional) — X da queda rodado para que a linha central do setor aponte para cima (+Y). Calculado pelo servidor; apenas para lançamentos válidos com calibração das linhas do setor.
- `ry` (number, opcional) — Y da queda no referencial rodado (ver rx).

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

Geometria do campo registada ao calibrar o EDM.

- `circleType` (string) — Tipo de círculo / corredor de balanço, p. ex. "SHOT", "DISCUS", "HAMMER", "JAVELIN_ARC".
- `circleRadius` (number) — Raio do círculo em metros.
- `edmPosition` (Coordinate, opcional) — Uma posição X/Y em metros no referencial do EDM.
- `sectorLines` (SectorLines, opcional) — Geometria das linhas do setor de um círculo de lançamento.
- `timestamp` (string, opcional) — Quando a calibração foi feita (ISO 8601).
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

Geometria das linhas do setor de um círculo de lançamento.

- `rightLine` (Coordinate) — Uma posição X/Y em metros no referencial do EDM.
- `leftLine` (Coordinate) — Uma posição X/Y em metros no referencial do EDM.
- `sectorAngle` (number) — Ângulo do setor em graus (34.92 para um setor de lançamentos padrão).

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

Uma posição X/Y em metros no referencial do EDM.

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

Um concorrente e a sua série.

- `bib` (string)
- `order` (integer) — Ordem na lista de partida.
- `name` (string)
- `club` (string)
- `ageGroup` (string, opcional)
- `classification` (string, opcional) — Classe da World Para Athletics, p. ex. "F56".
- `gender` (string, opcional) — "M" ou "W" (usado para a pontuação RAZA).
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

Formato de competição de uma prova.

- `attempts` (integer) — Ensaios por atleta (p. ex. 3, 4 ou 6).
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

Corpo devolvido em cada resposta 4xx/5xx da API.

- `error` (string) — Mensagem de erro legível.

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
