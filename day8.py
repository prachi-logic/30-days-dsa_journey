#------STRING-------
a = "123"
b = 123
print(type(a))  
print(type(b))  

#----STRING INDEXING----
word = "PYTHON"

print(word[0])  
print(word[1])  
print(word[2])  
print(word[3])   
print(word[4])  
print(word[5])  

#---NEGATIVE 
print(word[-1])   
print(word[-2])  
print(word[-3])  
print(word[-4])


#-----TRANSVERSING----

#1.USING LOOP
WORD="PRACHI"
for ch in WORD:
    print(ch)
    
#2.INDEXING
WORD="DIWALI"
for i in range (len(WORD)):
    print(WORD[i])
    
#----Count vowels-----
word = "education"
count = 0
for ch in word:
    if ch in "aeiou":
        count += 1
print(count)

#----len function----
word="prachi"
print(len(word))


#-----Comparing characters using indexes-----
a="naman"
if a[0]==a[-1]:
    print("same")
else:
    print("different")
    
    
#-----Count occurrences of a character-----
a='aeroplane flying in the sky'
target='i'
count=0
for ch in a:
    if ch==target:
        count+=1
print(count)


#-----SLICING-----
A='PRACHI'
print(A[1:5])
print(A[1:])
print(A[:2])
print(A[:])

#---reverse a string----
print(A[::-1])


