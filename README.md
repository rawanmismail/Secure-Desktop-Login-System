# 🔒 Secure Desktop Login System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) 
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)

A **Python-based desktop login system** designed for security and usability, featuring password authentication, session timeout, and auto-lock functionality. 

---

##  Features

- 🔑 **Password Authentication** – Unlock the system with a predefined password.  
- 🚫 **Login Attempts Limit** – Maximum of 3 failed attempts before temporary lockout.  
- ⏱ **Session Timeout & Auto-Lock** – Locks automatically after 30 seconds of inactivity.  
- 👀 **Password Visibility Toggle** – Easily show or hide the entered password.  
- 📊 **Interactive Progress Bar** – Visual feedback during login and lockout periods.  
- 🖥 **User-Friendly Interface** – Clean and intuitive layout with clear status indicators.

---

##  Requirements

- Python 3.7+  
- No additional libraries required

---

##  How to Run & Use the Project
Follow these steps to run and use the Secure Desktop Login System:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/secure-desktop-login.git
cd secure-desktop-login
````

### 2. Run the Program

```bash
python login_system.py
```

### Login Instructions

* **Default password:**

  ```text
  12345
  ```
* Enter the password in the input field and click **Login**.
* Click **Show** to toggle password visibility if needed.

### Handling Failed Attempts

* You have a maximum of **3 attempts** to enter the correct password.
* After 3 failed attempts, the system will **lock for 10 seconds**.
* The **progress bar** displays the remaining lockout time.

### Session Timeout / Auto-Lock

* If there is **no mouse or keyboard activity for 30 seconds**, the system will **automatically lock**.
* Move your mouse or press any key to **reset the inactivity timer**.

### Post-Lock / Auto-Lock

* After the system locks (either due to failed attempts or inactivity), you must **enter the correct password** to unlock it again.
* The **progress bar** will show the remaining lock time during this period.

```
---
