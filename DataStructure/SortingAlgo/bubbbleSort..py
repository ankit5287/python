arr = [5,3,2,8,9]
n = len(arr)
for i in range(n):
    for j in range(n-1-i):
        if arr[i]<arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            
print(arr)