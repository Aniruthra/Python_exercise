class Car:
    def __init__(self,name,brand,year):
        self.name=name;
        self.brand=brand
        self.year=year


car1 = Car("Toyota", "Camry", 2024)
car2 = Car("Honda", "City", 2023)

print(car1.name)
print(car1.brand)
print(car1.year)
print()
print(car2.name)
print(car2.brand)
print(car2.year)

#understanding self
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"Hi, I am {self.name}")
        print(f"I am {self.age} years old")

d1=Dog("Bruno",10)
d2=Dog("Kuttan",12)
d1.introduce()
d2.introduce()

#understanding about class and instance attributes
class Employee:
    company="google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e1=Employee("Ani",10000)
e2=Employee("Mani",15000)
print(e1.company)
print(e2.company)
e1.company="Microsoft"
print(e1.company)
print(e2.company)
print(Employee.company)

#visibility and property
class Rectangle:
    def __init__(self,height,width):
        self._height=height
        self._width=width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if value<0:
            raise ValueError("Height should not less than 0")
        self._height=value


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if value<0:
            raise ValueError("Height should not less than 0")
        self._width=value
        

    def area(self):
        return self._width*self._height
    
    def perimeter(self):
        peri=2*self._width*self._height
        return peri
    
r=Rectangle(5,3)
print(r.area())
print(r.perimeter())
r.width=-5      
        