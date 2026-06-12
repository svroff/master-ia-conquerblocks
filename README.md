# Máster en Inteligencia Artificial - Conquer Blocks

![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Status](https://img.shields.io/badge/Status-En%20Progreso-green)
![Current](https://img.shields.io/badge/Actual-Python%20Avanzado-orange)
![Branch](https://img.shields.io/badge/Rama-learning%2Fexcepciones-purple)

Repositorio de prácticas, apuntes y proyectos del **Máster en Inteligencia Artificial de Conquer Blocks**.

El objetivo no es solo guardar ejercicios: este repo documenta el progreso real desde fundamentos de programación hasta proyectos aplicables a IA, con trazabilidad de sesiones, ramas de aprendizaje y proyectos incrementales.

---

## Estado Actual

**Módulo activo:** Python Avanzado  
**Tema actual:** Manejo de Archivos y Excepciones  
**Rama de trabajo:** `learning/excepciones`  
**Proyecto integrador activo:** [`TextAnalyzer`](./PYTHON/02_AVANZADO/02_ARCHIVOS_EXCEPCIONES/PROYECTO_TEXT_ANALYZER/)

Último avance consolidado:

- Decoradores cerrado para el nivel actual.
- Practicados `try/except FileNotFoundError`, `open()`, `with`, modos `w`, `a`, `r` y lectura de ficheros.
- Comparadas cuatro formas de lectura: `read()`, `readline()` con `while`, `readlines()` y `for linea in f`.
- Implementado `TextAnalyzer v0.1`: conteo de líneas, palabras y caracteres desde un fichero de texto, con manejo de `FileNotFoundError`.

Próximos pasos:

- Empezar `TextAnalyzer v0.2`: top 5 palabras con normalización mínima.
- Más adelante: JSON, modos avanzados de fichero, NumPy, Pandas y POO.

---

## Estructura Del Repo

```text
master-ia-conquerblocks/
├── .opencode/
│   └── agent/
│       └── maestro.md
├── Aprendiendo con IA/
│   ├── perfil-aprendiz.md
│   ├── estado-actual.md
│   └── perfil-maestro.md
├── PYTHON/
│   ├── 01_BASICO/
│   ├── 02_AVANZADO/
│   │   ├── 01_FUNCIONES/
│   │   └── 02_ARCHIVOS_EXCEPCIONES/
│   │       ├── EJERCICIOS/
│   │       ├── EXTRAS-CLASE/
│   │       └── PROYECTO_TEXT_ANALYZER/
│   └── bitacora/
│       └── sesiones.log
├── opencode.json
└── README.md
```

---

## Python Básico

Carpeta: [`PYTHON/01_BASICO`](./PYTHON/01_BASICO/)

Estado: **completado**

| Bloque | Contenido |
|--------|-----------|
| Primeros ejercicios | Variables, tipos de datos, operadores |
| Condicionales | `if`, `elif`, `else`, lógica de decisión |
| Listas y bucles | `for`, `while`, índices, acumuladores |
| Sets y tuplas | Estructuras inmutables y operaciones de conjunto |
| Diccionarios | Clave-valor, anidamiento, agrupaciones |
| Arrays y librerías | Introducción a NumPy y operaciones vectorizadas |

---

## Python Avanzado

Carpeta: [`PYTHON/02_AVANZADO`](./PYTHON/02_AVANZADO/)

Estado: **en curso**

| Módulo | Estado | Contenido |
|--------|--------|-----------|
| Funciones | Completado | `def`, parámetros, `*args`, `**kwargs`, scope, retorno múltiple |
| Lambdas | Completado | Funciones anónimas, `map()`, `filter()`, `sorted(key=...)` |
| Recursividad | Completado | Caso base, caso recursivo, pila de llamadas |
| Memoización | Completado | Cache manual con `dict`, claves simples y tuplas, `@lru_cache` |
| Decoradores | Completado | `@decorador`, `wrapper`, retorno de funciones decoradas |
| Archivos y Excepciones | En curso | `try/except`, `open()`, `with`, lectura/escritura, proyecto integrador |
| POO | Próximo | Clases, objetos, herencia, polimorfismo, dunder methods |
| NumPy y Pandas | Próximo | Análisis y manipulación de datos |

---

## Proyecto Actual: TextAnalyzer

Carpeta: [`PROYECTO_TEXT_ANALYZER`](./PYTHON/02_AVANZADO/02_ARCHIVOS_EXCEPCIONES/PROYECTO_TEXT_ANALYZER/)

Primer proyecto integrador del bloque de Python Avanzado. Une funciones, lectura de ficheros, strings, listas, diccionarios y validación por capas.

Versión actual: **v0.1 completada**

Función implementada:

```python
contar_basico(ruta)
```

Devuelve un diccionario con tres métricas:

```python
{
    "lineas": 7,
    "palabras": 55,
    "caracteres": 360,
}
```

Roadmap del proyecto:

| Versión | Estado | Objetivo |
|---------|--------|----------|
| v0.1 | Completada | Contar líneas, palabras y caracteres |
| v0.2 | Próxima | Top 5 palabras más frecuentes |
| v0.3 | Próxima | Decorador `@medir_tiempo` |
| v0.4 | Próxima | Excepciones en lectura de ficheros |
| v0.5 | Próxima | Analizar varios ficheros |
| v0.6 | Próxima | Exportar informe |

---

## Memoria De Aprendizaje

La carpeta [`Aprendiendo con IA`](./Aprendiendo%20con%20IA/) guarda el sistema de continuidad de estudio:

- `perfil-aprendiz.md`: cómo aprende Sergi, preferencias y reglas de tutoría.
- `estado-actual.md`: punto exacto del temario y resumen de sesiones.
- `perfil-maestro.md`: reglas pedagógicas del agente tutor.

La bitácora resumida vive en [`PYTHON/bitacora/sesiones.log`](./PYTHON/bitacora/sesiones.log).

---

## OpenCode Maestro

Este repo incluye el agente [`maestro`](./.opencode/agent/maestro.md), usado para retomar clases con contexto real del aprendizaje.

En cualquier equipo:

```bash
git pull
opencode
```

Dentro de OpenCode:

```text
Continuamos clase
```

El agente lee la memoria de aprendizaje, revisa Git y retoma desde el siguiente micro-paso.

---

## Stack Objetivo

| Área | Tecnologías |
|------|-------------|
| Lenguaje base | Python 3.11+ |
| Entorno | VS Code, terminal Linux, Git, GitHub |
| Datos | NumPy, Pandas, Matplotlib |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow, Keras, PyTorch |
| IA generativa | OpenAI API, Hugging Face, LLMs locales |
| Despliegue | FastAPI, Docker |

---

## Proyecto Capstone Previsto

RAG local con LLM + Elasticsearch.

Stack previsto:

- Python
- LlamaIndex o LangChain
- Ollama
- Elasticsearch
- FastAPI
- Docker

---

_Desarrollado por **Sergi Vicente** en el camino hacia la Ingeniería de IA._
