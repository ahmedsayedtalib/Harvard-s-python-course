from random import choice
from random import randint
from random import shuffle

coin = choice(['Ahmed','Sayed','Talib'])

print(coin)

x = randint(1,10)

print(x)

men = ['Ahmed','Sayed','Talib','Osman']

for man in men:
    shuffle(men)
    print(man, men)

