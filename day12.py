
# DAY 12 - HASHMAP PATTERN
# Topic: Key-Value, Frequency Map, O(1) Lookup
# LeetCode 383 - Ransom Note

# --------------------------------
# 1. HASHMAP BASICS
# --------------------------------

student = {
    101: "Prachi",
    102: "Aman",
    103: "Riya"
}

print("Student:", student[101])


# --------------------------------
# 2. FREQUENCY MAP
# --------------------------------

arr = [2, 3, 2, 5, 3, 2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency Map:", freq)


# --------------------------------
# 3. FREQUENCY MAP USING GET()
# --------------------------------

arr = [2, 3, 2, 5, 3, 2]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print("Using get():", freq)


# --------------------------------
# 4. HASHMAP LOOKUP
# --------------------------------

marks = {
    "Prachi": 85,
    "Aman": 90,
    "Riya": 88
}

print("Prachi's Marks:", marks["Prachi"])


# --------------------------------
# 5. LEETCODE 383 - RANSOM NOTE
# --------------------------------

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = {}

        # Count magazine characters
        for ch in magazine:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Check ransomNote characters
        for ch in ransomNote:

            if ch not in freq or freq[ch] == 0:
                return False

            freq[ch] -= 1

        return True


# Testing
obj = Solution()

print(obj.canConstruct("aa", "aab"))  # True
print(obj.canConstruct("a", "b"))     # False
print(obj.canConstruct("aa", "ab"))   # False


# --------------------------------
# TIME AND SPACE COMPLEXITY
# --------------------------------

# HashMap Lookup: O(1) Average
# Frequency Counting: O(n)
# LeetCode 383:
# Time Complexity: O(n + m)
# Space Complexity: O(1) for lowercase English letters
