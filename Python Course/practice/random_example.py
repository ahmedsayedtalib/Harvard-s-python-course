import random
import sys

employees = [{'name':'Ahmed','job':'IT Admin'},
       {'name':'Mohamed','job':'IT Admin'},
       {'name':'Ali','job':'IT Admin'},
       {'name':'Omer','job':'IT Admin'},
       {'name':'Ameer','job':'Programmer'},
       {'name':'Ammar','job':'Sys Admin'},
       {'name':'Maha','job':'Sys Admin'},
       ]

if len(sys.argv) < 2:
    print("Insert the job title to be searched")


for emp in employees:
    if emp['job'] == sys.argv[1]:
        print(emp['name'], emp['job'], sep=", ")
    # else:
    #     print('No employee found with this job title')



