# Problem 1
# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
# Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon
# yazın.
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir
# sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

def perfNum(tpNum):
    tpSum = 0
    for i in range(1,tpNum):
        if tpNum % i == 0:
            tpSum += i
    return tpSum == tpNum

for x in range(1,1001):
    if (perfNum(x)):
        print("Mükemmel Sayı: ",x)
#******************************************************************

# Problem 3
# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK)
# dönen bir tane fonksiyon yazın.

def find_ekok(tpNum1,tpNum2):
    i = 2
    ekok = 1
    while True:
        if tpNum1 % i == 0 and tpNum2 % i == 0:
            ekok *= i
            tpNum1 //= i
            tpNum2 //= i

        elif tpNum1 % i == 0 and tpNum2 % i == 0:
            ekok *= i
            tpNum1 //= i

        elif tpNum1 % i != 0 and tpNum2 % i == 0:
            ekok *= i
            tpNum2 //= i
        else:
            i += 1
        if tpNum1 == 1 and tpNum2 == 1:
            break
    return ekok

num1 = int(input("Birinci Sayıyı giriniz: "))
num2 = int(input("İkinci Sayıyı giriniz: "))

print("Ekok",find_ekok(num1,num2))
#******************************************************************

# Problem 4
# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu
# bulan bir fonksiyon yazın.

def spellNum(tpNum):

    onesDigit = tpNum % 10
    tensDigit = tpNum // 10

    return tensDigitList[tensDigit] + " " + onesDigitList[onesDigit]

tensDigitList = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
onesDigitList = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]

num = int(input("Bir sayı giriniz: "))
print(num,"'ın okunuşu:",spellNum(num))
#******************************************************************

# Problem 5
# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları
# ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisFind():
    pisListe = list()
    for x in range(1, 101):
        for y in range(1, 101):
            z = ((x ** 2) + (y ** 2)) ** 0.5

            if (z == int(z)):
                pisListe.append((x, y, int(z)))

    return pisListe

for i in pisFind():
    print(i)

