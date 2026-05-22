# Estado Actual de Aprendizaje

## Dónde estoy
Tema 2 de Python Avanzado — Decoradores iniciado. Sergi ya entiende que decorar una función significa sustituirla por un `wrapper` que añade comportamiento alrededor de la función original.

## Qué acabo de aprender
- Lambdas: funciones anónimas, map(), filter(), sorted(key=...). Bien consolidado.
- Recursividad básica: suma_hasta, factorial, potencia. Consolidado.
- Memoización explícita (dict manual): retomada y practicada con factorial y potencia. Concepto muy bien entendido.
- Memoización implícita (@lru_cache): vista y aplicada correctamente. Consolidado.
- Cache con un parámetro: uso de `cache[num]`.
- Cache con dos parámetros: uso de tuplas como clave, por ejemplo `cache[(base, exponente)]`.
- Visualización con `print()` internos: entendido cuándo se calcula y cuándo se reutiliza cache.
- Importante: la caché manual vive durante una ejecución del programa. Si el script se ejecuta de nuevo, `cache = {}` vuelve a empezar vacía.
- Para ver reutilización de caché, hacen falta dos llamadas dentro de la misma ejecución, por ejemplo calcular primero `potencia(2, 4)` y luego pedir `potencia(2, 3)`.
- `@lru_cache` memoriza automáticamente por combinación de argumentos. Misma entrada implica resultado reutilizable.
- Con `@lru_cache`, si un resultado está cacheado, Python no entra en el cuerpo de la función; por eso no se ejecutan los `print()` internos.
- En `potencia(2, 5)` tras haber calculado `potencia(2, 4)`, solo se calcula `2^5`; `2^4` sale de caché.
- En `factorial(6)` tras haber calculado `factorial(5)`, solo se calcula `factorial(6)`; `factorial(5)` sale de caché.
- `factorial.cache_info()` permite ver `hits`, `misses`, `maxsize` y `currsize`.
- `hits`: llamadas resueltas desde caché.
- `misses`: llamadas que no estaban en caché y tuvieron que calcularse. Si esa misma entrada se pide más adelante, podrá convertirse en `hit`.
- `factorial.cache_clear()` vacía la caché de esa función concreta y reinicia `hits`, `misses` y `currsize`.
- `% 10` extrae el último dígito de un número entero.
- `// 10` elimina el último dígito de un número entero.
- `return ultimo_digito + suma_digitos(resto_numero)` significa: "sumo mi último dígito con la suma recursiva de los dígitos restantes".
- En suma de dígitos, la recursividad baja reduciendo el número (`9876 -> 987 -> 98 -> 9 -> 0`) y sube resolviendo las sumas pendientes.

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

## Ejercicios completados (sesión 2026-05-08)
- Retomada suave tras varios días sin clase. ✅
- Verificado el ejercicio `practica-memo-exponente.py`. ✅
- Asumido que la primera llamada calcula y llena la caché, y que la segunda llamada dentro de la misma ejecución reutiliza valores guardados. ✅
- Confirmado el uso de tuplas `(base, exponente)` como clave de caché para funciones con dos parámetros. ✅
- Se creó una rama de trabajo para el bloque de memoización. Convención acordada: `learning/<tema>`, por ejemplo `learning/memoizacion`. ✅
- Convertido `potencia(base, exponente)` de caché manual a `@lru_cache` por capas: import, decorador, eliminación del diccionario, eliminación del check manual y eliminación del guardado manual. ✅
- Practicado `@lru_cache` con `potencia(2, 4)`, `potencia(2, 3)`, `potencia(2, 5)` y `potencia(3, 3)`. ✅
- Creado `practica-lru-factorial.py` con `factorial(num)` recursivo usando `@lru_cache`. ✅
- Practicado `factorial(5)`, `factorial(3)` y `factorial(6)` para comprobar reutilización de caché. ✅
- Sergi verbalizó que con el maestro aprender resulta fácil y una gozada. La sesión terminó con sensación positiva, claridad conceptual y confianza. ✅

## Sensaciones de sesión (2026-05-08)
- Sergi se mostró cómodo con la dinámica de micro-pasos: él teclea, el maestro observa, corrige y explica el porqué.
- El paso de caché manual a `@lru_cache` se entendió como simplificación natural, no como magia.
- La frase clave del alumno fue que aprender con el maestro es fácil y una gozada. Mantener esta mezcla de paciencia, claridad y avance progresivo.
- Sensación del maestro: Sergi no solo siguió instrucciones; detectó comportamientos, formuló hipótesis y explicó correctamente cuándo se calculaba y cuándo se reutilizaba caché.

## Ejercicios completados (sesión 2026-05-12)
- Practicado `factorial.cache_info()` sobre `practica-lru-factorial.py`. ✅
- Entendidos `hits`, `misses`, `maxsize` y `currsize`. ✅
- Practicado `factorial.cache_clear()` y entendido que limpia la memoria interna de `@lru_cache`. ✅
- Explicado cuándo interesa limpiar caché: datos externos cambiantes o liberación de memoria; no suele hacer falta en funciones puras como `factorial`. ✅
- Creado `practica-modulo-division.py` para practicar `% 10` y `// 10`. ✅
- Entendido que `% 10` saca el último dígito y `// 10` quita el último dígito. ✅
- Creado `practica-suma-digitos.py` y montada la primera versión recursiva de `suma_digitos(9876)`. ✅

## Sensaciones de sesión (2026-05-12)
- Duración de la clase: 60 minutos.
- Sergi entendió bien `cache_info()`, `cache_clear()`, `% 10` y `// 10`.
- La suma de dígitos recursiva quedó montada, pero el último `return ultimo_digito + suma_digitos(resto_numero)` no quedó plenamente entendido porque Sergi estaba cansado y con la mente en otras cosas.
- Próxima sesión: no avanzar de golpe. Reexplicar ese `return` con una traza visual y quizá una tabla de llamadas antes de pasar a decoradores.

## Ejercicios completados (sesión 2026-05-14)
- Reexplicado con calma el retorno recursivo `ultimo_digito + suma_digitos(resto_numero)`. ✅
- Consolidada la diferencia entre la bajada de llamadas y la subida de resultados. ✅
- Revisado y completado `ejercicio_03.py`: suma de dígitos recursiva con `@lru_cache`. ✅
- Corregido el nombre del parámetro de `digito` a `numero` para que el código sea más claro. ✅
- Tema de memoización dado por terminado. ✅

## Sensaciones de sesión (2026-05-14)
- La explicación visual de la bajada `9876 -> 987 -> 98 -> 9 -> 0` y la subida `9 + 0`, `8 + 9`, `7 + 17`, `6 + 24` funcionó bien.
- Sergi detectó una duda real en el paso `suma_digitos(9)` y corrigió la confusión entre `ultimo_digito` y `resto_numero`.
- La sesión cerró con claridad suficiente para pasar a Decoradores.

## Ejercicios completados (sesión 2026-05-15)
- Duración de la clase: 45 minutos.
- Iniciado el bloque de Decoradores desde la conexión con `@lru_cache`. ✅
- Entendido que `@decorador` equivale a `funcion = decorador(funcion)`. ✅
- Creado `01-decoradores.py` con un decorador básico que imprime antes y después de una función. ✅
- Entendido que, tras decorar, el nombre de la función apunta primero al `wrapper`. ✅
- Creado `02-decoradores.py` con `wrapper(*args, **kwargs)` y una función decorada con argumento por defecto. ✅
- Entendido que `*args` recoge argumentos posicionales y los reenvía a la función original. ✅
- Entendido que `**kwargs` recoge argumentos con nombre y que el patrón estándar es `wrapper(*args, **kwargs)`. ✅
- Guardada la preferencia de llamar "maestro" al tutor durante las clases. ✅

## Ejercicios completados (sesión 2026-05-22)
- Retomado `03_decoradores.py` con decorador que envuelve una función `sumar(a, b)`. ✅
- Consolidado que `resultado = funcion_original(*args, **kwargs)` recibe el valor devuelto por la función original dentro del `wrapper`. ✅
- Probado el fallo pedagógico: si el `wrapper` no hace `return resultado`, desde fuera la llamada devuelve `None`. ✅
- Restaurado `return resultado` y confirmado que el valor `5` sale del decorador y queda disponible fuera. ✅
- Añadido `print("Resultado guardado: ", resultado)` para visualizar que el valor ya salió del `wrapper`. ✅
- Conectado el mecanismo con `@lru_cache`: también es un decorador que envuelve la función, decide si llama a la original o devuelve un valor cacheado, y siempre debe devolver un resultado hacia fuera. ✅

## Sensaciones de sesión (2026-05-15)
- La explicación que mejor funcionó fue: decorar una función es sustituirla por un `wrapper` que añade comportamiento alrededor de la función original.
- Sergi razonó correctamente que primero se ejecuta el `wrapper` porque el orden de los `print()` demuestra el flujo real.
- La duda sobre por qué usar decoradores fue sana: el ejemplo de saludo es artificial, pero sirve para entender el mecanismo antes de casos reales como logs, medición de tiempo o `@lru_cache`.
- La clase cerró con buena comprensión de decoradores básicos y sin saturación.

## Sensaciones de sesión (2026-05-22)
- Sesión corta y directa, orientada a consolidar un punto ya practicado.
- Sergi detectó correctamente que el ejercicio ya estaba hecho y verificó el comportamiento real quitando/restaurando el `return`.
- El concepto clave quedó claro: el valor puede volver de la función original al `wrapper`, pero solo sale al exterior si el `wrapper` lo devuelve.
- Quedó iniciada la conexión conceptual con `@lru_cache` como decorador real.

## Qué me quedó a medias
- Decoradores con funciones que devuelven valores: concepto consolidado con `return resultado`. Falta practicar la forma corta `return funcion_original(*args, **kwargs)` solo cuando no hay trabajo posterior en el `wrapper`.
- Conexión con `@lru_cache` iniciada: falta practicarla con un ejemplo concreto y traza de `hit`/`miss`.

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
2. Crear o usar la rama `learning/decoradores`.
3. Practicar la forma corta `return funcion_original(*args, **kwargs)` en un decorador donde no haga falta ejecutar nada después de la función original.
4. Reforzar que un `return` corta la ejecución del `wrapper`; por eso no sirve si queremos imprimir o hacer lógica después.
5. Conectar con `@lru_cache` mediante una traza concreta: primera llamada calcula y guarda; segunda llamada devuelve desde caché sin entrar en la función original.
