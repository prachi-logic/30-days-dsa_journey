
# ==================================================
# DAY 13 - STRING + COUNTING
# Topics:
# 1. Frequency Counting
# 2. Comparing Frequencies
# 3. Hashing Pattern
# ==================================================


# --------------------------------------------------
# 1. FREQUENCY COUNTING
# --------------------------------------------------
# Frequency means counting how many times
# each character appears in a string.

# Example: Count frequency of each character.

s = "banana"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequency:", freq)

# Output:
# {'b': 1, 'a': 3, 'n': 2}


# --------------------------------------------------
# 2. FREQUENCY COUNTING USING get()
# --------------------------------------------------
# get() returns the existing value of a key.
# If key does not exist, it returns 0.

s = "apple"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print("Frequency using get():", freq)

# Output:
# {'a': 1, 'p': 2, 'l': 1, 'e': 1}


# --------------------------------------------------
# 3. FREQUENCY COUNTING IN AN ARRAY
# --------------------------------------------------

arr = [2, 4, 2, 5, 4, 2]
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print("Number Frequency:", freq)

# Output:
# {2: 3, 4: 2, 5: 1}


# --------------------------------------------------
# 4. COMPARING FREQUENCIES
# --------------------------------------------------
# Anagram:
# Two strings are anagrams if they contain
# the same characters with the same frequency.

s1 = "listen"
s2 = "silent"

freq1 = {}
freq2 = {}

for ch in s1:
    freq1[ch] = freq1.get(ch, 0) + 1

for ch in s2:
    freq2[ch] = freq2.get(ch, 0) + 1

if freq1 == freq2:
    print("Anagram")
else:
    print("Not Anagram")

# Output:
# Anagram


# --------------------------------------------------
# 5. FIRST UNIQUE CHARACTER
# --------------------------------------------------
# Find the first character that appears only once.

s = "leetcode"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print("First Unique Character:", ch)
        break

# Output:
# First Unique Character: l


# --------------------------------------------------
# 6. HASHING PATTERN - DICTIONARY
# --------------------------------------------------
# Hashing helps store and access information quickly.
# Dictionary stores data in key-value pairs.

student = {
    "name": "Prachi",
    "marks": 85
}

print("Student Name:", student["name"])
print("Student Marks:", student["marks"])


# --------------------------------------------------
# 7. HASHING PATTERN - SET
# --------------------------------------------------
# Set stores only unique values.
# Duplicate values are automatically removed.

arr = [1, 2, 2, 3, 3, 4]

unique = set(arr)

print("Unique Elements:", unique)

# Output:
# {1, 2, 3, 4}


# ==================================================
# IMPORTANT CONCEPTS
# ==================================================

# 1. Frequency = Number of occurrences.
# 2. Dictionary = Key-value pairs.
# 3. Anagram = Same characters with same frequency.
# 4. Hashing = Efficient storage and lookup.
# 5. Set = Stores unique elements.
# 6. get(key, 0) = Returns value or 0 if absent.

# ==================================================
# TIME COMPLEXITY
# ==================================================

# Dictionary insertion = O(1) average
# Dictionary lookup = O(1) average
# Set lookup = O(1) average
# Frequency counting = O(n)
# Comparing two frequency dictionaries = O(k)
# where k is the number of distinct characters.

# ==================================================
# DAY 13 - LEETCODE PRACTICE
# ==================================================

# 1. Valid Anagram - 242
# 2. First Unique Character in a String - 387
# 3. Isomorphic Strings - 205
# 4. Ransom Note - 383

# ==================================================
# END OF DAY 13
# ==================================================
