from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age:int

s=Student("Ani",21)
print(s)
print(s.name)