class Student:
    def __init__(self,name,college,city,gpa=None):
        if not name:
            raise ValueError("No name provided")
        if college not in ["IT","CS","GIS","MIS","BA"]:
            raise ValueError("College not listed")
        self.name = name
        self.college = college
        self.city = city
    def __str__(self):
        return f"{self.name} is a student"
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self,city):
        self._city = city
        if city not in ["Khartoum","Dongola","Madani","Obaid","Port Sudan"]:
            raise ValueError("City is not listed")
        self._city = city
def main():
    info = get_student()
    print(f"{info.name} from {info.college}, {info.city} \n {info}")
def get_student():
    name = input("Name:- \n").title()
    college = input("College:- \n").upper()
    city = input("City:- \n").title()
    return Student(name,college,city)
if __name__ == "__main__":
    main()
