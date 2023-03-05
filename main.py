from animals import Dog, Cat, Bird, Elephant, Fish, Animals
from human import Centaur
from profile import Profile
from laptop import HPLaptop
if __name__ == "__main__":
    dog = Dog()
    elephant = Elephant()
    bird = Bird()
    fish = Fish()
    cat = Cat()

    dog.wash()
    elephant.jump()
    bird.sing()
    fish.blink()
    cat.meow()

    print(isinstance(dog, Animals))
    print(isinstance(elephant, Animals))
    print(isinstance(bird, Animals))
    print(isinstance(fish, Animals))
    print(isinstance(cat, Animals))

    centaur = Centaur()

    centaur.who_am_i()
    centaur.work()
    centaur.meow()

    profile = Profile(name="Volodya",
                      last_name="Kozariz",
                      phone_number="+380679803550",
                      address="Some address",
                      email="dovakin746@gmail.com",
                      birthday="04.08.04",
                      age="18",
                      sex="M")
    print(profile)

    laptop = HPLaptop()
    laptop.screen()
    laptop.ports()
    laptop.webcam()
    laptop.dynamics()
    laptop.keyboard()
    laptop.touchpad()
