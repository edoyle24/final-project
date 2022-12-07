import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Final Project")
root.configure(bg="blue")

label = tk.Label(root, text="Please pick a team", font=('arial', 18))
label.pack(padx=20, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)

btn1 = tk.Button(buttonframe, text="Maple Leafs", font=('arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()
