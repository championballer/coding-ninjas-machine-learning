n = int(input())

for i in range(1,n+1):
	for j in range(1,n+1):
		if j<=i:
			print(j,end="")
		else:
			print(" ",end="")

	for j in range(1,n+1):
		if n-j>=i:
			print(" ",end="")
		else:
			print(n-j+1,end="")
	print()