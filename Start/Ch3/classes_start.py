# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#
class Vehicle:

  # Like the constructor of the class, always has self parameter
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle

  def drive(self, speed):
    self.mode = "driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, enginetype):
    super().__init__("Car") # body style for extended class
    self.wheels = 4
    self.doors = 4
    self.engine = enginetype

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "car at", self.speed)

class Motorcycle(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Mortorcycle")
    if (hassidecar):
      self.wheels = 3
    else :
      self.wheels = 2

    self.doors = 0
    self.engietype = enginetype

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engietype, "motorcycle at", self.speed)


car1 = Car("gas")
car2 = Car("electric")

mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.engine)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)