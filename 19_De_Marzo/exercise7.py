list1 = []

list1.append("Gabriela")
list1.append("Steven")
list1.append("Kenneth")
list1.append(18)
list1.append(True)
list1.append(3.14)

print(list1)
print(type(list1))

list2 = [1,2,3,4,5,]
print(list2)

list3 = list(range(1,21))
print(list3)

list4 = list()
list4.append(1)
list4.append(list1)
print(list4)
tam = len(list4)
print(tam)