
from django.test import TestCase
from model_mommy import mommy
from employee.models import Employee


class TestEmployee(TestCase):

    def setUp(self):
        self.employee = mommy.make(Employee, name='Fabricio Machado',
                                   email='fabricio.renan@live.com',
                                   department='E-commerce')

    def test_employee_creation(self):
        self.assertTrue(isinstance(self.employee, Employee))
        self.assertEquals(self.employee.__str__(), self.employee.name)