import pytest

from calculator import Calculator, CalculatorError, safe_eval


@pytest.mark.parametrize(
    "expr, expected",
    [("2+3", 5), ("10-4", 6), ("3*4", 12), ("8/2", 4), ("2+3*4", 14), ("-5+2", -3), ("1.5*2", 3)],
)
def test_safe_eval(expr, expected):
    assert safe_eval(expr) == expected


@pytest.mark.parametrize("expr", ["__import__('os')", "2**10", "abc", "1/0", "2+", ""])
def test_safe_eval_rejects(expr):
    with pytest.raises(CalculatorError):
        safe_eval(expr)


def test_calculator_flow():
    calc = Calculator()
    assert calc.press(1) == "1"
    assert calc.press(2) == "12"
    assert calc.press("+") == "+"
    assert calc.press(3) == "3"
    assert calc.equal() == "15"
    assert calc.expression == ""


def test_backspace_and_error():
    calc = Calculator()
    for k in "12":
        calc.press(k)
    assert calc.backspace() == "1"
    calc.press("/")
    calc.press(0)
    assert calc.equal() == "error"
