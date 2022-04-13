from datetime import date


# BEGIN
def get_current_year():
    current_date = date.today()
    return int(current_date.isoformat()[0:4])
# END
