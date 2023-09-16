mytuple = ("apple", "banana", "cherry")

#----------------------------

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#----------------------------

thistuple = ("apple",)
print(type(thistuple))

#bu tuple değil
thistuple = ("apple")
print(type(thistuple))

#----------------------------

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#----------------------------

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#-----------------------------

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#----------------------------

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#-----------------------------

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#------------------------------

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])