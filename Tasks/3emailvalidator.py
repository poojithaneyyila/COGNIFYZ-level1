import tkinter as tk
from tkinter import messagebox
import re

def is_valid_email(email):
    # Regular expression for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_email():
    email = entry.get()
    if is_valid_email(email):
        result_label.config(text="✅ Valid Email Address", fg="green")
    else:
        result_label.config(text="❌ Invalid Email Address", fg="red")

def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x220")
root.config(bg="#e6f2ff")

tk.Label(root, text="Email Validator", font=("Segoe UI", 16, "bold"), bg="#e6f2ff").pack(pady=10)

tk.Label(root, text="Enter your email:", bg="#e6f2ff", font=("Segoe UI", 11)).pack()
entry = tk.Entry(root, width=40, font=("Segoe UI", 11))
entry.pack(pady=5)

tk.Button(root, text="Validate", command=validate_email, font=("Segoe UI", 10)).pack(pady=8)
result_label = tk.Label(root, text="", font=("Segoe UI", 12), bg="#e6f2ff")
result_label.pack()

tk.Button(root, text="Clear", command=clear_input, font=("Segoe UI", 10)).pack(pady=5)

root.mainloop()