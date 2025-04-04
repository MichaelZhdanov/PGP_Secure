#!/usr/bin/env python

import os
import sys

choice_readable = ""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("-----------------------------")
    print("  M A I N   M E N U")
    print("-----------------------------")
    print("1) Option 1: Encrypt file")
    print("2) Option 2: Decrypt file")
    print("3) Quit")

    while True:
        try:
            choice = int(input("Please enter your choice (1 - 3)"))
            handle_choice(choice)
            break
        except ValueError:
            print("Invalid input", file=sys.stderr)
            continue

def handle_choice(choice):
    if choice == 1:
        choice_readable == "encryption"
    elif choice == 2:
        choice_readable == "decryption"
    elif choice == 3:
        print("Exiting program...")
        sys.exit(0)
    else:
        print("Select 1 -3!", file=sys.stderr)
        input("Press Enter to countinie...")
        show_menu()
        return choice_readable

    input("Press Enter to countinie...")
    show_menu()

if __name__ == "__main__":
    show_menu()

