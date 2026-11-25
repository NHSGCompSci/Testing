import operations

OPERATORS = {
    "+": operations.add,
    "-": operations.subtract,
    "*": operations.multiply,
    "/": operations.divide,
}


def calculate(a, b, op):
    if op not in OPERATORS:
        return "Error: unknown operator"
    return OPERATORS[op](a, b)


def main():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Error: please enter valid numbers")
        return
    op = input("Operator (+, -, *, /): ").strip()
    print("Result:", calculate(a, b, op))


if __name__ == "__main__":
    main()
