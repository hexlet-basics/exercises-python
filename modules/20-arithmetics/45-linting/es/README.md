Ya hemos aprendido a escribir programas simples, por lo que ahora podemos hablar un poco sobre cómo escribirlos correctamente.

El código debe ser formateado de una manera específica para que sea comprensible y fácil de mantener en el tiempo. Existen conjuntos de reglas especiales que describen varios aspectos de la escritura de código, llamadas **convenciones de codificación**. En Python, hay una convención estándar: [PEP8](https://peps.python.org/pep-0008/). Este documento estándar responde prácticamente todas las preguntas sobre cómo formatear una parte específica del código. Este documento contiene todas las reglas que se deben seguir. Recomendamos a los principiantes que se acostumbren a consultar el estándar PEP8 y escribir cualquier código siguiendo sus pautas.

Hoy en día no es necesario recordar todas las reglas de la convención estándar, ya que existen programas especiales que verifican automáticamente el código y señalan las violaciones. Estos programas se llaman **linters**. Verifican el código para asegurarse del cumplimiento de los estándares. En Python, hay muchos linters, y el más popular de ellos es [flake8](https://flake8.pycqa.org/en/latest/).

Echemos un vistazo a un ejemplo:

```python
result = 1+ 3
```

El linter mostrará un error por violar la regla: *E225 missing whitespace around operator*. Según el estándar, el operador `+` siempre debe estar separado por espacios de los operandos.

En el ejemplo anterior, vimos la regla [E225](https://pep8.readthedocs.io/en/release-1.7.x/intro.html#error-codes), que es apenas una sola de la larga lista de reglas. Otras reglas describen la indentación, los nombres, los paréntesis, las operaciones matemáticas, la longitud de las líneas y muchos otros aspectos. Cada regla individual puede parecer insignificante y pequeña, pero juntas forman la base de un buen código. La lista completa de reglas de flake8 está disponible en [esta documentación](https://flake8.pycqa.org/en/latest/user/error-codes.html).

Ya estás familiarizado con el linter, ya que la plataforma de Hexlet verifica tu código utilizando uno. Pronto comenzarás a usarlo fuera de Hexlet, cuando implementes proyectos educativos. Configurarás el linter y verificará el código en tiempo real, informándote sobre las violaciones.
