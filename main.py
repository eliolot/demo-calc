from src.calculator import add, subtract, multiply, divide

if __name__ == "__main__":
    a = 10
    b = 5

    print(f"Addition: {a} + {b} = {add(a, b)}")
    print(f"Subtraction: {a} - {b} = {subtract(a, b)}")
    print(f"Multiplication: {a} * {b} = {multiply(a, b)}")
    print(f"Division: {a} / {b} = {divide(a, b)}")