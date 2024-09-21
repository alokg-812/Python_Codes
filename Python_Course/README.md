## Why Programming???
*Ans:* Language needed to be learnt to communicate with computer.


## Why Python only???
*Ans:* Beacause python is very widely spoken, easy to understand and very powerful language.

### Ex-
```
print("Hello")
```
**Output:** 
```
Hello
```
### Ex-
```
print("*")
print("**")
print("***")
print("****")
print("*****")
```
**Output:** 
```
*
**
***
****
*****
```

#### Is it possible to print multiple statements in a same print statement???
**Ans:**
100% __Yes__ we can do that as the following way:
```
print("Hello India", "Hello Madrasians")
```
**Output:**
```
Hello India, Hello Madrasians
```
>[!NOTE]
>* We can use multiple statements while printing them.
>* Only **()** are allowed to print statements.
>* We can print anything we want to inside the "" thing.
>* If want to print any type of number, be it whole number or any decimal number, they are not written inside these " ".

## Variables:
Variables are containers on RAM used to store data values.
Ex:
```
x = 10
y = "Hello India"
```
**Explanation:**
- x is storing the integer value 10.
- y is storing the string value "Hello India".
Ex:
```
age = 10
Age = 12
name = "Alok"
print(age)
print(Age)
print(name)
```
**Ouput:**
```
10
12
Alok
```
**Explanation:**
- age, Age & name are storing the values
  
>[!TIP]
>* Variables should have _meaningful_ names.
>* Python is case-sensitive, so Age and age are different variables.

## Input Taking:
_Ans:_ We can take input from the user using the **input()** function.

Ex:
```
name = input("Enter your name: ")
print("Hello", name)
```
**Output:**
```
Enter your name: Alok
Hello Alok
```
>[!Note]
>If taking input, the input's default type would be **string.**

```
print("Hello, type your name here:")
n=input()
print("Which place are you from?")
p = input()
print("Hello!", n, "How is the weather in", p,"?")
print("What is your age?")
age = int(input())
print("Good to know you are", age, " years old")
```
**Output:**
```
Hello, type your name here:
Alok
Which place are you from?
Bengaluru
Hello! Alok How is the weather in Bengaluru ?
What is your age?
19
Good to know you are 19  years old
```

### Variables v/s Literals:
**Literals** are the constants that appear directly in the program and can be assigned to the variables.
```
print("Enter the radius of the circle:")
rad = int(input())
area = 3.14 * rad * rad
print("The area of the circle with",rad,"is:",area)
```
>[!Note]
>* area, rad are the variables here
>* while 3.14 is the constant value used hence it is a literal

## Datatypes:
```
n=10
print(n)
p=6.3
print(p)
s = 'Python'
print(s)
print("n is of type:", type(n))
print("p is of type:", type(p))
print("s is of type:", type(s))
```
**Output:**
```
10
6.3
Python
n is of type: <class 'int'>
p is of type: <class 'float'>
s is of type: <class 'str'>
```
>[!Note]
>* these 'int', 'float', 'str' are different data types.
>* python is a **_Dynalmically Typed Programming Lang_** and hence it automatically fetch what type of data it has been provided.

👉 We will discuss about different datatypes later but for now, we need to know only that python has different datatypes(like int, float, string, bool, list).

### To explicitly convert a certain datatype into another suitable datatype can be done by following method:
This is also known as _**Type conversion**_
```
n = 10.71
p = int(n)
print(type(n)) #float
print(type(p)) #int
a = 10
b = float(a) 
print(type(a)) # int
print(type(b)) #float
c = 10
d = str(c)
print(type(c)) #int
print(type(d)) #str
```
**Output:**
```
<class 'float'>
<class 'int'>
<class 'int'>
<class 'float'>
<class 'int'>
<class 'str'>
```
>[!Note]
>* 0 represent _true_ rest any value represent _false_ part except the null value.

## Operators & Expressions:

Let's take an example:
```
n = 10+13*2
```
* Here, we all know that by default nature is left to right and hence we will evaluate this as first _10+13_ as _23_ and then _23*2_ is _46_ but ans is _**36**_. But question is **why** so???
**Ans:** It is because we have some mathematical rules in the python language. Here while doing some operations, we term them as **_Operator Precedence._**
* Here, the correct answer would be _36_.
* If you want to completely go in the left to right direction only, you can use brackets.
* Ex:
  ```
  n = ((10+13)*2)
  ```

  ### Types of Operators:
  In python, we have 3 major types of operators named as:
  * Arithmetic Operators
    - (+, -, *, /, //, % , **)
  * Relational Operators
    - (<, >, <=, >=, ==, !=)
  * Logical Operators
    - (and, or, not)

⭐Arithmatic Operator
```
print("Addition: ", 7+3)
print("Subtraction:", 7-3)
print("Multiplication:", 7*3)
print("Division:", 7/3) #leaves quotient as a floating-point number
print("Floor Division:", 7//3) #leaves quotient
print("Modulo:", 7%3) # leaves remainder
print("Power:", 7**3) # leaves 7 raise to the power of 3
```
**Output:**
```
Addition:  10
Subtraction: 4
Multiplication: 21
Division: 2.3333333333333335
Floor Division: 2
Modulo: 1
Power: 343
```
⭐Relational Operator
```
print("Equal to (7 == 3):", 7 == 3)            # Checks if 7 is equal to 3
print("Not equal to (7 != 3):", 7 != 3)        # Checks if 7 is not equal to 3
print("Greater than (7 > 3):", 7 > 3)          # Checks if 7 is greater than 3
print("Less than (7 < 3):", 7 < 3)             # Checks if 7 is less than 3
print("Greater than or equal to (7 >= 3):", 7 >= 3)  # Checks if 7 is greater than or equal to 3
print("Less than or equal to (7 <= 3):", 7 <= 3)     # Checks if 7 is less than or equal to 3
```
**Output:**
```
Equal to (7 == 3): False
Not equal to (7 != 3): True
Greater than (7 > 3): True
Less than (7 < 3): False
Greater than or equal to (7 >= 3): True
Less than or equal to (7 <= 3): False
```
⭐Logical Operator
```
print(True and True)
print(False or True)
print(not True)
```
**Output:**
```
True
True
False
```
