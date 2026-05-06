Implementa la función `amount_per_person()`. Recibe el total de la cuenta del restaurante, el número de personas y el porcentaje de propina, y devuelve la cantidad que paga cada persona. El resultado se redondea hacia arriba — nadie debe pagar de menos.

Usa la función `math.ceil()` del módulo `math` para el redondeo.

```python
# Cuenta 300, 4 personas, propina 20% — total 360, cada uno paga 90
print(amount_per_person(300, 4, 20))  # => 90

# Cuenta 350, 3 personas, propina 10% — total 385, cada uno paga 129
print(amount_per_person(350, 3, 10))  # => 129
```

## Pista

* Primero calcula el total con propina, luego divide entre el número de personas y redondea hacia arriba
* No olvides importar el módulo `math` al inicio del archivo
