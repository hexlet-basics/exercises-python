'''
Exercise tesing utils
'''
import importlib

__all__ = (
    'expect_output',
)

def expect_output(capsys, output):
    importlib.import_module('index')
    out, _err = capsys.readouterr()
    assert out.strip() == output
    print("\n")
    print(out)
