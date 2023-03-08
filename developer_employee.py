from employee import Employee

class DeveloperEmployee(Employee):
    def __init__(self, id, email, password, first_name, last_name, dob, salary, programming_language):
        super().__init__(id, email, password, first_name, last_name, dob, salary)
        self.programming_language = programming_language
    
    def display(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.__password,
            "dob": self.dob,
            "salary": self.salary,
            "programming_language": self.programming_language

        }
        print("id:{self._id}, Full Name:{self.first_name+' '+self.last_name}, Email:{self.email}, programming_language:{self.programming_language}")

    
# developer = DeveloperEmployee(1, "ravindr@dummy.com", 1234567890, "Ravindra", "Bura", '12-08-2000', '120000', 'python')
# developer.display()