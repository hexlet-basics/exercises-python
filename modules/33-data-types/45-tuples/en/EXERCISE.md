Two cities lie on the same road. Each is described by a tuple with a name and a position in kilometers from the start of the route:

```python
city_a = ("Moscow", 10)
city_b = ("Saint Petersburg", 644)
```

Calculate the distance between the cities and print the result in this format:

```text
From: Moscow
To: Saint Petersburg
Distance: 634 km
```

The check compares the output character by character, so after `From:`, `To:` and `Distance:` there must be exactly one space, and before `km` one more.
