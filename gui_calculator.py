import tkinter as tk

from calculator import add, subtract, multiply, divide


def calculate(operation):

    try:

        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
           result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        label_result.config(text= "Result: " + str(result))

    except ValueError:

        label_result.config(text="Invalid input. Please enter numbers only, not letters or words.")

def clear_inputs():

    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ---")

# Create the main application window

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x350")

# Create and place the input fields, buttons, and result label

label_title = tk.Label(window, text = "Simple Calculator", font = ("Arial", 16, "bold"))

label_num1 = tk.Label(window, text="Enter First Number:")
entry_num1 = tk.Entry(window) # A text box for the user to type in

label_num2 = tk.Label(window, text="Enter Second Number:")
entry_num2 = tk.Entry(window)

# Buttons: The 'command' tells the button what function to run when clicked!
# lambda to pass the specific math symbol to our calculate function.
btn_add = tk.Button(window, text="Add (+)", command=lambda: calculate('+'), width=15)
btn_sub = tk.Button(window, text="Subtract (-)", command=lambda: calculate('-'), width=15)
btn_mul = tk.Button(window, text="Multiply (*)", command=lambda: calculate('*'), width=15)
btn_div = tk.Button(window, text="Divide (/)", command=lambda: calculate('/'), width=15)

btn_clear = tk.Button(window, text="Clear", command=clear_inputs, width=15, fg="red")

label_result = tk.Label(window, text="Result: ---", font=("Arial", 12, "bold"), fg="blue")

# Pack the widgets into the window (you can also use .grid() or .place() for more control over layout)
label_title.pack(pady=10)

label_num1.pack()
entry_num1.pack(pady=5)

label_num2.pack()
entry_num2.pack(pady=5)

btn_add.pack()
btn_sub.pack()
btn_mul.pack()
btn_div.pack()
btn_clear.pack(pady=10)

label_result.pack(pady=10)

# 4. Start the application!
window.mainloop()