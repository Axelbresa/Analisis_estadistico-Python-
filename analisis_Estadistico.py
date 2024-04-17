import pandas as pd

def analisis_estadistico(valores):
    """
    Realiza un análisis estadístico básico de una lista de valores numéricos.

    Parámetros:
    valores (list): Lista de valores numéricos.

    Retorna:
    pandas.DataFrame: Dataframe que contiene las siguientes columnas como claves:
        - 'fi': Frecuencia absoluta de cada valor en la lista.
        - 'Fi': Frecuencia acumulada.
        - 'ri': Frecuencia relativa.
        - 'Ri': Frecuencia relativa acumulada.
        - 'pi%': Probabilidad (en porcentaje).
        - 'Pi%': Probabilidad acumulada (en porcentaje).
    """
    if not isinstance(valores, list):
        return "Error: El parámetro 'valores' debe ser una lista de valores numéricos."
    if len(valores) == 0:
        return "Error: La lista de valores está vacía. Debe contener al menos un valor numérico."
    if len(valores) != 30:
        return "Error: La lista de valores debe contener exactamente 30 elementos."

    # Continuar con el análisis estadístico
    print(valores)


# Valores
valores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

# análisis estadístico de los valores
resultado_analisis = analisis_estadistico(valores)
print(resultado_analisis)