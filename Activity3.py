# creating parent class
class bird:
    def __init__(self):
        print("bird is ready")
    def who_is_this(self):
        print("bird")
    def swim_faster(self):
        print('swim faster')


# creating child class
class penguin(bird):
    def __init__(self):
        super().__init__()
        print('penguin is ready')
    def who_is_this(self):
        print('penguin')
    def run(self):
        print('run faster')


# object creation
obj1=penguin()
obj1.who_is_this()
obj1.swim_faster()
obj1.run()