'''
Exercise tesing utils
'''
import importlib
import io
from unittest.mock import patch

from asserts import assert_equal


__all__ = (
    'expect_output',
)


def expect_output(expected: str) -> None:
    '''
    Imports an "index" module and checks its output
    '''
    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        importlib.import_module('index')
        actual = fake_output.getvalue().strip()
        assert_equal(actual, expected)
    print(actual)


if __name__ == '__main__':
    importlib.import_module('test')
