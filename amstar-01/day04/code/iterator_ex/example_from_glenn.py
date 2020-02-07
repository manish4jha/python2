class generator(object):
    #make an arbitrary bunch of data
    data=['a','b','c','some string','this is the last item....']
    bottom=0
    top=len(data) 
    iterIndex=0
    
    def printit(self):
        for i  in range(self.bottom , self.top):
            print(self.data[i])
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iterIndex == self.top: 
            raise StopIteration
        else:
            returnValue=self.data[self.iterIndex]
            self.iterIndex = self.iterIndex + 1
            return(returnValue)        


if __name__ == '__main__':

    g=generator()
    g.printit()
    for item in g:
        print("This is the iteration loop: ", item)

