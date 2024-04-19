def condiciones(edades_alumnos):
      # Verifica si es una lista
    if not isinstance(edades_alumnos, list):
        return "Error: El parámetro 'edades_alumnos' debe ser una lista de valores numéricos."
    # Verifica si la lista está vacía
    if len(edades_alumnos) == 0:
        return "Error: La lista de valores está vacía. Debe contener al menos un valor numérico."
    # Verifica que la lista tenga exactamente 30 elementos
    if len(edades_alumnos) != 30:
        return "Error: La lista de valores debe contener exactamente 30 elementos."
    # Verifica si todos los elementos de la lista son numéricos
    if not all(isinstance(valor, (int, float)) for valor in edades_alumnos):
        return "Los valores de la lista deben ser numéricos."
    # Si pasa todas las verificaciones, devuelve True
    return True
