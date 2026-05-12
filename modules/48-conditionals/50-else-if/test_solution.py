import solution


def test1():
    assert solution.get_traffic_light_action("green") == "go"
    assert solution.get_traffic_light_action("yellow") == "slow down"
    assert solution.get_traffic_light_action("red") == "stop"
    assert solution.get_traffic_light_action("blue") == "unknown"
    assert solution.get_traffic_light_action("purple") == "unknown"
