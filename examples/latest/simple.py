
def hello():
    print("Hello, world!")


def print_info():
    print("This is just a sample python file.")


def add_numbers(value1, value2):
    return value1 + value2


def subtract_numbers(value1, value2):
    return value1 - value2


if __name__ == "__main__":
    hello()
    print_info()

    a = 10
    b = 4

    print("The sum of", a, "+", b, "is", add_numbers(a, b))

    print("The difference between", a, "-", b, "is", subtract_numbers(a, b))
