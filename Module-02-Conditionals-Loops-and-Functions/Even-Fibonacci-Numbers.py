sum = 0
current = 1
next = 1
n = int(input())

while current<=n:
    if current%2==0:
	    sum+=current
    temp = current
    current = next
    next = next+temp

print(sum)