class department:
    def __init__(self):
       self.department="physics"
       self.hod="ramesh"
       self.depart_code="1007"
class person(department):
    def __init__(self,name,salary,age,code):
        self.name1=name
        self.age1=age
        self.salary1=salary
        self.emp_code=code
        super().__init__()
    def total(self):
        total=self.salary1*12
        return total
person1=person("ram",40000,40,"185")
person2=person("sita",10000,20,"143")
person3=person("sofiya",45000,27,"121")
person4=person("suresh",60000,38,"100")
person5=person("anaya",100000,45,"300")
print(person1.total(),"is the anual salary of person1")
print("name is",person2.name1,"his age is",person2.age1,"HOD is ",person2.hod)
print("emloyee id of person3 is",person3.depart_code+person3.emp_code)