Input= 'aaabbcc'
count=1
result=""
for letter in range(len(Input)):
    if letter< len(Input)-1 and Input[letter] == Input[letter+1]:
        count+=1
    else:
        result+= str(count)+Input[letter]
        count=1
print(result)