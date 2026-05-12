def get_traffic_light_action(color: str) -> str:
    if color == "green":
        return "go"
    elif color == "yellow":
        return "slow down"
    elif color == "red":
        return "stop"
    return "unknown"
