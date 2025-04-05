import platform
import subprocess
import os

def read_commands

def is_gpg_installed():
    try:
        # Run the 'gpg --version' command to check if GPG is installed
        subprocess.run(["gpg", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_package_manager():
    system = platform.system().lower()
    release = platform.release().lower()
    
    if system == "linux":
        # Check for specific package managers
        try:
            # Check for apt (Debian/Ubuntu)
            subprocess.run(["apt", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return "apt"
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                # Check for yum (RHEL/CentOS)
                subprocess.run(["yum", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return "yum"
            except (subprocess.CalledProcessError, FileNotFoundError):
                try:
                    # Check for dnf (Fedora/newer RHEL)
                    subprocess.run(["dnf", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    return "dnf"
                except (subprocess.CalledProcessError, FileNotFoundError):
                    try:
                        # Check for pacman (Arch)
                        subprocess.run(["pacman", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        return "pacman"
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        try:
                            # Check for zypper (openSUSE)
                            subprocess.run(["zypper", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            return "zypper"
                        except (subprocess.CalledProcessError, FileNotFoundError):
                            return "unknown (Linux)"
    
    elif system == "darwin":
        # macOS - check for Homebrew or MacPorts
        try:
            subprocess.run(["brew", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return "brew"
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(["port", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return "port"
            except (subprocess.CalledProcessError, FileNotFoundError):
                return "unknown (macOS)"
    
    elif system == "windows":
        # Windows - check for Chocolatey, Scoop, or Winget
        try:
            subprocess.run(["choco", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            return "choco"
        except (subprocess.CalledProcessError, FileNotFoundError):
            try:
                subprocess.run(["scoop", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                return "scoop"
            except (subprocess.CalledProcessError, FileNotFoundError):
                try:
                    subprocess.run(["winget", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    return "winget"
                except (subprocess.CalledProcessError, FileNotFoundError):
                    return "unknown (Windows)"
    
    else:
        return "unknown (unsupported OS)"

package_manager = get_package_manager()

def install_command_lookup(package_manager):
    return PACKAGE_MANAGER_COMMANDS.get(package_manager, None)
    else:
        print("Unsupported OS or package manager.")
        
def test_gpg(is_gpg_installed, package_manager):
    if is_gpg_installed:
        return True
    else:
        install_command = install_command_lookup(package_manager)
        try:
            subprocess.run(install_command, check=True, shell=True)
            return True
        except subprocess.CalledProcessError:
            print("Failed to install GPG. Please install it manually.")
            print(f"Command to install GPG: {install_command}")
            return False
        
if __name__ == "__main__":  
    if is_gpg_installed():
        print("GPG is installed.")
    else:
        print("GPG is not installed.")
    
    package_manager = get_package_manager()
    print(f"Detected package manager: {package_manager}")
    
    if test_gpg(is_gpg_installed(), package_manager):
        print("GPG is successfully installed or already present.")
    else:
        print("GPG installation failed.")
    print("Please install GPG manually.")
