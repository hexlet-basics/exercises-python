def who_is_this_house_to_starks(house_name):
    if house_name == "Karstark" or house_name == "Tully":
        return "friend"
    elif house_name == "Lannister" or house_name == "Frey":
        return "enemy"
    return "neutral"
