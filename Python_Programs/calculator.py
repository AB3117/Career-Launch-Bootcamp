"""
calculator.py
A simple command-line calculator supporting +, -, *, / on two numbers.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    return OPERATIONS[op](a, b)


def main():
    print("Simple Calculator")
    print("Supported operators: +, -, *, /")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))
        result = calculate(a, op, b)
        print(f"Result: {a} {op} {b} = {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
