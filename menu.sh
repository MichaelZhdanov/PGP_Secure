#!/bin/bash

# Function to display the menu
show_menu() {
    clear
    echo "-----------------------------"
    echo "  M A I N   M E N U"
    echo "-----------------------------"
    PS3="Please enter your choice (1-2): "
    select choice in \
        "Option 1: Encrypt file" \
        "Option 2: Decrypt file" \
        "Quit"; do
        handle_choice "$REPLY"
        break
    done
}

# Function to handle user choice
handle_choice() {
    case $1 in
        1)
            echo -e "\nYou selected: Option 1 - Encryption"
            read -p "Enter file to encrypt: " file
            ;;
        2)
            echo -e "\nYou selected: Option 2 - Decryption"
            read -p "Enter file to decrypt: " file
            ;;
        3)
            echo -e "\nExiting program..."
            exit 0
            ;;
        *)
            echo -e "\nInvalid option! Please select 1, 2, or 3." >&2
            sleep 1
            show_menu
            ;;
    esac
    
    # Return to menu after action
    read -p "Press Enter to continue..."
    show_menu
}

# Start the menu
show_menu