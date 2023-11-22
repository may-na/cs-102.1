import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(f"230x210+100+200")
        self.window['bg'] = 'pink'
        self.window.title('Калькулятор Барби')
        self.window.bind('<Key>', self.press_key)

        self.calc = tk.Entry(self.window, justify=tk.RIGHT, font=('Arial',15), width=15)
        self.calc.insert(0,'0')
        self.calc.grid(row=0, column=0, columnspan=4,stick='we', padx=5)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '0', 'C', '=', '/'
        ]
        row = 1
        col = 0
        for button in buttons:
            if button == "=":
                btn = tk.Button(self.window, text=button, bd=3, font=('Arial',14), command=lambda: self.calculate())
            elif button == "C":
                btn = tk.Button(self.window, text=button, bd=3, font=('Arial',14), command=lambda: self.clear())
            else:
                btn = tk.Button(self.window, text=button, bd=3, font=('Arial',14), command=lambda button=button: self.add_digit(button))
            btn.grid(row=row, column=col, stick='wens', padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_digit(self, digit):
        value = self.calc.get()
        if value[0]=='0' and len(value)==1:
            value=value[1:]
        self.calc.delete(0,tk.END)
        self.calc.insert(0, value + str(digit))

    def add_operation(self, operation):
        value = self.calc.get()
        if value[-1] in '+-/*':
            value = value[:-1]
        elif '+' in value or '-' in value or '/' in value or '*' in value:
            self.calculate()
            value = self.calc.get()
        self.calc.delete(0,tk.END)
        self.calc.insert(0, value + operation)

    def calculate(self):
        value = self.calc.get()
        if value[-1] in '+-/*':
            operation = value[-1]
            value = value[:-1] + operation + value[:-1]
        self.calc.delete(0,tk.END)
        try:
            self.calc.insert(0, eval(value))
        except (NameError, SyntaxError):
            messagebox.showinfo('Внимание', 'Вы ввели недопустимые символы')
            self.calc.insert(0, 0)
        except ZeroDivisionError:
            messagebox.showinfo('Внимание', 'Даже Барби знает, что на ноль делить нельзя!')
            self.calc.insert(0, 0)

    def clear(self):
        self.calc.delete(0, tk.END)
        self.calc.insert(0, 0)

    def press_key(self, event):
        if event.char.isdigit():
            self.add_digit(event.char)
        elif event.char in '+-/*':
            self.add_operation(event.char)
        elif event.char == '\r':
            self.calculate()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
