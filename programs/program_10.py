def binary_search(list1, key):
    first = 0
    last = len(list1) - 1
    while first <= last:
        mid = (first + last) // 2
        if list1[mid] == key:
            return mid
        elif key > list1[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return None

list1 = []
n = int(input("Enter number of elements: "))
print("Enter the elements (in ascending order):")
for i in range(n):
    item = int(input())
    list1.append(item)

print("The list contents are:", list1)
key = int(input("Enter the num to be searched: "))
pos = binary_search(list1, key)

if pos is None:
    print(key, "is not found")
else:
    print(key, "is found at position", pos + 1)