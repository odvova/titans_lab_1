class Animals:
    def eat(self):
        print("It's time to eat")

    def sleep(self):
        print("It`s time to sleep")


class Dog(Animals):
    def take_the_ball(self):
        print("Apport boy!")

    def wash(self):
        print("\nI hate washing!")


class  Cat(Animals):
    def meow(self):
        print("Meow\n")

    def crash_a_vase(self):
        print("*clank*")


class Elephant(Animals):
    def jump(self):
        print("Sorry, I can`t")

    def voice(self):
        print("*Hrruuuuv")


class Bird(Animals):
    def sing(self):
        print("Beautiful melody")

    def fly(self):
        print("Let`s flap together!")


class Fish(Animals):
    def blink(self):
        print("*blink*")

    def swim(self):
        print("*swimming")

