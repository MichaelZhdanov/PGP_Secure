#!/usr/env python

import os
def get_current_dir():
    return str(Path(__file__).resolve().parent)

current_dir = get_current_dir()
os.system(f"python {current_dir}/python_env/menu.py")