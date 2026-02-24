# 🔒 Secure Desktop Login System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) 
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)

A **Python-based desktop login system** designed for security and usability, featuring password authentication, session timeout, and auto-lock functionality. 

---

## ✨ Features

- 🔑 **Password Authentication** – Unlock the system with a predefined password.  
- 🚫 **Login Attempts Limit** – Maximum of 3 failed attempts before temporary lockout.  
- ⏱ **Session Timeout & Auto-Lock** – Locks automatically after 30 seconds of inactivity.  
- 👀 **Password Visibility Toggle** – Easily show or hide the entered password.  
- 📊 **Interactive Progress Bar** – Visual feedback during login and lockout periods.  
- 🖥 **User-Friendly Interface** – Clean and intuitive layout with clear status indicators.

---

## 🛠 Requirements

- Python 3.7+  
- No additional libraries required

---

## 🚀 Getting Started
1. **Clone the repository**:

```bash
git clone https://github.com/your-username/secure-desktop-login.git
cd secure-desktop-login

2. **Run The Program**:
```bash
python login_system.py

3. Login Instructions:
Default password:
```bash
12345

Enter the password in the input field and click Login.
Click Show to toggle password visibility.

Failed Attempts Handling:

You have a maximum of 3 attempts to enter the correct password.

After 3 failed attempts, the system locks for 10 seconds.

The progress bar shows the remaining lock time.

Session Timeout / Auto-Lock:

If there is no mouse or keyboard activity for 30 seconds, the system will auto-lock.

Move your mouse or press any key to reset the inactivity timer.

Post-Lock / Auto-Lock:

After the system locks, you must enter the correct password to unlock it again.

Progress bar indicates lockout period during auto-lock or failed attempts.
