import math
import re


def calculator(input_string):
    match = re.match(r'(-?\d*\d+)?([+\-*/]|sqrt|log)?(-?\d*\d+)?$', input_string)
    if match is None:
        return "Invalid input. Please provide a valid expression."

    groups = match.groups()

    num1 = int(groups[0]) if groups[0] is not None else None
    operator = groups[1]
    num2 = int(groups[2]) if groups[2] is not None else None

    if operator == '+':
        if num1 is None or num2 is None:
            return "Invalid input. Please provide valid numbers."
        result = num1 + num2
    elif operator == '-':
        if num1 is None or num2 is None:
            return "Invalid input. Please provide valid numbers."
        result = num1 - num2
    elif operator == '*':
        if num1 is None or num2 is None:
            return "Invalid input. Please provide valid numbers."
        result = num1 * num2
    elif operator == '/':
        if num1 is None or num2 is None:
            return "Invalid input. Please provide valid numbers."
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    elif operator == 'sqrt' and num1 is None:
        if num2 < 0:
            return "Square root of a negative number is not allowed."
        result = math.sqrt(num2)
    elif operator == 'log' and num1 is None:
        if num2 < 0:
            return "Logarithm of a negative number is not allowed."
        result = math.log2(num2)
    else:
        return "Invalid operation. Please use '+', '-', '*', '/', 'sqrt', 'log'"
    return float(result)


def main():
    while True:
        input_str = input(
            "Enter an expression  '5*14', '2+3', '-42/7', 'sqrt5', 'log11', '-6*-2', '-2--5' or type 'exit' to end: ")

        if input_str.lower() == 'exit':
            break

        result = calculator(input_str)
        print("Result:", result)


if __name__ == "__main__":
    main()
