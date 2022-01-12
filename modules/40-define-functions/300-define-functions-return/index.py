from hexlet.code_basics import get_current_date


# BEGIN
def get_current_year():
    date = get_current_date()
    year = date[0:4]
    return int(year)
# END
