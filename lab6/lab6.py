import Lab6Classes
import re

def validate_input(pattern, prompt):
    while True:
        value = input(prompt)
        if re.fullmatch(pattern, value):
            return value
        print("Input invalid! Reîncercați.")

employees = []
for _ in range(2):
    employee = Lab6Classes.Employee()
    employee.nameEmployee = validate_input(r"^[A-Za-z]+$", "Introduceți numele angajatului: ")
    employee.phone = validate_input(r"^\+373\d{8}$", "Introduceți telefonul (+373xxxxxxxx): ")
    employee.bday = validate_input(r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19[6-9]\d|200[0-7])$", "Introduceți data nașterii (zz.ll.aaaa): ")
    employee.email = validate_input(r"^[A-Za-z0-9._|-]{2,20}@[A-Za-z]{4,7}\.[A-Za-z]{2,4}$", "Introduceți e-mail-ul: ")
    employee.position = validate_input(r"^[A-Za-z]{4,20}$", "Introduceți specialitatea: ")
    employees.append(employee)

hourly_employees = []
for _ in range(2):
    employee = Lab6Classes.HourlyEmployee()
    employee.nmbrOfHour = int(validate_input(r"^\d+$", "Introduceți numărul de ore: "))
    employee.hourlyPay = float(validate_input(r"^\d+(\.\d+)?$", "Introduceți plata pe oră: "))
    hourly_employees.append(employee)

salary_employees = []
for _ in range(2):
    employee = Lab6Classes.SalaryEmployee()
    employee.salary = float(validate_input(r"^\d+(\.\d+)?$", "Introduceți salariul lunar: "))
    salary_employees.append(employee)

print("\nDetalii angajați:")
for emp in employees:
    print(f"Nume: {emp.nameEmployee}")
    print(f"Telefon: {emp.phone}")
    print(f"Data nașterii: {emp.bday}")
    print(f"E-mail: {emp.email}")
    print(f"Specialitate: {emp.position}\n")

print("\nDetalii angajați cu plată orară:")
for emp in hourly_employees:
    print(f"Număr de ore: {emp.nmbrOfHour}")
    print(f"Plată pe oră: {emp.hourlyPay}\n")

print("\nDetalii angajați cu salariu fix:")
for emp in salary_employees:
    print(f"Salariu lunar: {emp.salary}\n")

hourly_salaries = [emp.calculateSalary() for emp in hourly_employees]
salary_salaries = [emp.calculateSalary() for emp in salary_employees]

print("\nSalarii angajați cu plată orară:", hourly_salaries)
print("Salarii angajați cu salariu fix:", salary_salaries)
