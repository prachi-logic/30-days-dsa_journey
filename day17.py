
# ==========================================
# DAY 17 - BINARY SEARCH PRACTICE
# DSA WEEK 3
# ==========================================


# 1. HOW TO MOVE LEFT
# If middle element is smaller than target,
# search in the right half.

# nums = [10, 20, 30, 40, 50, 60, 70]

# target = 60

# left = 0
# right = len(nums) - 1

# mid = (left + right) // 2

# if nums[mid] < target:
#     left = mid + 1

# print("Updated Left:", left)


# 2. HOW TO MOVE RIGHT
# If middle element is greater than target,
# search in the left half.

# nums = [10, 20, 30, 40, 50, 60, 70]

# target = 20

# left = 0
# right = len(nums) - 1

# mid = (left + right) // 2

# if nums[mid] > target:
#     right = mid - 1

# print("Updated Right:", right)


# 3. WHEN TO STOP
# If target is found, return its index.
# If left becomes greater than right,
# the element is not present.


# 4. BINARY SEARCH USING FUNCTION

# def binary_search(nums, target):

#     left = 0
#     right = len(nums) - 1

#     while left <= right:

#         mid = (left + right) // 2

#         if nums[mid] == target:
#             return mid

#         elif nums[mid] < target:
#             left = mid + 1

#         else:
#             right = mid - 1

#     return -1


# Example 1: Element Present

# nums = [10, 20, 30, 40, 50]
# target = 30

# result = binary_search(nums, target)

# print("Result:", result)


# # Example 2: Element Not Present

# nums = [10, 20, 30, 40, 50]
# target = 100

# result = binary_search(nums, target)

# print("Result:", result)


# 5. DRY RUN

# nums = [2, 4, 6, 8, 10, 12, 14]
# target = 10

# left = 0
# right = len(nums) - 1

# while left <= right:

#     mid = (left + right) // 2

#     print("Left:", left)
#     print("Right:", right)
#     print("Mid:", mid)
#     print("Element:", nums[mid])

#     if nums[mid] == target:
#         print("Target Found at index:", mid)
#         break

    # elif nums[mid] < target:
    #     left = mid + 1

    # else:
    #     right = mid - 1


# 6. IMPORTANT CONDITIONS

# Target == nums[mid]
# Element found.

# Target > nums[mid]
# Move left = mid + 1

# Target < nums[mid]
# Move right = mid - 1

# left > right
# Search space is empty.


# 7. TIME AND SPACE COMPLEXITY

# Best Case: O(1)
# Average Case: O(log n)
# Worst Case: O(log n)
# Space Complexity: O(1)


# 8. PRACTICE QUESTIONS

# Q1. Find 30 in [10, 20, 30, 40, 50]

# Q2. Find 70 in [10, 20, 30, 40, 50, 60, 70]

# Q3. Find 100 in [10, 20, 30, 40, 50]

# Q4. Find 10 in [2, 4, 6, 8, 10, 12]


# 9. LEETCODE PRACTICE

# 704 - Binary Search
# 35 - Search Insert Position
# 374 - Guess Number Higher or Lower


# ==========================================
# END OF DAY 17
# ==========================================



nums = [10, 20, 30, 40, 50]
target = 30

left = 0
right = len(nums) - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        print("Element found at index:", mid)
        break

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1