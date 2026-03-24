# Polymorphism (version 3)

class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies fast")

class Eagle(Bird):
    def fly(self):
        print("Eagle flies high")

birds = [Sparrow(), Eagle()]

for b in birds:
    b.fly()
