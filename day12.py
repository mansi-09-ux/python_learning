#FOR LOOP PROBLEMS
#basic understanding
#1. print numbers from 1 to 10 in one line
for i in range(1, 11):
    print(i, end="")
#2. print even numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 == 0:
        print(i, end=" ")
#3. print odd numbers from 5 to 30 in one line
for i in range(5, 31):
    if i % 2 != 0:
        print(i, end=" ")
#4. print numbers divisible by 5 from 1 to 30 in one
# for i in range(1, 101):
    for i in range(1, 101):
        if i % 5 == 0 and i % 7 == 0:
            print(i, end=" ")
#5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
#6. sum of numbers from 10 to 25 
total = 0
for i in range(10, 26):
    total = total + i
print("Sum =", total)
#7. sum of numbers in any list
numbers = [10, 20, 30, 40, 50]

total = 0

for i in numbers:
    total = total + i

print("Sum =", total)
#8. multiplication table of a number 
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#interview problems
#9. factorial 
n = int(input("Enter a number"))

factorial = 1
for i in range(1, n+1):
    factorial = factorial * i
    print("Factorial=" , factorial)
    
#10. fibonacci 
n = int(input("Enter a number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#11. reverse a string
text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string:", reverse)
#12. count vowels in a string
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count = count + 1
print("Number of vowels =", count)
#13. count z's and y's in a string
text = input("Enter a string: ")
z_count = 0
y_count = 0
for ch in text.lower():
    if ch == "z":
        z_count = z_count + 1
    elif ch == "y":
        y_count = y_count + 1
print("Number of z's =", z_count)
print("Number of y's =", y_count)
#14. check whether a number is prime number or not 
n = int(input("Enter a number: "))
if n <= 1:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

#interview problems
#count digits
n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits =", count)
#reverse a number
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)
#palindrome number 
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")
#palindrome string (without slicing, built in function)
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")
#armstrong number
n = int(input("Enter a number: "))

original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
#print even numbers from 1 to 10g