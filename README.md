# Máster en Inteligencia Artificial - Conquer Blocks

![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Status](https://img.shields.io/badge/Status-En%20Progreso-green)
![Focus](https://img.shields.io/badge/Focus-AI%20%26%20Data%20Science-orange)

Repositorio de prácticas y proyectos del **Máster de Inteligencia Artificial** de Conquer Blocks. Documenta el progreso desde fundamentos de programación hasta implementación de modelos de IA.

---

## Estructura del Proyecto

```
master-ia-conquerblocks/
├── .opencode/
│   └── agent/
├── PYTHON/
│   ├── 01_BASICO/
│   ├── 02_AVANZADO/
│   └── aprendizaje con OpenCode/
├── opencode.json
└── README.md
```

---

## PYTHON

### [01_BASICO](./PYTHON/01_BASICO/) ✅

Fundamentos de programación y estructuras de datos.

| Módulo | Contenido |
|--------|-----------|
| Primeros Ejercicios | Variables, tipos de datos, operadores |
| Condicionales | `if/elif/else`, lógica de decisión |
| Listas y Bucles | `for`, `while`, manipulación de listas (3 bloques progresivos) |
| Sets y Tuplas | Estructuras inmutables, operaciones de conjuntos |
| Diccionarios | Clave-valor, anidamiento, agrupaciones (3 bloques progresivos) |
| Arrays y Librerías | Introducción a NumPy, operaciones vectorizadas (3 bloques progresivos) |

---

### [02_AVANZADO](./PYTHON/02_AVANZADO/) — en curso

Ingeniería de software y algoritmos.

| Módulo | Estado | Contenido |
|--------|--------|-----------|
| Funciones | ✅ | `def`, `*args`, `**kwargs`, scope, retorno múltiple |
| Lambdas | ✅ | Funciones anónimas, `map()`, `filter()`, `sorted(key=...)` |
| Recursividad | ✅ | Casos base/recursivos, pila de llamadas |
| Manejo de Archivos y Excepciones | En curso | `try/except`, lectura/escritura de ficheros, JSON |
| POO | Próximo | Clases, herencia, polimorfismo, dunder methods |
| NumPy & Pandas | Próximo | Análisis y manipulación de datos masivos |

---

### [aprendizaje con OpenCode](./PYTHON/aprendizaje%20con%20OpenCode/)

Sistema de seguimiento personalizado del progreso, con perfil del aprendiz y estado actualizado de cada sesión de estudio.

---

## OpenCode Maestro

Este repo incluye el agente de OpenCode [`maestro`](./.opencode/agent/maestro.md) para mantener la misma dinámica de mentoría Python en Ubuntu Horus, Mac M3 Pro y workstation Ubuntu Orion.

En cualquier equipo:

```bash
git pull
opencode
```

Después, dentro de OpenCode, basta con decir:

```text
Continuamos clase
```

El agente leerá la memoria de aprendizaje del repo, revisará Git y retomará la clase desde el último punto.

---

## Tecnologías

- **Lenguaje:** Python 3.11+
- **IDE:** VS Code
- **Control de versiones:** Git & GitHub
- **Librerías actuales:** NumPy
- **Librerías próximas:** Pandas, Matplotlib, Scikit-learn, TensorFlow, Keras, PyTorch

---

## Proyecto Capstone

RAG local con LLM + Elasticsearch — stack: Python, LlamaIndex o LangChain, Ollama, FastAPI.

---

_Desarrollado por **Sergi Vicente** en el camino hacia la Ingeniería de IA._
