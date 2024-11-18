""" #adds zeros until 10 characters long, if the value of the len is less than length of the string,no filling is done.
txt = "50"
x = txt.zfill(10)
print(x)
#does it starts with "Hello" then true/false.
txt  = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
#or check if position 7 to 20 starts with the characters "wel"
txt = "Hello,welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)
#to add a element to the fruits list, any type of element:
fruits = ['apple','banana','cherry']
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b) #combine a and b.
print(a)
#Remove all elements from the fruits list:
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

#copies the fruit list,but it copies only the list so if you change x it dosent affect it.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

print(10 + 5)

x = 5
y = 3

print(x + y)

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2

x = 5
print(x)

x = 5
x *= 3
print(x)

x = 5
x -= 3
print(x)

x = 5
x *= 3
print(x)

x = 5
x /= 3
print(x)

x = 5
x//=3
print(x)

x = 5
x**=3
print(x) #samma värde som 5 upphöjt till 3.Så 5 x 5 x 5 = 125.

x = 5
x &= 3
print(x)

x = 5
x **= 3
print(x)

x = 5
x |= 3
print(x)

x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

x = 5
y = 3

print(x != y) #not equal to so true!

x = 5
y = 3

print(x >= y) #returns true because 5 is greater or equal to 3.

x = 5
print(x > 3 and x < 10)
#returns True because 5 is greater than 3 AND 5 is less than 10. The and operator, Returns True if both statements are true.

x = 5
print(x > 3 or x < 4)

#(5 is > greater than 3, but 5 is not less < than 4)returns True because one of the conditions are true

a = str(100)
b = int(a)
c = type(b)
print(c)
#Type Conversion

quote = 'to be or not to be'
print(quote.upper()) #to uppercase letters.

quote = 'never late than sorry'
print(quote.capitalize()) #Capitalized letters.

#create a int
birth_year = input('what year were you born?')
age = 2024 - int(birth_year)
print(f'your age is: {age}')

study_year = input('How long time have you study here?')
age = 2024 - int(study_year)
print(f'you have studied here: {age} year')

single_year = input('How long have you been single?')
age = 2024 - int(single_year)
print(f'You have been single in {age} years')

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)

basket = ['a','x','b','c','d','e','d']
#basket sort

print(sorted(basket)) # the new list sorted.
print(basket) #the orginal list. """

""" 
basket = ['a','x','b','c','d','e','d']
basket.sort() #you sort the list first 
basket.reverse() #and then reverse.
print(len(basket)) #the length of the list. """

# list unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)

#tuples

mytuple = ( "apple", "banana", "cherry", "apple","banana") #tuples are written with round brackets if you put len()function you can count them.
print(len(mytuple))

thistuple = ("apple",)#if you create tuple with only one item,you have to add comma after the item,otherwise python will not regonize it as tuple. 
print(type(thistuple))

#a tuple with strings,integers and boolen values: a string, a intenger,a boolean,intenger,string
tuple1 = ("abc", 34, True, 40, "male")

mytuple = ("apple," "banana" ,"cherry")
print(type(mytuple))#if you want to know the datatype

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #print the second item

#negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry" ) #create a tuple
y = list(thistuple) #convert the tuple to a list
y.append("orange") #add "orange" to the list"
thistuple = tuple(y)#convert the modified list back to a tuple.
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)#you put a comma when tuple is single element.
thistuple += y #adds elements of y to the end of thistuple.
print(thistuple)

thistuple = ("apple", "banana", "cherry")  # Create a tuple
y = list(thistuple)  # Convert the tuple to a list
y.remove("apple")  # Remove the element "apple" from the list
thistuple = tuple(y)  # Convert the modified list back to a tuple
print(thistuple)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red) #you are unpacking the values back into variables.The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

fruits = ("apple", "banana", "cherry","strawberry","raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) #rest of the values as a list called "red"

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) #apple
print(tropic) #takes the ones with no values so mango-pineapple
print(red)#cherry
#puts the rest in brackets: ['mango', 'papaya', 'pineapple']

thistuple = ("apple", "banana", "cherry") #return the length of the tuple,witch is 3
for i in range(len(thistuple)): #creates a senquence of numbers starting from 0 up to 3.
  print(thistuple[i]) #the for loop accesses each element of the tuple using the index i and prints it.

thistuple = ("apple", "banana", "cherry")
i = 0 #first element in the tuple. i = 0, i = 1 , i = 2
while i < len(thistuple): #i of thistuple is printed.
    print(thistuple[i])
    i = i + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple","banana","cherry")
mytuple = fruits * 2 #multiplies with 2,mades a new tuple.

print(mytuple)
tuple1 = (1,2,3)
tuple1 = tuple1 * 2

thisset = {"apple", "banana", "cherry"}
print(thisset) #sets can not have duplicate values it will be ignored and are unchangeable.

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)#sets contains diffrent values and are unsorted.
print(False == 0)
thisset = {False, 0, "apple"}
print(thisset)

set1 = {"abc", 34, True, 40, "male"}
print(type(set1)) #datatype 'set'.

thisset = set(("apple", "banana", "cherry")) #note the double round-brackets, using the set() constructor to make a set.
print(thisset)

thisset = {"apple","banana","cherry"}
print("banana" not in thisset) #if banana is not in thisset.Once a set is created, you cannot change its items, but you can add new items.

thisset = {"apple", "banana", "cherry"}
thisset.add("aicha")
print(thisset)

#or use update method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

myset = {1, 2, 3, 4, 5}
myset.add(6)
myset.remove(2)
print(myset)