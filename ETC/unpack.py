import sys
import argparse
# def f(*args,**kwargs):
#     print("Args:- ", args)

# def g(*args,**kwargs):
#     print("Kwargs:- ", kwargs)

# f(100,300,400)

# g(Ahmed=500,Ali=300,Khalid=50)

parser = argparse.ArgumentParser(description="Ok Man from Sudan")
parser.add_argument("-n",default=1,type=int,help="Prints the output of your argument\n, IF not arg is provided, -n default is 1")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("Hello, Ahmed")