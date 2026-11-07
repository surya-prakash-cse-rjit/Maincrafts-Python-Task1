# MAINCRAFTS TECHNOLOGY
# Python Programming Internship - Task 1
# Core Python Challenges
# Name: Surya Prakash



# 1. Sum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("Sum of two numbers is:", sum)


# 2. Odd or Even Checker
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# 3. Factorial Calculation
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial of", num, "is:", fact)


# 4. Fibonacci Sequence
n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Sequence:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# 5. String Reverse
text = input("Enter a string: ")
reverse = text[::-1]
print("Reversed string:", reverse)


# 6. Palindrome Check
word = input("Enter a word: ")
reverse = word[::-1]
if word == reverse:
    print("The word is a Palindrome")
else:
    print("The word is not a Palindrome")


# 7. Leap Year Check
year = int(input("Enter a year: "))
if year % 400 == 0:
    print("It is a Leap Year")
elif year % 100 == 0:
    print("It is not a Leap Year")
elif year % 4 == 0:
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")


# 8. Armstrong Number
num = int(input("Enter a number: "))
temp = num
sum = 0
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10
if sum == num:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")