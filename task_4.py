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

    @classmethod
    def get_hours(cls, hours, rest_days):
        if not hours or hours is None:
            hours = (7 - rest_days) * 8
       
        return hours

    @classmethod
    def get_email(self, email, name):
        if not email or email is None:
            email = f'{name}@email.com'
        
        return email

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        EmployeeSalary.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment


if __name__ == "__main__":
    actual_hour = EmployeeSalary.get_hours(8, 1)
    assert actual_hour == 8

    actual_hour = EmployeeSalary.get_hours(None, 1)
    assert actual_hour == 48

    actual_email = EmployeeSalary.get_email('Mike@email.com', None)
    assert actual_email == 'Mike@email.com'

    actual_email = EmployeeSalary.get_email(None, 'Mike')
    assert actual_email == 'Mike@email.com'

    assert EmployeeSalary.hourly_payment == 400
    
    EmployeeSalary.set_hourly_payment(200)
    assert EmployeeSalary.hourly_payment == 200
