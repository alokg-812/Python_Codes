str = "tHis IS gOING To bE eaSY"
str = str.lower()
lst = []
for i in str.split():
    lst.append(i[0].upper() + i[1:])
print(lst)
ans = ""
for i in range(len(lst)):
    ans += lst[i]
print(ans)

##########################################

# Approach 2:
'''
word = input().split()
ans = ""
for i in word:
    temp = ""
    c = i.lower()
    temp += c[0].upper()
    temp += c[1:len(c)]
    ans += temp
print(ans)
'''