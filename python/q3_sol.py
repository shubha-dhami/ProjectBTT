arr = []

n = int(input("Enter size of the array: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Given array ", arr)
arr.sort()
print("Sorted array ", arr)