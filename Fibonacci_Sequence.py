import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fib(n-1) + calculate_fib(n-2)

def calculate_fib_sequence(n1, n2):
    if n1 <= 0:
        n1 = 1
    if n2 <= 0:
        n2 = 1
    if n1 > n2:
        n1, n2 = n2, n1
    fib_sequence = []
    for i in range(n1, n2 + 1):
        fib_sequence.append(calculate_fib(i))
    return fib_sequence

def calculate_one_number():
    try:
        n = int(entry_n.get())
        answer = calculate_fib(n)
        answer_label.config(text=f"Answer: F{n} = {answer}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

def calculate_sequence():
    try:
        n1 = int(entry_n1.get())
        n2 = int(entry_n2.get())
        fib_sequence = calculate_fib_sequence(n1, n2)
        answer_label.config(text=f"Answer:\n{fib_sequence}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

def clear_fields():
    entry_n.delete(0, tk.END)
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    answer_label.config(text="Answer:")

# Create main window
window = tk.Tk()
window.title("Fibonacci Number Generator")
window.geometry("400x250")

# Create heading label
heading_label = tk.Label(window, text="Fibonacci Number Generator", font=("Arial", 16, "bold"), bg="red", fg="white", width=30, height=1)
heading_label.pack(pady=10)

# Create generate dropdown
generate_var = tk.StringVar(window)
generate_var.set("one Number")
generate_dropdown = ttk.Combobox(window, textvariable=generate_var, values=["one Number", "a Sequence"], state="readonly")
generate_dropdown.pack(pady=5)

# Create frame for input fields
input_frame = tk.Frame(window)
input_frame.pack(pady=5)

# Create label and entry for one number
label_n = tk.Label(input_frame, text="F_n for n =")
label_n.pack(side=tk.LEFT)
entry_n = tk.Entry(input_frame, width=5)
entry_n.pack(side=tk.LEFT, padx=5)

# Create label and entries for sequence
label_n1 = tk.Label(input_frame, text="n1")
label_n1.pack(side=tk.LEFT)
entry_n1 = tk.Entry(input_frame, width=5)
entry_n1.pack(side=tk.LEFT, padx=5)
label_to = tk.Label(input_frame, text="to")
label_to.pack(side=tk.LEFT)
entry_n2 = tk.Entry(input_frame, width=5)
entry_n2.pack(side=tk.LEFT, padx=5)

# Create answer label
answer_label = tk.Label(window, text="Answer:", font=("Arial", 12))
answer_label.pack(pady=10)

# Create frame for buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create clear and calculate buttons
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields)
calculate_button = tk.Button(button_frame, text="Calculate", command=lambda: calculate_one_number() if generate_var.get() == "one Number" else calculate_sequence())
clear_button.pack(side=tk.LEFT, padx=5)
calculate_button.pack(side=tk.LEFT, padx=5)

# Update GUI based on selection
def update_gui():
    if generate_var.get() == "one Number":
        label_n1.pack_forget()
        entry_n1.pack_forget()
        label_to.pack_forget()
        entry_n2.pack_forget()
        entry_n.pack(side=tk.LEFT, padx=5)
        calculate_button.config(command=calculate_one_number)
    else:
        label_n1.pack(side=tk.LEFT)
        entry_n1.pack(side=tk.LEFT, padx=5)
        label_to.pack(side=tk.LEFT)
        entry_n2.pack(side=tk.LEFT, padx=5)
        entry_n.pack_forget()
        calculate_button.config(command=calculate_sequence)

generate_var.trace("w", lambda *args: update_gui())

# Start main loop
window.mainloop()
