n = 5

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
    
#Right triangle
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    
#Number triangle
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
#pyramid triangle
n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)