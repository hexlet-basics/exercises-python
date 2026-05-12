import math


def amount_per_person(total: float, people: int, tip_percent: int) -> int:
    # BEGIN
    with_tip = total * (1 + tip_percent / 100)
    return math.ceil(with_tip / people)
    # END
