import string
import random

SPECIAL_CHARS = "!@#$%^&*"

def generate_password(length):
    if length < 8:
        print("Password length should be at least 8 for strength.")
        return None
    chars = string.ascii_letters + string.digits + SPECIAL_CHARS
    # Ensure at least one upper, one lower, one digit, one special
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(SPECIAL_CHARS)
    ]
    password += [random.choice(chars) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)

def save_password(site, username, password):
    with open("passwords.txt", "a") as f:
        f.write(f"{site},{username},{password}\n")

def show_password_history():
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No password history found.")
                return
            print("Password History:")
            for idx, line in enumerate(lines, 1):
                site, username, password = line.strip().split(",")
                print(f"{idx}. Site: {site}, Username: {username}, Password: {password}")
    except FileNotFoundError:
        print("No password history found.")

def delete_password():
    try:
        with open("passwords.txt", "r") as f:
            lines = f.readlines()
        if not lines:
            print("No password history to delete.")
            return
        print("Password History:")
        for idx, line in enumerate(lines, 1):
            site, username, password = line.strip().split(",")
            print(f"{idx}. Site: {site}, Username: {username}, Password: {password}")
        to_delete = input("Enter the number of the password to delete: ")
        if not to_delete.isdigit() or int(to_delete) < 1 or int(to_delete) > len(lines):
            print("Invalid selection.")
            return
        del lines[int(to_delete) - 1]
        with open("passwords.txt", "w") as f:
            f.writelines(lines)
        print("Password deleted.")
    except FileNotFoundError:
        print("No password history found.")

def main():
    print("Simple Password Manager")
    print("1. Add new password")
    print("2. Show password history")
    print("3. Delete a password from history")
    choice = input("Choose an option (1, 2 or 3): ")
    if choice == "1":
        site = input("Enter site name: ")
        username = input("Enter username: ")
        length = int(input("Enter password length (min 8): "))
        password = generate_password(length)
        if password:
            print(f"Generated password: {password}")
            save_password(site, username, password)
            print("Password saved to passwords.txt")
    elif choice == "2":
        show_password_history()
    elif choice == "3":
        delete_password()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
