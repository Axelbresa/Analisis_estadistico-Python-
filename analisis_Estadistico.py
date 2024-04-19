from condiciones_lista import condiciones
from data_fragmet import data_fragment

def analisis_estadistico(edades_alumnos):
    # Verificar condiciones
    condicion_valida = condiciones(edades_alumnos)
    if condicion_valida is not True:
        return condicion_valida  # Retorna el mensaje de error

    data_fragment(edades_alumnos)

# Valores
edades_alumnos = [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# análisis estadístico de los valores se pasa como argumento las edades o valores
print(analisis_estadistico(edades_alumnos))
