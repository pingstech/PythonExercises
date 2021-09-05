import random
import time
print("""************************************

SAYI TAHMİN OYUNU


1 İLE 40 ARASINDA SAYI TAHMİN EDİN
************************************""")

randNum = random.randint(1,40)
tryNum = 7
while True:
    guessNum = int(input("Tahmininizi Yazınız: "))

    if guessNum < randNum:
        print("Bilgilerinizi Sorgulanıyor...")
        time.sleep(1)

        print("Daha Yüksek Bir Sayı Söyleyin...")
        tryNum -=1

    elif guessNum > randNum:
        print("Bilgilerinizi Sorgulanıyor...")
        time.sleep(1)

        print("Daha Küçük Bir Sayı Söyleyin...")
        tryNum -= 1

    else:
        print("Bilgilerinizi Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! Sayınız:",randNum)
        break
    if tryNum == 0:
        print("Tahmin Hakkınız Bitti")
        print("Sayınız:",randNum)
        break