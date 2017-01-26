"""Python 3.6.0
Georgia Barnes
Appends input into a list and sorts in ascending order"""

def start(listA):
    n = int(input("How many numbers would you like to sort? "))
    for i in range(int(n)):
        x = int(input("Enter numbers(one at a time): "))
        listA.append(int(x))
    listsort(listA)
    print(listA)
    
"""BubbleSort    
def listsort(listA):
    for passnum in range(len(listA)-1,0,-1):
        for i in range(passnum):
            if listA[i]>listA[i+1]:
                listA[i],listA[i+1] = listA[i+1],listA[i]"""


"""Selection sort
def listsort(listA):
    for fillslot in range(len(listA)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if listA[location]>listA[positionOfMax]:
                positionOfMax = location

        listA[fillslot],listA[positionOfMax] = listA[positionOfMax],listA[fillslot]"""

"""insertion sort
def listsort(listA):
    for i in range(1,len(listA)):
        currentvalue = listA[i]
        position = i

        while position>0 and listA[position-1]>currentvalue:
            listA[position] = listA[position-1]
            position = position-1

        listA[position] = currentvalue"""

"""shell sort
def listsort(listA):
    sublistcount = len(listA)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(listA,startposition,sublistcount)
        sublistcount = sublistcount//2

def gapInsertionSort(listA, start,gap):
    for i in range(start+gap,len(listA),gap):

        currentvalue = listA[i]
        position  = i

        while position>=gap and listA[position-gap]>currentvalue:
            listA[position] = listA[position-gap]
            position = position-gap
        listA[position] = currentvalue"""

#quick sort
def listsort(listA):
    quickSortHelper(listA,0,len(listA)-1)

def quickSortHelper(listA,first,last):
    if first<last:
        
        splitpoint = partition(listA,first,last)

        quickSortHelper(listA,first,splitpoint-1)
        quickSortHelper(listA,splitpoint+1,last)

def partition(listA,first,last):
    pivotvalue = listA[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and listA[leftmark] <= pivotvalue:
            leftmark = leftmark+1
        while listA[rightmark]>=pivotvalue and rightmark >= leftmark:
            rightmark = rightmark-1
        if rightmark<leftmark:
            done = True
        else:
            listA[leftmark],listA[rightmark] = listA[rightmark],listA[leftmark]
            
    listA[first],listA[rightmark] = listA[rightmark],listA[first]

    return rightmark
              

if __name__== "__main__":
    start(listA = [])


