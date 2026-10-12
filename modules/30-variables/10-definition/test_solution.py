import ast
from pathlib import Path


def run_solution(capsys, tree=None):
    path = Path(__file__).with_name("solution.py")
    if tree is None:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    namespace = {"__name__": "solution", "__file__": str(path)}
    exec(compile(tree, str(path), "exec"), namespace)
    out, _err = capsys.readouterr()
    return namespace, out.strip("\n")


def test(capsys):
    namespace, out = run_solution(capsys)
    assert out == "https://hexlet.io\nhttps://hexlet.io", (
        "Print the result in the required format"
    )
    assert namespace.get("url") == "https://hexlet.io", (
        "Create variables with the given values"
    )
