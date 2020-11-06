
import unittest
from employee import Employee

class test_employee(unittest.TestCase):

    def setUp(self):
        fname = 'W'
        lname = 'S'
        salary = 500
        self.employee = Employee(fname, lname, salary)

    def test_give_default_raise(self):
        self.employee.give_raise()


    def test_give_custom_raise(self):
        self.employee.give_raise(500)


if __name__ == "__main__":
    unittest.main()
