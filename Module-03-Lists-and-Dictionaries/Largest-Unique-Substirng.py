s = input()

result = ""
length = 0
map = {}
for i in range(len(s)):
    current = ""
    map.clear()
    map[s[i]] = 1
    for j in range(i,len(s)):
        if i==j:
            continue
        else:
            if s[j] in map:
                if j-i>length:
                    length = j-i
                    result = s[i:j]
                break
            else:
                map[s[j]] = 1
                
print(result)