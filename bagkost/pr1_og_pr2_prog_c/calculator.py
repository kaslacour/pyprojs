
import tkinter as tk

# setup of tkinter window environment
window = tk.Tk()
window.title('Title of window')


a = (lambda : 2)()
print(a)


# ingredients: buttons (+) (-) (*) (^) (!), label expr

label_expr = tk.Label(master=window, text = "")

def fun(): label_expr["text"] += "+"


ops = ["+","-","*","^"]

def key_handler(event):
    # print(event.char, event.keysym, event.keycode)

    if event.char in ops:
        if event.char in ops:
            if label_expr["text"] == "" or label_expr["text"][-1] not in ops:
                label_expr["text"] += event.char    
            else:
                label_expr["text"] = label_expr["text"][:-1] + event.char
    else:
        try:
            int(event.char)
            label_expr["text"] += event.char
        except:
            pass


        
window.bind("<Key>", key_handler)

# button_add = tk.Button(master=window, text = "+", command = fun)

label_expr.grid(row = 0, column = 0)
# button_add.grid(row=1,column=0)



window.mainloop()


