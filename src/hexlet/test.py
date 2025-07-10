import importlib
import types

__all__ = ("expect_output",)


def expect_output(capsys, expected):
    importlib.import_module("index")
    out, _err = capsys.readouterr()
    actual = out.strip()

    if isinstance(expected, types.FunctionType):
        expected(actual)
    else:
        assert actual == expected

    print("\n")
    print(out)
