class Manager():
    def __init__(self,name,level):
        self.name=name
        self.level=level
    
    def showmanagerdetails(self):
        print(self.name, self.level)

class Employee(Manager):
    def __init__(self,name,level):
        super().__init__(name,level)
        self.site="India"
    
    def showemployeedetails(self):
        print(self.name, self.level,self.site)
        
obj_employee=Employee("santhosh","developer")
obj_employee.showemployeedetails()
obj_employee.showmanagerdetails()