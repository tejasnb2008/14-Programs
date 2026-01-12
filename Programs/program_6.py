def sort_bubble(list1):
    length = len(list1)
    for i in range(length):
        for j in range(0, length - i - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

list1 = []
n = int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(n):
    item = int(input())
    list1.append(item)