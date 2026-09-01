# Chuleta De Patrones Python

Chuleta corta para repasar patrones vistos pero no automatizados.

## Diccionario A Parejas

```python
conteo = {
    "python": 7,
    "es": 3,
    "lenguaje": 2,
}

parejas = conteo.items()
```

Idea:

```python
("python", 7)
   [0]     [1]
 palabra frecuencia
```

## Ordenar Por Valor

```python
ordenado = sorted(
    conteo.items(),
    key=lambda pareja: pareja[1],
    reverse=True,
)
```

Lectura humana:

```text
Ordena las parejas mirando la posicion 1, la frecuencia, de mayor a menor.
```

## Sacar Top N

```python
top_5 = ordenado[:5]
```

Idea:

```text
[:5] significa: dame los primeros 5 elementos.
```

## Mini Ejercicio De Calentamiento

```python
notas = {
    "ana": 8,
    "luis": 5,
    "marta": 10,
}
```

Objetivo:

```python
[("marta", 10), ("ana", 8)]
```
