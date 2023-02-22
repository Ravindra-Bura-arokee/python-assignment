from employee import Employee

class HumanResourceEmployee(Employee):
    def __init__(self, id, email, password, first_name, last_name, dob, salary, specialty):
        super().__init__(id, email, password, first_name, last_name, dob, salary)
        self.specialty = specialty
    
    def display(self):
        print(f"id:{self._id}, Full Name:{self.first_name+' '+self.last_name}, Email:{self.email}, specialty:{self.specialty}")

    def get_specialty(self):
        print(f"HR specialty is {self.specialty}")


# HR = HumanResourceEmployee(1, "ravindr@dummy.com", 1234567890, "Ravindra", "Bura", '12-08-2000', '120000', 'Labor Relations Specialist')
# HR.get_specialty()