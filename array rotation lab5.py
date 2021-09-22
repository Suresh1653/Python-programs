def rotateArray(arr,d):
    temp = []
    n=len(arr)
    for i in range(d,n):
        temp.append(arr[i])
    i = 0
    for i in range (0,d):
        temp.append(arr[i])
    arr=temp.copy()
    return arr
 
arr= []
t=int(input("enter size of array:"))
for i in range (t):
    k=int(input("Enter number:"))
    arr.append(k)
    
print("Array after left rotation is: \n")
print("enter where the rotation should start")
l=int(input())
print(rotateArray(arr,l))
