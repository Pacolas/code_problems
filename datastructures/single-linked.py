from typing import List

class LinkedList:
    
    def __init__(self):
        self.size = 0
        self.head = None
    
    def get(self, index: int) -> int:
        result = -1
        if index < self.size:
            actual = self.head
            for _ in range (self.size):

                if index ==  _:
                    result = actual['value'] 
                    
                actual = actual['next']             
        return result
    def insertHead(self, val: int) -> None:
        node = {'next': self.head, 'value': val}
        if self.head is None:
            self.head = node
        else:
            self.head = node
        self.size +=1

        

    def insertTail(self, val: int) -> None:
        node = {'next': None, 'value': val}
        if self.head is None:
            self.head = node
        else:
            actual = self.head
            while actual.get('next') is not None:
                actual = actual['next']
            actual['next'] = node
        self.size +=1
        

    def remove( self, index: int) -> bool:

        result = False
        prev = None

        if index < self.size:
            actual = self.head
            prev = None
            for _ in range (self.size):
                if index ==  _ :
                    if prev is not None:
                        prev['next'] =  actual['next']
                    else:
                        self.head = self.head['next']

                    result =  True
                    self.size-=1
                elif index -1 == _  :
                    prev = actual
                actual = actual['next']
        return result


        

    def getValues(self) -> List[int]:
        result = []
        actual = self.head
        for _ in range (self.size):
            result.append(actual['value'])
            actual = actual['next']
        return result
