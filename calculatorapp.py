import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Input field
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        input_field.grid(row=0, column=0)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            '(', ')', '%', 'dlt',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_value = 0
        col_value = 0

        for button in buttons:
            button_cmd = lambda x=button: self.on_button_click(x)
            tk.Button(button_frame, text=button, padx=20, pady=20, font=("Arial", 18), command=button_cmd).grid(row=row_value, column=col_value)
            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += char
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
