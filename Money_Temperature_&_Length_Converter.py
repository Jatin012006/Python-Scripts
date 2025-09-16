import tkinter as tk

def convert():
    input_value = e1.get()
    try:
        value = float(input_value)
    except ValueError:
        l3.config(text = "Please enter a valid number")
        return

    conversion_type = convertion.get()
    if conversion_type == "Rupees to Dollars":
        result = value * 0.012
        l3.config(text=f"{value} Rupees = {result:.2f} Dollars")
    elif conversion_type == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        l3.config(text=f"{value} °C = {result:.2f} °F")
    elif conversion_type == "Inches to Feet":
        result = value / 12
        l3.config(text=f"{value} Inches = {result:.2f} Feet")
    else:
        l3.config(text="Select a valid conversion type")

window = tk.Tk()
window.title("Unit Converter")
window.geometry("600x400")

l1 = tk.Label(window, text = "Enter value")
l1.pack()

e1 = tk.Entry(window)
e1.pack()

l2 = tk.Label(window, text = "Please select the convertion type")
l2.pack()

convertion = tk.StringVar(value = "Rupees to Dollars")
r1 = tk.Radiobutton(window, text = "Rupees to Dollars", variable = convertion, value = "Rupees to Dollars")
r1.pack()
r2 = tk.Radiobutton(window, text = "Celsius to Fahrenheit", variable = convertion, value = "Celsius to Fahrenheit")
r2.pack()
r3 = tk.Radiobutton(window, text = "Inches to Feet", variable = convertion, value = "Inches to Feet")
r3.pack()

b1 = tk.Button(window, text = "Convert", command = convert)
b1.pack()

l3 = tk.Label(window, text = "")
l3.pack()

window.mainloop()