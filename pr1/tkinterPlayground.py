
import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("300x200")

label_output = tk.Label(root, text="")

text_calculation = tk.Text(root, height=2, width = 10)

def addition():
    text_calculation.config(text=text_calculation.get(1.0,tk.END)+"+")

def function():
    label_output.config(text="Hello!")
    pass
button_hello = tk.Button(root, text="Hi", command=function)

button_add = tk.Button(root, text="+", command=addition)

text_calculation.pack(pady=20)


button_hello.pack(pady=10,padx=10)
label_output.pack(pady=20)





root.mainloop()

