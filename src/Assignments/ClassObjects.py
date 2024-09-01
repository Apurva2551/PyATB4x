class Employee:
    # A
    name = None
    age = None
    phone = None
    address = None
    eid = None

    # B


    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid


    def walk(self):
        print("Walking")


    def talk(self):
        print("Talking")


employee1 = Employee(input("Enter Name "), int(input("Enter Age ")), int(input("Enter Number ")), input("Enter Address "), input("Enter Eid "))
print(employee1.name)
print(employee1.age)
print(employee1.phone)
print(employee1.address)
print(employee1.eid)
employee1.talk()
employee1.walk()

employee2 = Employee(input("Enter Name "), int(input("Enter Age ")), int(input("Enter Number ")), input("Enter Address "), input("Enter Eid "))
print(employee2.name)
print(employee2.age)
print(employee2.phone)
print(employee2.address)
print(employee2.eid)
employee2.talk()
employee2.walk()