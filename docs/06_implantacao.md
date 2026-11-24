# 6. Implantação: como o radar de risco funciona no dia a dia

> **Em uma frase:** toda manhã, cada reserva nova recebe uma nota de risco (baixo, médio ou
> alto), e é gerada a lista das reservas de **alto risco** com chegada nos próximos 30 dias.

Este documento é para a **gerência dos hotéis**. Todos os números vêm de
[`reports/tables/`](../reports/tables/) e dos notebooks
[`01`](../notebooks/01_etl_preparacao_dos_dados.ipynb) e
[`03`](../notebooks/03_modelo_preditivo.ipynb). Nada foi estimado fora deles.

## O que o radar entrega

- **Quase 4 em cada 10 reservas são canceladas** (37%), o que somou **€ 16,7 milhões** de
  receita estimada que não se concretizou em pouco mais de dois anos
  ([`01_resumo_do_problema.csv`](../reports/tables/01_resumo_do_problema.csv)).
- O radar de risco foi testado em **2017, ano que ele nunca tinha visto**, e passou nos dois
  critérios definidos antes de modelar
  ([`03_criterio_de_sucesso.csv`](../reports/tables/03_criterio_de_sucesso.csv)):

| Critério | Meta | Resultado |
|---|---|---|
| Acertar mais do que a "regra do gerente" (nota F1) | maior que 0,58 | **0,67** |
| Na faixa alta, pelo menos 7 em cada 10 cancelam | 70% ou mais | **81%** |

- A faixa **alta** tem **23%** das reservas, mas concentra **48%** de todos os cancelamentos
  ([`03_faixas_de_risco.csv`](../reports/tables/03_faixas_de_risco.csv)): um grupo pequeno
  que concentra quase metade dos cancelamentos.

## Como funciona no dia a dia

1. **Toda manhã**, o sistema dá uma nota de risco às reservas novas e atualiza as antigas.
2. É gerada a **lista de alto risco das chegadas dos próximos 30 dias**, ordenada pela
   receita em jogo (veja o exemplo abaixo).

## As faixas de risco

| Faixa | Chance de cancelar | Em 2017, cancelaram de fato |
|---|---|---|
| **Alto** | 60% ou mais | **81%** |
| **Médio** | de 30% a 60% | **52%** |
| **Baixo** | menos de 30% | **19%** |

Fonte: [`03_faixas_de_risco.csv`](../reports/tables/03_faixas_de_risco.csv).

> **Alarmes falsos:** mesmo na faixa alta, 19% dos hóspedes vieram (1.761 reservas em 2017).
> A nota de risco é uma chance, não uma certeza.

## Exemplo de lista diária

Abaixo, as 10 reservas de alto risco com mais receita em jogo entre 3 e 9 de julho de 2017
(uma semana do período de teste). Arquivo completo:
[`reports/tables/06_exemplo_lista_diaria.csv`](../reports/tables/06_exemplo_lista_diaria.csv),
gerado por [`src/exemplo_lista_diaria.py`](../src/exemplo_lista_diaria.py) a partir de
[`03_reservas_teste_com_risco.csv`](../reports/tables/03_reservas_teste_com_risco.csv).

| Hotel | Chegada | Reservada com (dias de antecedência) | Origem | Depósito | Noites | Receita em jogo (€) | Chance de cancelar |
|---|---|---|---|---|---|---|---|
| Resort | 03/07/2017 | 277 | Agência online | Sem depósito | 14 | 3.638 | 70% |
| Resort | 04/07/2017 | 335 | Agência online | Sem depósito | 14 | 2.696 | 72% |
| Resort | 05/07/2017 | 65 | Agência online | Sem depósito | 10 | 2.640 | 74% |
| Resort | 03/07/2017 | 347 | Agência online | Sem depósito | 10 | 2.320 | 76% |
| Resort | 03/07/2017 | 268 | Agência online | Sem depósito | 11 | 2.296 | 75% |
| Resort | 06/07/2017 | 140 | Agência online | Sem depósito | 12 | 2.261 | 66% |
| Hotel de cidade | 03/07/2017 | 153 | Agência online | Sem depósito | 14 | 2.129 | 72% |
| Resort | 03/07/2017 | 269 | Agência online | Sem depósito | 10 | 2.047 | 76% |
| Hotel de cidade | 08/07/2017 | 159 | Agência online | Sem depósito | 13 | 1.977 | 72% |
| Resort | 09/07/2017 | 315 | Agência online | Sem depósito | 8 | 1.942 | 73% |

Na vida real, a coluna "cancelou de fato" não existe (só se sabe depois). Por isso ela foi
deixada de fora da lista.

## Como saber se está funcionando

Acompanhar **todo mês**:

1. **Taxa real de cancelamento por faixa** (alto, médio, baixo). Se a faixa alta deixar de
   cancelar 8 em cada 10, ou se as faixas pararem de se separar, o radar perdeu a qualidade.
2. **Nota F1 do mês**, comparada com a regra do gerente, para confirmar que o radar continua
   avisando melhor do que ela.

## Manutenção

- **Retreinar o radar a cada 3 meses** com as reservas novas, para ele acompanhar o
  comportamento atual dos hóspedes.
- **Revisar** se algo mudou no mercado (nova companhia aérea, evento grande, mudança nas
  políticas de cancelamento). Esses fatores o radar não enxerga.

## Riscos e cuidados

| Risco | O que fazer |
|---|---|
| **Privacidade.** Os dados são de hóspedes na Europa, protegidos pelo **RGPD** (a lei europeia de proteção de dados). | Usar só os dados necessários, limitar quem acessa a lista e não guardar a nota de risco no cadastro permanente do hóspede. |
| **Dados antigos.** O radar aprendeu com 2015 a 2017, antes da pandemia. | Retreinar com dados recentes **antes** de usar de verdade. |
| **Alarme falso.** Na faixa alta, 19% dos hóspedes vieram. | Tratar a nota como chance, não como certeza; acompanhar a taxa real por faixa. |
| **Reservas "não reembolsáveis".** Elas cancelam 99% das vezes, um padrão estranho (possível reserva de grupo liberada depois ou erro de registro). | Investigar com a equipe antes de confiar nesse sinal ([`03_fatores_de_risco.csv`](../reports/tables/03_fatores_de_risco.csv)). |
| **Nota cai fora do treino.** F1 de 0,79 nos simulados do treino contra 0,67 em 2017. | Acompanhar a nota real mês a mês; a que vale é a de 2017. |
| **Só dois hotéis, sem dados de fora** (preço da concorrência, eventos, clima). | Não generalizar para outros hotéis sem testar. |
| **País fora do modelo.** O país foi deixado de fora de propósito (suspeita de registro tardio). | Manter assim até confirmar como o país é registrado. |

## Próximos passos

1. **Reprocessar o radar** com reservas mais recentes e confirmar que continua passando nos
   dois critérios de sucesso.
2. **Esclarecer as reservas "não reembolsáveis"** com a equipe do hotel (possível erro de
   registro).
