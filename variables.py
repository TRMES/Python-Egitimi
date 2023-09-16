# Python'un değişken bildirmek için bir komutu yoktur.("int" yada "string" gibi ifadelere gerek yoktur!)

x = 5
y = "Hello, World!"

# Değişken adları büyük/küçük harfe duyarlıdır.
a = 4
A = "furkan"

# Bir değişkenin veri tipini fonksiyonla alabilirsiniz
x = 5
y = "furkan"
print(type(x))
print(type(y))

# Python, tek satırda birden fazla değişkene değer atamanıza olanak tanır

x, y, z = "muz", "portakal", "çilek"
print(x)
print(y)
print(z)


# Global değişkenler hem fonksiyonların içinde hem de dışında herkes tarafından kullanılabilir.

x = "çok güzel."

def myfunc():
  print("Python " + x)

myfunc()