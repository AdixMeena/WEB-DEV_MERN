# # ---------- 1. Single inheritance ----------
# class Animal:
#     def __init__(self, name):
#         self.name = name                      # stored on the same object (self)

#     def speak(self):
#         return f"{self.name} makes a sound"

#     def info(self):
#         return f"Animal: {self.name}"


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)                # runs Animal.__init__ -> sets self.name
#         self.breed = breed                    # Dog's own attribute

#     def speak(self):                          # override
#         return super().speak() + " -> Woof!"  # reuse parent's version, then add more

#     # info() is NOT overridden, so Python finds Animal.info automatically


# d = Dog("Bruno", "Labrador")
# print(d.speak())   # Bruno makes a sound -> Woof!
# print(d.info())    # Animal: Bruno
# print(d.breed)     # Labrador


# ---------- 2. Multiple inheritance (cooperative super) ----------
class Swimmer:
    def __init__(self, swim_speed, **kwargs):
        super().__init__(**kwargs)            # pass the rest to the next class in MRO
        self.swim_speed = swim_speed

    def move(self):
        return "swims"


class Runner:
    def __init__(self, run_speed, **kwargs):
        super().__init__(**kwargs)
        self.run_speed = run_speed

    def move(self):
        return "runs"


class Duck(Swimmer, Runner):
    def __init__(self, swim_speed, run_speed):
        super().__init__(swim_speed=swim_speed, run_speed=run_speed)

    def move(self):
        return "Duck " + super().move()       # goes to Swimmer.move (first in MRO)


duck = Duck(5, 3)
print(duck.swim_speed, duck.run_speed)   # 5 3  (both inits ran)
print(duck.move())                       # Duck swims
print(Duck.__mro__)
# (Duck, Swimmer, Runner, object)