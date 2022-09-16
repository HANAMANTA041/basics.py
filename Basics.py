
"""Python statement ends with the token NEWLINE character (carriage return)
   The following Python script contains three statements in three separate lines."""
#print("id:",1)
#print("First Name:", "Stew")
#print("Last Name:","Jobs")

#Use backslash character \ to join a statement span over multiple lines
if 100>99 and\
   200<=300 and\
   True != False:
    print("Hello World")
#Please note that the backslash character spans a single statement in one logical line and multiple physical lines
# but not the two different statements in one logical line.
print("Hello \
 World!")#multiline statement

"""print("Hello")\
print("World") two statements in a one logical line leads to syntax error
Expressions in parentheses (), square brackets [ ], or curly braces { } can be spread over 
multiple lines without using backslashes."""
list = [1,2,3,4,
         5,6,7,8,
         9,10,11,12]
"""---------------------------------------"""
#Demonstration of if elif blocks
if 10>5: #first block starts
    print("10 is greater than 5")#1st block

    print("Now checking 20 is greater than 10")#1st block

    if 20 > 10:#1st block
        
        print("20 is greater  than 10")#inner block

else: #2nd block starts
    
    print("10 is less than 5")#2nd block

    print("This will never print")#2nd block
# is used for comment and
"""
comment1
comment2
comment3
"""

#Python Naming Conventions
"""An identifier should start with either an alphabet letter (lower or upper case) or an 
underscore (_). After that, more than one alphabet letter (a-z or A-Z), digits (0-9), 
or underscores may be used to form an identifier. No other characters are 
allowed.
Python coding standards tell us to use Snake Case eg. variable_name for 
variable names and Pascal Case for class names eg. StudentClass or Student.
Never use any keyword as variable name."""

#Display output:The print() serves as an output statement in Python. It echoes the value of any Python expression on the Python shell.
"""
print("Bengaluru", end = "*")
Bengaluru*
name = "Ram"
print(name)#display single variable
Ram
age = 21
print(name,age)#display multiple variable
Ram 21
print("Name :",name, "Age :",age)#display formmatted output
Name : Ram Age : 21


By default, a single space ' ' acts as a separator between values. However, any other 
character can be used by providing a sep parameter
a =10
a
10
b=20
b
20
c = 30
print(a, b, c, sep = "-")
10-20-30

In python by default print statement add new line , if we want to change end of the 
statement , we can do that by using end parameter.
print("Bengaluru", end = "#")"""

#Formatted String
"""%i -> int 
%d -> int
%f -> float
%s -> st

a = 10
b = 20
print("Value of a is %d and value of b is %d " %(a,b))
Value of a is 10 and value of b is 20

#Print with replacement operator:
naname = "Mary"
age = 22
Following are various ways for printing output using replacement operator.
print("Hello { } your age is { }".format(name,age)
 Hello Mary your age is 22
print("Hello { 0} your age is { 1}".format(name,age)
 Hello Mary your age is 22
print("Hello { 1} your age is { 0}".format(age, name)
 Hello Mary your age is 2me = "Mary"
age = 22
Following are various ways for printing output using replacement operator.
print("Hello { } your age is { }".format(name,age)
 Hello Mary your age is 22
print("Hello { 0} your age is { 1}".format(name,age)
 Hello Mary your age is 22
print("Hello { 1} your age is { 0}".format(age, name)
 Hello Mary your age is 22

#f-strings:To create an f-string, prefix the string with the letter " f "."""
name = "Hbs"
print(f"Hi {name}, How are you?.")

a = 10
b = 20
print(f"Addition of a and b is {a+b}")

name = "Odkar"
age = 22
print(f"Hello,My name is {name} and i'm {age} years old")

#Getting users input
"""The input() function is a part of the core library of standard Python distribution. It reads 
the key strokes as a string object which can be referred to by a variable having a suitable 
name.
The input() function has an optional string parameter that acts as a prompt for the user."""


#Variables: Are used to store the values in computer's memory

#primitive datatypes
"""
i)Integers – This data type is used to represent numerical data, that is, positive or 
 negative whole numbers without a decimal point. Say, -1, 3, or 6

ii)Float – Float signifies ‘floating-point real number.’ It is used to represent rational 
 numbers, usually containing a decimal point like 2.0 or 5.77.Since Python is a 
dynamically typed programming language, the data type that an object stores is 
mutable, and there is no need to state the type of your variable explicitly.

iii)String – This data type denotes a collection of alphabets, words or alphanumeric 
characters. It is created by including a series of characters within a pair of double or 
single quotes. To concatenate two or more Strings, the ‘+’ operation can be applied 
to them. Repeating, splicing, capitalizing, and retrieving are some of the other String 
operations in Python. Example: ‘blue,’ ‘red,’ etc.

iv)Boolean – This data type is useful in comparison and conditional expressions and 
can take up the values TRUE or FALSE
 
int:This data type is used for data with whole number.

x = 10
id(x) gives the address of x in memory

float:eg. y = 12.23: This data type is used for values with decimal point

complex:This data type is used for values with real and imaginary parts in numbers
       This is most commonly used in scientific computing
       eg. r = 1+2j :1 is real part of a number and 2 is imaginary part
print(r.real) => 1.0
print(r.imag) => 2.0

Bool:This datatype has only two values True and False
False, blank string,0,None these are false values
This datatype is mostly useful in comparison operation.

#Type Conversion:int():,float():,complex():,bool():,str():

int():
int(123.45) => 123
int(20+20j) => Invalid(Not possible)
int(True) => 1
int("10") => 10
We can convert from any data type to int type except complex type.
To convert string into int , string should be integral literal of base 10. eg. 
int("10.89")=>invalid

float():
float(123) => 123.0
float(20.9+20j) => Invalid(Not possible)
float(True) => 1.0
float("10.90") => 10.9
We can’t convert complex to float.
String literal should be decimal or float number

complex():
complex(x) => Here x is considered as real number and imaginary part is zero.
complex(10.5) => 10.5+0j
complex("10.5") => 10.5+0j
complex(False) => 0j
complex(1,2) => 1+2j
complex(True,False) => 1+0j
complex("10","10.5") => Invalid

Bool():Any type to boolean is possible
bool(12) => True
bool("name") => True
bool(1+2j) => True
bool(0) => False
bool(None) => False
bool(j) => invalid

str():Any data type to string convertion is possible
str(True) => 'True'
str(1) => '1'
str(12.7) => '12.7'
str(1+2j) => '1+2j'

Python is a dynamically typed programming language, the data type that an object stores is 
mutable, and there is no need to state the type of your variable explicitly.

All fundamental or primitive data types are immutable, once created we can’t 
change its value, if we try to change new object will get created.

None is similar to null
"""
#String Data Type
city = "Yadgiri"
print(city[0],city[-4],city[-1],city[5])

"""Slice Operator: It divides string into multiple pieces, syntax is 
string_name[begin:end], it slices string from begin index to end-1 index."""


print(city[1:3])
print(city[6:2])#empty result:bein value should be less than end value
print(city[3:6])
print(city[2:50])

"""S[:end] => default value for begin is 0.
S[begin:] => default value for end is end of the string.
S[:] => total string will be considered.
string_name[begin:end:step],default value for step is 1.
Step => +ve => Forward Direction(Trace string from left to right)
Step => -ve => Backward Direction(Trace string from right to left)
"""

print(city [::2])
print(city [::-1])
print(city.upper())

#split() method, Splits the string at the specified separator, and returns a list.
city_string = " My city name is Yadgiri"
print(city_string.split())
print(len(city))






