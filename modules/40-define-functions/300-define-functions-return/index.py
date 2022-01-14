from datetime import date


# BEGIN
def get_current_year():
    current_date = f"{date.today()}"
    current_year = current_date[0:4]
    return int(current_year)
# END
