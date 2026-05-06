import index


def test1():
    assert index.calculate_delivery_cost("canada", 0.5) == 600
    assert index.calculate_delivery_cost("canada", 1) == 600
    assert index.calculate_delivery_cost("canada", 2) == 900
    assert index.calculate_delivery_cost("usa", 1) == 800
    assert index.calculate_delivery_cost("usa", 3) == 1200
    assert index.calculate_delivery_cost("germany", 0.3) == 700
    assert index.calculate_delivery_cost("germany", 1.5) == 1000
    assert index.calculate_delivery_cost("france", 1) is None
