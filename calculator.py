"""Calculator logic, independent of the GUI so it can be tested."""

import ast
import operator

_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}
_UNARY_OPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}

OPERATORS = "+-*/"


class CalculatorError(ValueError):
    """Raised when an expression cannot be evaluated."""


def safe_eval(expression: str) -> float:
    """Evaluate a basic arithmetic expression without using eval()."""
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise CalculatorError("invalid expression") from exc
    return _eval_node(tree.body)


def _eval_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
        left, right = _eval_node(node.left), _eval_node(node.right)
        try:
            return _BIN_OPS[type(node.op)](left, right)
        except ZeroDivisionError as exc:
            raise CalculatorError("division by zero") from exc
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        return _UNARY_OPS[type(node.op)](_eval_node(node.operand))
    raise CalculatorError("unsupported expression")


def format_result(value: float) -> str:
    """Show 4.0 as 4 and keep decimals otherwise."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


class Calculator:
    """Keeps the current expression and what the display should show."""

    def __init__(self) -> None:
        self.expression = ""
        self.current = ""

    def press(self, key: str) -> str:
        key = str(key)
        self.expression += key
        if key in OPERATORS:
            self.current = ""
            return key
        self.current += key
        return self.current

    def backspace(self) -> str:
        self.expression = self.expression[:-1]
        self.current = self.current[:-1]
        return self.current

    def clear(self) -> str:
        self.expression = self.current = ""
        return ""

    def equal(self) -> str:
        try:
            result = format_result(safe_eval(self.expression))
        except CalculatorError:
            result = "error"
        self.clear()
        return result
