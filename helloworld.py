""" """ #print("Hello World!")

#x = 5
#print(type(x))

#x = "Hello World"

#display x:
#print(x)

#display the data type of x:
#print(type(x))

#x = ["apple", "banana", "cherry"]

#display x:
#print(x)

#display the data type of x:
#print(type(x))

#x = True
#display x:

#display the data type of x:
#print(type(x))

#x = b"Hello"
#display x:
#print(x)

#display the data type of x:
#print(type)

#x = memoryview(bytes(5))

#display x:
#print(x)

#display the data type of x:
#print(type(x))

#x = int(20) int
#x = float(20.5) float
#x = complex(1j) complex
#x = list(("apple","banana","cherry")) list
#x = tuple(("apple", "banana", "cherry")) tuple
#x = range(6) range
#x = dict(name="John", age=36) 
#x = set(("apple","banana","cherry"))
#x = bytes(5)
# x = frozenset(("apple", "banana", "cherry"))
# #x = bool(5)
# # Convert a string to an integer
# #x = int("42")  # x will be 42

# """
# """ x = "Hello World"
# print(type(x)) 
# this is a str (string)
""" """

# Intengers is a whole number positive or negative, without decimals of unlimited length.
#x = 1
#y = 2.8
#z = 1j

#float, is a number positive or negative, containing one or more decimals. Can also be scientific with an "e".
#x = 1.10
#y = 1.0
#z = -35.59
""" x = 35e3
y = 12E4
z = -87.7e100


print(type(x))
print(type(y))
print(type(z))

x = 1 #int
y = 2.8 #float
z = 1j #complex
 """
#convert from in to float
#a = float(x)
#b = int(x)
#c = complex(x)

""" #convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

import random

print(random.randrange(7,10))

x = float(1)
print(x)
y = float(6.7)
print(y)
w = float("4.2")
print(w) """
#string both single and double quotation marks.
""" print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"') """
""" 
a = "Hello, World"
print(a[4])
# den väljer ut vilken bokstav den ska visa i koden,..01234..
for x in "Aicha":
    print(x) """
# you can  loop through the characters in a string, with a for loop. To use a length of a string use len() function.
#The len() function return the length of a string.
#a = "Hello, World!"
#print(len(a))
""" 
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.") """

""" #To check if certain phrase or character is NOT present in a string, we can use NOT IN.
txt = "THE BEST THINGS IN LIFE ARE FREE!"
print("expensive" not in txt)

txt = "The best thing in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

b = "Hello, World!"
print(b[:5])

#get the characters from position 2, and all the way to the end: You change the place to (b[2:]) it the beginning first.
b = "Hello, World!"
print(b[2:])

txt = "The best things in life are free!"
if "expensive" not in txt:
    print ("No, 'expensive' not in txt.")

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) #return "Hello, World!" removes any whitespace from the beginning or the end.

a = "Hello, World!"
print(a.replace("H", "B")) #you are replacing the letter H to B.

a = "Hello, World!"
print(a.split(","))

txt = " Hello World "
x = txt.strip()

#you are merging variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a "".
a = "Hello"
b = "World"
c = a + " " + b
print(c) """ """

#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#{price:.2f} formaterar värdet av variabeln price som ett flyttal (decimaltal) med två decimaler.
price = 59
txt = f"the price is {price:.2f} dollars"
#så här tar du matematisk tal {20 * 59} 
txt = f"The price is {20 * 59} dollars"
print(txt)

txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 

txt = "Hello\rWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt) 

txt = "Hello \bWorld!"
print(txt) #backspace

#first letter is Upper case:
txt = "hello, and welcome to my world"
x = txt.capitalize()
print(x)
# makes the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#20 characters taking up the space, banana in the middle.
txt = "banana"
x = txt.center(20)
print(x)
#"O" används för att fylle ut utrymmet på båda sidorna om "banana",
# så att den centreras i fältet med totalt 20 tecken.
txt = "banana"
x = txt.center(20, "O")
print(x)
#returns the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x) 
#Check if position 5 to 11 ends with the phrase "my world" true/false.
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x) 

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)  """
""" #fixed point two decimal, string format()
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

#{: <8} anger att talet 49 ska vänsterjusteras inom ett fält på 8 tecken.
txt = "We have {:<8} chickens"
print(txt.format(49))

#{:+}-formateringen lägger till ett plustecken (+) för positiva tal och ett minustecken (-) för negativa tal.
txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#{:-} formateringen indikerar om numret är negativt(positiva nummer visas utan tecken.)
txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

txt = "The universe is {:,} years old"
print(txt.format(13800000000))


txt = "The universe is {:_} years old."
print(txt.format(13800000000))
#to add a underscore character as a thousand separator

txt = "The binary version of {0} is {0:b}" #stands for binary
print(txt.format(5))

txt = "We have {:d} chickens."
print(txt.format(0b101))
#{:e} används för att formatera talet i vetenskaplig notation.
txt = "We have {:e} chickens."
print(txt.format(5))
#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars." #45.00 dollars.
print(txt.format(45))
#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars." # 45.000000 dollars. 
print(txt.format(45))

#Use "x" to convert the number into Hex format, if you want to use upper-case then use {0:X}
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))

#Use % to convert the number into percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))

#without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.25))
#Where in the text is the word "welcome"?Count from position 7.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) 

txt = "Company12" #true or false,isalnum means if all characters are alpanumeric,meaning alphabet letter(a-z) and numbers(0-9).
#Example of characters that are not alphanumeric: (space)!#%&? etc.
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)
#because you have a space between Company and 12,its a special sign then its false.

#check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x)
#check if all the characters in the text are ascii characters:
txt = "Company123"
x = txt.isascii()
print(x) 

txt = "1234"
x = txt.isdecimal()
print(x) 
#check if all characters in a string are decimals(0-9)

#checks if the characters in the text are digits:
txt = "50800"
x = txt.isdigit()
print(x) """

# to concatenate,or combine two strings you can use the +operator
a = "Hello"
b = "World"
c = a + b
print(c)
#you are adding space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#2f which means fixed point number with 2 decimals:
price = 59
txt = f"the price is {price:.2f} dollars"
print(txt)
#you can also peform math operations in the placeholder.
txt = f"The price is {20 * 59} dollars"
print(txt)
age = 36
txt = f"My name is Aicha, and I am {age}"
print(txt)
# followed by a legal formatting type, like .2f and if you just have variable then ex {price}.
#duble quotes use backslash
txt = "Aicha is the best \"Person\" from the north."
print(txt)
txt = "This will insert one \\ (backslash)."
print(txt)
txt = "Hello\nWorld!"
print(txt) 
#\r Carriage Return,moves the markup back to the beginning.So answer is "World".
txt = "Hello\rWorld!"
print(txt)
#tab
txt = "Hello\tWorld!"
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
#Upper case the first letter:
txt = "hello, and welcome to my world"
x = txt.capitalize()
print(x)
#if its a number then it wont effect anything
txt = "36 is my age."
x = txt.capitalize()
print(x)
#returns a string where all the characters are lower case.
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20, "B")
print(x)
#number of times the value apple appears.
txt = "I love apples"
x = txt.count("apple")
print(x)
#you can also add the position to search in by this word.
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)
#check if the string ends with a punctuation sign(.)true/false
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
#set the tab size to 2 whitespaces, but you can set by yourself a own number.
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
#finds the word in meaning in position.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
txt = "If you get bored, try again"
x = txt.find("bored")
print(x)
#where in the text is the first letter of "e" when you search between 5 and 10?
txt = "Hello, welcome to my World."
x = txt.find("e", 5, 10)
print(x)
#Use "," to add a comma as a thousand separator:
txt = "The universe is {:,} years old"
print(txt.format(13800000000))
#Use "b" to convert the number into binary format:{0:b}
txt = "The binary version of {0} is {0:b}"
print(txt.format(6))
##Use "f" to convert a number into a fixed point number, default with 6 decimals, 
# but use a period followed by a number to specify the number of decimals:
txt = "The price is {:.2f} dollars"
print(txt.format(45))
#without the ".2" inside the placeholder,this number will be displayed like this:
txt = "The price is {:f} dollars"
print(txt.format(45))
# use "o" to convert the number into octal format:
txt = "The octal version of {0} is {0:o}"
print(txt.format(10))
#Use "x" to convert the number into Hex format:
txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
#use "%" to convert the number into a percentage format:
txt = "You scored {:%}"
print(txt.format(0.25))
#without decimals
txt = "You scored {:.0%}"
print(txt.format(0.25))
#startposition for the word "welcome" i txt.0123456...
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
#same as find,exception the find() method returns -1 and index will raise an exception.
#Check if all the characters in the text are in lower case
txt = "hello world!"
x = txt.islower()
print(x)
#Check if all the characters in the text are numeric, this means also ² and ¾.
txt = "565543"
x = txt.isnumeric()
print(x)
#lstrip()method removes any leadin characters (space is the default leading character to remove).
txt = "    banana    "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
#use translate() method to replace any S characters with P character.
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

#if you want to replace a word you write the word first and then to change the word.
txt = "I like Peter"
x = txt.replace("Peter","Aicha")
print(x)
#söker sista förekomsten av en angiven sträng och returnerar dess index för andra förekomsten.Första börjar vid index 3 och andra 14.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
#kontrollera om alla tecken i strängen är printbara, tex inte kontrolltecken eller radbrytningar.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
#check if all the characters in the text are whitespaces:
txt = "   "
x = txt.isspace()
print(x) 
#example if not whitespaces:
txt = "   s   "
x = txt.isspace()
print(x) 
#if each word start with upper case letter.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) 
#this means also all characters.
a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())

#The join() method takes all items in an iterable and joins them into one string.
myTeam = ("John","Peter","Vicky")
x = "#".join(myTeam)
print(x)
#removing the leading characters ",.asw".
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)
#searches for a specific string and splits string into a tuple containing three elements.
# I if dosent found the word then returns the string empty.
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
#returns a 20 character long version of "banana".
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
#Make the lower case letters upper case and the upper case letters lower case:
txt = "Hello My Name Is Aicha"
x = txt.swapcase()
print(x)
