La propia palabra «variable» sugiere que su valor puede cambiar. Esa es una de las razones principales de que las variables existan.

Aquí tienes un ejemplo simple:

```python
# greeting se traduce como saludo
greeting = "Father!"
print(greeting)  # => Father!

greeting = "Mother!"
print(greeting)  # => Mother!
```

Aquí primero escribimos en la variable una cadena (_Father!_), después otra (_Mother!_). El nombre de la variable no cambió, pero el valor de dentro pasó a ser otro.

```text
Antes:   greeting ──→ "Father!"
                       ╳
Después: greeting ──→ "Mother!"
```

## ¿Para qué cambiar el valor?

En los programas reales las variables cambian constantemente. Estas son algunas razones:

- El programa reacciona a las acciones del usuario. Por ejemplo, mientras introduces datos en los formularios de un sitio, es muy probable que en ese momento estén cambiando constantemente las variables que contienen esos datos
- Resultados intermedios. A menudo los datos pasan por una serie de transformaciones, y en cada etapa la variable se actualiza con un valor nuevo. Un mecanismo parecido existe incluso en las calculadoras, cuando los valores intermedios se guardan con las teclas `m+` o `m-`.
- Almacenamiento del estado. Si escribes un juego, la posición del personaje, su salud, la puntuación y el nivel actual son variables que cambian constantemente.

## Las variables se crean a medida que se usan

En Python una variable no hay que «declararla de antemano»: aparece en el momento en que escribes por primera vez un valor en ella:

```python
name = "Arya"  # la variable se crea aquí
```

Si después escribes de nuevo name = ..., eso sobrescribirá el valor anterior. Así funciona la mayoría de los lenguajes de programación modernos.

## Por qué esto es importante

Las variables son una forma flexible de guardar datos que pueden cambiar durante la ejecución del programa. Gracias a eso se pueden escribir programas que se comportan de distinta manera según las condiciones, las acciones del usuario o los resultados de los cálculos.

Pero la flexibilidad tiene su otra cara. A veces cuesta entender de inmediato qué está escrito exactamente en una variable en un momento u otro. El desarrollador tiene que seguir dónde y cómo cambió, sobre todo si el código es largo.

Eso es precisamente lo que se hace durante la depuración: intentar entender por qué el programa funciona de otra manera de la prevista. Se comprueban los valores de las variables, se sigue el orden de ejecución del código, se busca dónde algo salió mal.
