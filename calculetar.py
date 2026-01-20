from tkinter import *

# --- Functions ---
def press(key):
    entry_text.set(entry_text.get() + str(key))

def calculate():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("Error")

def clear():
    entry_text.set("")

def backspace():
    entry_text.set(entry_text.get()[:-1])

# --- Main Window ---
root = Tk()
root.title("Real World Calculator")
root.geometry("320x530")
root.resizable(False, False)
root.config(bg="#1C1C1C")

entry_text = StringVar()
entry = Entry(root, textvariable=entry_text, font=('Arial', 22), bd=10, insertwidth=2,
              width=15, borderwidth=4, relief="ridge", justify='right', bg="#2C2C2E", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# --- Helper to Create Buttons ---
def create_button(text, row, col, color="#4E4E4E"):
    Button(root, text=text, padx=20, pady=20, font=('Arial', 14),
           bg=color, fg="white", command=lambda: press(text)).grid(row=row, column=col, padx=5, pady=5)

# --- Number and Operator Buttons ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, "#FF9500"),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, "#FF9500"),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, "#FF9500"),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2, "#FF9500")
]

for b in buttons:
    if len(b) == 3:
        create_button(b[0], b[1], b[2])
    else:
        create_button(b[0], b[1], b[2], b[3])

# --- Special Buttons ---
Button(root, text="C", padx=20, pady=20, font=('Arial', 14),
       bg="#FF3B30", fg="white", command=clear).grid(row=4, column=3, padx=5, pady=5)

Button(root, text="⌫", padx=20, pady=20, font=('Arial', 14),
       bg="#5AC8FA", fg="white", command=backspace).grid(row=5, column=0, padx=5, pady=5)

Button(root, text="=", padx=20, pady=20, font=('Arial', 18, 'bold'),
       bg="#34C759", fg="white", command=calculate).grid(row=5, column=1, columnspan=3, sticky="nsew", padx=5, pady=5)

root.mainloop()
