a = 33
b = 200
if b > a:
  print("b is greater than a")

#--------------
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#----------------------
if a > b: print("a is greater than b")

#------------------------------------

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#-------------------------------
#WHILE

i = 1
while i < 6:
  print(i)
  i += 1

#------------
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#----------------------------
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#----------------------------------

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#---------------------------------
#FOR
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)  

#---------------------
for x in "banana":
  print(x)

#----------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#--------------------------

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#-----------------------------
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#------------------------------

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#------------------------------------

for x in [0, 1, 2]:
  pass      