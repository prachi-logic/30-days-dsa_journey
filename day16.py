
# ==========================================
# DAY 16 - BINARY SEARCH
# DSA WEEK 3
# ==========================================

# 1. WHAT IS BINARY SEARCH?
# Binary Search is used to search an element
# in a sorted array.
# It divides the search space into two halves.


# 2. BASIC EXAMPLE

arr = [10, 20, 30, 40, 50, 60, 70]

target = 50

left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        print("Element found at index:", mid)
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


# 3. BINARY SEARCH USING FUNCTION

def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


numbers = [5, 10, 15, 20, 25, 30]

result = binary_search(numbers, 20)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


# 4. SEARCHING AN ELEMENT NOT PRESENT

arr = [10, 20, 30, 40, 50]

target = 100

result = binary_search(arr, target)

print("Result:", result)


# 5. DRY RUN

arr = [10, 20, 30, 40, 50, 60, 70]
target = 60

left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    print("Left:", left)
    print("Right:", right)
    print("Mid:", mid)
    print("Middle Element:", arr[mid])

    if arr[mid] == target:
        print("Target found!")
        break

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


# 6. IMPORTANT POINTS

# left = Starting index
# right = Ending index
# mid = Middle index
# Search space = Remaining part of array

# Time Complexity:
# Best Case: O(1)
# Average Case: O(log n)
# Worst Case: O(log n)

# Space Complexity: O(1)


