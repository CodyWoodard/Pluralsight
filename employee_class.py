from dataclasses import dataclass


@dataclass(slots=True) 
class Project:
    name: str
    payment: int
    client: str
    
    def notify_client(self):
        print(f"{self.name}")
        

class Employee:
    def __init__(self, name, age, salary, project) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


    
p = Project("Python app", 20000, "ShipStation")
e = Employee("Cody", 30, 6500, p) #look here
print(e.project)

