# 1. Entendimento do negócio

> **Em uma frase:** quase 4 em cada 10 reservas dos dois hotéis são canceladas, e isso
> representa cerca de € 16,7 milhões em receita que não se concretizou em pouco mais de dois
> anos.

Todos os números deste documento vêm de
[`reports/tables/01_resumo_do_problema.csv`](../reports/tables/01_resumo_do_problema.csv),
calculados no notebook
[`01_etl_preparacao_dos_dados.ipynb`](../notebooks/01_etl_preparacao_dos_dados.ipynb).

## Quem é o cliente

A gerência de **dois hotéis em Portugal**:

- um **hotel de cidade**, em Lisboa;
- um **resort**, no Algarve.

Juntos, eles registraram **119.208 reservas** com chegadas entre julho de 2015 e agosto
de 2017.

## O problema

| | Hotel de cidade | Resort | Os dois juntos |
|---|---|---|---|
| Reservas | 79.162 | 40.046 | 119.208 |
| Canceladas | 33.078 | 11.120 | 44.198 |
| **Taxa de cancelamento** | **42%** | **28%** | **37%** |
| Receita estimada das canceladas | € 10,9 milhões | € 5,8 milhões | **€ 16,7 milhões** |

- **37% das reservas são canceladas**: quase 4 em cada 10.
- No **hotel de cidade** é pior: mais de 4 em cada 10.
- Somando diária × noites das reservas canceladas, são **€ 16,7 milhões** de receita
  estimada que não se concretizou, **39%** de tudo o que foi reservado (€ 42,7 milhões).

> "Receita estimada" é o que o hotel esperava receber se o hóspede viesse. Parte desses
> quartos pode ter sido revendida, então o prejuízo real é menor; mas a ordem de grandeza
> mostra o tamanho do problema.

## Por que isso dói

- **Quarto vazio:** um cancelamento perto da data quase nunca é revendido a tempo. A noite
  não vendida não volta.
- **Receita que não volta:** o hotel deixa de ganhar e, muitas vezes, recusou outros
  hóspedes porque o quarto parecia ocupado.
- **Equipe e compras planejadas à toa:** escala de funcionários, café da manhã, limpeza e
  estoque são preparados para hóspedes que não chegam.
- **Preço mal calibrado:** sem saber quantos vão cancelar, o hotel não sabe se deve vender
  mais quartos do que tem (como fazem as companhias aéreas) nem quanto cobrar.

## A pergunta de negócio

> **"Quais reservas têm alta chance de serem canceladas, antes da chegada do hóspede?"**

## Objetivos

- **Objetivo de negócio:** reduzir a receita perdida com cancelamentos.
- **Objetivo do projeto de dados:** estimar, para cada reserva, a **chance de
  cancelamento** e colocá-la numa faixa de risco fácil de entender:

| Faixa de risco | Chance de cancelar |
|---|---|
| Baixo | menos de 30% |
| Médio | de 30% a 60% |
| Alto | 60% ou mais |

## Critério de sucesso

Definido **antes** de construir o modelo, para não "ajustar a régua" depois. O modelo será
considerado útil se, nas reservas de **2017** (que ele nunca viu durante o aprendizado):

1. **acertar mais do que uma regra simples** que qualquer gerente usaria: "a reserva vai
   cancelar se foi feita com mais de 90 dias de antecedência ou com depósito não
   reembolsável". Se o modelo não superar essa regra, não vale a pena usá-lo; **e**
2. na faixa de **alto risco**, **pelo menos 7 de cada 10 reservas** realmente cancelarem.
   Assim, a maioria das reservas marcadas como alto risco é, de fato, um cancelamento.

Se o modelo não atingir esses dois pontos, isso será dito com transparência.

## O que temos e o que não temos

**Temos:**

- 119.208 reservas reais de dois hotéis, de 2015 a 2017;
- para cada reserva: antecedência, datas, noites, hóspedes, refeição, canal de venda, tipo
  de depósito, histórico do hóspede, diária e se foi cancelada.

**Não temos:**

- preço da concorrência, clima, eventos na cidade ou feriados;
- identificação do hóspede (os dados são anônimos), então não dá para acompanhar uma pessoa
  ao longo do tempo além do que a própria reserva informa;
- o motivo do cancelamento.

## Riscos do projeto

- **Dados antigos:** são de antes da pandemia. O comportamento de quem reserva pode ter
  mudado (mais reservas de última hora, mais cancelamento grátis).
- **Só dois hotéis:** o que vale para eles pode não valer para outros hotéis ou regiões.
- **Possíveis erros de registro:** encontramos reservas com zero hóspedes e diárias
  impossíveis (removidas na limpeza). Há também sinais de que algumas informações, como o
  país do hóspede, podem ter sido preenchidas só no check-in; por isso o país **não** é
  usado na previsão.
