from tkinter import *
from tkinter import ttk

expr = ""
aux = ""


def press(key):
    global expr
    global aux
    expr += str(key)
    if key != "+" and key != "-" and key != "*" and key != "/":
        aux += str(key)
        display.set(aux)
    else:
        aux = ""
        display.set(key)


def equal():
    global expr
    global aux
    try:
        result = str(eval(expr))
        display.set(result)
        expr = aux = ""
    except:
        display.set("error")
        expr = aux = ""


def clear():
    global expr
    global aux
    expr = aux = ""
    display.set("")


def key_press(event):
    key = event.char

    if key in "0123456789.":
        press(key)
    elif key in "+-*/":
        press(key)
    elif key == "\r":
        equal()
    elif key == "\x1b":
        clear()
    elif key == "\x08":
        global expr, aux
        expr = expr[:-1]
        aux = aux[:-1]
        display.set(aux)

    return "break"


if __name__ == "__main__":
    root = Tk()
    root.title("Basic Calculator")
    root.minsize(250, 300)
    root.iconbitmap("calculator_icon.ico")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "Number.TButton",
        font=("Arial", 10, "bold"),
        foreground="white",
        background="#771096",
        padding=6,
    )

    style.map(
        "Number.TButton",
        background=[("active", "#4A075F"), ("pressed", "#370746")],
        foregorund=[("active", "white")],
    )

    style.configure(
        "Operator.TButton",
        font=("Arial", 10, "bold"),
        foreground="white",
        background="#3498db",
        padding=6,
    )

    style.map(
        "Operator.TButton",
        background=[("active", "#2980b9"), ("pressed", "#21618c")],
    )

    style.configure(
        "Equals.TButton",
        font=("Arial", 10, "bold"),
        foreground="white",
        background="#2ecc71",
        padding=6,
    )

    style.map(
        "Equals.TButton", background=[("active", "#27ae60"), ("pressed", "#229954")]
    )

    style.configure(
        "Clear.TButton",
        font=("Arial", 10, "bold"),
        foreground="white",
        background="#e67e22",
        padding=6,
    )

    style.map(
        "Clear.TButton", background=[("active", "#d35400"), ("pressed", "#ba4a00")]
    )

    style.configure(
        "Display.TEntry",
        font=("Arial", 12, "bold"),
        fieldbackground="white",
        foreground="black",
        padding=5,
    )

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    mainframe = ttk.Frame(root, padding="10")
    mainframe.grid(column=0, row=0, sticky=(N, S, E, W))

    display = StringVar()
    entry = ttk.Entry(mainframe, textvariable=display, style="Display.TEntry")
    entry.grid(column=0, row=0, columnspan=4, sticky=(W, E), pady=(0, 10))

    numbers = [
        (1, 2, 0),
        (2, 2, 1),
        (3, 2, 2),
        (4, 3, 0),
        (5, 3, 1),
        (6, 3, 2),
        (7, 4, 0),
        (8, 4, 1),
        (9, 4, 2),
        (0, 5, 0),
    ]

    for num, row, col in numbers:
        btn = ttk.Button(
            mainframe,
            text=str(num),
            style="Number.TButton",
            command=lambda n=num: press(n),
        )
        btn.grid(row=row, column=col, sticky=(W, E), padx=2, pady=2)

    operators = [("+", 2), ("-", 3), ("*", 4), ("/", 5)]

    for op, row in operators:
        btn = ttk.Button(
            mainframe, text=op, style="Operator.TButton", command=lambda o=op: press(o)
        )
        btn.grid(row=row, column=3, sticky=(W, E), padx=2, pady=2)

    doot = ttk.Button(
        mainframe, text=".", command=lambda: press("."), style="Number.TButton"
    )
    doot.grid(row=6, column=0, sticky=(W, E), padx=2, pady=2)
    eq = ttk.Button(mainframe, text="=", command=equal, style="Equals.TButton")
    eq.grid(row=6, column=2, sticky=(W, E), padx=2, pady=2)
    clear = ttk.Button(mainframe, text="Clear", command=clear, style="Clear.TButton")
    clear.grid(row=6, column=1, sticky=(W, E), padx=2, pady=2)

    for col in range(4):
        mainframe.columnconfigure(col, weight=1)
    for row in range(7):
        mainframe.rowconfigure(row, weight=1)

    root.bind("<Key>", key_press)
    root.bind("<Return>", lambda e: equal())
    root.bind("<KP_Enter>", lambda e: equal())
    root.bind("<Escape>", lambda e: clear())
    root.focus()
    root.mainloop()
