arr = [5,3,2,8,9]

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

