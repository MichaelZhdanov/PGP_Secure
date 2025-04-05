#!/usr/bin/env python

import subprocess

list_recipents = subprocess.check_output("gpg --list-keys", shell=True, text=True)
list_recipents = [
    line.strip() for line in list_recipents.splitlines() 
    if "@" in line
]

for i, recipient in enumerate(list_recipents, start=1):
    print(f"{i}. {recipient}")
