import sys

def equilibriumIndex(arr):
	# Please add your code here
	larr = list([0])
	rarr = list([0])
	
	for i in range(len(arr)-1):
		larr.append(larr[i]+arr[i])
		rarr.append(rarr[i]+arr[len(arr)-i-1])
		
	#print(larr)
	#print(rarr)
	for i in range(len(larr)):
		if larr[i]==rarr[len(arr)-i-1]:
			return i
	return -1

# Main
n = int(input())
if n==0:
    print(-1)
    sys.exit()

    
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
