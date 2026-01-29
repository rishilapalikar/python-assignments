#Creating list
a = [1, 2, 3, 4, 5] # List of integers
b = ['apple', 'banana', 'cherry'] # List of strings
c = [1, 'hello', 3.14, True] # Mixed data types

print(a)
print(b)
print(c)    

#Accessing list
a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1])
print(a[1:4])

#Adding element to list
a.append(10)  
print("After append(10):", a)  

a.insert(0, 5)
print("After insert(0, 5):", a) 

#Removing elements from list
a.remove(30)  
print("After remove(30):", a)
