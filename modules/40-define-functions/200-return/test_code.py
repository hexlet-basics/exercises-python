import index
from datetime import date


def test():
    expected = date.today().year
    assert index.get_current_year() == expected
