def insertion_sort(list1):
    n = len(list1)
    for i in range(1, n):
        temp = list1[i]
        j = i - 1
        while j >= 0 and temp < list1[j]:
            list1[j + 1] = list1[j]
            j = j - 1
        list1[j + 1] = temp

list1 = []
n = int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(n):
    item = int(input())
    list1.append(item)

insertion_sort(list1)
print("The sorted list is:")
for i in list1:
    print(i, end=" ")