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
for num in iterator_obj:
    print(num)
