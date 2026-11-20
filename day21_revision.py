
# ==========================================
# DAY 21 - WEEK 3 REVISION
# Topics: Sorting, Binary Search, Two Pointers
# ==========================================


# ------------------------------------------
# 1. SORTING
# ------------------------------------------

print("\n----- SORTING -----")

arr = [5, 2, 8, 1, 3]

# Ascending Order
arr.sort()
print("Ascending:", arr)

# Descending Order
arr.sort(reverse=True)
print("Descending:", arr)


# ------------------------------------------
# 2. BINARY SEARCH
# LeetCode 704
# ------------------------------------------

print("\n----- BINARY SEARCH -----")


def binarySearch(arr, target):
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


nums = [-1, 0, 3, 5, 9, 12]
target = 9

print("Binary Search Index:", binarySearch(nums, target))


# ------------------------------------------
# 3. SEARCH INSERT POSITION
# LeetCode 35
# ------------------------------------------

print("\n----- SEARCH INSERT POSITION -----")


def searchInsert(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left


nums = [1, 3, 5, 6]
target = 2

print("Insert Position:", searchInsert(nums, target))


# ------------------------------------------
# 4. TWO POINTERS - REVERSE ARRAY
# ------------------------------------------

print("\n----- TWO POINTERS -----")


def reverseArray(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr


arr = [1, 2, 3, 4, 5]

print("Reversed Array:", reverseArray(arr))


# ------------------------------------------
# 5. TWO SUM II
# LeetCode 167
# ------------------------------------------

print("\n----- TWO SUM II -----")


def twoSum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left < right:

        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]

        elif total < target:
            left += 1

        else:
            right -= 1

    return []


numbers = [2, 7, 11, 15]
target = 9

print("Two Sum II:", twoSum(numbers, target))


# ------------------------------------------
# REVISION COMPLETED
# ------------------------------------------

print("\nWeek 3 Revision Completed!")
