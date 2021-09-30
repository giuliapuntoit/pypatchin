class MySampleClass:
    adjectives = []

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, I am", self.name)

    def add_adjective(self, adj):
        self.adjectives.append(adj)

    def print_adjectives(self):
        for adj in self.adjectives:
            print("I am", adj)


if __name__ == "__main__":
    my_class = MySampleClass("pypatchin")
    my_class.say_hi()
    my_class.add_adjective("Tremendous")
    my_class.add_adjective("Useful")
    my_class.add_adjective("Suitable")
    my_class.print_adjectives()
