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

g=myGenerator()
print(g) #genertor objct from class Generator
print(next(g)) # Hello world
print(next(g)) # MSA
# print generator value by for loop
for value in g:
    print(value) # Tata