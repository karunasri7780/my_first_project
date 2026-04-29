import tkinter as tk
root=tk.Tk()
def test():
    print("hello")
tk.Button(root,text="click me",command=test).pack()
root.mainloop()    