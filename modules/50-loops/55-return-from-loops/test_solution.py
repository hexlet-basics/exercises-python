from solution import has_at_symbol


def test_has_at_symbol():
    assert has_at_symbol("support@example.com") is True
    assert has_at_symbol("wrong-email") is False
    assert has_at_symbol("@admin") is True
    assert has_at_symbol("admin@") is True
