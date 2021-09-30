class AnotherSampleClass:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_name(self, name):
        self.name = name

    def change_color(self, color):
        self.color = color

    def print_info(self):
        print("Hello, I am", self.name, "and I am", self.color)


if __name__ == "__main__":
    my_class = AnotherSampleClass("pypatchin", "green")
    my_class.print_info()
    my_class.change_name("PyPatchin")
    my_class.change_color("blue")
    my_class.print_info()
