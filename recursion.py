#--n to 1----
def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n - 1)
n = int(input("Enter a number: "))
print_num(n)


#---1 to n---
def show(n):
    if n == 0:
        return

    show(n - 1)
    print(n)

n = int(input("Enter a number: "))
show(n)

#----sum of n natural----

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)
n = int(input("Enter your number: "))
print(sum_n(n))

#---factorial---
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n - 1)
n = int(input("Enter your number: "))
print(fact(n))

#---raise to power----
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
a = int(input("Enter base: "))
b = int(input("Enter power: "))
print(power(a, b))


#----count the digits in a number------
def count(n):
    if n == 0:
        return 0
    return 1 + count(n // 10)
n = int(input("Enter your number to count digit : "))
if n == 0:
    print(1)
else:
    print(count(n))
    
    
#----sum of digits-----
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
n = int(input("Enter your number: "))
print(sum_digits(n))


#---products of digits-----
def product_digits(n):
    if n == 0:
        return 1
    return n % 10 * product_digits(n // 10)
n = int(input("Enter your number: "))
print(product_digits(n))


#----reverse a string-----
def reverse(s):
    if s == "":
        return s
    return reverse(s[1:]) + s[0]
s = input("Enter a string: ")
print(reverse(s))


#----check string is palindrome or not-----

def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])
s = input("Enter a string: ").lower()
if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")


#----fabocinni series----
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
for i in range(5):
    print(fib(i), end=" ")