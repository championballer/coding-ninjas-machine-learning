s = input()

words = s.strip().split(" ")
words.reverse()
output = ""

for index, word in enumerate(words):
    output+=word
    if index!=len(words)-1:
        output+=" "
        
print(output)
