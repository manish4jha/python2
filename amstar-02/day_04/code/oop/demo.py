# Creation of the class -> plan
class Employee:
   'Common base class for all employees'
   empCount = 0

   # Data section
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      self.tax = 0
      Employee.empCount += 1

   # Methods/functions section
   # Setters
   # Getters
   # House keeping functions -> used to stabilize the state of the object
   # Logic, algorithms and other public interface functions
   # Miscellaneous,  debug functions

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# Creating objects
emp1 = Employee("Kumar", 2000)
emp2 = Employee("Abhinav", 5000)

# Using the objects
emp1.displayEmployee()
emp2.displayEmployee()

# Experimenting on class variables
print ("Total Employee %d" % emp1.empCount)
Employee.empCount = 5

print ("Total Employee after overriding the value externally %d" % emp1.empCount)
