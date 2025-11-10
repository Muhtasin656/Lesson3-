class vehicle:
    def __init__(self,category,id_number):
        self.category=category
        self.id_number=id_number
    def display(self):
        print(self.category)
        print(self.id_number)


# child class
class car(vehicle):
    def __init__(self, category, id_number,mileage,maxspeed):
        self.mileage=mileage
        self.maxspeed=maxspeed
        super().__init__(category, id_number)
obj=car("Toyota",1212,1290,200)
obj.display()