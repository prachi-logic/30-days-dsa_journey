#-------CHARACTER FREQUENCY-----------

#--------FREQUENCY COUNTING-------

a = input("Enter your string: ")
target = input("Enter character to count: ")
count = 0
for ch in a:
    if ch == target:
        count += 1
print("Frequency:", count)


#---DICTIONARY----
student = {
    "name": "Prachi",
    "age": 19,
    "course": "BCA"
}


#---ACCESS VALUE IN DICTIONARY----
freq = {"b": 1, "a": 3, "n": 2}
print(freq["a"])

#----UPDATE----
freq["a"] = 4
print(freq)

#-------Character frequency using a dictionary-------
s = "banana"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)D