# the addition function
def add(n1, n2):
    return n1 + n2

# the subtraction function
def subtract(n1, n2):
    return n1 - n2

# the multiplication function
def multiply(n1, n2):
    return n1 * n2

# the division function
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("Error: Division by zero is undefined.")
        return None  # return None to indicate an error

# the dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# the calculator function
def calculator():
    try:
        # the first number input with exception handling
        num1 = float(input("What's the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return calculator()  # Restart calculator on invalid input

    # loops through the operations and prints them out
    for operator in operations:
        print(operator)

    # boolean to check if the user wants to stop calculating
    stop_calculating = False

    # while loop to keep the calculator running
    while not stop_calculating:
        operator = input("Pick an operation: ")

        if operator not in operations:
            print("Invalid operator. Please choose a valid operation.")
            continue  # Ask for the operator again

        try:
            # the next number input with exception handling
            num2 = float(input("What's the next number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  # Ask for the number again

        calculation_function = operations[operator]
        answer = calculation_function(num1, num2)

        if answer is not None:  # Only print if there's a valid answer (no division by zero)
            print(f"{num1} {operator} {num2} = {answer}")

        # Ask user if they want to continue or start a new calculation
        choice_to_continue = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation, or z to exit the program: ").lower()
        if choice_to_continue == "n":
            stop_calculating = True  # stop the current calculation loop
            calculator()  # start a new calculation
        elif choice_to_continue == "y":
            num1 = answer  # update num1 to the new answer
        elif choice_to_continue == "z":
            print("Thank you for using the calculator. Exiting the program.")
             # stop the current calculation loop
            stop_calculating = True 
        else:
            print("Invalid choice. Starting a new calculation.")
            stop_calculating = True
            calculator()

calculator()
