## 217 - Contains Duplicate
# Concept: dekhe hue numbers ko set me rakho, repeat mile to duplicate
nums = [1, 2, 3, 1]
seen = set()
duplicate = False
for x in nums:
    if x in seen:        
        duplicate = True
        break
    seen.add(x)          
print(duplicate)    


# 1929 - Concatenation of Array
# Concept: array ko 2 baar repeat karna

nums = [1, 2, 1]
ans = nums * 2          
print(ans)               


# 1470 - Shuffle the Array
# Concept: x = nums[i], y = nums[i+n], dono ko ek-ek karke daalo
nums = [2, 5, 1, 3, 4, 7]
n = 3
ans = []
for i in range(n):
    ans.append(nums[i])     
    ans.append(nums[i + n])  
print(ans)                 