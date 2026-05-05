import index


def test1():
    assert index.get_traffic_light_action("green") == "go"
    assert index.get_traffic_light_action("yellow") == "slow down"
    assert index.get_traffic_light_action("red") == "stop"
    assert index.get_traffic_light_action("blue") == "unknown"
    assert index.get_traffic_light_action("purple") == "unknown"
