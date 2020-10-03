import importlib

__all__ = (
    'expect_output',
)

def expect_output(capsys, expected):
    importlib.import_module('index')
    out, _err = capsys.readouterr()
    actual = out.strip()

    assert actual == expected

    print("\n")
    print(out)
