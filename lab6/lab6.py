
class HourlyEmployee:
    def __init__(self):
        self.__nmbrOfHour
        self.__hourlyPay
    
     # GETTERS
    def get_nmbrOfHour(self):
        return self.__nmbrOfHour
    
    def get_hourlyPay(self):
        return self.__hourlyPay

     # SETTERS
    def set_nmbrOfHour(self, nmbrOfHour):
        self.__nmbrOfHour = nmbrOfHour

    def set_hourlyPay(self, hourlyPay):
        self.__hourlyPay = hourlyPay

    # PROPERTIES
    nmbrOfHour = property(get_nmbrOfHour, set_nmbrOfHour)
    hourlyPay = property(get_hourlyPay, set_hourlyPay)

class SalaryEmployee:
    def __init__(self):
        self.__salary

     # GETTERS
    def get_salary(self):
        return self.__salary

    # SETTERS
    def set_salary(self, salary):
        self.__salary = salary

    # PROPERTIES
    salary = property(get_salary, set_salary)
    

class Employee(HourlyEmployee, SalaryEmployee):
    def __init__(self):
        self.__nameEmployee
        self.__phone
        self.__bday
        self.__email
        self.__position
    
    # GETTERS
    def get_nameEmployee(self):
        return self.__nameEmployee
    
    def get_phone(self):
        return self.__phone
    
    def get_bday(self):
        return self.__bday
    
    def get_email(self):
        return self.__email
    
    def get_position(self):
        return self.__position

    # SETTERS
    def set_nameEmployee(self, nameEmployee):
        self.__nameEmployee = nameEmployee

    def set_phone(self, phone):
        self.__phone = phone

    def set_bday(self, bday):
        self.__bday = bday
        
    def set_email(self, email):
        self.__email = email
        
    def set_position(self, position):
        self.__position= position


    # PROPERTIES
    nameEmployee = property(get_nameEmployee, set_nameEmployee)
    phone = property(get_phone, set_phone)
    bday = property(get_bday, set_bday)
    email = property(get_email, set_email)
    position = property(get_position, set_position)


    # RESTUL
    def calculateAge():
        pass
    
    def _calculareSalary():
        pass
    
