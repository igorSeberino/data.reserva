"""Padrão visual comum dos gráficos do projeto.

A regra do grupo: tudo em cinza, só o que importa em destaque. Assim o gerente do hotel
bate o olho no gráfico e já vê onde está a mensagem.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
PASTA_FIGURAS = RAIZ / "reports" / "figures"
PASTA_TABELAS = RAIZ / "reports" / "tables"

CORES = {
    "cancelada": "#C8553D",
    "veio": "#8D99AE",
    "destaque": "#C8553D",
    "neutro": "#BFC5CF",
    "texto": "#2B2D42",
}


def aplicar_estilo() -> None:
    """Deixa os gráficos limpos e legíveis.

    Fonte grande (12 ou mais), fundo branco, sem bordas de cima e da direita e sem grade
    pesada, para que só os dados chamem a atenção.
    """
    plt.rcParams.update(
        {
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
            "figure.figsize": (9, 5),
            "font.size": 12,
            "axes.titlesize": 15,
            "axes.titleweight": "bold",
            "axes.titlelocation": "left",
            "axes.titlepad": 14,
            "axes.labelsize": 12,
            "xtick.labelsize": 12,
            "ytick.labelsize": 12,
            "legend.fontsize": 12,
            "legend.frameon": False,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.edgecolor": CORES["neutro"],
            "axes.grid": False,
            "text.color": CORES["texto"],
            "axes.labelcolor": CORES["texto"],
            "xtick.color": CORES["texto"],
            "ytick.color": CORES["texto"],
        }
    )


def salvar_figura(fig, nome: str) -> Path:
    """Salva o gráfico em reports/figures/{nome}.png (dpi 150, sem margem sobrando)."""
    PASTA_FIGURAS.mkdir(parents=True, exist_ok=True)
    caminho = PASTA_FIGURAS / f"{nome}.png"
    fig.savefig(caminho, dpi=150, bbox_inches="tight")
    return caminho


def salvar_tabela(df: pd.DataFrame, nome: str) -> Path:
    """Salva a tabela em reports/tables/{nome}.csv (UTF-8, sem índice)."""
    PASTA_TABELAS.mkdir(parents=True, exist_ok=True)
    caminho = PASTA_TABELAS / f"{nome}.csv"
    df.to_csv(caminho, index=False, encoding="utf-8")
    return caminho
