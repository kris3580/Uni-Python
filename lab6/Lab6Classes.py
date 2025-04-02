
class HourlyEmployee:
    def __init__(self):
        self.__nmbrOfHour = 0
        self.__hourlyPay = 0
    
    @property   
    def nmbrOfHour(self):
        return self.__nmbrOfHour
    
    @nmbrOfHour.setter
    def nmbrOfHour(self, value):
        self.__nmbrOfHour = value
    
    @property
    def hourlyPay(self):
        return self.__hourlyPay
    
    @hourlyPay.setter
    def hourlyPay(self, value):
        self.__hourlyPay = value
    
    def calculateSalary(self):
        return self.__nmbrOfHour * self.__hourlyPay


class SalaryEmployee:
    def __init__(self):
        self.__salary = 0

    @property   
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value
    
    def calculateSalary(self):
        return self.__salary


class Employee(HourlyEmployee, SalaryEmployee):
    def __init__(self):
        super().__init__()
        self.__nameEmployee = ""
        self.__phone = ""
        self.__bday = ""
        self.__email = ""
        self.__position = ""
    
    @property    
    def nameEmployee(self):
        return self.__nameEmployee
    
    @nameEmployee.setter
    def nameEmployee(self, value):
        self.__nameEmployee = value
    
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, value):
        self.__phone = value
    
    @property
    def bday(self):
        return self.__bday
    
    @bday.setter
    def bday(self, value):
        self.__bday = value
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__position = value