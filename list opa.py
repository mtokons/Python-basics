list = [2, 3, 5, 6, 7, 89, [[9,7],4,5,6,6]]


print(list[6][0][1])


list1 = [2, 3, 5, 6, 7, 89, 5]

list1.append(44)
list1.insert(2,90)
list1.extend([0,1,1])
list1 = list1 + [3,2,1]
list1.remove(89)
list1.pop()
list1.remove(list1[0])
list1.sort()

print(list1.index(6))

print(list1.count(5))

print(list1)


