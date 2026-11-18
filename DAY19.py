# DAY 19 — TWO POINTERS INTRODUCTION
# DSA WEEK 3

## 1. What is Two Pointers?

Two Pointers is a technique in which we use two variables
to track two different positions in an array or string.

- Left Pointer: Starts from the first index.
- Right Pointer: Starts from the last index.

Example:

arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

## 2. Left Pointer

The left pointer starts from index 0.

arr = [10, 20, 30, 40, 50]

left = 0

print(arr[left])

Output:
10

## 3. Right Pointer

The right pointer starts from the last index.

arr = [10, 20, 30, 40, 50]

right = len(arr) - 1

print(arr[right])

Output:
50

## 4. Moving Pointers

Left pointer moves forward:

left = left + 1

Right pointer moves backward:

right = right - 1

Example:

arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

left = left + 1
right = right - 1

print(arr[left])
print(arr[right])

Output:
20
40

## 5. Printing Elements From Both Ends

arr = [10, 20, 30, 40, 50]

left = 0
right = len(arr) - 1

while left < right:
    print(arr[left], arr[right])

    left = left + 1
    right = right - 1

Output:
10 50
20 40

## 6. Reverse an Array Using Two Pointers

arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left = left + 1
    right = right - 1

print(arr)

Output:
[5, 4, 3, 2, 1]

## 7. Why Two Pointers?

1. Reduces unnecessary work.
2. Avoids extra loops in many problems.
3. Helps solve array and string problems.
4. Can reduce extra space.
5. Useful for in-place operations.

## 8. Two Pointers Patterns

1. Opposite Direction:
   Left moves forward and Right moves backward.

2. Same Direction:
   Both pointers move forward.

3. Fast and Slow:
   One pointer moves faster than the other.

## 9. Time and Space Complexity

For reversing an array:

Time Complexity: O(n)
Space Complexity: O(1)

## 10. Practice Questions

1. Reverse an Array using Two Pointers.
2. Print pairs from opposite ends.
3. LeetCode 344 — Reverse String.
4. LeetCode 167 — Two Sum II (practice later).

## 11. Important Points to Remember

- left = 0
- right = len(arr) - 1
- left = left + 1
- right = right - 1
- while left < right

Two Pointers is an important DSA pattern used
to solve array and string problems efficiently.

# END OF DAY 19