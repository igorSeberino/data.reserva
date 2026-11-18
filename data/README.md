# Dados

## Origem

- **Arquivo:** `raw/hotels.csv` (119.390 linhas, 32 colunas, 16,9 MB)
- **SHA-256:** `7c2ae42a7353905ea136e5c2287f17c92c5435826598bfbb8491c6f0c7b1fc06`
- **Baixado de:** <https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv>
- **Fonte original:** Antonio, N.; de Almeida, A.; Nunes, L. *Hotel booking demand datasets*.
  Data in Brief, v. 22, p. 41–49, 2019. <https://doi.org/10.1016/j.dib.2018.11.126>
  (publicação em acesso aberto, CC BY 4.0).
- **O que é:** reservas reais de dois hotéis em Portugal — um hotel de cidade (Lisboa) e um
  resort (Algarve) — com chegadas entre 01/07/2015 e 31/08/2017. Os dados foram anonimizados
  pelos autores (sem nome ou documento de hóspede).

`raw/` nunca é alterado. A versão limpa é gerada por `src/etl.py` em
`processed/reservas_tratadas.parquet` (issue #2). O significado de cada coluna, em linguagem
simples, fica em `docs/dicionario_de_dados.md`.

## Colunas originais

| Coluna | Significado |
|---|---|
| `hotel` | `City Hotel` (cidade) ou `Resort Hotel` (resort) |
| `is_canceled` | 1 = reserva cancelada, 0 = hóspede veio (**é o que queremos prever**) |
| `lead_time` | dias entre o momento da reserva e a data de chegada |
| `arrival_date_year` / `_month` / `_week_number` / `_day_of_month` | data de chegada |
| `stays_in_weekend_nights` / `stays_in_week_nights` | noites de fim de semana / de dias úteis |
| `adults` / `children` / `babies` | número de hóspedes |
| `meal` | regime de refeição (`BB` café da manhã, `HB` meia pensão, `FB` pensão completa, `SC`/`Undefined` sem refeição) |
| `country` | país de origem (código ISO de 3 letras) |
| `market_segment` / `distribution_channel` | por onde a reserva chegou (agência online, operadora, direto, corporativo...) |
| `is_repeated_guest` | 1 = hóspede que já esteve no hotel |
| `previous_cancellations` / `previous_bookings_not_canceled` | histórico do hóspede |
| `reserved_room_type` / `assigned_room_type` | quarto reservado / quarto entregue no check-in |
| `booking_changes` | alterações feitas na reserva até o check-in ou cancelamento |
| `deposit_type` | `No Deposit`, `Non Refund` (não reembolsável), `Refundable` |
| `agent` / `company` | código da agência / empresa que reservou (`NULL` = nenhuma) |
| `days_in_waiting_list` | dias em lista de espera até a confirmação |
| `customer_type` | `Transient` (avulso), `Transient-Party` (avulso ligado a outra reserva), `Contract`, `Group` |
| `adr` | diária média em euros |
| `required_car_parking_spaces` | vagas de estacionamento pedidas |
| `total_of_special_requests` | pedidos especiais (andar alto, berço...) |
| `reservation_status` / `reservation_status_date` | situação final da reserva e data dessa situação |

## Problemas de qualidade conhecidos (tratados no ETL, issue #2)

- `children` vazio em 4 linhas; `country` = `NULL` em 488; `agent` em 16.340; `company` em 112.593.
- 180 reservas com zero hóspedes; 1 diária negativa (−6,38) e 1 diária de 5.400 €.
- 31.994 linhas idênticas a outra (não há número de reserva; muitas são reservas de grupo legítimas).
- `reservation_status`, `reservation_status_date`, `assigned_room_type` e `booking_changes`
  só são conhecidas depois da chegada ou do cancelamento: **não podem ser usadas para prever**.
