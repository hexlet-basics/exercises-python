'''
Exercise tesing utils
'''
import importlib
import io
from unittest.mock import patch

from asserts import assert_equal, assert_has_attr


__all__ = (
    'expect_output',
    'Module',
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


class Module(object):
    '''
    Context manager that inspects user defined module
    '''
    def __init__(self):
        self.module = importlib.import_module('index')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return True

    def expect_defined(self, name):
        '''
        Assertss that module defines the @name
        '''
        assert_has_attr(self.module, name)

    def expect_eq(self, name, value):
        '''
        Assertss that module defines the @name and name has a @value
        '''
        self.expect_defined(name)
        assert_equal(getattr(self.module, name), value)


if __name__ == '__main__':
    importlib.import_module('test')
