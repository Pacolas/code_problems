from typing import List
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:

    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        lt = []
        n= len(pairs)

        for i in range(n):
            actual = pairs.pop(i)
            cont = 0 
            for j in range(i):
                if actual.key>=pairs[j].key:
                    cont +=1
            pairs.insert(cont, actual)
            lt.append(pairs.copy())
        return lt