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
    actual_hour = EmployeeSalary.get_hours(8, 1)
    assert actual_hour == 8

    actual_hour = EmployeeSalary.get_hours(None, 1)
    assert actual_hour == 48
