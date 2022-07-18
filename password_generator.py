import random
import tkinter as tk
from tkinter import font


root = tk.Tk()
font.families()
root.title("Password Generator")
root.resizable(False, False)

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "~`! @#$%^&*()_-+={[}]|\:;"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 30
amount = 1

def genPass():

    for widget in frame.winfo_children():
        widget.destroy()

    for x in range(amount):
        password = "".join(random.sample(all, length))
        
    label = tk.Label(frame, text=password, bg="#78BDA2", fg = "black", font=("Comic Sans MS",10), padx=10, pady=12)
    label.pack()

canvas = tk.Canvas(root, height=100, width=300, bg="#4D7A69", )
canvas.pack()

frame = tk.Frame (root, bg="#78BDA2")
frame.place(relwidth=0.83, relheight=0.3, relx=.5, rely=.35, anchor="center")    

genPassButton = tk.Button(root, text="Generate Password", width=29, pady = 5, fg = "black", bg="#78BDA2", font=("Comic Sans MS", 12), command=genPass)
genPassButton.pack()

root.mainloop()