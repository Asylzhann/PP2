#1
def sqgen(n):
    for i in range(1,n+1):
        yield i*i
n=int(input("N: "))
print(*sqgen(n))

#2
def evgen(n):
    for i in range(0,n,2):
        yield i
n=int(input("n: "))
print(*evgen(n),sep=", ")

#3
def divgen(n):
    for i in range(0,n):
        if i%3==0 or i%4==0:
            yield i
n=int(input("n: "))
print(*divgen(n))

#4
def squares(a,b):
    for i in range(a,b+1):
        yield i*i
a=int(input(("a: ")))
b=int(input(("b: ")))
for i in squares(a,b):
    print(i,end=" ")
print()

#5
def revgen(n):
    for i in range(n,-1,-1):
        yield i
n=int(input("n: "))
print(*revgen(n))