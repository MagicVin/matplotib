#!/usr/bin/python3
list1 = [1,5,3,2,5,4,6,6,8,9,0]
list2 = [6,2,3,0,4,1]
listsub1 = list(set(list1))
print("listsub1 = " ,listsub1)
listsub1.sort(key=list1.index)
print("listsub1 = " ,listsub1)

print("list2 = ",list2)
list2.sort(key=list1.index)
print("list2.sort = ",list2)


#Atom Runner: sort.py

#listsub1 =  [0, 1, 2, 3, 4, 5, 6, 8, 9]
#listsub1 =  [1, 5, 3, 2, 4, 6, 8, 9, 0]
#list2 =  [6, 2, 3, 0, 4, 1]
#list2.sort =  [1, 3, 2, 4, 6, 0]
