class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("No name provided")
        self.name = name
    def __str__(self):
        return f"{self.name} \n"

class Student(Wizard): 
    def __init__(self,name,college,city):
        super().__init__(name) 
        self.college = college
        self.city = city

    @property
    def college(self):
        return self._city
    @college.setter
    def college(self,college):
        if college not in ["IT","CS","GIS","MIS","MBA","Cybersecurity"]:
            raise ValueError("College is not listed")
        self._college = college

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self,city):
        if city not in ["Khartoum","Dongola","Port Sudan"]:
            raise ValueError("City not listed")
        self._city = city


    def __str__(self):
        return f"Name:- {self.name}, College:- {self.college}, City:- {self.city} \n"
  
class Professor(Wizard): 
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
    def __str__(self):
        return f"Name:- {self.name}, Subject:- {self.subject}"

def main():
    wizard = Wizard("The National Ribat University")
    student = Student("Ahmed","IT","Dongola")
    professor = Professor("Ahmed Sayed","DevOps")
    print(wizard,student,professor)

if __name__ == "__main__":
    main()

        