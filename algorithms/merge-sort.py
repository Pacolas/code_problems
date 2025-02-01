class MergeSort():
    def __init__(self, lt):
        self.lt = lt
        self.size = len(lt)
        self.sorted = None
        
        
    def sort(self):
        result  = []
        if self.size != 1:
            pivot = (self.size)//2
    
            sublist1 = MergeSort(self.lt[:pivot]).sort()
            sublist2 = MergeSort(self.lt[pivot:]).sort()
            l1_size = len(sublist1)
            l2_size = len(sublist2)
            i = 0
            j = 0
            for _ in range(len(self.lt)):
                if i == l1_size:
                    result.append(sublist2[j])
                    j += 1  
                elif j == l2_size:
                    result.append(sublist1[i])
                    i += 1  
                elif sublist1 [i] < sublist2 [j]     :
                    result.append(sublist1[i])
                    i+=1
                else:
                    result.append(sublist2[j])
                    j += 1  

        else:
            result = self.lt

        self.sorted = result
        return result
                

    def __str__(self):
        if self.sorted is None:
            return str(self.lt)
        return str(self.sorted)


