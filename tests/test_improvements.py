import pytest
from calculator import Calculator, CalculatorError, safe_eval
@pytest.mark.parametrize("expr, expected", [("((2+3)*4)",20),("--2",2),(" 2 + 3 ",5)])
def test_nested_and_whitespace(expr, expected):
    assert safe_eval(expr) == expected
@pytest.mark.parametrize("expr", ["1e309", "1e308*1e308", "2$3"])
def test_nonfinite_and_malformed(expr):
    with pytest.raises(CalculatorError): safe_eval(expr)
def test_error_preserves_expression_and_history_restores():
    calc = Calculator()
    for k in "1/0": calc.press(k)
    assert calc.equal() == "error"
    assert calc.expression == "1/0"
    assert calc.last_error == "division by zero"
    calc.clear()
    for k in "2+3": calc.press(k)
    assert calc.equal() == "5"
    assert calc.history == [("2+3", "5")]
    assert calc.restore_history(0) == "2+3"
