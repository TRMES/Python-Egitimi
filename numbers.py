# Int veya tam sayı, sınırsız uzunlukta, pozitif veya negatif, ondalık sayılar içermeyen bir tam sayıdır.

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# Float, bir veya daha fazla ondalık sayı içeren pozitif veya negatif bir sayıdır.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Python'un rastgele sayı oluşturma işlevi yoktur , ancak Python'un rastgele sayılar oluşturmak için kullanılabilecek 
# random()yerleşik bir modülü vardır

import random

print(random.randrange(1, 10))