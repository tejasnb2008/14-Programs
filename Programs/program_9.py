def linear_search(list1, key):
    for i in range(len(list1)):
        if list1[i] == key:
            return i
    return None

list1 = []
n = int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(n):
    item = int(input())
    list1.append(item)

print("The list contents are:", list1)
key = int(input("Enter the number to be searched: "))
pos = linear_search(list1, key)

if pos is None:
    print(key, "is not found in the list")
else:
    print(key, "is found at position", pos + 1)