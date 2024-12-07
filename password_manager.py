import os

# Shift value for Caesar cipher encryption
SHIFT = 3

# Function to encrypt a string using Caesar cipher
def encrypt(text):
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Shift letter
            start = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - start + SHIFT) % 26 + start)
        else:
            # Non-alphabet characters remain unchanged
            encrypted += char
    return encrypted

# Function to decrypt a string using Caesar cipher
def decrypt(text):
    decrypted = ""
    for char in text:
        if char.isalpha():
            # Shift letter
            start = ord('a') if char.islower() else ord('A')
            decrypted += chr((ord(char) - start - SHIFT + 26) % 26 + start)
        else:
            # Non-alphabet characters remain unchanged
            decrypted += char
    return decrypted

# Function to save username and password to a file
def savePassword(username, password):
    with open("pass.txt", "a") as file:
        encrypted_password = encrypt(password)
        file.write(f"{username} {encrypted_password}\n")
    print("Password saved successfully.")

# Function to list all saved passwords
def listPasswords():
    adminPassword = input("Enter admin password to view saved passwords: ")
    
    # Check if the entered admin password is correct
    if adminPassword != "123":
        print("Incorrect admin password. Access denied.")
        return

    try:
        with open("pass.txt", "r") as file:
            for line in file:
                line = line.strip()  # Remove any leading or trailing whitespace
                if line:  # Skip empty lines
                    parts = line.split()  # Split by whitespace
                    if len(parts) >= 2:  # Ensure there are at least two values
                        username = parts[0]
                        encrypted_password = parts[1]
                        
                        # Decrypt the password, not the username
                        decrypted_password = decrypt(encrypted_password)
                        
                        # Debugging print to check decrypted password
                        print(f"Encrypted: {encrypted_password}, Decrypted: {decrypted_password}")
                        
                        print(f"Username: {username}, Password: {decrypted_password}")
                    else:
                        print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("Password file not found.")





# Main function for the menu
def main():
    while True:
        print("\nPassword Manager")
        print("1. Add a new password")
        print("2. List all passwords")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            savePassword(username, password)
        elif choice == "2":
            listPasswords()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
