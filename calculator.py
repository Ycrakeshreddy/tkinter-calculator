import tkinter as tk

def calculator(op):
    try:
        value_1 = float(entry1.get())
        value_2 = float(entry2.get())

        if op == "+":
            result = value_1+value_2
        elif op == "-":
            result = value_1-value_2
        elif op == "*":
            result = value_1 *value_2
        elif op == "/":
            result = value_1 /value_2
        else:
            result = "invalid operations !"
        return_result.delete(0,tk.END)
        return_result.insert(0,str(result))
    except:
        return_result.delete(0,tk.END)
        return_result.insert(0,"error")


root = tk.Tk()
root.title("Calculator")
root.geometry("800x800")

tk.Label(root,text="Type value 1 →→→ : ").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root,text="Type value 2  →→→ : ").pack()
entry2 = tk.Entry(root)
entry2.pack()

btn_frame  = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame,text="+",command= lambda : calculator('+')).pack()
tk.Button(btn_frame,text="-",command= lambda : calculator('-')).pack()
tk.Button(btn_frame,text="*",command= lambda : calculator('*')).pack()
tk.Button(btn_frame,text="/",command= lambda : calculator('/')).pack()

tk.Label(root,text = "Result  :   ").pack()
return_result = tk.Entry(root)
return_result.pack()
root.mainloop()
