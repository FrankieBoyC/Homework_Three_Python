from Data import Employee
import queue
import csv


#Initialize Queues
input_queue = queue.Queue()
payStubs_queue = queue.Queue()

fields = ['ID', 'Name', 'Title', 'Hours Worked', 'Hourly Wage', 'Federal Tax Rate']

rows = [['1234', 'Franklin', 'Engineer', '2', '9.0', '.20'],
        ['5467', 'Raberto', 'Developer', '2', '9.1', '.20'],
        ['2345', 'Caity', 'FrontEnd', '2', '9.3', '.20'],
        ['1235', 'Patrick', 'FrontEnd', '1', '9.5', '.20'],
        ['3465', 'Prateek', 'Engineer', '3', '7.8', '.20'],
        ['4567', 'Alberto', 'Engineer', '2', '9.1', '.20'],
        ['5678', 'Orin', 'Engineer', '2', '9.0', '.20'],
        ['1678', 'Eric', 'Developer', '2', '9.1', '.20'],
        ['7565', 'Jose', 'FrontEnd', '2', '9.3', '.20'],
        ['5677', 'Alberto', 'FrontEnd', '1', '9.5', '.20'],
        ['7325', 'Alfred', 'Engineer', '3', '7.8', '.20'],
        ['9043', 'Albert', 'Engineer', '2', '9.1', '.20'],
        ['3065', 'Sarah', 'FrontEnd', '1', '9.5', '.20'],
        ['9042', 'John', 'Engineer', '3', '7.8', '.20'],
        ['2346', 'Tyler', 'Engineer', '2', '9.1', '.20']]

filename = "EmployeeInfo.csv"


'''Writing to the File.'''
try:
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)
except IOError:
    print("This file does not exist.")
except Exception as err:
    print(f"Unexpected error opening {filename} is",repr(err))



'''Reading the File.'''
try:
    with open('EmployeeInfo.csv') as csv_file:
        cvsRead = csv.reader(csv_file)
        next(csv_file, None)
        for line in cvsRead:
            emp_id, first_name, job_title, hours_worked, hourly_wage, federal_tax_rate = (field.strip() for field in line)
            employee = Employee(emp_id, first_name, job_title, float(hours_worked), float(hourly_wage), float(federal_tax_rate))
            input_queue.put(employee)
except IOError:
    print("This file does not exist.")
except Exception as err:
    print(f"Unexpected error opening {filename} is",repr(err))


'''Process data from the input queue and enqueue pay stubs into the payStubs queue.'''
while not input_queue.empty():
    employee = input_queue.get()
    gross_pay = employee.calculate_gross_pay()
    federal_tax = employee.calculate_federal_tax()
    
    state_tax = 0.1 * gross_pay
    social_security_tax = 0.05 * gross_pay
    medicare_tax = 0.02 * gross_pay
    
    net_pay = gross_pay - (federal_tax + state_tax + social_security_tax + medicare_tax)
    
    pay_stub = (employee.emp_id, f'{employee.first_name}', gross_pay, federal_tax, state_tax, social_security_tax, medicare_tax, net_pay)
    payStubs_queue.put(pay_stub)


'''Saves pay stub into text file.'''
try:
    with open('Covington.txt', 'w') as output_file:
        while not payStubs_queue.empty():
            pay_stub = payStubs_queue.get()
            output_file.write(','.join(map(str, pay_stub)) + '\n')
except IOError:
    print("This file does not exist.")
except Exception as err:
    print(f"Unexpected error opening {filename} is",repr(err))


'''Generates a summary report.'''
total_gross_pay = 0
total_federal_tax = 0
total_state_tax = 0
total_social_security_tax = 0
total_medicare_tax = 0

#Testing
with open('EmployeeInfo.csv') as csv_file:
        cvsRead = csv.reader(csv_file)
        next(csv_file, None)
        for line in cvsRead:
            emp_id, first_name, job_title, hours_worked, hourly_wage, federal_tax_rate = (field.strip() for field in line)
            employee = Employee(emp_id, first_name, job_title, float(hours_worked), float(hourly_wage), float(federal_tax_rate))
            input_queue.put(employee)


while not input_queue.empty():
    employee = input_queue.get()
    gross_pay = employee.calculate_gross_pay()
    federal_tax = employee.calculate_federal_tax()
    
    state_tax = 0.1 * gross_pay
    social_security_tax = 0.05 * gross_pay
    medicare_tax = 0.02 * gross_pay
    
    net_pay = gross_pay - (federal_tax + state_tax + social_security_tax + medicare_tax)
    
    pay_stub = (employee.emp_id, f'{employee.first_name}', gross_pay, federal_tax, state_tax, social_security_tax, medicare_tax, net_pay)
    payStubs_queue.put(pay_stub)
#Testing

try:
    with open('summary.txt', 'w') as summary_file:
        while not payStubs_queue.empty():
            pay_stub = payStubs_queue.get()
            total_gross_pay += pay_stub[2]
            total_federal_tax += pay_stub[3]
            total_state_tax += pay_stub[4]
            total_social_security_tax += pay_stub[5]
            total_medicare_tax += pay_stub[6]
            
            summary_file.write(f'Employee ID: {pay_stub[0]}, Employee Name: {pay_stub[1]}, Net Pay: {pay_stub[7]}\n')
except IOError:
    print("This file does not exist.")
except Exception as err:
    print(f"Unexpected error opening {filename} is",repr(err))

try:
    with open('summary.txt', 'w') as summary_file:
        summary_file.write(f'Total Gross Pay for All Employees: {total_gross_pay}\n')
        summary_file.write(f'Total Federal Taxes Withheld for All Employees: {total_federal_tax}\n')
        summary_file.write(f'Total State Taxes Withheld for All Employees: {total_state_tax}\n')
        summary_file.write(f'Total Social Security Withheld for All Employees: {total_social_security_tax}\n')
        summary_file.write(f'Total Medicare Amount Withheld for All Employees: {total_medicare_tax}\n')
except IOError:
    print("This file does not exist.")
except Exception as err:
    print(f"Unexpected error opening {filename} is",repr(err))

#Prints summary to the screen
print(f'Total Gross Pay for All Employees: {total_gross_pay}\n')
print(f'Total Federal Taxes Withheld for All Employees: {total_federal_tax}\n')
print(f'Total State Taxes Withheld for All Employees: {total_state_tax}\n')
print(f'Total Social Security Withheld for All Employees: {total_social_security_tax}\n')
print(f'Total Medicare Amount Withheld for All Employees: {total_medicare_tax}\n')