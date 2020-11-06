
class Employee:

    def __init__(self, fname, lname, salary):
        
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self, raises=5000):

        self.salary += raises

emp = Employee('w', 's', 500)
emp.give_raise()
emp.give_raise(6000)