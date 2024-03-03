str1 = 'abcba'
str2 = str1[::-1]
is_palindrome = True


for i,j in zip(str1,str2):
        if i !=j :
            is_palindrome = False
            break
        
if is_palindrome:
      print("Yes")
else :
      print("No")