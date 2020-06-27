## Read input as specified in the question.
## Print output as specified in the question.

def reverse(s):
    result = ""
    for index in range(len(s)):
        result+=s[len(s)-index-1]
        
    return result

result = ""
n = int(input())
if n==0:
    print(0)
    exit
    
while n>0:
    if n%2==0:
        result+='0'
    else:
        result+='1'
    n = n//2
print(reverse(result))