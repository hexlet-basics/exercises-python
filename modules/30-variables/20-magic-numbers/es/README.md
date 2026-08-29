Veamos un ejemplo de programa que realiza una conversión de divisas:

```python
euros_count = 1000
dollars_count = euros_count * 1.25  # 1250.0
rubles_count = dollars_count * 60  # 75000.0

print(rubles_count)
```

Técnicamente el código funciona. Pero desde el punto de vista del desarrollo profesional, ese código se considera una mala práctica.

## ¿Cuál es el problema?

En las expresiones se han usado números incomprensibles: __1.25__ y __60__. ¿Qué valores son esos? ¿El tipo de cambio? ¿De dónde salieron? Dentro de un mes o de un año, lo más probable es que no recuerdes qué significan exactamente esos números. Y si el código lo abre otro desarrollador, simplemente no entenderá de dónde sale todo. Esos números se llaman mágicos.

Los números mágicos (magic numbers) son valores numéricos cuyo sentido no queda claro a partir del código. Normalmente se usan directamente en expresiones matemáticas, sin variables con nombres comprensibles. Para entender su propósito hay que meterse en el contexto o leer documentación adicional. Los números mágicos dificultan la lectura, la comprensión y el mantenimiento del código.

## Cómo evitar la magia

La forma más simple consiste en llevar esos valores a variables con nombres comprensibles. Entonces el sentido se volverá evidente:

```python
dollars_per_euro = 1.25
rubles_per_dollar = 60

euros_count = 1000
dollars_count = euros_count * dollars_per_euro  # 1250.0
rubles_count = dollars_count * rubles_per_dollar  # 75000.0

print(rubles_count)
```

Los números en sí no han desaparecido, pero ahora están escritos en variables cuyos nombres dicen sin ambigüedad qué son.

## Conclusión

Los números mágicos hacen el código incomprensible y difícil de mantener. Para evitar ese problema hay que reemplazar esos números por variables con nombres significativos. Eso hace el código más legible, especialmente a largo plazo. Un código claro es siempre más importante que la compacidad, aunque el programa se alargue un poco.
