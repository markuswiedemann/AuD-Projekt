from array import array


test1 = [[8,9,5,0],
        [3,2,1,0],
        [3,2,1,0]]
test2 = [[4,5,6,7],
        [4,5,6,7],
        [4,5,6,7]]
def indexing (array1):
    indexes = []
    for i in range(len(array1[1])):
        indexes.append(i)
    return indexes


    

def zusammenführen (array1,array2):
    for i in range(len(array1)):
        for j in range(len(array1[i])):
            array1[i].append(array2[i][j])
    return array1

def tauschen(itemIndex1,itemIndex2,array1):
    temp = []
    for i in range(len(array1)):
        temp.append(array1[i][itemIndex1])
    
    for j in range(len(array1)):
        array1[j][itemIndex1]=array1[j][itemIndex2]
        array1[j][itemIndex2]=temp[j]
    return array1

def bubbleSort(arr,indexes):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                indexes[j], indexes[j + 1] = indexes[j + 1], indexes[j]
    return arr,indexes


    
#TESTS----------------------------------------------
test1=zusammenführen(test1,test2)
indexes = indexing(test1)
print(test1[0])
temp,indexes = bubbleSort(test1[0],indexes)
print(temp)
print(indexes)
#print(test)
#print(test1)
#print(test1[1])
#test1=tauschen(2,4,test1)
#print(test1)