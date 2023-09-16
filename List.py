thislist = ["apple", "banana", "cherry"]
print(thislist)

#-----------------

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#------------------

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#------------------

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#-------------------

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#-------------------

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#---------------------
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#--------------------

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#---------------------

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
  