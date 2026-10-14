#1.. Print all elements
# arr=[10,20,30,40,50]
# for i in arr:
#     print(i)
    
# # 2 Print elements using indexes
# arr=[10,20,30,40,50]
# for i in range(len(arr)):
#     print(arr [i])
    
#3.Print elements using indexes
# arr = [5, 15, 25, 35, 45]
# print(arr[3])

# #4.Print the first and last element
# arr=[12, 24, 36, 48, 60]
# print(arr[0])
# print(arr[len(arr) - 1])

# #5.count array
# arr=[10,20,30,14,35]
# count=0
# for i in arr:
#     count+=1
# print("your count is", count)


#---beginner level-----
#1.sum of all element
# arr=[2, 4, 6, 8, 10]
# sum=0
# for i in arr:
#     sum+=i
# print(sum)

# #2. count even 
# arr=[2,4,5,6,7,10,11]
# count=0
# for i in arr:
#     if i %2==0:
#         count+=1
# print("your count even digits is :",count)


# #3,update element
# arr=[10,20,30,40,50]
# arr[2]=100
# print(arr)

# #4.double element
# arr=[1,2,3,4,5]
# for i in arr:
#     arr=i*2
#     print(arr)
    

# arr = [1, 2, 3, 4, 5]
# for i in range(len(arr)):
#     arr[i] = arr[i] * 2
# print(arr)


# # 5.reverse

# arr = [10, 20, 30, 40, 50]
# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i])


# sum ang avg
arr = [12, 5, 8, 21, 3, 16, 9]
sum=0
avg=0
for i in arr:
    sum+=i
    avg=sum/len(arr)
print(sum)
print(avg)

# find max or min
arr = [12, 5, 8, 21, 3, 16, 9]
max=arr[0]
min=arr[0]
for i in arr:
    if i> max:
        max=i
    if i< min:
        min=i
print(max,min)


# count even or odd
arr=[12, 5, 8, 21, 3, 16, 9]
even_count=0
odd_count=0
for i in arr:
    if i % 2==0:
        even_count+=1
    else:
        odd_count+=1
print("your even count is :", even_count)
print("your odd count is :",odd_count)


#10 se chhote elements ka count nikalo
arr=[12, 5, 8, 21, 3, 16, 9]
count=0
for i in arr:
    if i<10:
        count+=1
print("your small 10 digits number is :",count)

#Max element ka index batao
arr=[12, 5, 8, 21, 3, 16, 9]
max_index=0
for i in (len(arr)):
    if arr[i]>arr[max_index]:
        max_index=i
print("your max index is :", max_index)
