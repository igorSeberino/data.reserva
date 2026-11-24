"""Gera um exemplo da lista diária de alto risco que a equipe de reservas receberia.

Usa as reservas de teste (2017) já com nota de risco, escolhe uma semana e mostra as 10 da faixa
alta com mais receita em jogo, com colunas em linguagem de gerente. Não faz nenhuma análise
nova: só reorganiza `reports/tables/03_reservas_teste_com_risco.csv`.

Uso: python src/exemplo_lista_diaria.py
"""

import pandas as pd

from visual import PASTA_TABELAS, salvar_tabela

INICIO_SEMANA = "2017-07-03"  # segunda-feira
FIM_SEMANA = "2017-07-09"  # domingo
QTD = 10


def gerar_lista() -> pd.DataFrame:
    reservas = pd.read_csv(
        PASTA_TABELAS / "03_reservas_teste_com_risco.csv", parse_dates=["data_chegada"]
    )
    semana = reservas[
        (reservas["data_chegada"] >= INICIO_SEMANA)
        & (reservas["data_chegada"] <= FIM_SEMANA)
        & (reservas["faixa_risco"] == "Alto")
    ]
    # Dentro da faixa alta, a equipe começa pelas reservas com mais receita em jogo.
    top = semana.sort_values(
        ["receita_estimada", "probabilidade_cancelamento"], ascending=False
    ).head(QTD)
    return pd.DataFrame(
        {
            "Hotel": top["hotel"].values,
            "Chegada": top["data_chegada"].dt.strftime("%d/%m/%Y").values,
            "Reservada com (dias de antecedência)": top["antecedencia_dias"].values,
            "Origem da reserva": top["segmento_mercado"].values,
            "Depósito": top["tipo_deposito"].values,
            "Noites": top["total_noites"].values,
            "Receita em jogo (€)": top["receita_estimada"].round(0).astype(int).values,
            "Chance de cancelar (%)": (top["probabilidade_cancelamento"] * 100).round(0).astype(int).values,
            "Faixa": top["faixa_risco"].values,
        }
    )


if __name__ == "__main__":
    lista = gerar_lista()
    salvar_tabela(lista, "06_exemplo_lista_diaria")
    print(lista.to_string(index=False))
