# TextAnalyzer

Pequeño analizador de ficheros de texto en Python que cuenta líneas, palabras y caracteres, y (en versiones futuras) muestra las palabras más frecuentes.

Es tu **primer proyecto integrador** del máster. Está pensado para que juntes en algo real todo lo que has aprendido de Python Básico + Python Avanzado (sin librerías externas todavía), capa a capa, una versión por sesión.

---

## ¿Qué tengo que hacer? (v0.1)

El objetivo de esta versión es implementar una sola función: `contar_basico(ruta)`. Una función, una responsabilidad.

### Enunciado

> Escribe una función que reciba la ruta de un fichero de texto y devuelva un diccionario con tres números: cuántas líneas tiene, cuántas palabras y cuántos caracteres en total.

### Ejemplo de uso

```python
>>> from text_analyzer import contar_basico
>>> contar_basico("samples/ejemplo.txt")
{'lineas': 7, 'palabras': 55, 'caracteres': 360}
```

Los números exactos dependerán del contenido del fichero, pero la forma del diccionario es siempre la misma: tres claves, tres enteros.

### Conocimientos que pone en juego

Esto ya lo sabes, solo hay que juntarlo:

- `with open(ruta, "r", encoding="utf-8") as f:` — abrir y cerrar ficheros de forma segura.
- `contenido = f.read()` — leer todo el fichero en un solo string.
- `contenido.split()` — partir por palabras (cualquier whitespace: espacios, tabs, saltos).
- `contenido.splitlines()` — partir por líneas reales.
- `len(...)` — contar.
- Devolver un `dict` con tres claves.

**No hay nada nuevo.** Solo encajar piezas que ya conoces en una función con retorno de diccionario.

---

## Plan por capas (tu estilo: una idea cada vez)

Sigue estos pasos en orden. Cada capa es un paso pequeño, no te saltes ninguna. Puedes escribir una capa, ejecutar la función (aunque no haga nada útil todavía) y comprobar que no falla, antes de pasar a la siguiente.

### Capa 1 — Apertura y lectura (lo más simple)

Abre el fichero con `with`, léelo entero, guárdalo en una variable `contenido`. Si ejecutas la función ahora mismo, no debería fallar (aunque devuelva `None` porque aún no hay `return`).

```python
def contar_basico(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()
    # Próximas capas vendrán aquí.
```

**¿Por qué `encoding="utf-8"`?** Para que las tildes y la `ñ` se lean bien. En Python, si no lo pones, a veces se interpreta en otra codificación del sistema y salen caracteres raros tipo `Ã±` en lugar de `ñ`. Acostúmbrate a ponerlo siempre.

### Capa 2 — Contar caracteres

La métrica más fácil. `len(contenido)` te da el total de caracteres del string, contando espacios y saltos de línea. Un número entero.

```python
caracteres = len(contenido)
```

### Capa 3 — Contar palabras

`contenido.split()` parte el string por cualquier whitespace (espacios, tabs, saltos) y te devuelve una lista de palabras. `len(...)` te da el conteo.

```python
palabras = len(contenido.split())
```

**Truco:** `split()` sin argumentos es más útil que `split(" ")`. El segundo solo parte por un único espacio, no por tabs ni saltos, así que puede dar conteos incorrectos.

### Capa 4 — Contar líneas

Dos opciones equivalentes:

- `contenido.count("\n")` — cuenta los saltos de línea. Simple, pero falla si el fichero no termina en `\n`.
- `len(contenido.splitlines())` — parte por líneas reales (maneja también `\r\n` de Windows). Más robusto.

Te recomiendo `splitlines()` porque es más limpio y no te dará sorpresas.

```python
lineas = len(contenido.splitlines())
```

### Capa 5 — Empaquetar y devolver

Junta los tres conteos en un diccionario y devuélvelo:

```python
return {
    "lineas": lineas,
    "palabras": palabras,
    "caracteres": caracteres,
}
```

Sustituye los valores por tus variables de las capas 2, 3 y 4.

---

## ¿Cómo sé que está bien?

Tienes un sample preparado en `samples/ejemplo.txt`: 7 líneas sobre Python. Para probar tu función:

```bash
cd PYTHON/02_AVANZADO/02_ARCHIVOS_EXCEPCIONES/PROYECTO_TEXT_ANALYZER
python3 -c "from text_analyzer import contar_basico; print(contar_basico('samples/ejemplo.txt'))"
```

Lo que esperas ver es un `dict` con tres números. Los números exactos no importan siempre que sean razonables para un fichero de 7 líneas:

- `caracteres` debería ser mayor que 100 (es un texto con 7 frases).
- `palabras` debería estar alrededor de 55.
- `lineas` debería ser exactamente 7.

Si los tres números son razonables, **v0.1 está listo** ✅.

---

## Errores típicos y cómo los detectas

| Error | Síntoma | Cómo lo ves |
|---|---|---|
| Olvidaste `encoding="utf-8"` y el fichero tiene tildes/ñ | Caracteres raros tipo `Ã±` en el print | Mira el `print(contenido)` durante la Capa 1. Si ves `Ã±` en lugar de `ñ`, es esto. |
| Usaste `split(" ")` en vez de `split()` | El conteo de palabras es mayor del esperado | `split(" ")` solo parte por un único espacio. Si el fichero tiene dobles espacios o tabs, los cuenta mal. Usa `split()` a secas. |
| Usaste `count("\n")` y el fichero no termina en salto | El conteo de líneas es 6 en vez de 7 | Mira las últimas líneas de `samples/ejemplo.txt` con `cat -A` o con un editor que muestre saltos. Si no hay `\n` al final, usa `splitlines()`. |
| `return` antes de calcular las tres variables | `NameError` o `UnboundLocalError` | El `return` va al final, con los tres campos ya calculados. |

---

## Y después de v0.1, ¿qué?

El proyecto sigue con cinco versiones más, una por sesión. **No intentes hacerlas todas a la vez.** Mejor cerrar v0.1 limpia que tener seis a medias.

| Versión | Qué añade | Para qué |
|---|---|---|
| ✅ v0.1 | `contar_basico(ruta)`: nº de líneas, palabras y caracteres, con `FileNotFoundError` controlado | Juntar `read()`, `split()`, `len()`, diccionarios y excepciones |
| ⏳ v0.2 | `top_palabras(ruta, n=5)`: las n palabras más frecuentes | Practicar `dict` de conteo y `sorted(key=lambda...)` |
| ⏳ v0.3 | Decorador `@medir_tiempo` que envuelve la función principal | Llevar los decoradores a un caso real (no solo `@lru_cache`) |
| ⏳ v0.4 | `analizar_fichero(ruta)` con `try/except FileNotFoundError` | Combinar lo que ya sabes en una función de entrada robusta |
| ⏳ v0.5 | `analizar_varios(*rutas)`: aceptar varios ficheros | Practicar `*args` |
| ⏳ v0.6 | `exportar_informe(informe, ruta_salida)`: escribir el informe | Volver a escribir ficheros con `with open(..., "w")` |

---

## Reglas del proyecto

- **Una versión por sesión (o menos).** Si te quedan 5 minutos y has cerrado v0.1, deja v0.2 para la próxima.
- **No borres prints pedagógicos** mientras el código esté en fase de aprendizaje.
- **Cuando termines una versión, marca la casilla** de la tabla de arriba.
- **El README es parte del proyecto:** mantenlo al día con tu progreso.

---

## Cómo ejecutar la prueba final

Cuando todas las versiones estén terminadas (muchas sesiones después):

```bash
cd PYTHON/02_AVANZADO/02_ARCHIVOS_EXCEPCIONES/PROYECTO_TEXT_ANALYZER
python3 text_analyzer.py samples/ejemplo.txt
```

Por ahora, en v0.1, el script mantiene una prueba directa al final del archivo. Más adelante, cuando toque módulos/imports, se reorganizará la entrada principal del programa.
