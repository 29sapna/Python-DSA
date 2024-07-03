#class -->blueprint
#object -->entity

class Person:
    name ="sapna"
    occupation ="software developer"
    networth = 10
def info(self):
    print(f"{self.name} is a {self.occupation}")
a= Person()
a.name = "sonal"
a.occupation ="web devloper"
# print(a.name, a.occupation)
a.info() # self means, that obj by which method is call

#CONSTRUCTOR
class Person:
    # name = "sapna"
    # occ = "devlopeer"
    def __init__(self, name, occ):
        print("I am devloper")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

    a = Person("Sapna", "Devloper")
    # a.name ="Divya"
    # a.occ ="HR"
    a.info()


#DECORATOR
def greet(fx):
  def mfx(*args, **kwargs):
    print("GM")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
   print("happy new year")

def add(a,b):
   print(a+b)

hello()
add(1,2)

#GETTERS & SETTERS
class MyClass:
   def __init__(self,value):
      self._value = value

      def show(self):
        print(f"value is {self._value}")

      @property
      def ten_value(self):
         return 10* self._value
      
      @ten_value.setter
      def ten_value(self,new_value):
         self._value = new_value/10


      obj =MyClass(10)
      obj.ten_value =67
      print(obj.ten_value)
      obj.show()
      
#INHERITANCE
class Employee:
  def __init__(self,name, id):
      self.name = name
      self.id = id
    
  def showDetails(self):
     print(f"the name of employee: {self.id} is {self.name}")


class programmer(Employee):
  def showLanguage(self):
    print("The default language is python")
e1 = Employee("Adi",200)
e1.showDetails()
e2=programmer("Sapna",123)
e2.showLanguage()

#access specifiers
class Employee:
   def __init__(self):
    self.__name ="Sapna"

a = Employee()
print(a.__name)#cannot be accesed directly
print(a._Employee__name)#can be accesd indirectly

#STATIC METHOD
class Math:
  def __init__(self, num):
      self.num = num

  def addtonum(self, n):
      self.num =self.num +n

  @staticmethod
  def add(a, b):
      return a +b 
    
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(Math.add(7,2))

#class and instance variable
class Employee:
  companyName = "Apple"
  noOfEmployees = 0
  def __init__(self, name):
    self.name = name
    self.raise_amount = 0.02
    Employee.noOfEmployees +=1
  def showDetails(self):
    print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}")

# Employee.showDetails(emp1)
emp1 = Employee("Harry")
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" 
emp1.showDetails()
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Nestle"
emp2.showDetails()

#class Method
class Employee:
   company = "Apple"
   def show(self):
      print(f"The name is {self.name} and company is {self.company}")
   @classmethod
   def changeCompany(cls, newCompany):
      cls.company =newCompany
e1 = Employee()
e1.name ="sapna"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

#class works
from sys import argv
a=eval(argv[1])
b=eval(argv[2])
print("Nos are",a,"and",b)
print("Their sum is",a+b)

print("Hello",argv[1])




    
   