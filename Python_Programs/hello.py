"""
hello.py
A simple starter program.
"""


def greet(name: str = "World") -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main():
    print(greet("Aryan"))
    print(greet())


if __name__ == "__main__":
    main()
