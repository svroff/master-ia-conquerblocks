# Estado Actual de Aprendizaje

## Dónde estoy
Tema 3 de Python Avanzado — Manejo de Archivos y Excepciones. Rama activa: `learning/excepciones`. Decoradores cerrado. Excepciones iniciado: `try/except FileNotFoundError` practicado, diferencia modo texto/binario explicada, `.read()` practicado en ambos modos. `open()` con `with` practicado en modos `w`/`a`/`r`; lectura iterando con `for` + `.strip()` practicada. `f.read()`, `f.readline()` con `while`, `readlines()` y lectura con `for` practicados y comparados. `TextAnalyzer` v0.1 implementado con `contar_basico(ruta)`: abre fichero con `with`, lee con `.read()`, cuenta caracteres con `len()`, palabras con `.split()`, líneas con `.splitlines()` y devuelve un `dict`. `try/except FileNotFoundError` ya está aplicado a un `with open(...)` real dentro de `contar_basico`; si el archivo no existe, devuelve un `dict` con ceros para mantener el mismo tipo de retorno. Próximo micro-paso: empezar `TextAnalyzer` v0.2, top 5 palabras con normalización mínima.

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

## Ejercicios completados (sesión 2026-05-27)
- Duración de la clase: 15 minutos.
- Practicada la forma corta `return funcion_original(*args, **kwargs)` dentro del `wrapper`. ✅
- Entendido que `return` corta la ejecución del `wrapper`, por lo que no sirve si necesitamos ejecutar lógica después de la función original. ✅
- Creado `decorador_corto` en `03_decoradores.py`, con una función `multiplicar(a, b)` decorada. ✅
- Confirmado que `resultado_corto = multiplicar(2, 3)` recibe correctamente el valor `6`. ✅

## Ejercicios completados (sesión 2026-05-27 — continuación)
- Duración de la clase: 15 minutos.
- Cerrado el bloque de Decoradores para el nivel actual. ✅
- Confirmado que no hace falta repetir caché manual ni `@lru_cache`, porque ya se trabajó durante recursividad y memoización. ✅
- Creada la carpeta `PYTHON/02_AVANZADO/02_ARCHIVOS_EXCEPCIONES` con el PDF del temario `Python-avanzado-Teoria-2-Manipulacion-de-Archivos-Diapositivas_9a4fbe5a.pdf`. ✅
- Revisado el PDF de teoría y detectado el temario: `open()`, rutas relativas/absolutas, lectura línea a línea, escritura, modos `r/w/a/x/b/t/r+/w+/a+`, NumPy y JSON. ✅
- Decidido empezar el bloque por manejo de excepciones antes de archivos, porque los errores de archivos son casos reales y frecuentes. ✅

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

## Sensaciones de sesión (2026-05-27)
- Clase rápida y clara. Sergi identificó correctamente que la forma corta no sirve cuando hay un `print()` posterior, porque ese código no se ejecutaría después del `return`.
- Buena comprensión de la diferencia entre guardar resultado para hacer trabajo posterior y devolver directamente la llamada original.
- Sergi detectó con criterio que no hacía falta repetir la clase de caché manual, ya trabajada durante recursividad. Buen ajuste de rumbo.

## Qué me quedó a medias
- Modos `x`, `r+`, `w+`, `a+` aún no practicados.
- Encoding utf-8 explícito en `open()` aún no practicado.
- `try/except` aplicado a la apertura con `with` aún no practicado.
- `try/except` aplicado a la lectura/escritura con `with` aún no practicado.

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

## Ejercicios completados (sesión 2026-05-29)
- Rama `learning/excepciones` creada a partir de `main`. ✅
- Empezado manejo de excepciones: `try/except FileNotFoundError`. ✅
- Entendido que `except` con tipo específico solo captura ese error; `except:` sin tipo captura cualquiera. ✅
- Explicada diferencia entre modo texto (`"r"`) y binario (`"rb"`). ✅
- Practicado `.read()` en modo texto y binario: texto devuelve string, binario devuelve bytes (con `b'...'`). ✅
- Aprendido que mezcla binario + encoding (`"rb"` + `encoding="utf-8"`) da error. ✅
- Creado `fichero-test.txt` para prácticas. ✅
- Cerrada la sesión a petición de Sergi tras pregunta sobre el temario del PDF. ✅

## Sensaciones de sesión (2026-05-29)
- Duración de la clase: ~45 minutos.
- Sergi pidió seguir el PDF como guía, no desviarse con binarios. Aceptado — el modo binario no es prioritario en el temario.
- Frustración temporal por planteamiento rápido del maestro sobre modo binario. Recuperado el rumbo con explicación clara.
- Clase cerrada por agotamiento/fin de sesión.

## Ejercicios completados (sesión 2026-06-02)
- Duración de la clase: 45 minutos.
- Reconstruida en Horus la clase impartida ayer desde Atlas (no pusheada): `open()` con `write()` y lectura iterando con `for`. ✅
- Practicado `with open(...) as f:` en sus tres modalidades: escritura (`"w"`), append (`"a"`) y lectura (`"r"`). ✅
- Diferencia `w` vs `a` demostrada en vivo: `w` borra el contenido previo, `a` añade al final. ✅
- Lectura iterando con `for linea in f:` y limpieza con `linea.strip()` para evitar el doble salto en pantalla. ✅
- Sergi aplicó `.strip()` por iniciativa propia antes de que apareciera el problema — buen razonamiento. ✅
- Reorganización de archivos: `aprendizaje con OpenCode/` renombrado a `Aprendiendo con IA/` en la raíz del repo; el log movido a `PYTHON/bitacora/`. ✅
- Limpiado `01-excepciones.py`: eliminado el bloque roto (`except:Ho` y copia.bin erróneo). ✅
- Discusión profunda sobre rutas: absoluta, relativa al cwd, y absoluta por barra inicial. Sergi corrigió al maestro dos veces con criterio (rechazó `pathlib` por avanzado y eligió configurar VSCode; diagnosticó que `"/fichero-test.txt"` falla por ser absoluta desde `/`). ✅
- Configurado setting de VSCode `python.terminal.executeInFileDir: true` para que el cwd sea la carpeta del script al ejecutar con ▶. ✅
- `02-archivos.py` creado y funcionando con rutas relativas. ✅

## Sensaciones de sesión (2026-06-02)
- Sesión muy buena. Sergi cerró con sensación positiva.
- Momento clave: Sergi dejó de seguir recetas y empezó a razonar sobre el comportamiento del entorno (cwd, `/` inicial, configuración de VSCode). Dos correcciones al maestro en una clase son señal de autonomía real.
- La decisión de no usar `pathlib` fue del aprendiz y fue correcta: la curva de dificultad manda.
- El error de la barra `/` inicial se convirtió en una lección memorable sobre cómo Linux interpreta rutas.
- Cierre limpio, con victoria clara (archivo 02 funcionando) y concepto denso bien asentado (rutas y cwd).

## Ejercicios completados (sesión 2026-06-04)
- Duración de la clase: 45 minutos.
- Empezado el bloque "métodos de lectura" del temario de archivos. ✅
- Explicación corregida tras precipitarme con tabla de referencia antes de mostrar un ejemplo real: Sergi señaló "no me has enseñado nada, maestro". Lección clara: concepto + ejemplo mínimo ejecutable, después la tabla de comparación. ✅
- Creado `03-read.py` con `with open(..., "r") as f: contenido = f.read()` y confirmación de `type(contenido) == str`. ✅
- Detectado y corregido import erróneo `from certifi import contents` (VSCode autocompletó mal): regla reforzada de no importar nada que no se sepa para qué sirve. ✅
- Practicado `len(contenido)` y `contenido.count("\n")` para contar caracteres y líneas. Sergi se atascó brevemente con la signatura de `count(sub[, start[, end]])` por no reconocer los corchetes como "argumento opcional": regla reforzada, los corchetes en una firma se pueden ignorar. ✅
- Explicado el cursor interno del archivo: `readline()` lee hasta el próximo `\n` y mueve el puntero. Aclarado que no es un `for` por dentro, es una operación directa. ✅
- Explicada la convención de Python "valor vacío del mismo tipo" al agotarse: `readline()` agotado devuelve `""`, no `None`. ✅
- Visto en vivo que una tercera llamada a `readline()` devuelve `""` cuando no quedan más líneas. ✅
- Ejercicio de `readline()` con bucle `while` y líneas numeradas queda pendiente para la próxima sesión. ⏳
- Decidido arrancar proyecto integrador "TextAnalyzer" como práctica sólida de portfolio. Esqueleto y README dejados preparados en `PYTHON/02_AVANZADO/02_ARCHIVOS_EXCEPCIONES/PROYECTO_TEXT_ANALYZER/`. ✅

## Sensaciones de sesión (2026-06-04)
- Sesión con buen aprendizaje tras un tropiezo inicial: lancé una tabla de referencia sin haber mostrado antes un ejemplo real, y Sergi lo señaló correctamente. Aceptado y corregido en el momento.
- El momento del import espurio fue útil como lección de disciplina: "no importes nada que no sepas para qué sirve". El alumno razonó que VSCode autocompletó y entendió por qué sobra.
- La confusión con la signatura `str.count(sub[, start[, end]])` fue genuina: no había visto corchetes en firmas todavía. Explicación corta y regla memorable.
- Sergi preguntó "¿readline() hace un for interno?" y "¿por qué devuelve '' y no None?" — dos preguntas de nivel intermedio que muestran que está pasando de "teclear lo que dice el maestro" a "entender cómo funciona por dentro".
- Cierre limpio, con un ejercicio (readline + while + numerar) y un proyecto integrador (TextAnalyzer) listos para la próxima sesión.
- Sergi pidió expresamente subir el ritmo hacia proyectos sólidos publicables en GitHub. Bien: la unidad de archivos es buen momento para empezar a producir artefactos con README y estructura de proyecto.

## Ejercicios completados (sesión 2026-06-05)
- Duración de la clase: 43 minutos.
- Cerrado el micro-paso abierto: `readline()` con bucle `while` + contador + líneas numeradas en `04-readline-while.py`. ✅
- Consolidado el patrón `while True: ... if linea == "": break` (no `if not linea:`) para no cortar líneas vacías legítimas. ✅
- Repasado el por qué de `.strip()`: `readline()` no "aplica" un `\n`, lo trae pegado del archivo; `print()` añade otro → doble salto. `.strip()` quita el del archivo. ✅
- Ampliado el catálogo: `readlines()` devuelve `list`, cada elemento con su `\n`; `len(lineas)` cuenta líneas sin `count("\n")`. ✅
- Tabla mental de las 4 formas: `read()`, `readline()` en `while`, `readlines()`, `for linea in f:`. Trade-off: `readlines()` carga todo en memoria; `for linea in f:` es iterador eficiente. ✅
- Limpiado `03-read.py`: eliminado `from re import split` que quedó colgado de pruebas. ✅
- Añadida la línea "Hola mundo" a `fichero-test.txt` (queda con 3 líneas, sin `\n` final). ✅
- Decidido aplazar el arranque de `TextAnalyzer` v0.1 a la próxima sesión por tiempo. ⏳

## Sensaciones de sesión (2026-06-05)
- Sesión eficiente, sin tropiezos de ritmo.
- El momento más útil fue la aclaración del `.strip()`: Sergi llegó con la intuición correcta ("`readline()` aplica un salto y el archivo también tiene, se duplica") y solo necesitó el matiz de que `readline()` no "aplica", devuelve tal cual viene del archivo. La idea del "valor vacío del mismo tipo" (`""` al agotar) reforzó la conexión.
- Sergi añadió `print(lineas)` por iniciativa propia para ver la lista completa con los `\n` escapados — buena lectura del output.
- Detectado en el cierre: el `print(f"{n}: {linea.strip()}")` quedó colocado **antes** del `if linea == "": break`, lo que produce un `4: ` fantasma al agotarse el archivo. Es un bug menor del ejercicio (no del concepto) y queda como tarea de limpieza para la próxima sesión.
- Cerrado con sensacion de avance claro y sin saturación.

## Siguiente paso
1. Arrancar `TextAnalyzer` v0.2: top 5 palabras con normalización mínima.
2. Practicar conteo con diccionario: crear clave si no existe, sumar si ya existe.
3. Ordenar palabras por frecuencia y devolver solo las 5 primeras.
4. Más adelante en el `TextAnalyzer`: v0.3 (`@medir_tiempo`), v0.4 (función integradora `analizar_fichero`), v0.5 (varios ficheros), v0.6 (exportar informe).
5. Más adelante: modos `x` y `+`, `pathlib`, JSON, NumPy y POO.

## Ejercicios completados (sesión 2026-06-09)
- Duración de la clase: 55 minutos.
- Implementado `TextAnalyzer` v0.1 en `PROYECTO_TEXT_ANALYZER/text_analyzer.py`. ✅
- `contar_basico(ruta)` abre el fichero con `with open(ruta, "r", encoding="utf-8")`, lee todo con `.read()` y calcula tres métricas. ✅
- Practicado `len(contenido)` para caracteres, `len(contenido.split())` para palabras y `len(contenido.splitlines())` para líneas. ✅
- Devuelto el resultado como diccionario con claves `lineas`, `palabras` y `caracteres`. ✅
- Verificado con `samples/ejemplo.txt`: `{'lineas': 7, 'palabras': 55, 'caracteres': 359}`. ✅
- Sergi preguntó si la salida debía ser diccionario sí o sí y entendió que el objetivo era devolver varios datos etiquetados. ✅
- Sergi probó la forma directa `return { ... }` y entendió que `{clave: valor}` crea un diccionario aunque no exista una variable llamada `dic`. ✅
- Corregido bug menor de `04-readline-while.py`: el `print()` queda después del `if linea == "": break`, evitando la línea fantasma al agotarse el archivo. ✅

## Sensaciones de sesión (2026-06-09)
- Sesión de proyecto real, clara y productiva.
- Sergi implementó la función completa, pidió referencias exactas de salida y verificó comportamiento con criterio.
- La pregunta sobre `return { ... }` fue importante: conectó sintaxis literal de diccionarios con flujo real de retorno y posterior `.items()`.
- Cierre con victoria clara: `TextAnalyzer` v0.1 ya funciona.

## Ejercicios completados (sesión 2026-06-12)
- Duración de la clase: 60 minutos.
- Aplicado `try/except FileNotFoundError` a un `with open(...)` real dentro de `contar_basico(ruta)`. ✅
- Entendido que el `open()` es la zona peligrosa: si la ruta no existe, Python salta al `except`. ✅
- Detectado y corregido el problema de poner el `return` del diccionario dentro del `except`: si el archivo existe, la función terminaba devolviendo `None` implícito. ✅
- Visto el error `UnboundLocalError` cuando se intenta devolver variables que no se crearon porque el `open()` falló. ✅
- Decidido diseño final: en caso de `FileNotFoundError`, `contar_basico()` devuelve un diccionario con ceros para mantener siempre el mismo tipo de retorno (`dict`). ✅
- Verificado manualmente que una ruta inexistente muestra mensaje controlado y devuelve `{"lineas": 0, "palabras": 0, "caracteres": 0}`. ✅
- Explicado que `encoding="utf-8"` no siempre es obligatorio en Linux, pero es buena práctica para leer tildes, `ñ` y evitar sorpresas entre sistemas. ✅
- Limpieza del archivo `text_analyzer.py`: cálculos fuera del `with`, comentarios más claros y bloque comentado con enunciado de `TextAnalyzer` v0.2. ✅

## Sensaciones de sesión (2026-06-12)
- La clase tuvo que reiniciarse porque el maestro empujó una solución (`return None` + proteger el `for`) sin cerrar antes el diseño de retorno. Sergi lo detectó correctamente y pidió volver a empezar.
- Lección pedagógica: antes de tocar el código, decidir qué contrato debe cumplir la función. En este caso, si normalmente devuelve `dict`, en error también debe devolver `dict`.
- Sergi volvió a marcar una regla importante: no introducir `if __name__ == "__main__"` si aún no se ha enseñado. Para esta etapa, mantener el script simple es mejor.
- Cierre con victoria clara: `TextAnalyzer` v0.1 queda más robusto ante archivos inexistentes y listo para empezar v0.2.
