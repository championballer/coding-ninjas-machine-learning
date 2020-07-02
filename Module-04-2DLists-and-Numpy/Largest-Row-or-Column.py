'''
	In order to print two or more integers in a line separated by a single 
	space then you may consider printing it with the statement, 

	print(str(num1) + " " + str(num2))

'''

from sys import stdin

def findLargest(arr, nRows, mCols):
	#Your code goes here
	
	maxRowSum = -2147483648
	maxRowIndex = 0
	maxColSum = -2147483648
	maxColIndex = 0
	
	for i in range(nRows):
		sum = 0
		for j in range(mCols):
			sum+=arr[i][j]
		
		if i == 0:
			maxRowSum = sum
			maxRowIndex = i
			
		if sum > maxRowSum:
			maxRowSum = sum
			maxRowIndex = i
	
	for i in range(mCols):
		sum = 0
		for j in range(nRows):
			sum+=arr[j][i]
		if i == 0:
			maxColSum = sum
			maxColIndex = i
		
		if sum > maxColSum:
			maxColSum = sum
			maxColIndex = i
	
	if maxRowSum >= maxColSum:
		print("row",maxRowIndex,maxRowSum)
	else:
		print("column",maxColIndex,maxColSum)

#Taking Input Using Fast I/O
def take2DInput() :
	li = stdin.readline().rstrip().split(" ")
	nRows = int(li[0])
	mCols = int(li[1])
	
	if nRows == 0 :
		return list(), 0, 0
	
	mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
	return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

	mat, nRows, mCols = take2DInput()
	findLargest(mat, nRows, mCols)

	t -= 1