#!/usr/bin/env python

import platform
import subprocess

package_manager_commands = {
    "apt": "sudo apt install -y gnupg",
    "yum": "sudo yum install -y gnupg",
    "dnf": "sudo dnf install -y gnupg",
    "pacman": "sudo pacman -S --noconfirm gnupg",
    "zypper": "sudo zypper install -y gnupg",
    "brew": "brew install gnupg",
    "port": "sudo port install gnupg",
    "choco": "choco install gpg4win -y",
    "scoop": "scoop install gpg4win",
    "winget": "winget install --id GPG4Win.GPG4Win --silent"
}

def is_gpg_installed():
    try:
        subprocess.run(["gpg", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_package_manager():
    system = platform.system().lower()
    
    if system == "linux":
        for manager in ["apt", "yum", "dnf", "pacman", "zypper"]:
            try:
                subprocess.run([manager, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return manager
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
    elif system == "darwin":
        for manager in ["brew", "port"]:
            try:
                subprocess.run([manager, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return manager
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
    elif system == "windows":
        for manager in ["choco", "scoop", "winget"]:
            try:
                subprocess.run([manager, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                return manager
            except (subprocess.CalledProcessError, FileNotFoundError):
                continue
    return None

def install_gpg(package_manager):
    if package_manager in package_manager_commands:
        install_command = package_manager_commands[package_manager]
        try:
            subprocess.run(install_command, check=True, shell=True)
            print("GPG installed successfully.")
            return True
        except subprocess.CalledProcessError:
            print("Failed to install GPG. Please install it manually.")
            print(f"Command to install GPG: {install_command}")
            return False
    else:
        print("Unsupported OS or package manager.")
        return False

if __name__ == "__main__":
    if is_gpg_installed():
        print("GPG is already installed.")
    else:
        print("GPG is not installed.")
        package_manager = get_package_manager()
        if package_manager:
            print(f"Detected package manager: {package_manager}")
            if install_gpg(package_manager):
                print("GPG is now installed.")
            else:
                print("GPG installation failed.")
        else:
            print("Could not detect a supported package manager. Please install GPG manually.")