# Modules

import mymodule

mymodule.greeting("Jonathan")


person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


a = mymodule.person1["age"]
print(a)


import mymodule as mx

a = mx.person1["age"]
print(a)



import platform

x = platform.system()
print(x)



x = dir(platform)
print(x)


from mymodule import person1

print (person1["age"])