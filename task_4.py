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
    def get_hours(cls, name, hours, rest_days, email):
        if not hours or hours is None:
            hours = (7 - rest_days) * 8
       
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(self, email, name):
        if not email or email is None:
            email = f'{name}@email.com'
        
        return email

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment


if __name__ == "__main__":
    test_data_with_hours = {
        'name': 'Mike',
        'hours': 8,
        'rest_days': 1,
        'email': 'Mike@email.com'
    }
    employee_salary = EmployeeSalary.get_hours(*list(test_data_with_hours.values()))
    assert employee_salary.__dict__['name'] == test_data_with_hours['name']
    assert employee_salary.__dict__['hours'] == test_data_with_hours['hours']
    assert employee_salary.__dict__['rest_days'] == test_data_with_hours['rest_days']
    assert employee_salary.__dict__['email'] == test_data_with_hours['email']

    test_data_without_hours = {
        'name': 'Mike',
        'hours': None,
        'rest_days': 2,
        'email': 'Mike@email.com'
    }
    employee_salary = EmployeeSalary.get_hours(*list(test_data_without_hours.values()))
    assert employee_salary.hours == 40, f'The actual hours is {employee_salary.hours}'

    actual_email = EmployeeSalary.get_email('Mike@email.com', None)
    assert actual_email == 'Mike@email.com'

    actual_email = EmployeeSalary.get_email(None, 'Mike')
    assert actual_email == 'Mike@email.com'

    assert EmployeeSalary.hourly_payment == 400
    
    EmployeeSalary.set_hourly_payment(200)
    assert EmployeeSalary.hourly_payment == 200
