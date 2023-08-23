import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.result_label = tk.Label(root, textvariable=self.result_var, font=("Arial", 20))
        self.result_label.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for button_text, row, col in self.buttons:
            self.create_button(button_text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 15),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col)

    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
