from asserts import assert_true, assert_equal
from unittest.mock import patch
from io import StringIO

with patch("sys.stdout", new=StringIO()) as fake_output:
    import index

    actual = fake_output.getvalue().strip()
    assert_equal(actual, "49.0")

print(actual)
