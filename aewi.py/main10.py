#class method as alternative constructor
class Employee:
   def __init__(self,name,salary):
      self.name = name
      self.salary = salary

   @classmethod
   def fromStr(cls, string):
      return cls(string.split("-")[0], string.split("-")[1])
e1= Employee("Harry",1200)
print(e1.name)
print(e1.salary)

string ="Sapna-2910"
e2= Employee.fromStr(string)
print(e2.name)
print(e2.salary)

#super keyword in py used to refer to parent class.
class ParentClass:
   def parent_method(self):
      print("This is the parent class")

class ChildClass(ParentClass):
   def child_method(self):
      print("this is the child class")
      super().parent_method()

child_object = ChildClass()
child_object.child_method()
    

class Employee:
   name = "Harry"
   def __len__(self):
      i=0
      for c in self.name:
         i =i + 1
         return i

e = Employee()
print(e.name)
print(len(e))

#METHOD OVERRIDING- redefined method in the define class
class Shape:
   def __init__(self,x,y):
      self.x=x
      self.y=y

   def area(self):
      return self.x * self.y

class Circle(Shape):
   def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius)  


   def area(self):
      return 3.14 * super().area()

   # rec= Shape(3,5)
   # print(rec.area())

c = Circle(5)
print(c.area())    

#OPERATOR OVERLOADING
class Vector:
   def __init__(self,i,j,k):
      self.i =i
      self.j =j
      self.k =k

   def __str__(self):
      return f"{self.i}i + {self.j}k + {self.k}k"
   

   def __add__(self, x):
      return f"{self.i + x.i}i + {self.j+x.j}j +{self.k+x.k}k"
v= Vector(3,5,7)
print(v)

v1 = Vector(1,2,7)
print(v1)

print(v1 + v)

#SINGLE INHERITANCE
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

#MUTILEVEL INHERITANCE
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())

#MULTIPLE INHERITANCE
class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())

#PATTER 
n=int(input("enter the no: "))
for i in range (n):
   for j in range(n):
      print("*", end="  ")
   print()

#hollow pattern
n=int(input())
for i in range(0,n):
   for j in range(0,n):
      if(i==0 or i==(n-1) or j==0 or j==(n-1)):
         print("*",end="")
      else:
         print(" ",end="")
   print()

#diagonal
n=int(input())
for i in range(0,n):
   for j in range(0,n):
      if(i==j or (i+j)==(n-1)):
         print("*",end="")
      else:
         print(" ",end="")
   print()


#pyramid
n=int(input())
for i in range(1,n+1):
   for s in range(1,n-i+1):
      print(" ",end="")
   for j in range(1,2*i):
      print("*",end="")
   print()



#DIAMOND
n=int(input())
for i in range(1,n+1):
   for s in range(1,n-i+1):
      print(" ",end="")
   for j in range(1,2*i):
      print("*",end="")
   print()
for i in range(n-1,0,-1):
   for s in range(1,n-i+1):
      print(" ",end="")
   for j in range(1,2*i):
      print("*",end="")
   print()


# Example of Hybrid Inheritance 
class BaseClass:
  pass

class Derived1(BaseClass):
  pass  

class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass

# Hierarchical Inheritance
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass
 




   
      

