def prime_num(num):
    if num == 1:
        return False

    elif num == 2:
        return True

    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


while True:
    print("********************")
    ent_num = input("Bir Sayı Giriniz:")
    if ent_num == "q":
        break

    else:
        if prime_num(int(ent_num)):
            print(ent_num, "Asal bir sayıdır")

        else:
            print(ent_num, "Asal bir sayı değildir")
