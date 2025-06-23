import tkinter as tk
from tkinter import messagebox

def reverse_string():
    original = input_entry.get()
    if original.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a valid string.")
        return
    reversed_str = original[::-1]
    result_label.config(text=f"Reversed: {reversed_str}")

def clear():
    input_entry.delete(0, tk.END)
    result_label.config(text="")

# Create GUI window
root = tk.Tk()
root.title("String Reversal Tool")
root.geometry("400x250")
root.configure(bg="#f0f8ff")

# Heading
tk.Label(root, text="String Reverse", font=("Segoe UI", 16, "bold"), bg="#f0f8ff").pack(pady=10)

# Input Field
tk.Label(root, text="Enter String:", bg="#f0f8ff", font=("Segoe UI", 11)).pack()
input_entry = tk.Entry(root, width=40, font=("Segoe UI", 11))
input_entry.pack(pady=5)

# Reverse Button
tk.Button(root, text="Reverse", font=("Segoe UI", 10), command=reverse_string).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#f0f8ff", fg="green")
result_label.pack()

# Clear Button
tk.Button(root, text="Clear", command=clear, font=("Segoe UI", 10)).pack(pady=5)

# Run app
root.mainloop()