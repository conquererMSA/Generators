class PowerOfTwo:
    def __init__(self,maxValue):
        self.limit=maxValue
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.limit:
            result=self.current
            self.current=self.current*2
            return result
        else:
            raise StopIteration
maxLimit=int(input("Enter the max limit: "))
iterator_obj=PowerOfTwo(maxLimit)
# print(next(iterator_obj))
# print(next(iterator_obj))
# print(next(iterator_obj))
# print(next(iterator_obj))
# print(next(iterator_obj))
#print by for loop
# for num in iterator_obj:
#     print(num)

# Create coustom range function
class My_range:
    def __init__(self,start=0,stop=None,step=1):
        if self.stop==None:
            raise TypeError('My_range take argument 3, but got 0')
        self.start=start
        self.stop=stop
        self.step=step

    def __iter__(self):
        return My_range_iterator(self)

class My_range_iterator(object):

    def __init__(self,iterableObj):
        self.iterableObj=iterableObj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterableObj.start<self.iterableObj.stop:
           result=self.iterableObj.start
           self.iterableObj.start=self.iterableObj.start+self\
             .iterableObj.step
           return result
        else:
            raise StopIteration
a=My_range_iterator(1,5,1)
iterObj=iter(a)
print(next(iterObj))
print(next(iterObj))
print(next(iterObj))