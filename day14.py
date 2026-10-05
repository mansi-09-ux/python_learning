n=6
for r in range(1,n+1):
    for c in range(r):
        print(1, end=' ')
    print()
   
#increasing number pattern 
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#same number pattern    
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()


#continues pattern
n = 4
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end="")
        num += 1
    print()


#number triangle
n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
    
#alphabet pattern
n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end="")
    print()


#same alphabet pattern
n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end="")
    print()
    
    
#alphabet pyramid
n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print(chr(65 + j), end="")
    print()
    
    
#diamond alphabet
n = 5
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print(chr(65 + j), end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print(chr(65 + j), end="")
    print()