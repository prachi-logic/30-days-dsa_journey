# nums = [1, 2, 3, 4, 5]
# pre = [0]                      # shuru mein 0
# for x in nums:
#     pre.append(pre[-1] + x)    # pichla total + naya number
# print(pre) 


nums = [5, 2, 8, 1, 4]
# Step 1: pre list banao
pre = [0]
for x in nums:
    pre.append(pre[-1] + x)

print(pre)   # [0, 5, 7, 15, 16, 20]

# Step 2: range sum
l = 1
r = 3
print(pre[r + 1] - pre[l])   # 11