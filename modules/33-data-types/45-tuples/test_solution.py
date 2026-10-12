import ast
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "inputs,expected",
    [
        (
            {"city_a": ("Moscow", 10), "city_b": ("Saint Petersburg", 644)},
            "From: Moscow\nTo: Saint Petersburg\nDistance: 634 km",
        ),
        (
            {"city_a": ("Town A", 12), "city_b": ("Town B", 47)},
            "From: Town A\nTo: Town B\nDistance: 35 km",
        ),
        (
            {"city_a": ("Start", 0), "city_b": ("End", 100)},
            "From: Start\nTo: End\nDistance: 100 km",
        ),
        (
            {"city_a": ("Station A", 10), "city_b": ("Station B", 10)},
            "From: Station A\nTo: Station B\nDistance: 0 km",
        ),
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
