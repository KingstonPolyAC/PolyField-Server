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
