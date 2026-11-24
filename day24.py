# DAY 24 — STACK (DSA)

## 1. What is Stack?

Stack is a linear data structure in which insertion and deletion happen from only one end.

**Real-life Example:** Stack of books or plates.

We add and remove books from the top.

## 2. LIFO (Last In First Out)

LIFO means the element inserted last will be removed first.

Example:

```python
stack = [10, 20, 30]
```

Here, 30 was inserted last, so 30 will be removed first.

## 3. Creating an Empty Stack

In Python, we can use a list to create a Stack.

```python
stack = []

print(stack)
```

Output:
```text
[]
```

## 4. PUSH Operation

Push means adding an element to the Stack.

In Python, we use `append()`.

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
```

Output:
```text
[10, 20, 30]
```

## 5. POP Operation

Pop means removing the top element from the Stack.

In Python, we use `pop()`.

```python
stack = [10, 20, 30]

stack.pop()

print(stack)
```

Output:
```text
[10, 20]
```

30 is removed because it was the top element.

## 6. TOP Operation

Top means checking the last element without removing it.

In Python, we use `stack[-1]`.

```python
stack = [10, 20, 30]

print(stack[-1])
```

Output:
```text
30
```

**Remember:** `stack[-1]` accesses the last element.

## 7. Complete Stack Program

```python
# DAY 24 - STACK

stack = []

# PUSH
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

# TOP
print("Top element:", stack[-1])

# POP
stack.pop()

print("After pop:", stack)

# TOP again
print("New top:", stack[-1])
```

Output:
```text
Stack: [10, 20, 30]
Top element: 30
After pop: [10, 20]
New top: 20
```

## 8. Time Complexity

| Operation | Time Complexity |
|---|---|
| Push | O(1) |
| Pop | O(1) |
| Top | O(1) |

## 9. Important Points

- Stack follows LIFO.
- Push adds an element.
- Pop removes the top element.
- Top checks the top element.
- Python List can be used to implement Stack.
- Never use `stack[-1]` on an empty Stack.

## 10. Practice Questions

1. Create an empty Stack.
2. Push 5, 10, 15 into the Stack.
3. Print the top element.
4. Remove one element using pop().
5. Print the updated Stack.
6. Find the top element after removing two elements.

## 11. LeetCode Practice

1. LeetCode 682 — Baseball Game
2. LeetCode 20 — Valid Parentheses
3. LeetCode 1047 — Remove All Adjacent Duplicates in String

**Today's Learning:** Stack, LIFO, Push, Pop and Top.