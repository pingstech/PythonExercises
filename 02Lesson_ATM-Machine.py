print("""
*********************************

Yayla Bank ATM'sine Hoşgeldiniz.

*********************************

İşlemler:

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

*********************************""")

acc_mon = 2888


while True:
    opr = int(input("İşlemi seçiniz: "))
    if opr == 1:
        print("Bakiyeniz sorgulanıyor....")
        print("Bakiyenizde bulunan para:",acc_mon)

    elif opr == 2:
        print("Bakiyeniz sorgulanıyor....")
        print("Bakiyenizde bulunan para:", acc_mon)
        dep_mon = int(input("Yatırmak istediğiniz tutarı giriniz: "))
        acc_mon += wit_mon
        print("Bakiyenizde bulunan para:", acc_mon)

    elif opr == 3:
        print("Bakiyeniz sorgulanıyor....")
        print("Bakiyenizde bulunan para:", acc_mon)
        dep_mon = int(input("Çekmek istediğiniz tutarı giriniz: "))

        if dep_mon > acc_mon:
            print("Hesabınızda çekmez istediğiniz tutar kadar bir ücret yok")
            continue

        acc_mon -= dep_mon
        print("!!!Paranızı almayı unutmayın!!!")
        print("Bakiyenizde bulunan para:", acc_mon)

    else:
        print("Hesaptan çıkılıyor")
        break
