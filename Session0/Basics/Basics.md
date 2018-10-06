# Basics

## Python Variables:
Python is dynamically-typed so you don’t need to declare the type of a variable you assign it.

```python
num1 = 8
num2 = 5
	
sum = num1 + num2
diff = num1 - num2
product = num1 * num2
division = num1 / num2

print(sum)
print(diff)
print(product)
print(division)
```

We have initialized two variables (named num1 & num2) and assigned them values.
Also we have initialized four variables (named sum, diff, product, division) and have assigned them values as their names suggest.

And later on we have printed the values.

So, let's see the output-

	13
	3
	40
	1.6

So, it is how we can use Python as a calculator.

Now let's see the type of the variables, and to get that we are going to use a funcion named type():

```python
print(type(sum))
print(type(division))
```

In this function we have passed the variables, whose type we want to find.
So, let's see the output-

```python
<class 'int'>
<class 'float'>
```

So, it gave the type of data this variable holds.

**Task- Try this and get the type of all the variables that we left.**

---

## Introduction to Strings-
String is a sequence of characters, and when taken in use is enclosed inside double quotes.

```python
greet = "Good Morning"
name = "Amrit"
	
print(greet + " " + name)
```

So, in this code segment we have taken two strings and assigned them into variables and then have concatenated the strings using plus.
So, here is the output-

	Good Morning Amrit

Now initialize another variable age and set any value to it.

```python
age = 18
```

Now think what could be the output for the below code-

```python
print("Hello" + " " + name + ", your age is " + age)
```

So, let's see the output-

```python
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print("Hello" + name + ", your age is " + age)
TypeError: must be str, not int
```

Why this happened? So, let's look into the error. It said "TypeError: must be str, not int", that age must be `str` not `int`. It mean we can't concatenate a string and a number.

So, we need to `typecast` age into a string. So, to achieve that, replace "age" with "str(age)", which will typecast age into a string.

Now the code becomes-

```python
print("Hello" + " " + name + ", your age is " + str(age))
```
and Let's see the output-

```python
Hello Amrit, your age is 18
```

Now, it looks fine.

---

## Decision making statements:
Let's talk about decision making statements. This includes if statements, if else statements, elif statements, nested if conditions.

```python
age = int(input("Please enter your age: "))
if age > 18:
	print("You can vote")
else:
	print("You can't vote")
```

So, what output do you expect? Let's see-

```python
Please enter your age: 17
You can't vote
```
See, if I entered age to be 17 which is less than 18, the if part didn't work as the condition was not satisfied and so, the else part worked.

```python
Please enter your age: 40
You can vote
```

In this case, the if part was satisfied as the age is greater than 18, so the if part run.

> Some of the keynotes-
> input() function which takes input from user, and we have typecasted it to 
> an integer value as the input function always takes input as string.

Let's look into another code:
```python
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num1 > num2:
	print(str(num1) + " is greater than "  + str(num2))
elif num1 < num2:
	print(str(num1) + " is less than " + str(num2))
else:
	print("Both numbers are equal")
```

So, what could be the outputs-

```python
Enter 1st number: 10
Enter 2nd number: 15
10 is less than 15
```
I think you may have got the concept which loop run and why?

**Task: Veify this for other set of values**

> Note: I think you have must note down something that the space used
> after each if or elif or else keyword. This is indentation
> Python programs get structured through indentation, i.e. code blocks are
> defined by their indentation.


> So, how does it work? All statements with the same distance to the right
> belong to the same block of code

---

## Loops:

### For loops:
In this part we are going to learn about Python Loops and various conditions that we can use to control Python loops.

Let's see a code-

```python
for i in range(11):
	print(2*i)
```

So, what is your expected output? Let's see-

```python
0
2
4
6
8
10
12
14
16
18
20
```

This loop will execute the print() statement 11 times in which value of `i` ranges from `i = 0` to `i = (11 - 1) = 10` and hence is the output.
If you have noticed that loop started from i = 0. If you like to change its range to start from 1, then do as below-

```python
for i in range(1,11):
	print(2*i)
```

And here is the output-
```
2
4
6
8
10
12
14
16
18
20
```

There is again a thing to note down, that everytime print statement executes on a new line. What if we didn't want this, this could be changed as below-

```python
for i in range(1,11):
	print(2*i , end = '    ')
```

And here is the output-

```python
2    4    6    8    10    12    14    16    18    20
```

As default it is set that after every statement cursor should move to new line, and here we changed the end to new tab space. If we change that new space to noting then on next print, the line will continue from the last print.

**Task- Try this**

---

## List:
A list in Python is a heterogeneous container for items, which can be written as a list of comma-separated values (items) between square brackets.

```python
languages = ['C++','Python','Scratch']
```

We have initialized a list named languages with elements as strings. We can see the list by just printing it.

	['C++', 'Python', 'Scratch']

So, you see it's a list. 

Now, let's add an element to it-

```python
languages += ['Java']
```

So, we just added an element to the list. Let's again view this list by printing it. So, here is the output-

	['C++', 'Python', 'Scratch', 'Java']

So, you see we were able to add an element into the list.

We can also add lists inside lists. Let's have a try-

	['C++', 'Python', 'Scratch', 'Java', ['Ruby', 'Javascript']]

This is how we can add lists inside lists.

---

## Functions:

