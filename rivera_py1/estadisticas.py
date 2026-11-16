import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualizar_estadisticas_vector(vector):
    """Calcula estadísticas descriptivas y muestra histograma + boxplot."""
    v = np.asarray(vector, dtype=float)
    stats = {
        "Media": np.mean(v),
        "Mediana": np.median(v),
        "Desviación Estándar": np.std(v, ddof=1),
        "Varianza": np.var(v, ddof=1),
        "Mínimo": np.min(v),
        "Máximo": np.max(v),
        "Rango": np.ptp(v),
        "Q1 (25%)": np.percentile(v, 25),
        "Q3 (75%)": np.percentile(v, 75),
        "IQR": np.percentile(v, 75) - np.percentile(v, 25),
    }
    print("=" * 40)
    for k, val in stats.items():
        print(f"{k:<30}: {val:.4f}")
    print("=" * 40)

    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(v, kde=True, ax=axes[0], color="skyblue", bins="auto")
    axes[0].axvline(stats["Media"], color="red", linestyle="--",
                    label=f"Media: {stats['Media']:.2f}")
    axes[0].axvline(stats["Mediana"], color="green", linestyle="-",
                    label=f"Mediana: {stats['Mediana']:.2f}")
    axes[0].legend()
    axes[0].set_title("Histograma")
    sns.boxplot(y=v, ax=axes[1], color="lightgreen", width=0.4)
    axes[1].set_title("Boxplot")
    plt.tight_layout()
    plt.show()
    return stats


def detectar_atipicos(vector):
    """Detecta atípicos con la regla del IQR (1.5 × IQR)."""
    v = np.asarray(vector, dtype=float)
    q1 = np.percentile(v, 25)
    q3 = np.percentile(v, 75)
    iqr = q3 - q1
    li = q1 - 1.5 * iqr
    ls = q3 + 1.5 * iqr
    atipicos = v[(v < li) | (v > ls)]
    print(f"Límite inferior (Q1 - 1.5·IQR): {li:.4f}")
    print(f"Límite superior (Q3 + 1.5·IQR): {ls:.4f}")
    print(f"Número de atípicos: {len(atipicos)}")
    print(f"Valores atípicos: {atipicos}")
    return {"limite_inferior": li, "limite_superior": ls, "atipicos": atipicos}
