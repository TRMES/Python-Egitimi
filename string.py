print("Hello World")

 # a="merhaba"      # metinin 2. indexini yazdırdım
 # print(a[2])
 
 # for x in "apple":   # "aplle" metnini b ye atayıp for döngüsüyle alt alta yazdırdım
 #     print(x)
  
 # a = "bugün sen nasılsın"     # metnin içindeki uzunluğu buldum (boşlular dahil)
 # print(len(a))  
 # 
 # dosya = "bu belgeler önemli"    # "belgeler" diye bir kelime a'nın içinde varsa true yazdırcak
 # print("belgeler" in dosya)                         
 # 
 # if "önemli" in dosya:             # yukarının devamı: "önemli" diye bir kelime varsa if-else yapıyor
 #     print("Doğru")
 # else:
 #     print("Yanlış")

# a = "hayvanat bahçesi"
# print(a[2:7])
# print(a[:5])
# print(a[-5:-2])     # NOT: geriden index sayarken 0'dan başlamıyor (-1,-2,-3...) diye sonda saymaya başlanır
# print(a[3:0]) # bunu yazdırmıyor
# print(a[-9:-5])
# print(a.upper())   # hepsini büyük harf yaptı
# print(a.lower())   # hepsini küçük harf yaptı
# print(a.replace("a","e"))   # "a"ları "e" yaptı
# print(a.split(" "))   # arada boşluk varsa ayırıyor(istersek virgül koyup arada virgül olursa öyle yerleri ayırırız)


 # a="Furkan"
 # b="YAPICI"
 # print(a+ " "+b)

 # a = "Furkan"
 # metin="Merhaba benim adım {}"   # süslü parantez yerine a'yı yazdırdım
 # print(metin.format(a))

# fiyat="20"
# adet="500"
# sayi="30"
# metin = "ben {}'tl ye {} adet {} sayılı kitap alacağım"
# print(metin.format(fiyat,adet,sayi))
# print(metin.format(adet,sayi,fiyat))

# metin="yarın işe erken gideceğim çünkü \tçalışkanım"   # \n olursa alt satıra geçirir
# print(metin)                                           # \t olursa aynı satırda büyük boşluk
                                                         # \r olursa satır başının yerini alır (sanırım :D)


print(10>9)
print(10<9)
a=10
b=19
if a>b:
    print(a,",",b,"'den büyüktür.")
else:
    print(b,",",a,"'dan büyüktür.")

                                                       