# data.reserva — Quem vai cancelar a reserva?

> **Em uma frase:** quase 4 em cada 10 reservas dos dois hotéis estudados são canceladas.
> Este projeto usa o histórico de reservas para entender **por que** isso acontece, **prever**
> quais reservas têm mais chance de cancelar e **recomendar** o que a gerência pode fazer a respeito.

<!-- SEÇÃO: RESUMO EXECUTIVO — Gabriel (#5) -->
_Resumo executivo para a gerência do hotel: a preencher na issue #5._
<!-- FIM: RESUMO EXECUTIVO -->

---

## Para quem é este trabalho

Para a **gerência de dois hotéis em Portugal** (um hotel de cidade e um resort), que não tem
formação técnica. Tudo aqui é escrito para ser entendido por essa pessoa: frases curtas,
exemplos concretos e números em contexto ("4 em cada 10 reservas"), não jargão.

## A pergunta de negócio

**"Quais reservas têm alta chance de serem canceladas e o que podemos fazer, antes da chegada
do hóspede, para não perder a receita desses quartos?"**

## Como o trabalho foi organizado (CRISP-DM)

Seguimos as 6 fases do CRISP-DM, um roteiro padrão de projetos de dados: entender o negócio,
entender os dados, preparar os dados, construir o modelo, avaliar e colocar em uso.

| Fase do CRISP-DM | O que responde | Entrega | Responsável |
|---|---|---|---|
| 1. Entendimento do negócio | Qual é o problema e o que é sucesso? | [`docs/01_entendimento_do_negocio.md`](docs/01_entendimento_do_negocio.md) | Igor (#2) |
| 2. Entendimento dos dados (EDA) | O que os dados mostram? | [`notebooks/02_entendimento_dos_dados.ipynb`](notebooks/02_entendimento_dos_dados.ipynb) | Adrian (#3) |
| 3. Preparação dos dados (ETL) | Os dados são confiáveis? | [`notebooks/01_etl_preparacao_dos_dados.ipynb`](notebooks/01_etl_preparacao_dos_dados.ipynb) · [`src/etl.py`](src/etl.py) | Igor (#2) |
| 4. Modelagem (análise preditiva) | Dá para prever o cancelamento? | [`notebooks/03_modelo_preditivo.ipynb`](notebooks/03_modelo_preditivo.ipynb) | Renato (#4) |
| 5. Avaliação | O modelo é bom o bastante para o hotel? | [`notebooks/03_modelo_preditivo.ipynb`](notebooks/03_modelo_preditivo.ipynb) (parte final) | Renato (#4) |
| 6. Implantação + Data Storytelling | Como usar no dia a dia e como contar a história? | [`docs/06_implantacao.md`](docs/06_implantacao.md) · [`apresentacao/`](apresentacao/) | Gabriel (#5) |

O planejamento completo está na issue #1.

---

<!-- SEÇÃO: 1 ENTENDIMENTO DO NEGÓCIO + 3 PREPARAÇÃO — Igor (#2) -->
## 1. O problema do hotel

_A preencher na issue #2._

## 3. Preparação dos dados

_A preencher na issue #2._
<!-- FIM: IGOR -->

<!-- SEÇÃO: 2 ENTENDIMENTO DOS DADOS — Adrian (#3) -->
## 2. O que os dados mostram

_A preencher na issue #3._
<!-- FIM: ADRIAN -->

<!-- SEÇÃO: 4 MODELAGEM + 5 AVALIAÇÃO — Renato (#4) -->
## 4. Prevendo cancelamentos

_A preencher na issue #4._

## 5. O modelo é bom o bastante?

_A preencher na issue #4._
<!-- FIM: RENATO -->

<!-- SEÇÃO: 6 IMPLANTAÇÃO E RECOMENDAÇÕES — Gabriel (#5) -->
## 6. O que o hotel deve fazer

_A preencher na issue #5._
<!-- FIM: GABRIEL -->

---

## Os dados

119.390 reservas reais de dois hotéis portugueses, com chegadas entre julho de 2015 e agosto
de 2017. Fonte, licença e significado de cada coluna em [`data/README.md`](data/README.md).

## Estrutura do repositório

```
data/raw/            dados originais, nunca alterados (hotels.csv)
data/processed/      dados tratados pelo ETL (reservas_tratadas.parquet)
src/etl.py           funções de extração, transformação e carga
notebooks/           um notebook por etapa, executados e com saídas
reports/figures/     gráficos (PNG) usados no README e na apresentação
reports/tables/      tabelas de resultados (CSV)
docs/                textos das fases do CRISP-DM e dicionário de dados
apresentacao/        slides, PDF final e roteiro de fala
```

## Como rodar

Plataforma: VSCode + Jupyter Notebook (os notebooks também abrem no Google Colab).

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace notebooks/01_etl_preparacao_dos_dados.ipynb
```

Ordem de execução: `01` → `02` → `03`.

## Convenções do projeto

- **Linguagem para leigo:** cada gráfico tem um título que já diz a conclusão
  (ex.: "Quem reserva com mais de 6 meses de antecedência cancela o dobro"). Termos técnicos,
  quando inevitáveis, vêm explicados em uma frase.
- **Números só com origem:** todo número escrito no README, nos docs ou nos slides vem de uma
  saída de notebook ou de `reports/tables/`.
- **Dados:** sempre ler por `src/etl.py` (`carregar_dados_tratados()`); nunca alterar `data/raw/`.
- **Aleatoriedade:** `SEED = 42` em tudo.
- **Git:** branch `{tipo}/{issue}-{slug}` (ex.: `feat/3-eda`), commits no padrão
  [Conventional Commits](https://www.conventionalcommits.org/pt-br/) em português
  (ex.: `feat(eda): adiciona análise de antecedência`), PR com `Closes #N`, aprovado pelo
  revisor indicado na issue, merge com "Create a merge commit". Nunca commitar direto na `main`.
- Cada integrante edita apenas os próprios arquivos e a própria seção deste README
  (entre os marcadores `<!-- SEÇÃO -->` e `<!-- FIM -->`).

## Equipe

Adrian Cesar Gonçalves (@adrian-cesar) · Gabriel Carvalho (@gabrielcarvallho) ·
Igor Thiago Seberino (@igorSeberino) · Renato Colin Neto (@rcolinneto)
