import customtkinter as ctk
import re
import random
import string

def generate_random_pass():
    letters = random.sample(string.ascii_letters, 4)  # 4 letters
    digits = random.sample(string.digits, 2)  # 2 digits
    symbols = random.sample("!@#$%^&*()", 1)  # 1 special character
    extra_letters = random.sample(string.ascii_letters, 5)  # 5 more letters

    password_list = letters + digits + symbols + extra_letters  # Combine all
    random.shuffle(password_list)  # Shuffle for randomness
    password = ''.join(password_list)

    entry.delete(0, "end")
    entry.insert(0, password)
    on_typing()  # Update progress bar and label


def check_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):  # Uppercase
        strength += 1
    if re.search(r"\d", password):  # Digits
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  # Special Characters
        strength += 1

    return strength / 4  # Normalize to 0.0 - 1.0


def on_typing(event=None):
    password = entry.get()
    strength = check_strength(password)
    progress.set(strength)

    # Change color based on strength
    colors = ["red", "orange", "yellow", "green"]
    labels = ["Weak", "Fair", "Good", "Strong"]
    index = int(strength * 3)  # Convert 0.0-1.0 to 0-3 index

    progress.configure(progress_color=colors[index])
    strength_label.configure(text=labels[index], text_color=colors[index])


# GUI Setup
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Password Strength Check")
root.geometry("400x500")

entry = ctk.CTkEntry(root, placeholder_text="Enter password here...", height=50, font=("Courier New", 15), width=200)
entry.pack(padx=100, pady=50)
entry.bind("<KeyRelease>", on_typing)

progress = ctk.CTkProgressBar(root, progress_color="red")
progress.pack(pady=20)
progress.set(0)  # Initial state

strength_label = ctk.CTkLabel(root, text="Weak", font=("Arial", 20, "bold"), fg_color="transparent", text_color="red")
strength_label.pack(pady=20)

random_button = ctk.CTkButton(root, text="Generate Random", height=50, width=200, font=("Arial", 15, "bold"),command=generate_random_pass)
random_button.pack(pady=20)

root.mainloop()
