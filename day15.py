def add(a, b):
    print('add function') #add function
    c = a + b 
    return c 
    pirnt('HI')
def sub(a, b):
    print('sub function')  #sub function
    c = a - b
    return 
def div(a, b):
    print('div function')  #div function
    c = a / b 
x = add(10, 15)   
y = sub(20, 10)   
z = div(25, 10)   
print(x)   #25
print(y)   #10
print(z)   #5
print()

# #Type of arguments
# def detail(name, age, rollno):
#     print(f'My name is {name}') #my name is rakesh
#     print(f'My age is {age}')   #my age is 20
#     print(f'My rollno is {rollno}')  #my rollno is A101
# detail('rakesh', 20, 'A101')
# detail(20, 'A101', 'rakesh')
# detail(age=20, rollno='A101', name='rakesh')
# detail(rollno='A101', age=20, name='rakesh')
# def add(a, b=10, c=20):
#     return a + b + c   #31
# print(add(1)) 
# print(add(1,2))
# print(add(1,2,3))
# print(add(c=3, a=1, b=2))  

# #order of = in function def
# def sub(a=10, b, c):
#     pass 
# #order of = in function call.
# add(a=10, b, c)

# def f1(*a):
#     print(a)
#     print(type(a))
# f1(1,2,3,4)

# def f2(**a):
#     print(a)
#     print(type(a))
# f2(1,2,3,4)
# f2(a=1, b=2, c=3, d=4)