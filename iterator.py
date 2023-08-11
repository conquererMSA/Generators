'''
Iteration: A process of taking each item of something one after
another. [1,4,7,88,44,2]

Iterator: An iterator is an object that allows programmers to
travers through a sequence of data without storing the data in the
memory.

Iterable: An object which able perform iteration process on it.
Built in iter() method iter-obj return kore. ei object class
List_iterator theke ase.

next() method call kore iterable obj er protiti item access kora zay.
for loop diye ierable obj er sob gulu item eksathe access kora zay.
                 iterable     vs    iterator
magic method __iter__            __iter__ and __next__ thake
'''
# li=[1,2,3]
# iterObj=iter(li)
# print(iterObj) #<list_iterator object at 0x000001D610E29300>
# print(type(iterObj)) # <class 'list_iterator'>

nums=[1,4,6,78,]
numsObj=nums.__iter__()
print(numsObj) #list_iterator
print(type(numsObj)) #<class "list_iterator">
print(numsObj.__next__()) #1
print(numsObj.__next__()) #4
print(numsObj.__next__()) #6

# Check an input obj iterator or iterable
inputObj=iter(eval(input("Enter the obj: ")))


