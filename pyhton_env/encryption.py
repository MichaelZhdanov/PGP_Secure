#!/usr/bin/env python

import os
import sys
import subprocess

encrypted_text = None
encrypted_file = None

def show_recipients(): 
    list_recipents = subprocess.check_output("gpg --list-keys", shell=True, text=True)
    list_recipents = [
        line.strip() for line in list_recipents.splitlines() 
        if "@" in line
    ]
    for i, recipient in enumerate(list_recipents, start=1):
        print(f"{i}. {recipient}")
        recipients_count = i
    return recipients_count, list_recipents

def handle_encrypt_choice(choice):
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

def show_encrypt_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-----------------------------")
        print("  E N C R Y P T I O N   M E N U")
        print("-----------------------------")
        print("1) Encrypt a file")
        print("2) Encrypt a text")
        print("3) Back to main menu")

        try:
            choice = int(input("Please enter your choice (1 - 3): "))
            action = handle_encrypt_choice(choice)
            
            if action in ("file", "text"):
                return action
            elif action == "quit":
                sys.exit(0)
                
        except ValueError:
            print("Invalid input", file=sys.stderr)
            input("Press Enter to continue...")

def define_recipient():
    recipients_count, list_recipents = show_recipients()
    while True:
        try:
            recipient_choice = int(input(f"Select recipient (1-{recipients_count}): "))
            if 1 <= recipient_choice <= recipients_count:
                recipient = list_recipents[recipient_choice - 1]
                recipient = recipient.split()[-1].strip("<>")
                return recipient
            else:
                print("Invalid choice. Please select a valid recipient.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def text_encryption(recipient):
    print("Encrypting text...")
    text = str(input("Enter text to encrypt: "))
    # encrypted_text = os.system(f"gpg --encrypt --armor --recipient {recipient}")
    os.system(f'echo "{text}" | gpg --encrypt --armor --recipient {recipient} --output encrypted_text.asc')
    encrypted_text = subprocess.check_output(f'cat encrypted_text.asc', shell=True, text=True)
    os.system('rm encrypted_text.asc')
    input("Press Enter to continue...")
    return encrypted_text

def file_encryption(recipient):
    print("Encrypting file...")
    file_path = input("Enter the path of the file to encrypt: ")
    if os.path.isfile(file_path):
        os.system(f'gpg --encrypt --armor --recipient {recipient} --output {file_path}.asc {file_path}')
        encrypted_file = file_path + ".asc"
        print("Remove original file? (y/n)")
        delete_choice = input("Enter 'y' to delete or 'n' to keep: ").lower()
        if delete_choice == 'y':
            os.remove(file_path)
            print("Original file deleted.")
        elif delete_choice == 'n':
            print("Original file kept.")
        else:
            print("Invalid choice. Original file kept.")
        input("Press Enter to continue...")
        return encrypted_file
    else:
        print("File not found. Please check the path.")
        input("Press Enter to continue...")
        return None

choice = show_encrypt_menu()
recipient = define_recipient()
if choice == "file":
    encrypted_file = file_encryption(recipient)
elif choice == "text":
    encrypted_text = text_encryption(recipient)

def output(encrypted_text, encrypted_file, recipient):
    if encrypted_text is not None:
        print(f"Text is encrypted for {recipient}:")
        print("Encrypted text:\n")
        print(encrypted_text)
    else:
        print(f"Encrypted file: {encrypted_file}")

output(encrypted_text, encrypted_file, recipient)


