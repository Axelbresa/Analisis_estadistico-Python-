import pandas as pd

def data_fragment(edades_alumnos):
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

    # Guardar el DataFrame como archivo CSV
    df.to_csv('nuevo_datos.csv', index=False)
    
    # Que se guarde en el portapapeles
    df.to_clipboard()

    print(df)
    return df