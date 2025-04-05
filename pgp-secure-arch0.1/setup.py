from setuptools import setup, find_packages

setup(
    name="pgp-secure",
    version="1.0",
    packages=find_packages(),
    install_requires=[],  # List dependencies here (e.g., ["pygpgme", "click"])
    entry_points={
        "console_scripts": [
            "pgp-secure=python_env.menu:main",  # Runs `main()` in menu.py
        ],
    },
)