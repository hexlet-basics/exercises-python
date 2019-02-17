'''
Exercise tesing utils
'''
import importlib
import io
from contextlib import contextmanager
from unittest.mock import patch

import asserts


__all__ = (
    'assert_equal',
    'expect_output',
    'TestEnv',
)


def assert_equal(actual: object, expected: object) -> None:
    '''
    Asserts an equality of @actual value and @expected value.
    Then prints an @actual value.
    '''
    asserts.assert_equal(actual, expected)
    print(actual)


@contextmanager
def _check_output(expected: str) -> object:
    '''
    Returns a Context Manager that will capture all the output
    and match that output with expected one.
    '''
    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        yield None
        actual = fake_output.getvalue().strip()
        asserts.assert_equal(actual, expected)
    print(actual)


def expect_output(expected: str) -> None:
    '''
    Imports an "index" module and checks its output
    '''
    with _check_output(expected):
        importlib.import_module('index')


class TestEnv(object):
    '''
    Context manager that inspects user defined module
    '''
    def __init__(self):
        self.module = importlib.import_module('index')

    def __enter__(self) -> 'TestEnv':
        return self

    def __exit__(self, *args):
        return True

    def expect_defined(self, name: str) -> None:
        '''
        Asserts that module defines the @name. Returns a value of definition
        '''
        asserts.assert_has_attr(self.module, name)
        return getattr(self.module, name)

    def expect_equal(self, name: str, value: object) -> None:
        '''
        Assertss that module defines the @name and name has a @value
        '''
        assert_equal(self.expect_defined(name), value)


if __name__ == '__main__':
    importlib.import_module('test')
