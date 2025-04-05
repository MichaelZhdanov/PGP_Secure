#!/usr/bin/env python

import os
import sys
from pathlib import Path

def get_current_dir():
    return str(Path(__file__).resolve().parent)

current_dir = get_current_dir()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    while True:
        clear_screen()
        print("-----------------------------")
        print("  M A I N   M E N U")
        print("-----------------------------")
        print("1) Option 1: Encryption")
        print("2) Option 2: Decryption")
        print("3) Quit")

        try:
            choice = int(input("Please enter your choice (1 - 3): "))
            action = handle_choice(choice)
            
            if action in ("encryption", "decryption"):
                return action
            elif action == "quit":
                sys.exit(0)
                
        except ValueError:
            print("Invalid input", file=sys.stderr)
            input("Press Enter to continue...")

def handle_choice(choice):
    if choice == 1:
        choice_readable = "encryption"
        return choice_readable
    elif choice == 2:
        choice_readable = "decryption"
        return choice_readable
    elif choice == 3:
        print("Exiting...")
        return "quit"
    else:
        print("Select 1-3!", file=sys.stderr)
        input("Press Enter to continue...")
        return None

# Check with print
if __name__ == "__main__":
    choice_readable = show_menu()
    print(f"Selected action: {choice_readable}")
    
    # Calling other scripts based on the choice
if choice_readable == "encryption":
    os.system(f"python {os.path.join(current_dir, 'encryption.py')}")
elif choice_readable == "decryption":
    os.system(f"python {os.path.join(current_dir, 'decryption.py')}")