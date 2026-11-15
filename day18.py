
# ==========================================
# DAY 18 - BINARY SEARCH VARIATIONS
# ==========================================

# Topics:
# 1. First Occurrence
# 2. Last Occurrence
# 3. Lower Bound
# 4. Upper Bound


# ==========================================
# 1. FIRST OCCURRENCE
# ==========================================

# Find the first position of target.
# When target is found, search LEFT.

def firstPosition(arr, target):

    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            right = mid - 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


# ==========================================
# 2. LAST OCCURRENCE
# ==========================================

# Find the last position of target.
# When target is found, search RIGHT.

def lastPosition(arr, target):

    left = 0
    right = len(arr) - 1
    ans = -1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            ans = mid
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return ans


# ==========================================
# 3. LOWER BOUND
# ==========================================

# Find the first element >= target.

def lowerBound(arr, target):

    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] >= target:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1

    return ans


# ==========================================
# 4. UPPER BOUND
# ==========================================

# Find the first element > target.

def upperBound(arr, target):

    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid
            right = mid - 1

        else:
            left = mid + 1

    return ans


# ==========================================
# 5. MAIN PROGRAM - TESTING
# ==========================================

arr = [1, 2, 4, 4, 4, 4, 7, 9]
target = 4

print("Array:", arr)
print("Target:", target)

print("First Occurrence:", firstPosition(arr, target))
print("Last Occurrence:", lastPosition(arr, target))
print("Lower Bound:", lowerBound(arr, target))
print("Upper Bound:", upperBound(arr, target))

# Count occurrences
count = upperBound(arr, target) - lowerBound(arr, target)

print("Total Occurrences:", count)


# ==========================================
# OUTPUT
# ==========================================

# Array: [1, 2, 4, 4, 4, 4, 7, 9]
# Target: 4
# First Occurrence: 2
# Last Occurrence: 5
# Lower Bound: 2
# Upper Bound: 6
# Total Occurrences: 4
