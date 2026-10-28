#------REVERSE A STRING------
s = input("Enter a string: ")
rev = s[::-1]
print("Reversed string:", rev)

#-----USING LOOP----
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

#----CHARACTER COMPARISON-----
a = 'a'
b = 'a'
if a == b:
    print("Same characters")
else:
    print("Different characters")
    
    
#----String mein characters compare karna----
s = "apple"
if s[0] == s[4]:
    print("Same")
else:
    print("Different")
    
    
#----PALINDROME IN STRING------
s = input("Enter a string: ")
left = 0
right = len(s) - 1
is_palindrome = True
while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    
#---ISALPHA---
print("hello".isalpha())    # True
print("hello123".isalpha()) # False (digits hain)
print("hello world".isalpha()) # False (space bhi character hai)
print("".isalpha())         # False (empty string)

#----IS DIGIT----
print("2024".isdigit())     # True
print("12ab".isdigit())     # False
print("3.14".isdigit())     # False (dot hai)
print("-5".isdigit())       # False (minus sign hai)

#----ISALNUM----
print("abc123".isalnum())   # True
print("abc".isalnum())      # True
print("123".isalnum())      # True
print("abc 123".isalnum())  # False (space)
print("abc@123".isalnum())  # False (@ symbol)