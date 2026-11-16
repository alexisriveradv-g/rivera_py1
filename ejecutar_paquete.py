"""
Script de ejecución del paquete rivera_py1.
Taller 3 - C110 Redes Neuronales y Deep Learning
Autor: Alexis Rivera (alexisriveradv-g)
"""
from rivera_py1 import visualizar_estadisticas_vector, detectar_atipicos


def main():
    print("=" * 60)
    print("EJECUCIÓN DEL PAQUETE rivera_py1")
    print("=" * 60)
    datos = [12.0, 15.0, 18.0, 20.0, 22.0, 25.0, 28.0, 30.0, 35.0, 40.0, 100.0]
    print(f"\nVector de entrada ({len(datos)} elementos):")
    print(datos)
    print("\n--- Estadísticas descriptivas ---")
    stats = visualizar_estadisticas_vector(datos)
    print("\n--- Detección de atípicos (regla IQR) ---")
    atipicos = detectar_atipicos(datos)
    print("\n--- Resumen final ---")
    print(f"Media: {stats['Media']:.4f}")
    print(f"Mediana: {stats['Mediana']:.4f}")
    print(f"Desviación estándar: {stats['Desviación Estándar']:.4f}")
    print(f"Atípicos detectados: {len(atipicos['atipicos'])}")
    print("\nEjecución completada correctamente.")


if __name__ == "__main__":
    main()
