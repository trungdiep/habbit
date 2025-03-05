import random
import psycopg
import time
from faker import Faker

class Employee:
    OFFICE_CODE = tuple(range(1, 8))
    JOB_TITLE = ("President", "VP Sales", "VP Marketing", "Sales Manager (APAC)", "Sale Manager (EMEA)", "Sales Manager (NA)", "Sales Rep",)

    def __init__(self, faker) -> None:
        self.faker = faker

    def employeeNumber(self):
        return self.faker.unique.pyint(max_value=1_000_000, step=1)

    def lastName(self):
        return self.faker.last_name()

    def firstName(self):
        return self.faker.first_name()

    def extension(self):
        return faker.pystr(min_chars=5, max_chars=9, prefix='x')

    def email(self):
        return self.faker.safe_email()

    def officeCode(self):
        return random.choice(self.OFFICE_CODE)

    def jobTitle(self):
        return random.choice(self.JOB_TITLE)
    
    def reportsTo(self):
        return None

    def generate(self):
        return (
            self.employeeNumber(),
            self.lastName(),
            self.firstName(),
            self.extension(),
            self.email(),
            self.officeCode(),
            self.reportsTo(),
            self.jobTitle(),
            )


query = '''
    INSERT INTO public.employees(
	employeenumber, lastname, firstname, extension, email, officecode, reportsto, jobtitle)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
'''

if __name__ == "__main__":
    index = 0
    max_records = 1_000_000
    faker = Faker()
    employee = Employee(faker)
    
    with psycopg.connect("dbname=postgres user=postgres password=123456789 host=127.0.0.1") as conn:
        with conn.cursor() as cur:
            while index < max_records:
                data = employee.generate()
                cur.execute(query, data)
                index += 1
                if index % 1000 == 0:
                    conn.commit()
                    time.sleep(1)
