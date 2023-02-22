import abc

# @six.add_metaclass(abc.ABCMeta)
class Employee():
    def __init__(self, id, email, password, first_name, last_name, dob, salary):
        self._id= id
        self.email=email
        self.__password = password
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def get_full_name(self):
        return self.first_name +' '+ self.last_name


    @abc.abstractmethod
    def display(self):
        pass


# Instance creation:-
# emp=Employee(1,"ravindr@dummy.com", 1234567890, "Ravindra", "Bura", '12-08-2000')
# print(emp.get_full_name())