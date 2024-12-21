sen = 'this,is,not,as,hard,as,you,think,it,is'
D = dict()
for word in sen.split(','):
    for char in word:
        if char not in D:
            D[char] = 0
        D[char] += 1

mchar, mval = '', 0
alpha = 'abcdefghijklmnopqrstuvwxyz'
for char in alpha:
    if char not in D:
        continue
    if D[char] >=mval:
        mval = D[char]
        mchar = char
    
print(mchar) # output will be s as s and i both have 5 frequencies of occurances but s comes later in the alpha string
