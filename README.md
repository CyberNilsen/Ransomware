# Ransomware

A Python-based educational tool designed to demonstrate how ransomware works in a controlled environment. This project is created strictly for cybersecurity education and Python learning purposes.

![Ransomware](https://github.com/user-attachments/assets/d11d825f-a5ec-40d0-a28a-96716b100c57)


## ⚠️ EDUCATIONAL PURPOSE ONLY ⚠️

This software is designed **ONLY** for educational purposes to understand:
- Encryption/decryption mechanisms
- Python programming concepts
- GUI development with Tkinter
- Cybersecurity threats and protections

**NEVER** use this code for malicious purposes. Unauthorized encryption of files is illegal and unethical.

## Features

- **File Encryption/Decryption**: Simulates how ransomware encrypts and decrypts files
- **Interactive GUI**: Recreates the look and feel of ransomware interfaces
- **Safe Environment**: Includes built-in protection mechanisms (predefined password)
- **Educational Comments**: Code is thoroughly commented to explain functionality

## Technologies Used

- **Python**: Core programming language
- **Tkinter**: GUI framework
- **PIL (Pillow)**: Image processing
- **Cryptography**: Fernet symmetric encryption
- **Hashlib**: Password hashing

## Installation

1. Clone this repository
bash
```
git clone https://github.com/username/RansomwareSimulator.git
```
2. Install Required Dependencies
Open Command Prompt or PowerShell and run:  
bash
```
pip install cryptography pillow
```
3. Run the ransomware  
bash
```
python ransomware_simulator.py
```
⚠️ Run only in test folders with non-important files!

## 🔐 How It Works

-Encrypts .txt, .png, .jpg, and other common file types in a selected directory
-Uses Fernet symmetric encryption
-GUI displays a "ransom note" interface with a decryption field
-Built-in key ensures all files can be safely restored during simulation

