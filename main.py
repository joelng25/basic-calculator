import os
from tkinter import E, N, S, StringVar, Tk, W, ttk, Listbox
from calculator import Calculator
FONT = ("Arial", 10, "bold")
BUTTON_STYLES = {
    "Number": ("#771096", "#4A075F", "#370746"),
    "Operator": ("#3498db", "#2980b9", "#21618c"),
    "Equals": ("#2ecc71", "#27ae60", "#229954"),
    "Clear": ("#e67e22", "#d35400", "#ba4a00"),
}
def setup_styles() -> None:
    style = ttk.Style()
    style.theme_use("clam")
    for name, (bg, active, pressed) in BUTTON_STYLES.items():
        style_name = f"{name}.TButton"
        style.configure(style_name, font=FONT, foreground="white", background=bg, padding=6)
        style.map(style_name, background=[("active", active), ("pressed", pressed)], foreground=[("active", "white")])
    style.configure("Display.TEntry", font=("Arial", 12, "bold"), fieldbackground="white", foreground="black", padding=5)
class CalculatorApp:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.calc = Calculator()
        self.display = StringVar()
        self._build()
        self._bind_keys()
    def _button(self, frame, text, style, command, row, col):
        btn = ttk.Button(frame, text=text, style=f"{style}.TButton", command=command)
        btn.grid(row=row, column=col, sticky=(W, E), padx=2, pady=2)
    def _build(self) -> None:
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(column=0, row=0, sticky=(N, S, E, W))
        entry = ttk.Entry(frame, textvariable=self.display, style="Display.TEntry", state="readonly")
        entry.grid(column=0, row=0, columnspan=4, sticky=(W, E), pady=(0, 10))
        for num in range(1, 10):
            row, col = 2 + (num - 1) // 3, (num - 1) % 3
            self._button(frame, str(num), "Number", lambda n=num: self.press(n), row, col)
        self._button(frame, "0", "Number", lambda: self.press(0), 5, 0)
        for row, op in enumerate("+-*/", start=2):
            self._button(frame, op, "Operator", lambda o=op: self.press(o), row, 3)
        self._button(frame, ".", "Number", lambda: self.press("."), 6, 0)
        self._button(frame, "Clear", "Clear", self.clear, 6, 1)
        self._button(frame, "=", "Equals", self.equal, 6, 2)
        self.history = Listbox(frame, height=4, exportselection=False)
        self.history.grid(column=0, row=7, columnspan=4, sticky=(W, E))
        self.history.bind("<<ListboxSelect>>", self.restore_history)
        for col in range(4):
            frame.columnconfigure(col, weight=1)
        for row in range(7):
            frame.rowconfigure(row, weight=1)
    def _bind_keys(self) -> None:
        self.root.bind("<Key>", self.on_key)
        self.root.bind("<Return>", lambda e: self.equal())
        self.root.bind("<KP_Enter>", lambda e: self.equal())
        self.root.bind("<Escape>", lambda e: self.clear())
        self.root.bind("<BackSpace>", lambda e: self.display.set(self.calc.backspace()))
    def press(self, key) -> None:
        self.display.set(self.calc.press(key))
    def equal(self) -> None:
        result = self.calc.equal()
        self.display.set(self.calc.last_error if result == "error" else result)
        self.history.delete(0, "end")
        for expression, value in self.calc.history:
            self.history.insert("end", f"{expression} = {value}")
    def restore_history(self, event=None) -> None:
        selected = self.history.curselection()
        if selected:
            self.display.set(self.calc.restore_history(selected[0]))
    def clear(self) -> None:
        self.display.set(self.calc.clear())
    def on_key(self, event):
        if event.char and event.char in "0123456789.()+-*/=":
            self.equal() if event.char == "=" else self.press(event.char)
        return "break"
def main() -> None:
    root = Tk()
    root.title("Basic Calculator")
    root.minsize(250, 300)
    icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), "calculator_icon.ico")
    if os.path.exists(icon) and os.name == "nt":
        root.iconbitmap(icon)
    setup_styles()
    CalculatorApp(root)
    root.focus()
    root.mainloop()
if __name__ == "__main__":
    main()
