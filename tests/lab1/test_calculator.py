# import tkinter as tk
# import unittest
# import sys
# # import os
# sys.path.append('/Users/mayna/cs102/src/lab1/calculator.py')


# from src.lab1 import calculator

# from calculator import add_digit, add_operation, calculate, clear, press_key

# class TestCalculator(unittest.TestCase):

#     def setUp(self):
#         self.window = tk.Tk()
#         self.window.withdraw()  # Hide the main window during testing

#     def test_add_digit(self):
#         calc = tk.Entry(self.window)
#         add_digit(calc, '5')
#         self.assertEqual(calc.get(), '5')

#     def test_add_operation(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5')
#         add_operation(calc, '+')
#         self.assertEqual(calc.get(), '5+')

#     def test_calculate(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5+3')
#         calculate(calc)
#         self.assertEqual(calc.get(), '8')

#     def test_clear(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5+3')
#         clear(calc)
#         self.assertEqual(calc.get(), '')

#     def test_press_key_digit(self):
#         calc = tk.Entry(self.window)
#         press_key(calc, '5')
#         self.assertEqual(calc.get(), '5')

#     def test_press_key_operation(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5')
#         press_key(calc, '+')
#         self.assertEqual(calc.get(), '5+')

#     def test_press_key_calculate(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5+3')
#         press_key(calc, '=')
#         self.assertEqual(calc.get(), '8')

# if __name__ == '__main__':
#     unittest.main()

# import unittest
# from tkinter import messagebox
# from tkinter import END

# class TestCalculator(unittest.TestCase):
    
#     def setUp(self):
#         self.window = tk.Tk()
#         self.window.geometry(f"240x270+100+200")
#         self.window['bg'] = 'pink'
#         self.window.title('Калькулятор Барби')
#         self.calc = tk.Entry(self.window, justify=tk.RIGHT, font=('Arial',15), width=15)
#         self.calc.insert(0,'0')
#         self.calc.grid(row=0, column=0, columnspan=4,stick='we', padx=5)
    
#     def tearDown(self):
#         self.window.destroy()
    
#     def test_add_digit(self):
#         add_digit(1)
#         self.assertEqual(self.calc.get(), '1')
        
#         add_digit(2)
#         self.assertEqual(self.calc.get(), '12')
        
#         add_digit(3)
#         self.assertEqual(self.calc.get(), '123')
        
#     def test_add_operation(self):
#         add_operation('+')
#         self.assertEqual(self.calc.get(), '0+')
        
#         add_digit(1)
#         add_operation('-')
#         self.assertEqual(self.calc.get(), '1-')
        
#         add_digit(2)
#         add_operation('*')
#         self.assertEqual(self.calc.get(), '12*')
        
#     def test_calculate(self):
#         calculate()
#         self.assertEqual(self.calc.get(), '0')
        
#         add_digit(1)
#         calculate()
#         self.assertEqual(self.calc.get(), '1')
        
#         add_operation('+')
#         add_digit(2)
#         calculate()
#         self.assertEqual(self.calc.get(), '3')
        
#         add_operation('*')
#         add_digit(3)
#         calculate()
#         self.assertEqual(self.calc.get(), '9')
        
#     def test_clear(self):
#         clear()
#         self.assertEqual(self.calc.get(), '0')
        
#         add_digit(1)
#         clear()
#         self.assertEqual(self.calc.get(), '0')
        
#         add_operation('+')
#         add_digit(2)
#         clear()
#         self.assertEqual(self.calc.get(), '0')
        
#     def test_press_key(self):
#         event = tk.Event()
#         event.char = '1'
#         press_key(event)
#         self.assertEqual(self.calc.get(), '1')
        
#         event.char = '+'
#         press_key(event)
#         self.assertEqual(self.calc.get(), '1+')
        
#         event.char = '2'
#         press_key(event)
#         self.assertEqual(self.calc.get(), '1+2')
        
#         event.char = '/'
#         press_key(event)
#         self.assertEqual(self.calc.get(), '3/')
        
#         event.char = 'r'
#         press_key(event)
#         self.assertEqual(self.calc.get(), '3/3')
        
# if __name__ == '__main__':
#     unittest.main()




# import unittest
# import tkinter as tk
# import unittest
# import sys
# import os
# sys.path.append('/usr/local/bin/python3 /Users/mayna/cs102/tests/lab1/calculator.py ')


# from src.lab1 import calculator

# from calculator import Calculator

# class TestCalculator(unittest.TestCase):

#     def setUp(self):
#         self.window = tk.Tk()
#         self.window.withdraw()  # Hide the main window during testing

#     def test_add_digit(self):
#         calc = tk.Entry(self.window)
#         add_digit(calc, '5')
#         self.assertEqual(calc.get(), '5')

#     def test_add_operation(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5')
#         add_operation(calc, '+')
#         self.assertEqual(calc.get(), '5+')

#     def test_calculate(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5+3')
#         calculate(calc)
#         self.assertEqual(calc.get(), '8')

#     def test_clear(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5+3')
#         clear(calc)
#         self.assertEqual(calc.get(), '')

#     def test_press_key_digit(self):
#         calc = tk.Entry(self.window)
#         press_key(calc, '5')
#         self.assertEqual(calc.get(), '5')

#     def test_press_key_operation(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5')
#         press_key(calc, '+')
#         self.assertEqual(calc.get(), '5+')

#     def test_press_key_calculate(self):
#         calc = tk.Entry(self.window)
#         calc.insert(0, '5+3')
#         press_key(calc, '=')
#         self.assertEqual(calc.get(), '8')

# if __name__ == '__main__':
#     unittest.main()

# import unittest
# import tkinter as tk

# class TestCalculator(unittest.TestCase):

#     def setUp(self):
#         self.window = tk.Tk()
#         self.window.geometry(f"240x270+100+200")
#         self.window['bg'] = 'pink'
#         self.window.title('Калькулятор Барби')
#         self.calc = tk.Entry(self.window, justify=tk.RIGHT, font=('Arial',15), width=15)
#         self.calc.insert(0,'0')
#         self.calc.grid(row=0, column=0, columnspan=4,stick='we', padx=5)
    
#     def tearDown(self):
#         self.window.destroy()
    
#     def test_add_digit(self):
#         self.add_digit(1)
#         self.assertEqual(self.calc.get(), '1')
        
#         self.add_digit(2)
#         self.assertEqual(self.calc.get(), '12')
        
#         self.add_digit(3)
#         self.assertEqual(self.calc.get(), '123')
        
#     def test_add_operation(self):
#         self.add_operation('+')
#         self.assertEqual(self.calc.get(), '0+')
        
#         self.add_digit(1)
#         self.add_operation('-')
#         self.assertEqual(self.calc.get(), '1-')
        
#         self.add_digit(2)
#         self.add_operation('*')
#         self.assertEqual(self.calc.get(), '12*')
        
#     def test_calculate(self):
#         self.calculate()
#         self.assertEqual(self.calc.get(), '0')
        
#         self.add_digit(1)
#         self.calculate()
#         self.assertEqual(self.calc.get(), '1')
        
#         self.add_operation('+')
#         self.add_digit(2)
#         self.calculate()
#         self.assertEqual(self.calc.get(), '3')
        
#         self.add_operation('*')
#         self.add_digit(3)
#         self.calculate()
#         self.assertEqual(self.calc.get(), '9')
        
#     def test_clear(self):
#         self.clear()
#         self.assertEqual(self.calc.get(), '0')
        
#         self.add_digit(1)
#         self.clear()
#         self.assertEqual(self.calc.get(), '0')
        
#         self.add_operation('+')
#         self.add_digit(2)
#         self.clear()
#         self.assertEqual(self.calc.get(), '0')
        
#     def test_press_key(self):
#         event = tk.Event()
#         event.char = '1'
#         self.press_key(event)
#         self.assertEqual(self.calc.get(), '1')
        
#         event.char = '+'
#         self.press_key(event)
#         self.assertEqual(self.calc.get(), '1+')
        
#         event.char = '2'
#         self.press_key(event)
#         self.assertEqual(self.calc.get(), '1+2')
        
#         event.char = '/'
#         self.press_key(event)
#         self.assertEqual(self.calc.get(), '3/')
        
#         event.char = 'r'
#         self.press_key(event)
#         self.assertEqual(self.calc.get(), '3/3')
        
# if __name__ == '__main__':
#     unittest.main()
import unittest
import sys
sys.path.append('../../src/lab1')
from calculator import Calculator

class CalculatorTestCase(unittest.TestCase):

    def test_addition(self):
        calculator = Calculator()
        calculator.add_digit('5')
        calculator.add_operation('+')
        calculator.add_digit('7')
        calculator.calculate()
        result = calculator.calc.get()
        self.assertEqual(result, "12")

    def test_substruction(self):
        calculator = Calculator()
        calculator.add_digit('7')
        calculator.add_operation('-')
        calculator.add_digit('5')
        calculator.calculate()
        result = calculator.calc.get()
        self.assertEqual(result, "2")

    def test_multiplication(self):
        calculator = Calculator()
        calculator.add_digit('5')
        calculator.add_operation('*')
        calculator.add_digit('7')
        calculator.calculate()
        result = calculator.calc.get()
        self.assertEqual(result, "35")

    def test_division(self):
        calculator = Calculator()
        calculator.add_digit('12')
        calculator.add_operation('/')
        calculator.add_digit('6')
        calculator.calculate()
        result = calculator.calc.get()
        self.assertEqual(result, "2.0")
