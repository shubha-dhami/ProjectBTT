arr = input("Enter elements of array: ");
arr = arr.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort()
print(arr)
