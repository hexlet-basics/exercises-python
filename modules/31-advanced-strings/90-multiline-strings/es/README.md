
Imagina que necesitamos definir una cadena que consta de varias líneas, es decir, que contiene saltos de línea `\n`. Por ejemplo, se vería así:

```python
text = 'Ejemplo de texto,\ncompuesto por\nvarias líneas'
```

Al imprimir la cadena, se mostrará de la siguiente manera:

```text
Ejemplo de texto,
compuesto por
varias líneas
```

Para este tipo de situaciones, en Python existe otra forma de crear cadenas llamada **cadenas de varias líneas**. Para definir una cadena de varias líneas, debemos encerrarla entre triples comillas `"""` o `'''`. Dentro de una cadena de varias líneas, podemos agregar texto sin necesidad de utilizar saltos de línea `\n`:

```python
text = '''Ejemplo de texto,
compuesto por
varias líneas
'''
```

```text
Ejemplo de texto,
compuesto por
varias líneas

```

Observa que al final del texto hay una línea vacía. Esto se debe a que colocamos las comillas de cierre `'''` en una nueva línea. Si no colocamos las comillas de cierre en una nueva línea, la cadena no tendrá una línea vacía:

```python
text = '''Ejemplo de texto,
compuesto por
varias líneas'''
```

```text
Ejemplo de texto,
compuesto por
varias líneas
```

Gracias a las triples comillas, no es necesario escapar las comillas dentro de la cadena:

```text
Aquí no es necesario escapar las comillas 'simples' o "dobles"
```

Además, las cadenas de varias líneas pueden ser utilizadas como f-strings para interpolación:

```python
a = 'A'
b = 'B'

# Se agregó una f al inicio
text = f'''{a} y {b}
se sentaron en un tubo
'''
```

```text
A y B
se sentaron en un tubo

```

Para la computadora no importa qué método de concatenación y saltos de línea utilices. De todas formas, realizará los cálculos y mostrará el resultado correcto. La interpolación y las cadenas de varias líneas se utilizan para facilitar la lectura del código por parte de los desarrolladores.
