"""The fouth task.

Using a class method.
"""

class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if not self.hours or self.hours is None:
            self.hours = (7 - self.rest_days) * 8
       
        return self.hours

    def get_email(self):
        if not self.email or self.email is None:
            self.email = f'{self.name}@email.com'
        
        return self.email

    def salary(self):
        return self.hours * EmployeeSalary.hourly_payment

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        EmployeeSalary.hourly_payment = hourly_payment


if __name__ == "__main__":
    employee_salary = EmployeeSalary('Mike', 8, 1, 'Mike@email.com')
    assert employee_salary.salary() == 3200

    employee_salary = EmployeeSalary('Mike', 8, 1, '')
    assert employee_salary.get_email() == 'Mike@email.com'

    employee_salary = EmployeeSalary('Mike', None, 1, 'Mike@email.com')
    assert employee_salary.get_hours() == 48

    assert EmployeeSalary.hourly_payment == 400
    
    EmployeeSalary.set_hourly_payment(200)
    assert EmployeeSalary.hourly_payment == 200
