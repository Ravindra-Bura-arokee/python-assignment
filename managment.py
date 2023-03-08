from employee import Employee
from developer_employee import DeveloperEmployee
from human_resource_employee import HumanResourceEmployee
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb://localhost:27017")
db = client['python']
collection = db['users']
print("Connection Successful")

class EmployeeManagement:
    def __init__(self):
        self._employees = []

    def addEmployee(self, employee):
        print(employee)
        newEmployee = collection.insert_one(employee)
        print(newEmployee)
        return newEmployee

    def fetchEmployeeById(self, employee_id):
        employee = collection.find_one({"_id": ObjectId(employee_id)})
        print(employee);
        return employee

    def searchEmployeeByEmail(self, email):
        employeeDetail = collection.find({'email': email});
        print(employeeDetail)
        return employeeDetail

    def fetchAllEmployees(self):
        employeeDetails = collection.find()
        for employee in collection.find():
            print(employee)
        return employeeDetails

    def deleteEmployee(self, email):
        collection.delete_one({"email": email})
        print(f'Employee Deleted Successfully')


management = EmployeeManagement()

# add employees
developer_employee = DeveloperEmployee(1, "ravindr@dummy.com", 1234567890, "Ravindra", "Bura", '12-08-2000', '120000', 'python').display();
developer_employee1 = DeveloperEmployee(2, "naruto@dummy.com", 1234567890, "Naruto", "Uzumaki", '12-08-1995', '1550000', 'JavaScript').display()
# HumanResourceEmployee = HumanResourceEmployee(3, "sasuke@dummy.com", 1234567890, "Sasuke", "Uchiha", '12-08-1995', '125000', 'Java')
# print(developer_employee1)

management.addEmployee(developer_employee)
management.addEmployee(developer_employee1)
# management.addEmployee(HumanResourceEmployee)

management.fetchEmployeeById('640771d5f6b60b22f3530da0')

management.searchEmployeeByEmail("naruto@dummy.com")

management.deleteEmployee("naruto@dummy.com")

management.fetchAllEmployees()
