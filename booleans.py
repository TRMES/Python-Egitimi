# Bir if ifadesinde bir koşulu çalıştırdığınızda Python True veya False değerini döndürür.

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b a'dan daha büyüktür")
else:
  print("a b'den daha büyüktür")

# Bir fonksiyonun Boolean cevabına göre kod çalıştırabilirsiniz  

def myFunction() :
  return True

if myFunction():
  print("EVET!")
else:
  print("HAYIR!")