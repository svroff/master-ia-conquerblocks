# Conceptos Python - Seguimiento De Repaso

Este fichero no sustituye a `estado-actual.md`. Sirve para que el maestro detecte que conceptos necesitan repaso espaciado antes de avanzar.

Estados sugeridos:

- `consolidado`: Sergi lo explica y lo aplica con poca ayuda.
- `en_progreso`: lo aplica con apoyo, pero aun necesita calentamiento.
- `debil`: hay confusion recurrente o bloqueo reciente.
- `pendiente`: todavia no se ha practicado.

## Conceptos Actuales

| Concepto | Estado | Ultima evidencia | Proximo repaso recomendado |
|---|---|---|---|
| `with open(..., encoding="utf-8")` | consolidado | Usado en `contar_basico` y `contar_palabras` | Repaso corto al tocar escritura o JSON |
| `try/except FileNotFoundError` | consolidado | Aplicado en `contar_basico` con retorno `dict` seguro | Reforzar al definir nuevos contratos de retorno |
| Contrato de retorno de una funcion | en_progreso | Decidido devolver siempre `dict` en `contar_basico` | Repetir antes de nuevas excepciones |
| Conteo con diccionario | en_progreso | Practicado en `test_contador.py` y `contar_palabras` | Calentamiento antes de v0.3 |
| `dict.items()` como parejas | en_progreso | Usado para ordenar top de palabras | Calentamiento obligatorio antes de v0.3 |
| Indices de tupla `pareja[0]` / `pareja[1]` | en_progreso | Sergi explico palabra/frecuencia correctamente | Calentamiento obligatorio antes de v0.3 |
| `sorted(..., key=lambda ..., reverse=True)` | en_progreso | Cerrado en TextAnalyzer v0.2, no automatizado | Calentamiento obligatorio antes de v0.3 |
| Slicing `[:5]` | en_progreso | Usado para devolver top 5 | Calentamiento obligatorio antes de v0.3 |
| Decoradores basicos | consolidado | Decoradores cerrado para nivel actual | Reactivar antes de `@medir_tiempo` |
| Decorador `@medir_tiempo` | pendiente | Proximo paso de TextAnalyzer v0.3 | Introducir despues del calentamiento |

## Regla De Uso

Al empezar una clase, revisa esta tabla y elige un unico calentamiento pequeno. No conviertas el repaso en examen largo.

Cuando un concepto cambie de estado, actualiza solo la fila correspondiente y anade una evidencia breve.
