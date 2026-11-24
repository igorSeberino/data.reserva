# 6. Implantação: como o hotel usa o radar de risco no dia a dia

> **Em uma frase:** toda manhã, cada reserva nova recebe uma nota de risco (baixo, médio ou
> alto), e a equipe de reservas age primeiro nas de **alto risco**, antes que o quarto fique
> vazio.

Este documento é para a **gerência dos hotéis**. Todos os números vêm de
[`reports/tables/`](../reports/tables/) e dos notebooks
[`01`](../notebooks/01_etl_preparacao_dos_dados.ipynb) e
[`03`](../notebooks/03_modelo_preditivo.ipynb). Nada foi estimado fora deles.

## Por que vale a pena

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
  ([`03_faixas_de_risco.csv`](../reports/tables/03_faixas_de_risco.csv)). Ou seja, é
  possível focar o esforço num grupo pequeno que concentra quase metade do problema.

## Como o hotel usaria no dia a dia

1. **Toda manhã**, o sistema dá uma nota de risco às reservas novas e atualiza as antigas.
2. A equipe de reservas recebe a **lista de alto risco das chegadas dos próximos 30 dias**,
   ordenada pela receita em jogo (veja o exemplo abaixo).
3. Cada reserva da lista recebe a ação da faixa dela (tabela a seguir).
4. O resultado do contato (confirmou, alterou a data, cancelou, não respondeu) é anotado, para
   medir se está funcionando.

## O que fazer em cada faixa

| Faixa | Chance de cancelar | Em 2017, cancelaram de fato | O que fazer |
|---|---|---|---|
| **Alto** | 60% ou mais | **81%** | Contato de confirmação **7 a 14 dias antes** da chegada. Oferecer **alteração de data** em vez de cancelamento. Se não houver resposta, considerar **revenda controlada** do quarto. |
| **Médio** | de 30% a 60% | **52%** | **Lembrete automático por e-mail** com os serviços do hotel (restaurante, spa, passeios), para reforçar o compromisso. |
| **Baixo** | menos de 30% | **19%** | Nada muda. |

Fonte: [`03_faixas_de_risco.csv`](../reports/tables/03_faixas_de_risco.csv).

> **Importante:** nenhuma reserva é cancelada só porque o radar deu risco alto. A ação é um
> contato cordial. Mesmo na faixa alta, 19% dos hóspedes vieram (1.761 reservas em 2017), e
> esses não podem ser tratados como suspeitos.

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

## Piloto: 3 meses no Hotel de cidade

Em vez de mudar os dois hotéis de uma vez, o plano é um **piloto de 3 meses no Hotel de
cidade**, que tem a **maior taxa de cancelamento (42%, contra 28% do resort)**
([`01_resumo_do_problema.csv`](../reports/tables/01_resumo_do_problema.csv)). É onde há mais
a ganhar e onde o efeito aparece mais rápido.

- O **resort** segue como está e serve de **comparação**.
- Dentro do Hotel de cidade, se possível, **uma parte das reservas de alto risco não recebe
  contato** (grupo de comparação). Só assim dá para saber quanto do ganho vem de fato da ação.

## Quanto pode valer

A simulação do Renato mostra o que aconteceria se o hotel recuperasse só uma parte da receita
das reservas de alto risco que cancelam (€ 3,34 milhões entre janeiro e agosto de 2017). É uma
**estimativa com premissas**, não uma promessa
([`03_simulacao_impacto.csv`](../reports/tables/03_simulacao_impacto.csv)):

| Se o hotel recuperar... | Receita recuperada em 8 meses | Por mês |
|---|---|---|
| 10% (pessimista) | € 0,33 milhão | ≈ € 42 mil |
| 20% (moderado) | € 0,67 milhão | ≈ € 84 mil |
| 30% (otimista) | € 1,00 milhão | ≈ € 125 mil |

O piloto serve justamente para descobrir qual dessas faixas é a realista.

## Como saber se está funcionando

Acompanhar **todo mês**:

1. **Taxa real de cancelamento por faixa** (alto, médio, baixo). Se a faixa alta deixar de
   cancelar 8 em cada 10, ou se as faixas pararem de se separar, o radar perdeu a qualidade.
2. **Receita recuperada:** quartos que seriam perdidos e foram mantidos (data alterada) ou
   revendidos.
3. **Reclamações de hóspedes contatados.** Se aumentarem, o contato está incomodando e o texto
   ou o momento precisa mudar.
4. **Comparação com o grupo sem contato**, no piloto.

## Manutenção

- **Retreinar o radar a cada 3 meses** com as reservas novas, para ele acompanhar o
  comportamento atual dos hóspedes.
- **Revisar** se algo mudou no mercado (nova companhia aérea, evento grande, mudança nas
  políticas de cancelamento). Esses fatores o radar não enxerga.

## Riscos e cuidados

| Risco | O que fazer |
|---|---|
| **Privacidade.** Os dados são de hóspedes na Europa, protegidos pelo **RGPD** (a lei europeia de proteção de dados). | Usar só os dados necessários, limitar quem acessa a lista e não guardar a nota de risco no cadastro permanente do hóspede. |
| **Tratar o hóspede como "suspeito".** | O contato é um serviço ("confirmando a sua estadia"), nunca uma cobrança. Nenhuma reserva é cancelada pelo radar. |
| **Dados antigos.** O radar aprendeu com 2015 a 2017, antes da pandemia. | Retreinar com dados recentes **antes** de usar de verdade. |
| **Alarme falso.** Na faixa alta, 19% dos hóspedes vieram. | Contato cordial e de baixo custo; nunca penalizar o hóspede. |
| **Reservas "não reembolsáveis".** Elas cancelam 99% das vezes, um padrão estranho (possível reserva de grupo liberada depois ou erro de registro). | Investigar com a equipe antes de confiar nesse sinal ([`03_fatores_de_risco.csv`](../reports/tables/03_fatores_de_risco.csv)). |
| **Nota cai fora do treino.** F1 de 0,79 nos simulados do treino contra 0,67 em 2017. | Acompanhar a nota real mês a mês; a que vale é a de 2017. |
| **Só dois hotéis, sem dados de fora** (preço da concorrência, eventos, clima). | Não generalizar para outros hotéis sem testar. |
| **País fora do modelo.** O país foi deixado de fora de propósito (suspeita de registro tardio). | Manter assim até confirmar como o país é registrado. |

## Próximos passos

1. **Validar o plano** com a gerência e a equipe de reservas (quem recebe a lista e como).
2. **Reprocessar o radar** com reservas mais recentes e confirmar que continua passando nos
   dois critérios de sucesso.
3. **Investigar as reservas "não reembolsáveis"** com a equipe do hotel.
4. **Rodar o piloto de 3 meses** no Hotel de cidade, com grupo de comparação.
5. **Decidir** com os números do piloto se amplia para o resort.
