import csv

studentName = input("Enter the student's name:- \n")
gpa = float(input("Enter the Students GPA:- \n"))

with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","GPA"])
    writer.writerow({"name":studentName,"GPA":gpa})
