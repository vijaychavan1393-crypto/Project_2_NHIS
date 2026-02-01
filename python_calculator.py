import tkinter as tk

reset_display = False

def click(event):
    global reset_display
    button_text = event.widget["text"]
    current = entry.get()

    if button_text == "c":
        entry.delete(0, tk.END)

    elif button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(0, result)
            reset_display = True
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")

    else:
        if reset_display:
            entry.delete(0, tk.END)
            reset_display = False
        entry.insert(tk.END, button_text)


root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#F0F0F0")

entry = tk.Entry(root, bd=5, font=('Arial', 20),
                 justify='right', width=16)
entry.pack(pady=10)

btnFrame = tk.Frame(root)
btnFrame.pack(padx=10, pady=10)

buttons = [
    ['c', '(', ')', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['.', '0', '%', '=']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = tk.Button(
            btnFrame,
            text=buttons[i][j],
            font=('Arial', 16),
            width=3,
            height=1
        )
        btn.grid(row=i, column=j, padx=10, pady=10)
        btn.bind('<Button-1>', click)

root.mainloop()

