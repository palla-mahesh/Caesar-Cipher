# 🔐 Advanced Caesar Cipher GUI using Tkinter

## 📌 Project Description

This project is a simple **Caesar Cipher GUI application** built using **Python and Tkinter**. It allows users to easily **encrypt and decrypt text** using a shift value.

The application also includes a **brute-force feature** that shows all possible decrypted outputs, helping users understand how basic encryption works and how it can be broken.

It is useful for **students, beginners, and academic projects** to learn the basics of cryptography in a simple and interactive way.

---

## 🚀 Features

* 🔐 Encrypt text using Caesar Cipher
* 🔓 Decrypt encrypted text
* 🔍 Brute-force attack (tries all 26 shifts)
* 📋 Copy output to clipboard
* 🧹 Clear input and output fields
* ⚠️ Input validation with error messages
* 🎨 User-friendly GUI interface

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter (Standard Python GUI Library)**

---

## 📂 File Structure

```
project-folder/
│
├── caesar_gui.py     # Main application file
├── README.md         # Documentation
```

---

## ▶️ How to Run

### 1️⃣ Install Python

Download Python from: [https://www.python.org](https://www.python.org)

✔ Make sure to check **"Add Python to PATH"**

---

### 2️⃣ Run the Program

Open terminal / command prompt and run:

```
python caesar_gui.py
```

---

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

---

## 🔍 Brute Force Feature

The brute-force option automatically tries all possible 26 shifts and displays all results.
This helps demonstrate how weak encryption methods can be broken.

---

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

---

## 🎯 Applications

* Cryptography learning
* Cybersecurity demonstrations
* Academic projects
* Hackathon submissions

---

## 📸 Screenshot

*Add a screenshot of your GUI here (optional)*

---

## ⚠️ Limitations

* Works only with basic Caesar Cipher
* Not suitable for real-world secure encryption

---

## 🔮 Future Enhancements

* File encryption support
* Password-based encryption
* Advanced ciphers (AES, RSA)
* Modern UI using CustomTkinter

---

## 🧾 requirements.txt

# Tkinter is included with standard Python installation
# No external dependencies required

## ✅ Conclusion

This project successfully demonstrates the implementation of the Caesar Cipher using a graphical user interface in Python. It not only performs encryption and decryption but also highlights security weaknesses through the brute-force feature. The application is simple, interactive, and educational, making it a great starting point for understanding classical cryptography and basic cybersecurity concepts. With further enhancements, it can be extended into more advanced encryption systems.[caeser.py](https://github.com/user-attachment/files/26830632/caeser.py)

## 👨‍💻 Author

**PALLA VENKATA MAHESH**
GitHub: [https://github.com/palla-mahesh](https://github.com/palla-mahesh)

---

## 📜 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, please give it a **star**!
