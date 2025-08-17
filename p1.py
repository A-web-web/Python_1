class ToyCar:
    def __init__(self,color,size,wheels):
        self.colour= color
        self.size= size
        self.wheels= wheels
    def describe(self):
        return f"This toy car is {self.colour},size {self.size},and has {self.wheels} wheels"
car1 = ToyCar("red","small",4)
car2= ToyCar("blue","large",6) 

print(car1.describe())
print(car2.describe())