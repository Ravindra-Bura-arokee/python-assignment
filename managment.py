from employee import Employee
from developer_employee import DeveloperEmployee
from human_resource_employee import HumanResourceEmployee

class EmployeeManagement:
    def __init__(self):
        self._employees = []

    def addEmployee(self, employee):
        if isinstance(employee, Employee):
            self._employees.append(employee)

    def fetchEmployeeById(self, employee_id):
        for employee in self._employees:
            if employee.id == employee_id:
                return employee.display()
                print()
        return None

    def searchEmployeeByEmail(self, email):
        for employee in self._employees:
            if employee.email == email:
                return employee.display()
                print()
        return None

    def fetchAllEmployees(self):
        for employee in self._employees:
            employee.display()
            print()

    def deleteEmployee(self, employee):
        if isinstance(employee, Employee):
            self._employees.remove(employee)
            print(f'Employee name {employee.first_name +" "+ employee.last_name} Deleted Successfully')


management = EmployeeManagement()

# add employees
developer_employee = DeveloperEmployee(1, "ravindr@dummy.com", 1234567890, "Ravindra", "Bura", '12-08-2000', '120000', 'python')
developer_employee1 = DeveloperEmployee(2, "naruto@dummy.com", 1234567890, "Naruto", "Uzumaki", '12-08-1995', '1550000', 'JavaScript')
HumanResourceEmployee = HumanResourceEmployee(3, "sasuke@dummy.com", 1234567890, "Sasuke", "Uchiha", '12-08-1995', '125000', 'Java')


management.addEmployee(developer_employee)
management.addEmployee(developer_employee1)
management.addEmployee(HumanResourceEmployee)

# management.fetchAllEmployees()

# management.searchEmployeeByEmail("sasuke@dummy.com")

management.deleteEmployee(developer_employee1)

management.fetchAllEmployees()
