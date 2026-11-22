
# ==========================================
# DAY 23 - SLIDING WINDOW
# ==========================================

# 1. WHAT IS SLIDING WINDOW?
#
# Sliding Window is a technique used to solve
# array and string problems efficiently.
#
# It works on a continuous part of an array.
#
# Instead of calculating everything again,
# we add a new element and remove an old element.


# ==========================================
# 2. TWO POINTERS
# ==========================================

# left  = Starting index of window
# right = Ending index of window

arr = [2, 4, 1, 5, 3, 6]

left = 0
right = 2

# Window = [2, 4, 1]
# Window Length = right - left + 1


# ==========================================
# 3. TYPES OF SLIDING WINDOW
# ==========================================

# A. FIXED SIZE WINDOW
#
# Window size remains constant.
# Example: Maximum sum of 3 consecutive elements.
#
# B. VARIABLE SIZE WINDOW
#
# Window size can increase or decrease.
# Expand using right pointer.
# Shrink using left pointer.


# ==========================================
# 4. FIXED SIZE WINDOW
# ==========================================

# Problem:
# Find maximum sum of k consecutive elements.

arr = [2, 4, 1, 5, 3, 6]
k = 3

# Calculate first window sum
total = sum(arr[:k])

max_sum = total

# Slide the window
for right in range(k, len(arr)):

    # Add new element
    total += arr[right]

    # Remove old element
    total -= arr[right - k]

    # Update maximum sum
    max_sum = max(max_sum, total)

print("Maximum Sum:", max_sum)

# Output: 14


# ==========================================
# 5. VARIABLE SIZE WINDOW
# ==========================================

# Problem:
# Find longest subarray whose sum <= k.
# This example uses positive numbers.

arr = [2, 1, 3, 2, 1]
k = 5

left = 0
total = 0
max_length = 0

for right in range(len(arr)):

    # Expand window
    total += arr[right]

    # Shrink window if condition is invalid
    while total > k:

        total -= arr[left]
        left += 1

    # Calculate window length
    length = right - left + 1

    # Update maximum length
    max_length = max(max_length, length)

print("Maximum Length:", max_length)

# Output: 2


# ==========================================
# 6. IMPORTANT FORMULAS
# ==========================================

# Window Length:
# right - left + 1

# Expand:
# right += 1

# Shrink:
# left += 1

# Fixed Window:
# Add new element
# Remove old element


# ==========================================
# 7. TIME COMPLEXITY
# ==========================================

# Sliding Window usually takes O(n) time
# because both pointers move forward.


# ==========================================
# 8. LEETCODE PRACTICE
# ==========================================

# 643 - Maximum Average Subarray I
# Fixed Size Window
# https://leetcode.com/problems/maximum-average-subarray-i/

# 209 - Minimum Size Subarray Sum
# Variable Size Window
# https://leetcode.com/problems/minimum-size-subarray-sum/

# 1004 - Max Consecutive Ones III
# Variable Size Window
# https://leetcode.com/problems/max-consecutive-ones-iii/


# ==========================================
# END OF DAY 23
# ==========================================
