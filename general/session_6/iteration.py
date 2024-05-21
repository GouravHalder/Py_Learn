class Reverse:
    def __init__(self,data):
        self.data=data
        self.index= len(data)
    def __iter__(self):
        print ("__iter__")
        return self
    def __next__(self):
        print ("In __next__")
        if self.index==0:
            raise StopIteration
        else:
            self.index=self.index -1
            return self.data[self.index]
numbers=[1,2,3]
xx=Reverse(numbers)
yy=iter(xx)
for dd in yy:
    print (dd)
