end = 0
n = int(input())

for i in range(1,n+1):
    if i%2!=0:
        current = end+1
        for j in range(i):
            print(current,end=" ")
            current+=1
        print()
        end = current-1
    else:
        current = end+i
        end = current
        for j in range(i):
            print(current,end=" ")
            current-=1
        print()