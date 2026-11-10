A medida que el programa crece aumenta no solo la cantidad de líneas de código, sino también la cantidad de módulos. En proyectos pequeños, decenas de archivos todavía se pueden mantener en un solo directorio, pero en aplicaciones reales los archivos pueden ser cientos y miles.

Para organizar los módulos en grupos lógicos más grandes, en Python se usan los paquetes. En esta lección trabajamos con paquetes regulares. Un paquete regular es un directorio con un archivo _\_\_init\_\_.py_ y módulos de Python. El archivo _\_\_init\_\_.py_ puede estar vacío.

Por ejemplo, la estructura de un proyecto puede verse así:

```text
project/
├── main.py
├── payments/
│   ├── __init__.py
│   ├── stripe.py
│   └── paypal.py
└── users/
    ├── __init__.py
    ├── auth.py
    └── profile.py
```

En este ejemplo, `payments` y `users` son paquetes, y `stripe.py`, `paypal.py`, `auth.py` y `profile.py` son módulos.

Los paquetes ayudan a agrupar el código por tareas y simplifican la navegación por el proyecto. En lugar de cientos de archivos en un solo directorio, el código se divide en áreas de responsabilidad separadas.

## Importación desde un paquete

A los módulos que están dentro de un paquete se accede a través del punto:

```python
import payments.stripe
```

Después de la importación se puede usar el contenido del módulo:

```python
import payments.stripe

payments.stripe.create_payment()
```

El punto muestra el camino dentro del paquete. Python pasa secuencialmente del paquete al módulo.

## Importación de un módulo concreto

Las dos formas importan el módulo `payments.stripe`. La forma `from payments import stripe` lo asocia al nombre corto `stripe` en el archivo actual.

```python
from payments import stripe

stripe.create_payment()
```

Lo que se acorta es la llamada, `stripe.create_payment()` en lugar de `payments.stripe.create_payment()`. La instrucción de importación puede ser más larga.

## Paquetes anidados

Los paquetes pueden contener otros paquetes:

```text
project/
└── app/
    ├── __init__.py
    └── payments/
        ├── __init__.py
        ├── stripe/
        │   ├── __init__.py
        │   ├── client.py
        │   └── api.py
        └── paypal.py
```

En ese caso el camino hasta el módulo se vuelve más largo:

```python
from app.payments.stripe import client
```

Esa estructura se encuentra a menudo en proyectos grandes. Ayuda a dividir el código en partes independientes.

## Paquetes y espacios de nombres

Los paquetes crean un nivel adicional de espacio de nombres. Gracias a eso, distintas partes del programa pueden contener módulos con los mismos nombres.

Por ejemplo:

```text
project/
├── admin/
│   ├── __init__.py
│   └── config.py
└── user/
    ├── __init__.py
    └── config.py
```

Aquí existen dos módulos `config.py` distintos.

Python los distingue por el camino completo:

```python
import admin.config
import user.config
```

Sin los paquetes, esos nombres entrarían en conflicto entre sí.

## El archivo de inicialización del paquete

El archivo _\_\_init\_\_.py_ identifica un paquete regular. También se crea cuando el paquete no necesita código común. En ese caso se deja vacío.

```text
payments/
├── __init__.py
├── stripe.py
└── paypal.py
```

Un directorio puede contener cualquier tipo de archivo. Con _\_\_init\_\_.py_, `payments` es un paquete regular cuyos módulos se importan como `payments.stripe` y `payments.paypal`. Al importar `payments`, Python ejecuta el código de _\_\_init\_\_.py_. Allí se pueden definir los nombres accesibles mediante el paquete.

Python también tiene paquetes de espacio de nombres. Permiten reunir partes de un paquete desde varios directorios y no llevan _\_\_init\_\_.py_. Son otra forma de organizar paquetes. Los ejemplos de esta lección usan paquetes regulares y cada directorio de paquete, incluidos los anidados, contiene ese archivo.
