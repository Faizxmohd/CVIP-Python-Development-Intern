def add(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    if q == 0:
        return "Cannot divide by zero"
    return p / q

while True:
    # Display menu options
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # Take user input
    user_ip = input(": ")

    if user_ip == "quit":
        break
    elif user_ip in ["add", "subtract", "multiply", "divide"]:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if user_ip == "add":
            result = add(n1, n2)
        elif user_ip == "subtract":
            result = subtract(n1, n2)
        elif user_ip == "multiply":
            result = multiply(n1, n2)
        elif user_ip == "divide":
            result = divide(n1, n2)

        print("Output will be : ", result)
    else:
        print("Invalid input. Kindly try it again...")

