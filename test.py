from array import array
import csv
with open('C:/Users/marku/Documents/Studium/FH/Algorithmen und Datenstrukturen/Labor/AuD-Projekt/csvDatensatz1.csv', 'r') as csv_datei:
    reader = csv.reader(csv_datei, delimiter=';')
    test1=[]
    for zeile in reader:
        test1.append(zeile)

with open('C:/Users/marku/Documents/Studium/FH/Algorithmen und Datenstrukturen/Labor/AuD-Projekt/csvDatensatz2.csv', 'r') as csv_datei:
    reader = csv.reader(csv_datei, delimiter=';')
    test2=[]
    for zeile in reader:
        test2.append(zeile)

#Fehlerhandhandhabung:
if (len(test1)!=len(test2)):
    print("Die Dateitypen sind Fehlerhaft und enthalten unterschiedlich viele Argumente, bitte überprüfen!")
    quit()
check = len(test1[0])

for i in range(len(test1)):
    if (len(test1[i])!= check):
        print("Fehler, der Datensatz 1 enthällt nicht genau gleich viele Argumente, bitte Überprüfen!")
check = len(test2[0])
for i in range(len(test2)):
    if (len(test2[i])!= check):
        print("Fehler, der Datensatz 2 enthällt nicht genau gleich viele Argumente, bitte Überprüfen!")
#---------------------------------------------------------------------------------------------------------------------------
#Testfälle Entwickler Test
#test1 = [[8,9,5,0],[3,2,1,0],[3,2,1,0]]
#test2 = [[4,5,6,7],[4,5,6,7],[4,5,6,7]]

def indexing (array1):
    indexes = []
    for i in range(len(array1[1])):
        indexes.append(i)
    return indexes    

#def zusammenführen (array1,array2):
    for i in range(len(array1)):
        for j in range(len(array1[i])):
            array1[i].append(array2[i][j])
    return array1

def tauschen(sortierungsRegel,array1, sortierungsIndex):
    for i in range(len(array1)):
        if (i != sortierungsIndex):
            temp = []
            for j in range(len(array1[i])):
                temp.append(array1[i][sortierungsRegel[j]])
            array1[i]=temp
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
#test1=zusammenführen(test1,test2)
indexes = indexing(test1)
welcherSollSortiertwerden = int(input("Nach Welcher Spalte soll sortiert werden?"))
#print(test1[welcherSollSortiertwerden])
temp,indexes = bubbleSort(test1[welcherSollSortiertwerden],indexes)
#print("Gesamtes Array")
#print(test1[welcherSollSortiertwerden])
#print(test1)
test1=tauschen(indexes,test1,welcherSollSortiertwerden)
print("Gesammtes Array getauscht:")
print(test1)