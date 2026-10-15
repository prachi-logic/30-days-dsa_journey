# ---Swapping numbers-----
a=10
b=20
a,b=b,a
print(a)
print(b)


# swap first and last elements
arr = [10, 20, 30, 40, 50]
arr[0],arr[4]=arr[4],arr[0]
print(arr)


#Swap elements at index 1 and index 3
arr=[5,10,15,20,25]
arr[1],arr[3]=arr[3],arr[1]
print(arr)

#Swap the first two elements
arr = [2, 4, 6, 8, 10]
temp=arr[0]
arr[0]=arr[1]
arr[1]=temp
print(arr)

#swap middle emlemets
arr = [11, 22, 33, 44, 55, 66]
arr[2],arr[3]=arr[3],arr[2]
print(arr)