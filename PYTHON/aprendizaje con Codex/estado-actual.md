# Estado Actual de Aprendizaje

## Dónde estoy
Tema 1 de Python Avanzado — Recursividad y memoización retomadas tras una pausa. Siguiente: repasar memoización manual brevemente y pasar con calma a `@lru_cache`.

## Qué acabo de aprender
- Lambdas: funciones anónimas, map(), filter(), sorted(key=...). Bien consolidado.
- Recursividad básica: suma_hasta, factorial, potencia. Consolidado.
- Memoización explícita (dict manual): retomada y practicada con factorial y potencia. Concepto muy bien entendido.
- Memoización implícita (@lru_cache): vista y aplicada correctamente. Consolidado.
- Cache con un parámetro: uso de `cache[num]`.
- Cache con dos parámetros: uso de tuplas como clave, por ejemplo `cache[(base, exponente)]`.
- Visualización con `print()` internos: entendido cuándo se calcula y cuándo se reutiliza cache.

## Ejercicios completados (sesión 2026-04-21)
- `practica_recursividad.py`: factorial con dict cache + check `if num in cache`. ✅
- `ejercicio_01.py`: Collatz con @lru_cache. Costó entender el contador de pasos, pero lo resolvió. ✅
- `ejercicio_02.py`: Potencia con @lru_cache. Resuelto limpio a la primera. ✅
- `ejercicio_03.py`: Suma de dígitos. Demasiada dificultad para esta sesión — pendiente. ⏳

## Ejercicios completados (sesión 2026-05-04)
- Factorial con memoización manual, construido paso a paso: cache, caso base, cálculo recursivo, guardado y retorno. ✅
- Mejora del factorial guardando también el caso base en cache. ✅
- Pruebas con `factorial(5)`, `factorial(4)` y `factorial(7)` para entender reutilización de cache. ✅
- Potencia recursiva con memoización manual usando clave tupla `(base, exponente)`. ✅

## Qué me quedó a medias
- Suma de dígitos recursiva: no llega a entender cómo separar dígitos con `% 10` y `// 10`.
- Operadores `%` y `//`: necesita más práctica para interiorizarlos.
- Convertir el patrón manual de memoización a `@lru_cache` con calma, sin saltar pasos.

## Notas de sesión (2026-04-21)
- Sergi dio feedback directo: el maestro es demasiado frío, seco y asume demasiado.
- Necesita más calidez, paciencia y verificación de comprensión antes de avanzar.
- La dificultad subió demasiado rápido en el ejercicio 3 — ajustar la curva.

## Notas de sesión (2026-05-04)
- Sergi volvió después de unas dos semanas sin programar y pidió ir más despacio.
- La sesión funcionó muy bien con micro-pasos y una sola pieza nueva cada vez.
- Se reforzó la idea de que toda recursividad necesita caso base y que cada llamada debe acercarse a él.
- Sergi explicó correctamente que la cache evita recalcular valores ya conocidos.
- Decisión de hábito: cerrar antes de saturarse y mantener sesiones sostenibles.

## Siguiente paso
1. Empezar la próxima sesión leyendo `perfil-aprendiz.md`, `estado-actual.md` y `perfil-maestro.md`.
2. Repasar 5 minutos factorial y potencia con memoización manual.
3. Pasar el patrón a `@lru_cache` de forma guiada.
4. Retomar operadores `%` y `//` con ejemplos visuales.
5. Retomar `ejercicio_03.py` de suma de dígitos solo cuando `%` y `//` estén claros.
6. Empezar Decoradores después de cerrar bien memoización.
