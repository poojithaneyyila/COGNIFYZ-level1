import tkinter as tk
from tkinter import messagebox, ttk

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius to Fahrenheit":
            converted = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {converted:.2f}°F")
        elif unit == "Fahrenheit to Celsius":
            converted = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {converted:.2f}°C")
        else:
            result_label.config(text="Please select a valid unit")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

def clear_fields():
    entry_temp.delete(0, tk.END)
    combo_unit.set('')
    result_label.config(text='')

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.config(bg="#f2f2f2")

# Styling
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10))
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TCombobox", font=("Segoe UI", 10))

# Heading
tk.Label(root, text="Temperature Converter", font=("Segoe UI", 16, "bold"), bg="#f2f2f2").pack(pady=10)

# Input Field
tk.Label(root, text="Enter Temperature:", bg="#f2f2f2").pack()
entry_temp = ttk.Entry(root, width=25)
entry_temp.pack(pady=5)

# Unit Selection
tk.Label(root, text="Conversion Type:", bg="#f2f2f2").pack()
combo_unit = ttk.Combobox(root, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"], state="readonly", width=25)
combo_unit.pack(pady=5)

# Convert Button
ttk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#f2f2f2")
result_label.pack(pady=5)

# Clear & Exit Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Clear", command=clear_fields).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Exit", command=exit_app).grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()

