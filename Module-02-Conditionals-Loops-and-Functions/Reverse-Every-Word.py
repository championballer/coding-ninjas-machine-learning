s = input()

def reverse(s):
	result = ""
	for index in range(len(s)):
		result+=s[len(s)-index-1]

	return result

to_reverse = s.split()
result = ""
for index,i in enumerate(to_reverse):
	result+=reverse(i)
	if index!=len(i)-1:
		result+=" "
print(result)
	