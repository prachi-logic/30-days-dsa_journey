
# ==========================================
# DAY 15 - SORTING BASICS
# WEEK 3 - SORTING + BINARY SEARCH
# ==========================================


# 1. WHAT IS SORTING?
# Sorting means arranging elements in a particular order.
#
# Two types:
# 1. Ascending Order  -> Smallest to Largest
# 2. Descending Order -> Largest to Smallest
#
# Example:
# Original: [5, 2, 8, 1, 9, 3]
# Ascending: [1, 2, 3, 5, 8, 9]
# Descending: [9, 8, 5, 3, 2, 1]


# 2. WHY IS SORTING USEFUL?
# - Makes searching easier.
# - Helps find minimum and maximum elements.
# - Organizes data.
# - Binary Search requires sorted data.


# 3. SORTING IN ASCENDING ORDER

arr = [5, 2, 8, 1, 9, 3]

arr.sort()

print("Ascending Order:", arr)

# Output: [1, 2, 3, 5, 8, 9]


# 4. SORTING IN DESCENDING ORDER

arr = [5, 2, 8, 1, 9, 3]

arr.sort(reverse=True)

print("Descending Order:", arr)

# Output: [9, 8, 5, 3, 2, 1]


# 5. DIFFERENCE BETWEEN sort() AND sorted()

# sort() changes the original list.

arr = [5, 2, 8, 1]

arr.sort()

print("Using sort():", arr)

# sorted() creates a new sorted list.

arr = [5, 2, 8, 1]

new_arr = sorted(arr)

print("Using sorted():", new_arr)
print("Original List:", arr)

# Output:
# Using sorted(): [1, 2, 5, 8]
# Original List: [5, 2, 8, 1]


# 6. FIND SMALLEST AND LARGEST ELEMENT

arr = [45, 12, 89, 34, 5, 67]

arr.sort()

print("Smallest Element:", arr[0])
print("Largest Element:", arr[-1])

# Output:
# Smallest Element: 5
# Largest Element: 89


# 7. PRINT TOP 3 MARKS

marks = [45, 89, 67, 92, 56, 78]

marks.sort(reverse=True)

print("Top 3 Marks:", marks[:3])

# Output: [92, 89, 78]


# 8. TIME COMPLEXITY
#
# n = Number of elements
#
# Python sort() uses Timsort.
#
# Best Case    : O(n)
# Average Case : O(n log n)
# Worst Case   : O(n log n)
#
# O(n log n) is generally efficient for sorting.


# 9. PRACTICE QUESTIONS

# # Q1. Sort the list in ascending order.
arr = [10, 4, 7, 2, 15, 1]
arr.sort()
print(arr)

# # Q2. Sort the list in descending order.
arr = [23, 11, 45, 6, 18]
arr.sortr(reverse=True)
print(arr)

# Q3. Find the smallest and largest number.
# arr = [45, 12, 89, 34, 5, 67]

# Q4. Sort student marks and print top 3 marks.
# marks = [45, 89, 67, 92, 56, 78]


# ==========================================
# END OF DAY 15 - SORTING BASICS
# ==========================================
