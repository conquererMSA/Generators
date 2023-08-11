'''
What is Generator:A generator is a function which don't take any
parametre and return a generator object.
Generator objecet is a instance of class Generator.
Generator function er votorer kuno code exicute hoy na.
Generator er function line exicute korte hole function theke create kora variable built-in next function er
moddhye call korte hobe.Alada alada line print korar jonno alada
alada next() function call kortre hoy
'''
def myGenerator():
    yield"Hello world"
    yield"MSA"
    yield"Tata"

'''myGenerator function er sob yield value memory the save hy na. 
value print korar jonno next() method e call korle shudhu nirdisto 
value save hoy and amra print() e dekhte pai.
'''
g=myGenerator()
# print(g) #genertor objct from class Generator
# print(next(g)) # Hello world
# print(next(g)) # MSA
#
# print generator value by for loop
# for value in g:
#     print(value) # Tata
    #sob gulu print hobe na karon next() method diye protom duita
    # value print kora hoye geche.


def countDown_Generator(num):
    print("Start Countdown...")
    while num>0:
        yield num
        num-=1
nums=countDown_Generator(10)
print(next(nums)) #10
print(next(nums)) #9

#for loop e 8-1 porzonto print hobe karon generator function last
# state mone rakhe ebong arekbar call kora hole last exicution
# zekhane theme geche tarpor theke ek ek kore value return kore
print('.......')
for i in nums:
    print(i)


