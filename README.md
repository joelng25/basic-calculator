# Basic Calculator

[![CI](https://github.com/joelng25/basic-calculator/actions/workflows/ci.yml/badge.svg)](https://github.com/joelng25/basic-calculator/actions/workflows/ci.yml)

A basic calculator made with Python and Tkinter.

## Description

A calculator for addition, subtraction, multiplication and division, built as a learning project to practice GUI development with Tkinter.

The arithmetic logic lives in `calculator.py`, separate from the GUI in `main.py`. Expressions are evaluated with a small AST-based parser instead of `eval()`, so only numbers and `+ - * /` are accepted.

## Features

- Basic operations with operator precedence
- Safe expression evaluation (no `eval()`)
- Keyboard input (numbers, operators, Enter, Escape, Backspace)
- Error handling (invalid input, division by zero)
- Resizable window with custom styles
- Unit tests and CI

## Usage

```bash
git clone https://github.com/joelng25/basic-calculator.git
cd basic-calculator
python main.py
```

- Click the buttons or type with the keyboard
- Enter or `=` shows the result
- Clear or Escape clears the display
- Backspace deletes the last character

## Development

```bash
pip install -r requirements-dev.txt
ruff check .
pytest
```

## Author

Joel Novio — [github.com/joelng25](https://github.com/joelng25)

## License

MIT — see [LICENSE](LICENSE).
