from hexlet.test import expect_output


def test(capsys):
    expected = '''Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground.'''
    expect_output(capsys, expected)
