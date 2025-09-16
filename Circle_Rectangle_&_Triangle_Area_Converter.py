import tkinter as tk
import math

def calculate_area():
    s = shape.get()
    try:
        if s == "Circle":
            radius = float(e1.get())
            area = math.pi * radius ** 2
            l4.config(text=f"Area of Circle: {area:.2f}")

        elif s == "Rectangle":
            length = float(e1.get())
            width = float(e2.get())
            area = length * width
            l4.config(text=f"Area of Rectangle: {area:.2f}")

        elif s == "Triangle":
            base = float(e1.get())
            height = float(e2.get())
            area = 0.5 * base * height
            l4.config(text=f"Area of Triangle: {area:.2f}")

        else:
            l4.config(text="Please select a valid shape.")

    except ValueError:
        l4.config(text="Please enter valid numeric dimensions.")

window = tk.Tk()
window.title("Geometry Area Calculator")
window.geometry("600x400")

l1 = tk.Label(window, text = "Select Shape")
l1.pack()

shape = tk.StringVar(value = "Circle")
r1 = tk.Radiobutton(window, text = "Circle", variable = shape, value = "Circle")
r1.pack()
r2 = tk.Radiobutton(window, text = "Rectangle", variable = shape, value = "Rectangle")
r2.pack()
r3 = tk.Radiobutton(window, text = "Triangle", variable = shape, value = "Triangle")
r3.pack()

l2 = tk.Label(window, text="")
l2.pack()
e1 = tk.Entry(window)
e1.pack()

l3 = tk.Label(window, text="")
l3.pack()
e2 = tk.Entry(window)
e2.pack()

b1 = tk.Button(window, text = "Calculate Area", command = calculate_area)
b1.pack()

l4 = tk.Label(window, text="")
l4.pack()

window.mainloop()