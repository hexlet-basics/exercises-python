from unittest.mock import patch
from io import StringIO
from asserts import assert_true, assert_equal

with patch('sys.stdout', new=StringIO()) as fake_output:
    import index
    actual = fake_output.getvalue().strip()
    assert_equal(actual, 'Hello, World!')

print(actual)
