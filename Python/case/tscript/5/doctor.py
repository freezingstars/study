class Doctor:
    def __init__(self, name, idnumber, address):
        self.name = name
        self.idnumber = idnumber
        self.address = address

    def display(self):
        print(f'name:{self.name}, idnumber:{self.idnumber}, address:{self.address}')


doctor = Doctor('李静', 326, '江西南昌')
doctor.display()


class Specialist(Doctor):
    def __init__(self, name, idnumber, address, speciality):
        super().__init__(name, idnumber, address)
        self.speciality = speciality

    def display(self):
        print("我是{}专业的医生".format(self.speciality))
        super().display()


class NonSpecialist(Doctor):
    def display(self):
        print("我是非专业医生")
        super().display()


s = Specialist("王海", "491", "江西赣州", "眼科")
n = NonSpecialist("姜平", "287", "江西九江")

print("===== 专科医生信息 =====")
s.display()
print("\n===== 非专科医生信息 =====")
n.display()
