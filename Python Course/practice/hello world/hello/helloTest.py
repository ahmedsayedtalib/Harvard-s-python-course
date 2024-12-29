from hello import hello
import pytest

def main():
    hello_test()

def hello_test(name):
    assert hello() == "Ahmed"
    
if __name__ == "__main__":
    main()