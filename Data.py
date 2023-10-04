import queue
import csv


class Employee:
    '''Creates an employee object.'''
    def __init__(self, emp_id, first_name, job_title, hours_worked, hourly_wage, federal_tax_rate):
        self.emp_id = emp_id
        self.first_name = first_name
        self.job_title = job_title
        self.hours_worked = hours_worked
        self.hourly_wage = hourly_wage
        self.federal_tax_rate = federal_tax_rate


    def calculate_gross_pay(self):
        """Calculates the Gross Pay."""
        return self.hours_worked * self.hourly_wage


    def calculate_federal_tax(self):
        """Calculates Federal Tax Rate."""
        return self.calculate_gross_pay() * (self.federal_tax_rate / 100)


