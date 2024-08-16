import psycopg2

# Q1
class Human:
    count = 0

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Human.count += 1

    def eat(self):
        print("Human is eating")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

class Employee:
    count = 0

    def __init__(self, name=None, salary=None, department=None, connection=None, emp_id=0):
      
        if id ==0:
          self.name = name
          self.salary = salary
          self.department = department
          Employee.count += 1

          connection.query("insert into employ value (""name"", ""depertemt"" ,""salary"" )  ({self.name} , {self.department} , {sele.salary})")

        elif emp_id != 0 and connection is not None:
            query = f"SELECT * FROM employ WHERE id = {emp_id}"
          courser =  connection.query(query)

            self.name= courser.name
            self.salary=courser.sarary
            self.department=courser.department



           
            

