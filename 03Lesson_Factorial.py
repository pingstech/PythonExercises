print("""
***************************************

Faktöriyel Bulma Programı

***************************************""")
print("****** Çıkmak İsterseniz q'ya basınız... ******")

while True:
    num = (input("Faktöriyelini bulmak istediğiniz sayıyı giriniz: "))
    if num == "q":
        print("Program Sonlandırılıyor...")
        break
    else:
        num = int(num)
        temp = 1
        if num == 0:
            print("Sonuç:",temp)
        else:
            num = int(num)
            for i in range(1, num + 1):
                temp *= i
            print("Sonuç:",temp)

