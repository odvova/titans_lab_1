from animals import Animals, Cat


class Human:
    def eat(self):
        print("It`s time to eat")

    def sleep(self):
        print("It`s time to sleep")

    def work(self):
        print("I love my work")


class Centaur(Human, Cat):
    def who_am_i(self):
        print("\n*Miss identification struggle sound*")




