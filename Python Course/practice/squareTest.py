from squareNum import squareNum
import pytest

def main():
    testNegative()
    testZero()
    testPositive()


def testNegative():
    assert squareNum(-2) == 4

def testZero():
    assert squareNum(0) == 0

def testPositive():    
    assert squareNum(1) == 1
    assert squareNum(3) == 9

def testStr():
    with pytest.raises(TypeError):
        squareNum("Cat")




if __name__ == "__main__":
    main()