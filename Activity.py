class car:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
class masda(car):
    pass
obj1=masda("masda",100,12)
print(f"the name of the car is {obj1.name} and the maximum speed is {obj1.max_speed} and the mileage is {obj1.mileage} ")