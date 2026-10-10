import ast
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "distance,fuel_consumption,fuel_price,passengers",
    [
        (450, 8.4, 64.2, 4),
        (451, 8.4, 64.2, 4),
        (450, 8.43, 64.2, 4),
        (450, 8.4, 64.23, 4),
        (450, 8.4, 64.2, 3),
        (125, 7.25, 58.37, 2),
    ],
)
def test(capsys, distance, fuel_consumption, fuel_price, passengers):
    inputs = {
        "distance": distance,
        "fuel_consumption": fuel_consumption,
        "fuel_price": fuel_price,
        "passengers": passengers,
    }
    path = Path(__file__).with_name("solution.py")
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))

    # Vary only the four initial values supplied by the scaffold.
    # Student calculations and their variable names stay unchanged.
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
    assert not remaining, "Keep the four input variables from the scaffold"

    namespace = {"__name__": "solution", "__file__": str(path)}
    exec(compile(tree, str(path), "exec"), namespace)
    out, _err = capsys.readouterr()
    fuel = distance / 100 * fuel_consumption
    trip_cost = fuel * fuel_price
    expected = (
        f"{round(fuel, 1)}\n{round(trip_cost, 2)}\n{round(trip_cost / passengers)}"
    )
    assert out.strip("\n") == expected
