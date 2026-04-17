import tkinter as tk
from tkinter import messagebox

# ---------------- Cipher Functions ---------------- #
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(text):
    results = ""
    for i in range(26):
        results += f"Shift {i}: {decrypt(text, i)}\n"
    return results


# ---------------- GUI Functions ---------------- #
def perform_encrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_entry.get()

    if not text or not shift.isdigit():
        messagebox.showerror("Error", "Enter valid text and numeric shift!")
        return

    result = encrypt(text, int(shift))
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


def perform_decrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = shift_entry.get()

    if not text or not shift.isdigit():
        messagebox.showerror("Error", "Enter valid text and numeric shift!")
        return

    result = decrypt(text, int(shift))
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


def perform_bruteforce():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Error", "Enter text to analyze!")
        return

    result = brute_force(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)


def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Output copied to clipboard!")


def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)


# ---------------- GUI Design ---------------- #
root = tk.Tk()
root.title("Advanced Caesar Cipher Tool")
root.geometry("600x550")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Caesar Cipher GUI", font=("Arial", 20, "bold"), bg="#1e1e2f", fg="white")
title.pack(pady=10)

# Input
tk.Label(root, text="Enter Text:", bg="#1e1e2f", fg="white").pack()
input_text = tk.Text(root, height=5, width=60)
input_text.pack(pady=5)

# Shift
tk.Label(root, text="Shift Value:", bg="#1e1e2f", fg="white").pack()
shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

# Buttons
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Button(frame, text="Encrypt", command=perform_encrypt, bg="#4CAF50", fg="white", width=12).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Decrypt", command=perform_decrypt, bg="#2196F3", fg="white", width=12).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Brute Force", command=perform_bruteforce, bg="#ff9800", fg="white", width=12).grid(row=0, column=2, padx=5)

# Output
tk.Label(root, text="Output:", bg="#1e1e2f", fg="white").pack()
output_text = tk.Text(root, height=10, width=60)
output_text.pack(pady=5)

# Bottom Buttons
bottom_frame = tk.Frame(root, bg="#1e1e2f")
bottom_frame.pack(pady=10)

tk.Button(bottom_frame, text="Copy", command=copy_output, bg="#9c27b0", fg="white", width=10).grid(row=0, column=0, padx=5)
tk.Button(bottom_frame, text="Clear", command=clear_all, bg="#f44336", fg="white", width=10).grid(row=0, column=1, padx=5)

# Run App
root.mainloop()
