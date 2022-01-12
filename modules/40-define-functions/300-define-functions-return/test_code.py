from datetime import date
from index import get_current_year


def test():
    assert date.today().year == get_current_year()
