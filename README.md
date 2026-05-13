# Máster en Inteligencia Artificial - Conquer Blocks

![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Status](https://img.shields.io/badge/Status-En%20Progreso-green)
![Focus](https://img.shields.io/badge/Focus-AI%20%26%20Data%20Science-orange)

Repositorio de prácticas y proyectos del **Máster de Inteligencia Artificial** de Conquer Blocks. Documenta el progreso desde fundamentos de programación hasta implementación de modelos de IA.

---

## Estructura del Proyecto

```
master-ia-conquerblocks/
├── .codex/
│   └── skills/
├── PYTHON/
│   ├── 01_BASICO/
│   ├── 02_AVANZADO/
│   └── aprendizaje con Codex/
├── scripts/
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
| Manejo de Archivos y Excepciones | Próximo | `try/except`, lectura/escritura de ficheros |
| POO | Próximo | Clases, herencia, polimorfismo, dunder methods |
| NumPy & Pandas | Próximo | Análisis y manipulación de datos masivos |

---

### [aprendizaje con Codex](./PYTHON/aprendizaje%20con%20Codex/)

Sistema de seguimiento personalizado del progreso, con perfil del aprendiz y estado actualizado de cada sesión de estudio.

---

## Codex Tutor

Este repo incluye la skill personalizada [`sergi-python-tutor`](./.codex/skills/sergi-python-tutor/SKILL.md) para mantener la misma dinámica de mentoría Python en Mac, Ubuntu y Fedora.

Después de clonar o actualizar el repo en cualquier equipo:

```bash
git pull
./scripts/install-codex-skills.sh
```

Reinicia Codex para que detecte la skill instalada en `~/.codex/skills`.

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
