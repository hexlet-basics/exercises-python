A medida que el programa crece aumenta no solo la cantidad de líneas de código, sino también la cantidad de módulos. En proyectos pequeños, decenas de archivos todavía se pueden mantener en un solo directorio, pero en aplicaciones reales los archivos pueden ser cientos y miles.

Para organizar los módulos en grupos lógicos más grandes, en Python se usan los paquetes. Un paquete es un directorio con archivos de Python.

Por ejemplo, la estructura de un proyecto puede verse así:

```text
project/
├── main.py
├── payments/
│   ├── stripe.py
│   └── paypal.py
└── users/
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

A menudo no se importa todo el camino, sino un módulo concreto:

```python
from payments import stripe

stripe.create_payment()
```

Esa forma acorta la escritura y hace el código más compacto.

## Paquetes anidados

Los paquetes pueden contener otros paquetes:

```text
project/
└── app/
    └── payments/
        ├── stripe/
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
│   └── config.py
└── user/
    └── config.py
```

Aquí existen dos módulos `config.py` distintos.

Python los distingue por el camino completo:

```python
import admin.config
import user.config
```

Sin los paquetes, esos nombres entrarían en conflicto entre sí.

## El archivo __init__.py

Antes, para crear un paquete, dentro del directorio se colocaba obligatoriamente el archivo `__init__.py`:

```text
payments/
├── __init__.py
├── stripe.py
└── paypal.py
```

Ese archivo informaba a Python de que el directorio había que tratarlo como un paquete.

En las versiones modernas de Python los paquetes pueden funcionar también sin `__init__.py`. No obstante, ese archivo se sigue usando a menudo. Normalmente en él se coloca código común y la configuración del paquete.
