
def hello():
    print("Hello, world!")


def print_info():
    print("This is just a sample python file.")


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    hello()
    print_info()

    a = 10
    b = 4

    print("The sum of", a, "+", b, "is", add_numbers(a, b))
