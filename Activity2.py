class person:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(self.name)
        print(self.id_number)


# child class
class employee(person):
    def __init__(self, name, id_number,salary,post):
        self.salary=salary
        self.post=post
        super().__init__(name, id_number)
obj=employee("sam",1212,1290,"vice owner")
obj.display()