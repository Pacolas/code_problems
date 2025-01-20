class DynamicArray:
    
    def __init__(self, capacity: int):
        self.lt = []
        self.size = 0
        self.capacity = capacity


    def get(self, i: int) -> int:
        if self.size > i:
            return self.lt[i]


    def set(self, i: int, n: int) -> None:
        if self.size > i:
            self.lt[i] = n
            
        elif self.capacity > i:
            self.lt.insert(i, n)
            self.size = len(self.lt)

    def pushback(self, n: int) -> None:
        if self.size +1 > self.capacity:
            self.resize()
        self.lt.append(n)
        self.size +=1 


    def popback(self) -> int:
        item = self.lt.pop(self.size-1)
        self.size -= 1
        return item

        

    def resize(self) -> None:
        self.capacity =self.capacity *2



    def getSize(self) -> int:
        return self.size

    
    def getCapacity(self) -> int:
        return self.capacity
