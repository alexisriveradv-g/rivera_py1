# rivera_py1

Paquete de Python con funciones de estadística descriptiva y detección de atípicos.

Autor: Alexis Rivera (alexisriveradv-g) - C110 Redes Neuronales y Deep Learning.

## Instalación desde GitHub

pip install git+https://github.com/alexisriveradv-g/rivera_py1.git

## Instalación desde ZIP

pip install rivera_py1.zip

## Uso

from rivera_py1 import visualizar_estadisticas_vector, detectar_atipicos

datos = [12, 15, 18, 20, 22, 25, 28, 30, 35, 40, 100]
stats = visualizar_estadisticas_vector(datos)
atipicos = detectar_atipicos(datos)

## Funciones

- visualizar_estadisticas_vector(vector): media, mediana, desviación estándar, varianza, mínimo, máximo, rango, cuartiles e IQR; muestra histograma y boxplot.
- detectar_atipicos(vector): detecta atípicos con la regla del IQR (1.5 x IQR).
