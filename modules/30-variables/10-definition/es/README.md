Imagina que hay que imprimir la frase Father! dos veces:

```python
print("Father!")
print("Father!")
```

Ese modo sirve perfectamente si la frase aparece solo un par de veces. Pero ¿qué pasa si se va a usar a menudo, en distintas partes del programa? Entonces habrá que copiar la misma expresión una y otra vez.

¿Y qué ocurrirá si hay que cambiar la frase, por ejemplo reemplazar _Father!_ por _Mother!_? Habrá que buscar y corregir todas las apariciones a mano. Eso es incómodo y lleva a errores.

## Variables

Para no duplicar la misma cadena, se la puede guardar en una variable e imprimir su contenido:

```python
greeting = "Father!"

print(greeting)
print(greeting)
```

El resultado:

```text
Father!
Father!
```

Una **variable** es un nombre detrás del cual se guarda un valor. En nuestro ejemplo creamos una variable con el nombre `greeting` y escribimos en ella la cadena `'Father!'`.

```text
greeting = 'Father!'

Variable         Valor
┌──────────┐     ┌──────────┐
│ greeting │ ──→ │ 'Father!'│
└──────────┘     └──────────┘
```

La línea `greeting = 'Father!'` se lee así: «toma el valor `'Father!'` y asígnalo a la variable con el nombre `greeting`». El signo `=` aquí es el operador de asignación, no una indicación de igualdad como en matemáticas. Pone el valor dentro de la variable.

Cuando escribimos `print(greeting)`, el intérprete sustituye el nombre `greeting` por el valor que está guardado en ella. Como resultado, en la pantalla se muestra la cadena `'Father!'`.

```text
print(greeting)
      |
      v
print('Father!')
```

## Nombres de las variables

Los nombres de las variables los inventa el propio programador. En Python se pueden usar:

- Letras latinas (a-z, A-Z),
- cifras (pero no al principio),
- el guion bajo _.

Ejemplos de nombres admitidos: `greeting`, `name1`, `hello_world`. Python distingue entre minúsculas y mayúsculas. Las variables `greeting`, `Greeting` y `GREETING` son tres variables diferentes.

## Variables y literales

En el código es importante distinguir dónde usamos una variable y dónde escribimos un valor directamente. Eso se nota especialmente en el ejemplo con `print()`:

```python
greeting = "Mother!"
print(greeting)  # => Mother!
print("greeting")  # => greeting
```

En el primer caso se usa la **variable** `greeting`, y el programa sustituye su valor. En el segundo caso `'greeting'` está entre comillas, por eso es un **literal de cadena**, es decir, un valor listo escrito directamente en el código. A pesar de que vemos la palabra `greeting` en los dos casos, desde el punto de vista del intérprete son cosas absolutamente distintas.

Los literales son datos escritos de forma explícita (por ejemplo, `'Hello'`, `42`, `3.14`). Los identificadores son nombres de variables y funciones (por ejemplo, `greeting`, `print`), que apuntan a valores o comandos ya existentes.

## El orden de uso

Una variable hay que crearla primero (asignarle un valor) y solo después usarla. Si se intenta acceder a una variable antes de crearla, el programa dará un error:

```python
print(name)  # Error: la variable todavía no está definida
# NameError: name 'name' is not defined
name = "Alice"
```

Ese error se llama «acceso a una variable no declarada». Es bastante fácil de corregir, porque el texto del error dice sin ambigüedad qué variable se usa antes de declararla.

Y en el orden correcto todo funciona:

```python
name = "Alice"
print(name)  # => Alice
```

## Varias variables en un programa

En un mismo programa se pueden crear tantas variables como se quiera. Cada una guarda sus datos y no molesta a las demás:

```python
greeting1 = "Father!"
print(greeting1)
print(greeting1)

greeting2 = "Mother!"
print(greeting2)
print(greeting2)
```

¿Cómo saber cuándo hacen falta varias variables? La cantidad de variables depende de la lógica del programa. Ese tema se desarrolla en detalle más adelante, cuando nos encontremos con las funciones y las construcciones condicionales.

## Dónde crear las variables

Los programadores procuran crear las variables cerca del lugar donde se usan. Eso hace el código más legible. Es especialmente importante en programas grandes, donde las variables pueden ser decenas y cientos de miles.
