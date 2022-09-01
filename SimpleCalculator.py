#CALCULATOR:
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number? "))
    should_continue = True

    for symbol in operations:
        print(symbol)

    while should_continue:
        operation_symbol = input("Pick an operation ")
        num2 = float(input("What's the next number? "))

        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_input = input(f"Type y to continue calculating with {answer}, n to start fresh or e to exit: ")
        if user_input == "y":
            num1 = answer
        elif user_input == "n":
            should_continue = False
            calculator()
        elif user_input == "e":
            break


calculator()
