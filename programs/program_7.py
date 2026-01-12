sort_bubble(list1)
print("The sorted list is:")
for i in range(len(list1)):
    print(list1[i], end=" ")
def sort_selection(list1):
    length = len(list1)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if list1[j] < list1[min_index]:
                min_index = j
        list1[i], list1[min_index] = list1[min_index], list1[i]

list1 = []
n = int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(n):
    item = int(input())
    list1.append(item)

sort_selection(list1)
print("The sorted list is:")
for num in list1:
    print(num, end=" ")