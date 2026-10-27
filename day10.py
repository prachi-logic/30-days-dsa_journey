#----------SET------
s = {1, 2, 3}
s2 = set([1, 2, 2, 3])   # {1, 2, 3}
empty = set()            # NOT {} (that creates a dict)


#---------UNIQUE ELEMENTS--------
nums = [1, 2, 2, 3, 3, 3]
print(set(nums))            # {1, 2, 3}
print(len(set(nums)))       # 3 distinct elements


#---CORE-----
s = set()
s.add(10)        
s.add(20)
s.remove(10)    
s.discard(99)    
print(len(s))


#----FIND DUPLICATE ELEMENTS-------
arr = [1, 2, 3, 2, 4, 1]
seen = set()
for num in arr:
    if num in seen:
        print("Duplicate:", num)
    else:
        seen.add(num)
        
#----SET OPERATIONS------
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


#-----PRATICE SESSION------
arr = [1, 2, 2, 3, 3, 4]
new=set(arr)
print(new)


nums = {10, 20, 30, 40} #check whether 30 and 50 exist in the set.
print(30 in nums)
print(50 in nums)

 #print all duplicate values only once.
arr = [4, 1, 2, 4, 3, 1]
new = set()
duplicates = set()
for num in arr:
    if num in new:
        duplicates.add(num)
    else:
        new.add(num)

print("Duplicates:", duplicates)
