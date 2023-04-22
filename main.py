from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Basic Arithmetic Calculator")

        # Create input fields for number 1 and number 2
        self.number1_label = Label(master, text="Number 1:")
        self.number1_label.grid(row=0, column=0)
        self.number1_input = Entry(master)
        self.number1_input.grid(row=0, column=1)

        self.number2_label = Label(master, text="Number 2:")
        self.number2_label.grid(row=1, column=0)
        self.number2_input = Entry(master)
        self.number2_input.grid(row=1, column=1)

        # Create buttons for addition, subtraction, multiplication, division, and mod operation
        self.add_button = Button(master, text="+", command=self.add)
        self.add_button.grid(row=2, column=0)

        self.sub_button = Button(master, text="-", command=self.subtract)
        self.sub_button.grid(row=2, column=1)

        self.mul_button = Button(master, text="*", command=self.multiply)
        self.mul_button.grid(row=3, column=0)

        self.div_button = Button(master, text="/", command=self.divide)
        self.div_button.grid(row=3, column=1)

        self.mod_button = Button(master, text="%", command=self.modulo)
        self.mod_button.grid(row=4, column=0)

        # Create result label and layout
        self.result_label = Label(master, text="")
        self.result_label.grid(row=4, column=1)

    def add(self):
        try:
            num1 = float(self.number1_input.get())
            num2 = float(self.number2_input.get())
            result = num1 + num2
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")

    def subtract(self):
        try:
            num1 = float(self.number1_input.get())
            num2 = float(self.number2_input.get())
            result = num1 - num2
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")

    def multiply(self):
        try:
            num1 = float(self.number1_input.get())
            num2 = float(self.number2_input.get())
            result = num1 * num2
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")

    def divide(self):
        try:
            num1 = float(self.number1_input.get())
            num2 = float(self.number2_input.get())
            if num2 == 0:
                self.result_label.config(text="Cannot divide by zero")
            else:
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")

    def modulo(self):
        try:
            num1 = float(self.number1_input.get())
            num2 = float(self.number2_input.get())
            if num2 == 0:
                self.result_label.config(text="Cannot divide by zero")
            else:
                result = num1 % num2
                self.result_label.config(text=f"Result: {result}")
        except ValueError:
            self.result_label.config(text="Please enter valid numbers")


if __name__ == '__main__':
    root =""
