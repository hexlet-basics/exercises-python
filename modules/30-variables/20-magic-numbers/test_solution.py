import ast
from pathlib import Path

import pytest


def run_solution(capsys, tree=None):
    path = Path(__file__).with_name("solution.py")
    if tree is None:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    namespace = {"__name__": "solution", "__file__": str(path)}
    exec(compile(tree, str(path), "exec"), namespace)
    out, _err = capsys.readouterr()
    return namespace, out.strip("\n")


@pytest.mark.parametrize("counts,boxes", [(6, 17), (7, 19), (1, 12)])
def test(capsys, counts, boxes):
    namespace, out = run_solution(capsys)
    assert out == "Boxes in stock:\n102", "Print the result in the required format"
    assigned = {
        name: value
        for name, value in namespace.items()
        if type(value) is int and value in (6, 17)
    }
    assert 6 in assigned.values() and 17 in assigned.values(), (
        "Create variables with the given values"
    )
    replacements = {
        name: counts if value == 6 else boxes for name, value in assigned.items()
    }

    class Inputs(ast.NodeTransformer):
        def visit_Assign(self, node):
            if all(
                isinstance(t, ast.Name) and t.id in replacements for t in node.targets
            ):
                values = {replacements[t.id] for t in node.targets}
                assert len(values) == 1
                node.value = ast.copy_location(
                    ast.Constant(value=values.pop()), node.value
                )
            elif len(node.targets) == 1 and isinstance(
                node.targets[0], (ast.Tuple, ast.List)
            ):
                targets = node.targets[0].elts
                if all(
                    isinstance(t, ast.Name) and t.id in replacements for t in targets
                ):
                    node.value = ast.copy_location(
                        ast.Tuple(
                            elts=[
                                ast.Constant(value=replacements[t.id]) for t in targets
                            ],
                            ctx=ast.Load(),
                        ),
                        node.value,
                    )
            return node

    path = Path(__file__).with_name("solution.py")
    tree = Inputs().visit(ast.parse(path.read_text(encoding="utf-8")))
    ast.fix_missing_locations(tree)
    _namespace, changed = run_solution(capsys, tree)
    assert changed == "Boxes in stock:" + "\n" + str(counts * boxes), (
        "Calculate the result using the created variables"
    )
