"""
This is the main file of project package_name.

It is invoked when someone runs python like:
    python -m package_name
"""
from .bigfoot import FootExample


def main():
    FootExample().print_text()
  
if __name__ == "__main__":
    main()  