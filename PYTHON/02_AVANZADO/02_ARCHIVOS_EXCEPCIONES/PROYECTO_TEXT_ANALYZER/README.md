# TextAnalyzer

Pequeño analizador de ficheros de texto en Python. Cuenta líneas, palabras y
caracteres, y muestra las palabras más frecuentes. Es un proyecto
**integrador** pensado para practicar de forma sólida todo lo aprendido en
Python Básico + Python Avanzado antes de enfrentarse a librerías externas
(NumPy, Pandas, etc.).

## Qué conocimientos pone en juego

| Bloque | Conocimientos |
|---|---|
| Básico | `str`, `list`, `dict`, `set`, bucles, condicionales, `sorted`, `len` |
| Funciones | `def`, parámetros, `*args`, retorno de valores |
| Lambdas | `sorted(key=lambda ...)`, `map`, `filter` |
| Avanzado | recursividad, memoización, decoradores |
| Archivos | `open` con `with`, modos `r`/`w`/`a`, `read`, `readline`, `readlines`, `for` sobre fichero |
| Excepciones | `try/except FileNotFoundError`, mensajes claros al usuario |

## Estructura

```
PROYECTO_TEXT_ANALYZER/
├── README.md              ← este fichero
├── text_analyzer.py       ← esqueleto a completar por capas
└── samples/
    └── ejemplo.txt        ← fichero de prueba con texto repetido
```

## Plan por versiones (una capa cada vez)

| Versión | Qué añade | Concepto nuevo |
|---|---|---|
| v0.1 | `contar_basico(ruta)`: nº de líneas, palabras y caracteres | `read()`, `split()`, `len()` |
| v0.2 | `top_palabras(ruta, n=5)`: las n palabras más frecuentes | `dict` de conteo, `sorted` con `lambda` |
| v0.3 | Decorador `@medir_tiempo` que envuelve la función principal | decoradores reales sobre funciones propias |
| v0.4 | `try/except FileNotFoundError` con mensaje claro al usuario | excepciones aplicadas a `with open` |
| v0.5 | Aceptar varios ficheros y agregar resultados | `*args`, bucles sobre rutas |
| v0.6 | Exportar el informe a un fichero de salida | escritura con `with open(..., "w")` |

Cuando todas las versiones estén terminadas, este proyecto será un buen
candidato a repositorio público de portfolio junior: tiene README, código
modular, maneja errores reales y usa Python puro (sin dependencias).

## Cómo ejecutar

```bash
cd PYTHON/02_AVANZADO/02_ARCHIVOS_EXCEPCIONES/PROYECTO_TEXT_ANALYZER
python3 text_analyzer.py samples/ejemplo.txt
```

(El script principal se completará capa a capa; al principio solo tendrá
el esqueleto con `pass` y docstrings.)

## Reglas del proyecto

- **Una versión por sesión** (o menos). Mejor terminar v0.1 bien que tener
  seis versiones a medias.
- **No borrar prints pedagógicos** mientras el código esté en fase de
  aprendizaje.
- **El README es parte del proyecto**: cuando termines una versión,
  actualízalo marcando la casilla correspondiente.
