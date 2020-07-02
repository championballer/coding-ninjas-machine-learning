n1 = int(input())
arr1 = [int(x) for x in input().strip().split(" ")]

n2 = int(input())
arr2 = [int(x) for x in input().strip().split(" ")]

result = 0
sum1 = 0
sum2 = 0
i,j = 0,0 
while i<n1 and j<n2:
    if arr1[i] < arr2[j]:
        sum1+=arr1[i]
        i+=1
    elif arr1[i] > arr2[j]:
        sum2+=arr2[j]
        j+=1
    else:
        result+=max(sum1, sum2)
        sum1, sum2 = 0,0
        
        while i<n1 and j<n2 and arr1[i]==arr2[j]:
            result+=arr1[i]
            i+=1
            j+=1

while i<n1:
    sum1+=arr1[i]
    i+=1

while j<n2:
    sum2+=arr2[j]
    j+=1

result+=max(sum1, sum2)

print(result)