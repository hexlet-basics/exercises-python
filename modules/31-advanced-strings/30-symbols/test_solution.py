import ast
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "inputs,expected",
    [
        ({"text": "Python programming"}, "grip"),
        ({"text": "abcdefghijklmnopqr"}, "kiph"),
        ({"text": "ABCDEFGHIJKLMNOPQR"}, "KIPH"),
        ({"text": "0123456789ABCDEF"}, "A8F7"),
        ({"text": "αβγδεζηθικλμνξοπρσ"}, "λιπθ"),
    ],
)
def test(capsys, inputs, expected):
    path = Path(__file__).with_name("solution.py")
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    remaining = set(inputs)
    for statement in tree.body:
        if isinstance(statement, ast.Assign) and len(statement.targets) == 1:
            target = statement.targets[0]
            if isinstance(target, ast.Name) and target.id in remaining:
                statement.value = ast.copy_location(
                    ast.Constant(value=inputs[target.id]),
                    statement.value,
                )
                remaining.remove(target.id)
        if not remaining:
            break
    assert not remaining, "Keep the initial variables from the starter code"
    namespace = {"__name__": "solution", "__file__": str(path)}
    exec(compile(tree, str(path), "exec"), namespace)
    out, _err = capsys.readouterr()
    assert out.strip("\n") == expected, "The output must match the input data"
