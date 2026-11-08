import importlib
from unittest.mock import patch

import solution


def test():
    assert callable(getattr(solution, "escape_html", None)), (
        "Define the escape_html(text) function"
    )
    cases = [
        ("", ""),
        ("Hello", "Hello"),
        ("<b>A & B</b>", "&lt;b&gt;A &amp; B&lt;/b&gt;"),
        ('"Hello"', "&quot;Hello&quot;"),
        ("It's ok", "It&#x27;s ok"),
        ("&lt;", "&amp;lt;"),
        ("Привет, мир!", "Привет, мир!"),
    ]
    for text, expected in cases:
        assert solution.escape_html(text) == expected, (
            "escape_html must return the escaped string",
            text,
        )

    with patch("html.escape", return_value="escaped-by-html") as escape:
        importlib.reload(solution)
        assert solution.escape_html("source") == "escaped-by-html", (
            "Use the escape function from the html package"
        )
        assert escape.call_count == 1, "Use the escape function from the html package"
        args, kwargs = escape.call_args
        assert (args[0] if args else kwargs.get("s")) == "source", (
            "Use the escape function from the html package"
        )
    importlib.reload(solution)
