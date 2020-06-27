from sys import stdin

def selectionSort(arr, n) :
    #Your code goes here
	
    for i in range(n):
        mn_index = i
        for j in range(i+1,n):
            if arr[j]<arr[mn_index]:
                mn_index = j
        
        temp = arr[i]
        arr[i] = arr[mn_index]
        arr[mn_index] = temp
    
    return arr

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1