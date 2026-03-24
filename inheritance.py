# Inheritance example (version 3)

class Base:
    def __init__(self, name):
        self.name = name

class Derived(Base):
    def __init__(self, name, dept):
        Base.__init__(self, name)
        self.dept = dept

    def show(self):
        print(self.name, "-", self.dept)

d = Derived("Neha", "IT")
d.show()
