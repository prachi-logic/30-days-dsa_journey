
# DAY 20 - TWO POINTERS + STRINGS

# 1. Left and Right Comparison

s = "hello"

left = 0
right = len(s) - 1

while left < right:
    print(s[left], s[right])
    left += 1
    right -= 1


# 2. Reverse a String

s = list("python")

left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

print("Reversed String:", "".join(s))


# 3. Check Palindrome

s = "madam"

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1

else:
    print("Palindrome")


# 4. Check Palindrome using User Input

s = input("Enter a string: ")

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1

else:
    print("Palindrome")
