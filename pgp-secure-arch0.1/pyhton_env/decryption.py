#!/usr/bin/env python

import sys
import subprocess

encrypted_text = None
encrypted_file = None

def list_private_keys():
    """
    List all private keys available in the GPG keyring.
    """
    list_keys = subprocess.check_output("gpg --list-secret-keys", shell=True, text=True)
    list_keys = [
        line.strip() for line in list_keys.splitlines() 
        if "@" in line
    ]
    for i, key in enumerate(list_keys, start=1):
        print(f"{i}. {key}")
        keys_count = i
    return keys_count, list_keys

def handle_decrypt_choice(choice):
    if choice == 1:
        choice_readable = "file"
        return choice_readable
    elif choice == 2:
        choice_readable = "text"
        return choice_readable
    elif choice == 3:
        print("Exiting...")
        return "quit"
    else:
        print("Select 1-3!", file=sys.stderr)
        input("Press Enter to continue...")
        return None
    
def show_decrypt_menu():
    """
    Display the decryption menu and handle user input.
    """
    while True:
        print("-----------------------------")
        print("  D E C R Y P T I O N   M E N U")
        print("-----------------------------")
        print("1) Decrypt a file")
        print("2) Decrypt a text")
        print("3) Back to main menu")

        try:
            choice = int(input("Please enter your choice (1 - 3): "))
            action = handle_decrypt_choice(choice)
            
            if action in ("file", "text"):
                return action
            elif action == "quit":
                sys.exit(0)
                
        except ValueError:
            print("Invalid input", file=sys.stderr)
            input("Press Enter to continue...")

def define_private_key():
    keys_count, list_keys = list_private_keys()
    while True:
        try:
            choice = int(input(f"Please select a private key (1-{keys_count}): "))
            if 1 <= choice <= keys_count:
                private_key = list_keys[choice - 1]
                private_key = private_key.split()[-1].strip("<>")
                return private_key
            else:
                print("Invalid choice", file=sys.stderr)
        except ValueError:
            print("Invalid input", file=sys.stderr)
            input("Press Enter to continue...")

def decrypt_file(file_path, private_key):
    try:
        command = f"gpg --decrypt --recipient {private_key} {file_path}"
        decrypted_output = subprocess.check_output(command, shell=True, text=True)
        return decrypted_output
    except subprocess.CalledProcessError as e:
        print(f"Error decrypting file: {e}", file=sys.stderr)
        return None
    
def decrypt_text(text, private_key):
    try:
        command = f"echo '{text}' | gpg --decrypt --recipient {private_key}"
        decrypted_output = subprocess.check_output(command, shell=True, text=True)
        return decrypted_output
    except subprocess.CalledProcessError as e:
        print(f"Error decrypting text: {e}", file=sys.stderr)
        return None
    
choice = show_decrypt_menu()
if choice == "file":
    file_path = input("Enter the path to the encrypted file: ")
    private_key = define_private_key()
    decrypted_output = decrypt_file(file_path, private_key)
    if decrypted_output:
        print("Decrypted output:", decrypted_output)
elif choice == "text":  
    text = input("Enter the encrypted text: ")
    private_key = define_private_key()
    decrypted_output = decrypt_text(text, private_key)
    if decrypted_output:
        print("Decrypted output:", decrypted_output)
