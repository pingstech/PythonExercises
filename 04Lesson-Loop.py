# PROBLEM 1
# Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
#
# Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya
# "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

num = int(input("Bir sayı giriniz: "))
temp = 0
i = 1

while i < num:
    if (num % i) == 0:
        temp += i
    i += 1
if num == temp:
    print("Sayınızı mükemmel bir sayıdır.")
else:
    print("Sayınızı mükemmel bir sayı değildir.")

#Problem 2
#Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını
# bulmaya çalışın.

#Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan
#herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti )
#o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
#Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

num = (input("Bir sayı giriniz: "))
num_dig = len(num)
num = int(num)
temp = num
dig = 0
sum = 0

while temp > 0:
    dig = temp % 10
    sum += dig ** num_dig
    temp //= 10

if sum == num:
    print("Sayınız bir amstrong sayısıdır.")
else:
    print("Sayınız bir amstrong sayısı değildir.")

#Problem 3
#1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

#İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları
#range() fonksiyonunu kullanarak elde edin.

for i in range(1,11):
    print("----------")
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,(i*j)))

#Problem 4
#Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının
#girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q"
#tuşuna bastığı zaman döngüyü sonlandırın ve ekrana
#"toplam değişkenini" bastırın.

#İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı
#q'ya basarsa döngüyü break ile sonlandırın.

temp = 0
while True:
    num = input("Sayı giriniz: ")
    if num == "q":
        print("Programdan çıkılıyor")
        break
    temp += int(num)
print("Girdiğiniz sayıların toplamı: ",temp)

#Problem 5
#1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları
# ekrana bastırın. Bu işlemi continue ile yapmaya çalışın

for i in range(3,101):
    if i % 3 != 0:
        continue
    print(i)

#Problem 6
#Burada mantık yürüterek ve list comprehension kullanarak
# 1'den 100'e kadar olan sayılardan sadece çift sayıları bir
# listeye atmayı yapmayı çalışın.

#Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı
# yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur.
#Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu
# durumlarla kullanımını öğreneceksiniz.

odd_liste = [i*2 for i in range(1,51)]
print(odd_liste)
# YA DA
odd_liste2 = [i for i in range(1,101) if i % 2 == 0]
print(odd_liste2)