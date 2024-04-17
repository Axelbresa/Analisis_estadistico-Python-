import pandas as pd

def analisis_estadistico(edades_alumnos):
    #Se maneja entrada de valores en caso contrario lanza un mensaje de error:

    # Verifica si todos los elementos de la lista son numéricos
    if not all(isinstance(valor, (int, float)) for valor in edades_alumnos):
        return "Los valores de la lista deben ser numéricos."
    # Verifica si es una lista
    if not isinstance(edades_alumnos, list):
        return "Error: El parámetro 'valores' debe ser una lista de valores numéricos."
    #Verifica si la lista esta vacia
    if len(edades_alumnos) == 0:
        return "Error: La lista de valores está vacía. Debe contener al menos un valor numérico."
    #Verifica que la lista tenga 30 numeros
    if len(edades_alumnos) != 30:
        return "Error: La lista de valores debe contener exactamente 30 elementos."


    # Calcular frecuencia absoluta
    frecuencia_absoluta = {valor: edades_alumnos.count(valor) for valor in set(edades_alumnos)}
    # Crear el DataFrame con las columnas requeridas
    df = pd.DataFrame({
        'fi': pd.Series(frecuencia_absoluta),
        'Fi': pd.Series(frecuencia_absoluta).cumsum(),
    })

    # Calcular frecuencia relativa y acumulada relativa
    df['ri'] = df['fi'] / len(edades_alumnos)
    df['Ri'] = df['Fi'] / len(edades_alumnos)

    # Calcular porcentaje y porcentaje acumulada en porcentaje
    df['pi%'] = df['ri'] * 100
    df['Pi%'] = df['Ri'] * 100

    # Asignar nombre al índice
    df.index.name = 'edades'

    return df

# Valores
edades_alumnos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

# análisis estadístico de los valores
resultado_analisis = analisis_estadistico(edades_alumnos)
print(resultado_analisis)
