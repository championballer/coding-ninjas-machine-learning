from sys import stdin

def spiralPrint(arr, nRows, mCols):
	#Your code goes here
	p1 = [0,0]
	p2 = [0,mCols-1]
	p3 = [nRows-1, mCols-1]
	p4 = [nRows-1,0]
	
	while p1[0]<=mCols//2 and p1[1]<=nRows//2:
		
		for i in range(p1[1],p2[1]+1):
			print(arr[p1[0]][i],end=" ")
			# print(arr[p1[0]][i],end=" ")
		
		for i in range(p2[0]+1, p3[0]+1):
			print(arr[i][p2[1]],end=" ")
			# print(arr[i][p2[1]],end=" ")
			
		for i in range(p3[1]-1,p4[1]-1,-1):
			print(arr[p3[0]][i],end=" ")
			# print(arr[p3[0]][i],end=" ")
			
		for i in range(p4[0]-1,p1[0],-1):
			print(arr[i][p4[1]],end=" ")
			# print(arr[i][p4[1]],end=" ")
			
		p1[0],p1[1] = p1[0]+1, p1[1]+1
		p2[0],p2[1] = p2[0]+1, p2[1]-1
		p3[0],p3[1] = p3[0]-1, p3[1]-1
		p4[0],p4[1] = p4[0]-1, p4[1]+1

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
	spiralPrint(mat, nRows, mCols)
	print()

	t -= 1