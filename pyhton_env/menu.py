#!/usr/bin/env python

import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    while True:
        clear_screen()
        print("-----------------------------")
        print("  M A I N   M E N U")
        print("-----------------------------")
        print("1) Option 1: Encrypt file")
        print("2) Option 2: Decrypt file")
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
        return "encryption"
    elif choice == 2:
        return "decryption"
    elif choice == 3:
        print("Exiting...")
        return "quit"
    else:
        print("Select 1-3!", file=sys.stderr)
        input("Press Enter to continue...")
        return None

# Check with print
if __name__ == "__main__":
    choice = show_menu()
    print(f"Selected action: {choice}")
    
    # Calling other scripts based on the choice
    # if choice == "encryption":
    #     os.system("python ./encryption.py")
    # elif choice == "decryption":
    #     os.system("python ./decryption.py")