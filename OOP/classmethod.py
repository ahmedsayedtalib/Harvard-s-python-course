class Student:
    def __init__(self,name,college):
        self.name = name
        self.college = college
        
    @classmethod
    def get(cls):
        name = input("Name:- \n")
        college = input("College:- \n")
        return cls(name,college)
    
    

def main():
    info = Student.get()

    print(info.name)


if __name__ == "__main__":
    main()