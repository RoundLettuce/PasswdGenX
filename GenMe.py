#!/usr/bin/env python3
import random
import os
import string
import sys
import shutil

# Python3 Passwd Generator.
# Coded by RoundLettuce.
# v1.5 - 2025-10-28

# clear_screen() is Optional. - Uncomment the call below for cleaner output.

def clear_screen():
    # If OS is Windoze, use cls command. Else use clear command. (Linux/Mac)
    if os.name == 'nt':
        os.system('cls')
        return
    term = os.environ.get('TERM', '')
    # If running in a real TTY that understands ANSI, use ANSI clear
    if sys.stdout.isatty():
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
        return
    # If TERM is set and not 'dumb', call the system clear
    if term and term != 'dumb':
        os.system('clear')
        return
    # Fallback: print only the number of lines equal to terminal height
    rows = shutil.get_terminal_size(fallback=(80, 24)).lines
    print('\n' * rows)

def main():
    # Store possible characters in a variable.
    chars = string.ascii_lowercase + string.digits + string.punctuation

    try:
        length = int(input("Enter the length of the password (Ex: 8): "))
    except ValueError:
        print("Please enter a valid number.")
        sys.exit(1)
    # Fix for: 'TERM environment variable not set.'
    #clear_screen()
    passwd = ''.join(random.choice(chars) for _ in range(length))
    print()
    print("Generated Password: ", passwd)
    print()

    while True:
        save = input("Would you like to save this password to a text file?" +
        " (y/n) ").strip()

        if save in ("y", "Y"):
            purpose = input("What is this password for?: ").strip()
            filename = f"{purpose or 'password'}.txt"
            with open(f"{purpose}.txt", "w") as f:
                f.write(passwd)
            print(f"\nSaved to {filename}, with {length} characters.")
            break
        elif save in ("n", "N"):
            input("Press Enter To Exit. ")
            break
        else:
            print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
# EOF.