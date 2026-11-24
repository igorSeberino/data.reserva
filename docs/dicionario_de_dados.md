# Dicionário de dados (base tratada)

O que significa cada coluna de `data/processed/reservas_tratadas.parquet`, a base limpa que
todo o grupo usa (ler sempre com `carregar_dados_tratados()` de `src/etl.py`).

- **119.208 reservas** (uma por linha) e **32 colunas**, sem nenhum valor em branco.
- O nome e o significado de cada coluna original (em inglês) estão em [`data/README.md`](../data/README.md).
- **Pode usar para prever?** indica se a coluna pode entrar no modelo de previsão (issue #4).
  "Não" quer dizer que ela entregaria a resposta, repete outra coluna ou não seria conhecida
  no momento da previsão.

| Coluna | O que significa | Exemplo | Pode usar para prever? |
|---|---|---|---|
| `hotel` | Qual dos dois hotéis recebeu a reserva | `Hotel de cidade`, `Resort` | Sim |
| `cancelada` | **O que queremos prever:** 1 = a reserva foi cancelada; 0 = o hóspede veio | `1` | **Não** (é a resposta) |
| `antecedencia_dias` | Quantos dias antes da chegada a reserva foi feita | `69` (de 0 a 737) | Sim |
| `data_chegada` | Dia em que o hóspede deveria chegar | `2016-09-06` | Não (serve para separar treino e teste) |
| `ano_chegada` | Ano da chegada | `2016` | Não (o "ano que vem" nunca aparece no aprendizado) |
| `mes_chegada` | Mês da chegada, de 1 (janeiro) a 12 (dezembro) | `7` | Sim |
| `semana_chegada` | Semana do ano da chegada, de 1 a 53 | `28` | Sim |
| `noites_fim_semana` | Noites de sábado ou domingo na estadia | `1` | Sim |
| `noites_semana` | Noites de segunda a sexta na estadia | `2` | Sim |
| `total_noites` | Total de noites da estadia (as duas acima somadas) | `3` | Não (repete as duas acima) |
| `adultos` | Número de adultos | `2` | Sim |
| `criancas` | Número de crianças (em branco no original → 0) | `0` | Sim |
| `bebes` | Número de bebês | `0` | Sim |
| `total_hospedes` | Total de pessoas na reserva (adultos + crianças + bebês) | `2` | Não (repete as três acima) |
| `regime_refeicao` | O que está incluído na diária | `Café da manhã`, `Meia pensão`, `Pensão completa`, `Sem refeição` | Sim |
| `pais` | País de origem do hóspede, em código de 3 letras (em branco → `Desconhecido`) | `PRT` (Portugal), `GBR` (Reino Unido) | **Não** (suspeita de ser preenchido só no check-in; só para a análise exploratória) |
| `segmento_mercado` | Por onde a reserva chegou | `Agência online`, `Grupos`, `Direto`, `Corporativo` | Sim |
| `canal_distribuicao` | Canal técnico de venda | `Agência/operadora`, `Direto`, `Sistema global de reservas` | Sim |
| `hospede_recorrente` | 1 = o hóspede já esteve no hotel antes | `0` | Sim |
| `cancelamentos_anteriores` | Quantas reservas o hóspede já cancelou antes | `0` | Sim |
| `reservas_anteriores_nao_canceladas` | Quantas reservas anteriores o hóspede cumpriu | `0` | Sim |
| `tipo_quarto_reservado` | Tipo de quarto pedido (letra; os hotéis não informam o que cada letra é) | `A`, `D` | Sim |
| `tipo_deposito` | Se o hóspede deixou dinheiro adiantado | `Sem depósito`, `Não reembolsável`, `Reembolsável` | Sim |
| `tem_agente` | 1 = a reserva foi feita por uma agência de viagens | `1` | Sim |
| `tem_empresa` | 1 = a reserva foi feita ou paga por uma empresa | `0` | Sim |
| `dias_lista_espera` | Dias que a reserva ficou na lista de espera até ser confirmada | `0` | Sim |
| `tipo_cliente` | Tipo de reserva | `Avulso`, `Avulso ligado a outra reserva`, `Contrato`, `Grupo` | Sim |
| `diaria_media` | Preço médio por noite, em euros | `94,95` (de 0 a 510) | Sim |
| `receita_estimada` | Quanto a reserva vale: diária média × total de noites, em euros | `267,00` | Não (repete diária e noites) |
| `vagas_estacionamento` | Vagas de garagem pedidas | `0` | Sim |
| `pedidos_especiais` | Quantos pedidos especiais o hóspede fez (andar alto, berço...) | `0` (de 0 a 5) | Sim |
| `conjunto` | `treino` = chegada até 31/12/2016 (o modelo aprende com elas); `teste` = chegada em 2017 (usadas só para conferir o modelo no fim) | `treino` | Não (é só a separação) |

## O que foi descartado do arquivo original

| Coluna original | Por quê |
|---|---|
| `reservation_status`, `reservation_status_date` | Situação final da reserva e data dela: só existem **depois** do cancelamento ou da saída do hóspede. Seria "colar na prova" |
| `assigned_room_type` | Quarto entregue no check-in: só se sabe na chegada |
| `booking_changes` | Alterações até o check-in ou o cancelamento: vai sendo preenchida até o fim |
| `agent`, `company` (os códigos) | O número da agência ou empresa não diz nada ao gerente; guardamos só se havia ou não (`tem_agente`, `tem_empresa`) |
| `arrival_date_month` (nome do mês em inglês) e `arrival_date_day_of_month` | Viraram `mes_chegada` e `data_chegada` |
