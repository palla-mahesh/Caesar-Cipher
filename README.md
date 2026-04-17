# Caesar-Cipher
# 🔐 Advanced Caesar Cipher GUI using Tkinter

## 📌 Project Description

This project is a **GUI-based Caesar Cipher tool** developed using **Python and Tkinter**. It allows users to perform **encryption, decryption, and brute-force attacks** on text using a shift-based substitution technique.

The application is designed with a simple and interactive graphical interface, making it suitable for **students, cybersecurity beginners, and educational demonstrations**.

## 🚀 Features

* 🔐 Encrypt text using Caesar Cipher
* 🔓 Decrypt encrypted text
* 🔍 Brute-force attack (tries all 26 shifts)
* 📋 Copy output to clipboard
* 🧹 Clear input and output fields
* ⚠️ Input validation with error messages
* 🎨 User-friendly GUI interface

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter (Standard Python GUI Library)**

## 📂 File Structure

```
project-folder/
│
├── caesar_gui.py     # Main application file
├── README.md         # Documentation

## ▶️ How to Run

### 1️⃣ Install Python

Download Python from: [https://www.python.org](https://www.python.org)

✔ Make sure to check **"Add Python to PATH"**

### 2️⃣ Run the Program

Open terminal / command prompt and run:

python caesar_gui.py

## 🧠 Working Principle

The Caesar Cipher shifts each alphabet character by a fixed number (shift value).

### Example:

```
Plain Text : HELLO
Shift      : 3
Encrypted  : KHOOR
```

### Logic Used:

* `ord()` → Convert character to ASCII
* `chr()` → Convert ASCII to character
* `% 26` → Keeps characters within alphabet range
* Supports:

  * Uppercase letters
  * Lowercase letters
  * Special characters (unchanged)

## 🔍 Brute Force Feature

The brute-force option automatically tries all possible 26 shifts and displays all results.
This helps demonstrate how weak encryption methods can be broken.

## 🖥️ GUI Components

* Text area for input
* Entry field for shift value
* Buttons:

  * Encrypt
  * Decrypt
  * Brute Force
  * Copy
  * Clear
* Output display area

## 🎯 Applications

* Cryptography learning
* Cybersecurity demonstrations
* Academic projects
* Hackathon submissions
  
## ⚠️ Limitations

* Works only with basic Caesar Cipher
* Not suitable for real-world secure encryption

## 🔮 Future Enhancements

* File encryption support
* Password-based encryption
* Advanced ciphers (AES, RSA)
* Modern UI using CustomTkinter
## 🧾 requirements.txt
# Tkinter is included with standard Python installation
# No external dependencies required
## ✅ Conclusion

This project successfully demonstrates the implementation of the Caesar Cipher using a graphical user interface in Python. It not only performs encryption and decryption but also highlights security weaknesses through the brute-force feature. The application is simple, interactive, and educational, making it a great starting point for understanding classical cryptography and basic cybersecurity concepts. With further enhancements, it can be extended into more advanced encryption systems.
## 👨‍💻 Author

**PALLA VENKATA MAHESH**
GitHub: [https://github.com/palla-mahesh](https://github.com/palla-mahesh)
## 📜 License

This project is licensed under the **MIT License**.
⭐ If you found this project useful, please give it a **star**!
code
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
