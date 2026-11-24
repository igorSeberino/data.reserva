"""ETL das reservas dos hotéis: extrair, transformar e carregar.

"Organizar a bagunça antes de analisar": lê o arquivo original de reservas, corrige e
traduz o que for preciso e salva uma versão limpa que todo o grupo usa.

Uso rápido:
    python -c "import sys; sys.path.insert(0,'src'); import etl; etl.executar_etl()"
"""

from pathlib import Path

import pandas as pd

SEED = 42
RAIZ = Path(__file__).resolve().parents[1]
CAMINHO_BRUTO = RAIZ / "data" / "raw" / "hotels.csv"
CAMINHO_TRATADO = RAIZ / "data" / "processed" / "reservas_tratadas.parquet"

# Fim do período de treino (decisão D2): chegadas até esta data = "treino"; 2017 = "teste".
FIM_TREINO = pd.Timestamp("2016-12-31")

# Limite de diária considerado possível (decisão D3).
DIARIA_MAXIMA = 1000

# Colunas que só são conhecidas depois da chegada ou do cancelamento (decisão D4).
COLUNAS_DESCARTADAS = [
    "reservation_status",
    "reservation_status_date",
    "assigned_room_type",
    "booking_changes",
]

MESES = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
}

TRADUCOES = {
    "hotel": {"City Hotel": "Hotel de cidade", "Resort Hotel": "Resort"},
    "meal": {
        "BB": "Café da manhã",
        "HB": "Meia pensão",
        "FB": "Pensão completa",
        "SC": "Sem refeição",
        "Undefined": "Sem refeição",
    },
    "market_segment": {
        "Online TA": "Agência online",
        "Offline TA/TO": "Agência/operadora tradicional",
        "Groups": "Grupos",
        "Direct": "Direto",
        "Corporate": "Corporativo",
        "Complementary": "Cortesia",
        "Aviation": "Aviação",
        "Undefined": "Indefinido",
    },
    "distribution_channel": {
        "TA/TO": "Agência/operadora",
        "Direct": "Direto",
        "Corporate": "Corporativo",
        "GDS": "Sistema global de reservas",
        "Undefined": "Indefinido",
    },
    "deposit_type": {
        "No Deposit": "Sem depósito",
        "Non Refund": "Não reembolsável",
        "Refundable": "Reembolsável",
    },
    "customer_type": {
        "Transient": "Avulso",
        "Transient-Party": "Avulso ligado a outra reserva",
        "Contract": "Contrato",
        "Group": "Grupo",
    },
}

# Ordem final das colunas da base tratada (contrato com as issues #3, #4 e #5).
COLUNAS_TRATADAS = [
    "hotel",
    "cancelada",
    "antecedencia_dias",
    "data_chegada",
    "ano_chegada",
    "mes_chegada",
    "semana_chegada",
    "noites_fim_semana",
    "noites_semana",
    "total_noites",
    "adultos",
    "criancas",
    "bebes",
    "total_hospedes",
    "regime_refeicao",
    "pais",
    "segmento_mercado",
    "canal_distribuicao",
    "hospede_recorrente",
    "cancelamentos_anteriores",
    "reservas_anteriores_nao_canceladas",
    "tipo_quarto_reservado",
    "tipo_deposito",
    "tem_agente",
    "tem_empresa",
    "dias_lista_espera",
    "tipo_cliente",
    "diaria_media",
    "receita_estimada",
    "vagas_estacionamento",
    "pedidos_especiais",
    "conjunto",
]

COLUNAS_CATEGORICAS = [
    "hotel",
    "regime_refeicao",
    "pais",
    "segmento_mercado",
    "canal_distribuicao",
    "tipo_quarto_reservado",
    "tipo_deposito",
    "tipo_cliente",
    "conjunto",
]


def extrair() -> pd.DataFrame:
    """Lê o arquivo original de reservas, sem alterar nada nele.

    O texto "NULL" é lido como vazio, porque é assim que o arquivo marca informação ausente
    (por exemplo, reserva sem agência ou sem empresa).
    """
    return pd.read_csv(CAMINHO_BRUTO, na_values=["NULL"])


def _traduzir(serie: pd.Series, mapa: dict) -> pd.Series:
    """Traduz os valores de uma coluna e falha se aparecer algum valor não previsto."""
    traduzida = serie.map(mapa)
    faltando = sorted(serie[traduzida.isna()].dropna().unique())
    if faltando:
        raise ValueError(f"Valores sem tradução em '{serie.name}': {faltando}")
    return traduzida


def remover_impossiveis(df: pd.DataFrame) -> pd.DataFrame:
    """Remove só as reservas impossíveis (decisão D3).

    São elas: reservas com zero hóspedes, diária negativa e diária acima de € 1.000.
    Linhas repetidas **ficam**, porque não há número de reserva e, em geral, são reservas
    de grupo reais (vários quartos iguais reservados juntos).
    """
    hospedes = df["adults"] + df["children"].fillna(0) + df["babies"]
    impossivel = (hospedes == 0) | (df["adr"] < 0) | (df["adr"] > DIARIA_MAXIMA)
    return df.loc[~impossivel].copy()


def transformar(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica todas as regras de limpeza e tradução e devolve a base tratada.

    - remove as reservas impossíveis (D3);
    - descarta as colunas que "entregam a resposta" (D4) e os códigos de agência/empresa;
    - traduz as categorias para português e dá nomes claros às colunas;
    - cria colunas novas: data de chegada, total de noites, total de hóspedes,
      receita estimada e o conjunto de treino/teste (D2).
    """
    df = remover_impossiveis(df)

    mes = df["arrival_date_month"].map(MESES)
    data_chegada = pd.to_datetime(
        {"year": df["arrival_date_year"], "month": mes, "day": df["arrival_date_day_of_month"]}
    )

    t = pd.DataFrame(index=df.index)
    t["hotel"] = _traduzir(df["hotel"], TRADUCOES["hotel"])
    t["cancelada"] = df["is_canceled"].astype("int64")
    t["antecedencia_dias"] = df["lead_time"].astype("int64")
    t["data_chegada"] = data_chegada
    t["ano_chegada"] = df["arrival_date_year"].astype("int64")
    t["mes_chegada"] = mes.astype("int64")
    t["semana_chegada"] = df["arrival_date_week_number"].astype("int64")
    t["noites_fim_semana"] = df["stays_in_weekend_nights"].astype("int64")
    t["noites_semana"] = df["stays_in_week_nights"].astype("int64")
    t["total_noites"] = t["noites_fim_semana"] + t["noites_semana"]
    t["adultos"] = df["adults"].astype("int64")
    t["criancas"] = df["children"].fillna(0).astype("int64")
    t["bebes"] = df["babies"].astype("int64")
    t["total_hospedes"] = t["adultos"] + t["criancas"] + t["bebes"]
    t["regime_refeicao"] = _traduzir(df["meal"], TRADUCOES["meal"])
    t["pais"] = df["country"].fillna("Desconhecido")
    t["segmento_mercado"] = _traduzir(df["market_segment"], TRADUCOES["market_segment"])
    t["canal_distribuicao"] = _traduzir(
        df["distribution_channel"], TRADUCOES["distribution_channel"]
    )
    t["hospede_recorrente"] = df["is_repeated_guest"].astype("int64")
    t["cancelamentos_anteriores"] = df["previous_cancellations"].astype("int64")
    t["reservas_anteriores_nao_canceladas"] = df["previous_bookings_not_canceled"].astype("int64")
    t["tipo_quarto_reservado"] = df["reserved_room_type"]
    t["tipo_deposito"] = _traduzir(df["deposit_type"], TRADUCOES["deposit_type"])
    t["tem_agente"] = df["agent"].notna().astype("int64")
    t["tem_empresa"] = df["company"].notna().astype("int64")
    t["dias_lista_espera"] = df["days_in_waiting_list"].astype("int64")
    t["tipo_cliente"] = _traduzir(df["customer_type"], TRADUCOES["customer_type"])
    t["diaria_media"] = df["adr"].astype("float64")
    t["receita_estimada"] = (t["diaria_media"] * t["total_noites"]).round(2)
    t["vagas_estacionamento"] = df["required_car_parking_spaces"].astype("int64")
    t["pedidos_especiais"] = df["total_of_special_requests"].astype("int64")
    t["conjunto"] = (data_chegada <= FIM_TREINO).map({True: "treino", False: "teste"})

    for coluna in COLUNAS_CATEGORICAS:
        t[coluna] = t[coluna].astype("category")

    return t[COLUNAS_TRATADAS].reset_index(drop=True)


def carregar(df: pd.DataFrame) -> Path:
    """Salva a base tratada em formato parquet (rápido de ler e guarda os tipos das colunas)."""
    CAMINHO_TRATADO.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(CAMINHO_TRATADO, index=False)
    return CAMINHO_TRATADO


def carregar_dados_tratados() -> pd.DataFrame:
    """Lê a base tratada. É a função que todo o grupo usa para começar a análise."""
    return pd.read_parquet(CAMINHO_TRATADO)


def executar_etl() -> pd.DataFrame:
    """Roda o processo completo: extrair → transformar → carregar. Devolve a base tratada."""
    tratado = transformar(extrair())
    carregar(tratado)
    return tratado


if __name__ == "__main__":
    base = executar_etl()
    print(f"Base tratada salva em {CAMINHO_TRATADO} ({len(base):,} reservas)")
