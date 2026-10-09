#local, global variable
a = 1
def f1():
    b = 2
    print(a)  # Global variable: 1   
    print(b)  # Local variable: 2
    print(c)   # Error: c is not defined in f1()
def f2():
    c = 2 
    print(a)  # Global variable: 1
    print(b)  # Error: b is not defined in f1()
    print(c)  # Global variable: 1   
f1()
f2()
print(a)   #1   
print(b)   # Error: b is not defined globally   
print(c)   # Error: c is not defined globally 

#call by value, call by reference
# call by value 
def f1(a):
    a = 100
a = 4
f1(a)
print(a)     #4 

#call by reference
def f2(a):
    a = [10, 20, 30]
    a[2] = 200
a = [1, 2, 3]
f2(a)
print(a)   #[1,2,3] 

def f3(a):
    a[2] = 200
a = [1, 2, 3]
f3(a)
print(a)    #[1,2,200]

# recursive funcntions
#factorial using recursion

# Factorial using recursion


# Factorial using recursion

def factorial(n):
    if n == 0 or n == 1:  # Base condition
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
# factorial 
# fibonacci

# Fibonacci series in Python

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c