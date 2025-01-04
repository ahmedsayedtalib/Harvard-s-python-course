import argparse

parser = argparse.ArgumentParser(description="Hello n times using argparse lib")
parser.add_argument("-n",help="Enter the number of hellos you want to print",default=1,type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("Hello, Ahmed")