import random
import index


def test():
    annotations = index.generate_pin.__annotations__
    assert 'return' in annotations, "You should add a return type annotation"

    for seed in [1, 7, 42]:
        random.seed(seed)
        result = index.generate_pin()
        random.seed(seed)
        d1 = random.randint(0, 9)
        d2 = random.randint(0, 9)
        d3 = random.randint(0, 9)
        d4 = random.randint(0, 9)
        assert result == f"{d1}{d2}{d3}{d4}"
        assert len(result) == 4
