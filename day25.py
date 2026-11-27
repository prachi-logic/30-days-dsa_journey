# DAY 25 — STACK AS A MEMORY STRUCTURE

## 1. What is Memory Structure?

Memory structure means how a computer stores and manages information while a program is running.

When a program executes, the computer needs to remember:
- Which function is running?
- What are the local variable values?
- Where should the program return after a function finishes?

For managing this information, programming languages use a **Call Stack**.

## 2. What is Call Stack?

Call Stack is a memory structure that manages function calls during program execution.

It follows the **LIFO (Last In, First Out)** principle.

The function called last will complete first.

## 3. Example in Python

```python
def A():
    print("Inside A")

def B():
    A()
    print("Inside B")

def C():
    B()
    print("Inside C")

C()
```

### Output

```text
Inside A
Inside B
Inside C
```

## 4. How Call Stack Works

### Step 1: C() is called

Stack:
```text
| C() |
```

### Step 2: C() calls B()

Stack:
```text
| B() |  <- Top
| C() |
```

### Step 3: B() calls A()

Stack:
```text
| A() |  <- Top
| B() |
| C() |
```

### Step 4: A() completes

A() is removed from the stack.

### Step 5: B() completes

B() is removed from the stack.

### Step 6: C() completes

C() is removed from the stack.

Final execution order:

```text
A() -> B() -> C()
```

## 5. What does a Stack Frame Store?

Every function call creates a stack frame.

It generally stores:

1. Local variables
2. Function arguments
3. Return information
4. Execution-related information

When a function completes, its stack frame is removed.

## 6. Applications of Call Stack

1. Managing function calls
2. Managing recursion
3. Remembering return locations
4. Managing local variables
5. Tracking program execution

## 7. Normal Stack vs Call Stack

| Normal Stack | Call Stack |
|---|---|
| Created and managed by programmer | Managed by programming runtime |
| Uses append() and pop() | Manages function calls and returns |
| Stores elements | Stores function execution information |

## 8. Important Terms

- LIFO: Last In, First Out
- Push: Adding an element
- Pop: Removing the top element
- Call Stack: Manages function calls
- Stack Frame: Information related to one function call
- Recursion: A function calling itself

## 9. Interview Definition

A stack is a memory structure used by a program to manage function calls. It stores information such as local variables, function arguments and return information. It follows the LIFO (Last In, First Out) principle.

## 10. Quick Revision

- Call Stack manages function calls.
- Every function call creates a stack frame.
- The last called function completes first.
- Completed functions are removed from the stack.
- Recursion also uses the Call Stack.

**DAY 25 CONCEPT COMPLETED!**
