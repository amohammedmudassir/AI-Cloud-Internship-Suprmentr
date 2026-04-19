# Assignment 1- 7th Feb 2026 
# Create a strong code for password authentication using python.
import re
import hashlib
import os

# 1. PASSWORD VALIDATION
def is_strong_password(password):
    """
    Checks if password meets security rules:
    - Min 8 charactersz
    - At least 1 uppercase
    - At least 1 lowercase
    - At least 1 digit
    - At least 1 special character
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*]", password):
        return False
    return True

# 2. GENERATE SALT
def generate_salt():
    """
    Generates random salt (16 bytes)
    Salt = random data added to password before hashing
    """
    return os.urandom(16).hex()

# 3. HASH PASSWORD WITH SALT
def hash_password(password, salt):
    """
    Combines password + salt and hashes using SHA-256
    """
    combined = password + salt
    return hashlib.sha256(combined.encode()).hexdigest()

# 4. SAVE USER DATA (FILE STORAGE)
def save_user(username, salt, hashed_password):
    """
    Saves user data in file:
    Format: username,salt,hashed_password
    """
    with open("users.txt", "a") as file:
        file.write(f"{username},{salt},{hashed_password}\n")


# 5. LOAD USER DATA
def load_user(username):
    """
    Reads file and returns user data if found
    """
    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_username, salt, hashed_password = line.strip().split(",")
                if stored_username == username:
                    return salt, hashed_password
    except FileNotFoundError:
        return None
    return None

# 6. SIGNUP FUNCTION
def signup():
    username = input("Enter username: ")
    password = input("Create strong password: ")

    if not is_strong_password(password):
        print("❌ Weak password! Must include 8 chars, uppercase, lowercase, digit, special char.")
        return

    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    save_user(username, salt, hashed_password)
    print("✅ Account created successfully!")

# 7. LOGIN FUNCTION (3 ATTEMPTS LIMIT)
def login():
    username = input("Enter username: ")
    user_data = load_user(username)

    if not user_data:
        print("❌ User not found!")
        return

    salt, stored_hash = user_data

    attempts = 3

    while attempts > 0:
        password = input("Enter password: ")
        hashed_password = hash_password(password, salt)

        if hashed_password == stored_hash:
            print("✅ Login successful!")
            return
        else:
            attempts -= 1
            print(f"❌ Wrong password! Attempts left: {attempts}")

    print("🔒 Account locked due to too many failed attempts!")
# 8. MAIN MENU
while True:
    print("\n1. Signup\n2. Login\n3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")