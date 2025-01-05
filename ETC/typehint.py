import sys

# print(len(sys.argv))

if len(sys.argv) == 1:
    print("Hello, Ahmed")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    print("Hello, Ahmed \n" * n)
else:
    print("There is an error, you must use -n param")