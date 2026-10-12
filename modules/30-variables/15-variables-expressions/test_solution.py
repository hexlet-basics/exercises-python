import ast
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "inputs,expected",
    [
        ({"euros_count": 100}, "125.0\n863.75"),
        ({"euros_count": 3}, "3.75\n25.9125"),
        ({"euros_count": 120}, "150.0\n1036.5"),
        ({"euros_count": 0}, "0.0\n0.0"),
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
    assert not remaining, "Keep the input variables from the scaffold"
    namespace = {"__name__": "solution", "__file__": str(path)}
    exec(compile(tree, str(path), "exec"), namespace)
    out, _err = capsys.readouterr()
    assert out.strip("\n") == expected, "Output must match the input data"
