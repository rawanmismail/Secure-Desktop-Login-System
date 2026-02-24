import tkinter as tk
from tkinter import ttk
import time

# ---------------- CONFIG ----------------
CORRECT_PASSWORD = "12345"
MAX_ATTEMPTS = 3
BLOCK_TIME = 10
SESSION_TIMEOUT = 30  # Auto-lock after 30s of inactivity

failed_attempts = 0
blocked_until = 0
last_activity_time = time.time()

# ---------------- FUNCTIONS ----------------
def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        show_btn.config(text="Show")
    else:
        password_entry.config(show="")
        show_btn.config(text="Hide")

def hover_on(e):
    login_btn.config(bg="#005ea6")

def hover_off(e):
    login_btn.config(bg="#0078D7")

def update_attempt_indicator():
    remaining = MAX_ATTEMPTS - failed_attempts

    if remaining == 3:
        color = "green"
    elif remaining == 2:
        color = "orange"
    else:
        color = "red"

    attempts_label.config(
        text=f"Attempts Remaining: {'● '*remaining}{'○ '*failed_attempts}",
        fg=color
    )

def login_success_animation():
    system_status.config(text="System Status: Unlocked", fg="green")
    progress["value"] = 0
    animate_loading()

def animate_loading():
    if progress["value"] < 100:
        progress["value"] += 5
        status_label.config(text="Loading Desktop...")
        window.after(80, animate_loading)
    else:
        status_label.config(text="Welcome User")

def countdown():
    remaining = int(blocked_until - time.time())

    if remaining > 0:
        system_status.config(text="System Status: Locked", fg="red")
        status_label.config(text=f"System locked for {remaining} seconds")
        progress["value"] = (BLOCK_TIME - remaining) / BLOCK_TIME * 100
        window.after(1000, countdown)
    else:
        progress["value"] = 0
        system_status.config(text="System Status: Secure", fg="green")
        status_label.config(text="Please enter your password")

def check_password():
    global failed_attempts, blocked_until

    if time.time() < blocked_until:
        countdown()
        return

    if password_entry.get() == CORRECT_PASSWORD:
        failed_attempts = 0
        update_attempt_indicator()
        login_success_animation()
    else:
        failed_attempts += 1
        system_status.config(text="System Status: Warning", fg="orange")
        status_label.config(text="Incorrect password")
        update_attempt_indicator()

        if failed_attempts >= MAX_ATTEMPTS:
            blocked_until = time.time() + BLOCK_TIME
            failed_attempts = 0
            update_attempt_indicator()
            countdown()

# ---------------- SESSION TIMEOUT ----------------
def reset_activity(event=None):
    global last_activity_time
    last_activity_time = time.time()
    # If system was auto-locked, show secure status but require password
    if system_status.cget("text") == "System Status: Locked":
        system_status.config(text="System Status: Secure", fg="green")
        status_label.config(text="Please enter your password")
        progress["value"] = 0

def check_inactivity():
    global blocked_until
    inactive_time = time.time() - last_activity_time
    if inactive_time >= SESSION_TIMEOUT:
        system_status.config(text="System Status: Locked", fg="red")
        status_label.config(text="System locked due to inactivity")
        progress["value"] = 0
        blocked_until = time.time() + BLOCK_TIME
        countdown()
    else:
        window.after(1000, check_inactivity)

# ---------------- WINDOW ----------------
window = tk.Tk()
window.title("Desktop Login")
window.geometry("640x450")
window.configure(bg="#dfeaf6")

# ---------------- GLOW EFFECT ----------------
glow = tk.Frame(window, bg="#cfe0ff", padx=6, pady=6)
glow.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- LOGIN CARD ----------------
main_frame = tk.Frame(glow, bg="white", padx=50, pady=35)
main_frame.pack()

# ---------------- PROFILE SECTION ----------------
profile_icon = tk.Label(main_frame, text="👤", font=("Segoe UI", 40), bg="white")
profile_icon.pack()

username_label = tk.Label(
    main_frame,
    text="User",
    font=("Segoe UI", 14, "bold"),
    bg="white"
)
username_label.pack()

subtitle = tk.Label(
    main_frame,
    text="Secure System Login",
    font=("Segoe UI", 10),
    fg="gray",
    bg="white"
)
subtitle.pack(pady=(0, 10))

# ---------------- SYSTEM STATUS ----------------
system_status = tk.Label(
    main_frame,
    text="System Status: Secure",
    font=("Segoe UI", 10, "bold"),
    fg="green",
    bg="white"
)
system_status.pack(pady=5)

# ---------------- LOCK ICON ----------------
lock_icon = tk.Label(main_frame, text="🔒", font=("Segoe UI", 26), bg="white")
lock_icon.pack()

# ---------------- PASSWORD ----------------
password_entry = tk.Entry(
    main_frame,
    show="*",
    font=("Segoe UI", 12),
    width=26,
    justify="center"
)
password_entry.pack(pady=10)
password_entry.focus()

show_btn = tk.Button(
    main_frame,
    text="Show",
    relief="flat",
    command=toggle_password
)
show_btn.pack(pady=5)

# ---------------- LOGIN BUTTON ----------------
login_btn = tk.Button(
    main_frame,
    text="Login",
    font=("Segoe UI", 11, "bold"),
    width=24,
    bg="#0078D7",
    fg="white",
    relief="flat",
    command=check_password
)
login_btn.pack(pady=15)

login_btn.bind("<Enter>", hover_on)
login_btn.bind("<Leave>", hover_off)

# ---------------- ATTEMPTS ----------------
attempts_label = tk.Label(
    main_frame,
    font=("Segoe UI", 11, "bold"),
    bg="white"
)
attempts_label.pack(pady=5)

# ---------------- STATUS MESSAGE ----------------
status_label = tk.Label(
    main_frame,
    text="Please enter your password",
    font=("Segoe UI", 10),
    bg="white"
)
status_label.pack(pady=5)

# ---------------- PROGRESS BAR ----------------
progress = ttk.Progressbar(main_frame, length=220)
progress.pack(pady=10)

update_attempt_indicator()

# ---------------- ACTIVITY BINDINGS ----------------
window.bind_all("<Key>", reset_activity)
window.bind_all("<Motion>", reset_activity)
window.bind_all("<Button>", reset_activity)
window.after(1000, check_inactivity)

window.mainloop()
