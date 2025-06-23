import tkinter as tk
from tkinter import messagebox

def is_palindrome(text):
    # Remove spaces and convert to lowercase
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

class PalindromeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Palindrome Checker")
        self.master.geometry("400x250")
        self.master.config(bg="#f0f8ff")

        self.label = tk.Label(master, text="🔁 Enter a word or phrase:", font=("Segoe UI", 14), bg="#f0f8ff")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Segoe UI", 14), justify="center")
        self.entry.pack(pady=5)

        self.check_button = tk.Button(master, text="Check", command=self.check_palindrome, font=("Segoe UI", 12), bg="#4caf50", fg="white")
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Segoe UI", 12), bg="#f0f8ff")
        self.result_label.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset, font=("Segoe UI", 10), bg="#f44336", fg="white")
        self.reset_button.pack(pady=5)

    def check_palindrome(self):
        user_input = self.entry.get().strip()
        if not user_input:
            self.result_label.config(text="⚠ Please enter a word or phrase.", fg="red")
            return
        if is_palindrome(user_input):
            self.result_label.config(text="✅ It's a palindrome!", fg="green")
        else:
            self.result_label.config(text="❌ Not a palindrome.", fg="orange")

    def reset(self):
        self.entry.delete(0, tk.END)
        self.result_label.config(text="", fg="black")

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PalindromeApp(root)
    root.mainloop()