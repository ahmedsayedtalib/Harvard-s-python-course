from names import main
from names import goodbye
import sys

if len(sys.argv) == 2:
    print(goodbye(sys.argv[1]))
else:
    print("Arguments are not clear")
