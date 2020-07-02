## Read input as specified in the question.
## Print output as specified in the question.

import sys

result = list()

n = int(input())
if n==0:
    sys.exit()
arr = [int(x) for x in input().strip().split(" ")]

mx_element = arr[-1]
for i in range(n):
    if arr[n-i-1]>=mx_element:
        result.append(str(arr[n-i-1]))
        mx_element = arr[n-i-1]
        
result.reverse()
st = ""
for index,i in enumerate(result):
    st+=i
    if index!=len(result)-1:
        st+=" "
print(st)