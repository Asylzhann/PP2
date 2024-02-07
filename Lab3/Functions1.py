#1
def ounce(grams):
    print("ounces =",grams*28.3495231)
ounce(float(input("grams: ")))

#2
def celcius(fahrenheit):
    print("celcius =",(5/9)*(fahrenheit-32))
celcius(int(input("fahrenheit: ")))

#3
def solve(numheads, numlegs):
    print("rabbits =",int((numlegs-numheads-numheads)/2))
    print("chickens =",int(numheads-(numlegs - numheads - numheads)/2))
numheads = int(input("numheads: "))
numlegs = int(input("numlegs: "))
solve(numheads, numlegs)

#4
def filter_prime(n):
    c=0
    for i in range(1,n+1):
            if n%i==0:
                c=c+1
    return c==2
l=[x for x in map(int,input("list: ").split()) if filter_prime(x)]
print("primes:",l)

#5
from itertools import permutations
def permutate(s):
    p=permutations(s)
    for i in p:
        print(i)
permutate(input("string: "))

#6
def reverse(s):
    for i in range(len(s)):
        print(s[len(s)-i-1])
reverse(list(map(str, input("string: ").split())))

#7
def has_33(n):
    s=""
    for i in range(len(n)):
        s+=str(n[i])
        if(s.count("33")>=1):
            return "True"
    return "False"
print(has_33(list(map(int,input("numbers: ").split()))))

#8
def spy_game(n):
    s=""
    for i in range(len(n)):
        s+=str(n[i])
        if(s.count("007")>=1):
            return "True"
    return "False"
print(spy_game(list(map(int,input("numbers: ").split()))))

#9
import math
def volume(radius):
    return 4*math.pi*pow(radius,3)/3
print(volume(float(input("radius: "))))

#10
def unique(l):
    l.sort()
    for i in range(len(l)-1,0,-1):
        if(l[i]==l[i-1]):
            l.remove(l[i])
    print(l)
unique(list(input("list: ").split()))

#11
def pal(s):
    return s==s[::-1]
print(pal(input("phrase: ")))

#12
def histogram(l):
    for i in range(len(l)):
        print("*"*l[i])
histogram(list(map(int,input("list: ").split())))

#13
import random
def guess(s):
    r=random.randint(1,20)
    print(f"\nWell, {s}, I am thinking of a number between 1 and 20.")
    b=False
    i=0
    while(b==False):
        i+=1
        n=int(input("Take a guess\n"))
        if(r==n):
            print(f"\nGood job, {s}! You guessed my number in {i} guesses!")
            b=True
        elif(r>n):
            print("\nYour guess is too low.")
        else:
            print("\nYour guess is too high.")
guess(input("Hello! What is your name? \n"))