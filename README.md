# 🔐 CryptoEngine

**CryptoEngine** is a comprehensive, high-performance desktop application designed for classical and modern cryptography. Built with **Python** and **PyQt6**, it provides a secure environment for exploring, implementing, and challenging your knowledge of encryption algorithms.

---

## 🚀 Features

### 🛡️ Secure Authentication
- **User Registration & Login:** Robust user management system.
- **Email Verification:** Automated SMTP-based verification to ensure account authenticity.
- **Data Encryption:** User credentials are encrypted using the **Fernet** (symmetric encryption) algorithm.
- **Security Alerts:** Intelligent UI prompts with security tips for passwords, emails, and usernames.

### 🧩 Cryptographic Suite
A collection of diverse cipher algorithms with both encryption and decryption capabilities:
- **Caesar Cipher:** Classic shift-based substitution.
- **Playfair Cipher:** Digraph-based substitution using a 5x5 key matrix.
- **Hill Cipher:** Matrix-based polyalphabetic substitution.
- **RSA (Asymmetric):** Public/Private key generation and secure encryption/decryption.
- **Rail Fence Cipher:** Geometric transposition encryption.
- **ROT13:** Simple alphabetic rotation (13 shifts).
- **Substitution Cipher:** Customizable monoalphabetic substitution.

### 🛠️ Advanced Tools
- **File Integration:** Directly import `.txt` files for processing and export results.
- **Key Generation:** Built-in RSA key generator for p and q primes.
- **Crypto Challenge:** An interactive gamified system to test your cryptographic skills.
- **Modern UI:** Sleek, frameless window design with translucent backgrounds and custom gradients.

---

## 🏗️ Project Architecture

```text
CryptoEngine/
├── main.py                # Application entry point & Auth logic
├── encryption_key.key     # Master key for local data encryption
├── users.csv              # Encrypted user database
└── src/
    ├── ciphers/           # Individual Cipher implementations
    │   ├── ceaser.py
    │   ├── Hill.py
    │   ├── playfair.py
    │   ├── QUAD.py        # RSA Implementation
    │   ├── ROOT13.py
    │   └── substtt.py
    ├── core/              # Main UI screens & Logic
    │   ├── mainnn.py      # Home screen management
    │   ├── challenge.py   # Crypto Challenge module
    │   └── HOME.py        # Home screen UI
    ├── auth/              # Authentication modules
    ├── resources/         # QRC assets and images
    └── ui/
        └── designer/      # Original .ui design files
```

---

## 🛠️ Tech Stack

- **Language:** [Python 3.x](https://www.python.org/)
- **GUI Framework:** [PyQt6](https://www.riverbankcomputing.com/software/pyqt/)
- **Encryption:** [Cryptography (Fernet)](https://cryptography.io/en/latest/fernet/)
- **Networking:** `smtplib` for Email Verification
- **Storage:** CSV-based local data management

---

## ⚡ Quick Start

### 1️⃣ Prerequisites
Ensure you have Python 3.10+ installed.

### 2️⃣ Install Dependencies
```bash
pip install PyQt6 cryptography
```

### 3️⃣ Configuration
Update the `EMAIL_ADDRESS` and `EMAIL_PASSWORD` in `main.py` if you wish to use your own SMTP server for verification.
*Note: For Gmail, use an "App Password" if 2FA is enabled.*

### 4️⃣ Run the Application
```bash
python main.py
```

---

## 🎮 How to Use

1. **Welcome Screen:** Start by exploring the **Crypto Challenge** or move to the login.
2. **Registration:** Create a new account. Check your email for the 6-digit verification code.
3. **Login:** Authenticate with your secure credentials.
4. **Dashboard:** Select a cipher from the main menu.
5. **Encrypt/Decrypt:** 
   - Input text manually or **Import** a file.
   - Enter the required **Key**.
   - Click **CONVERT** to see the magic happen.
   - **Download** the result as a `.txt` file.

---

## 🔒 Security Note
This project is intended for educational purposes. While it implements RSA and Fernet, the classical ciphers (Caesar, Playfair, etc.) are inherently insecure by modern standards and are included for historical and educational exploration.

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

---

*Developed with ❤️ for the world of Cryptography.*
