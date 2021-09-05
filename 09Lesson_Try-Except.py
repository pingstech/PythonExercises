# PROBLEM 1
# liste = ["345","sadas","324a","14","kemal"]
# Bu listenin içindeki stringlerden içinde sadece rakam
# bulunanları ekrana yazdırın. Bunu yaparken try,except bloklarını kullanmayı unutmayın.


liste = ["345", "sadas", "324a", "14", "kemal"]

for num in liste:
    try:
        num = int(num)
        print(num)

    except:
        pass

print("*************************************************************************")

# PROBLEM 2
# Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın.
# Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün.
# Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın.
# Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste
# üzerinde gezinerek ekrana sadece çift sayıları bastırın.

def odd_num(tmpNum):
    if tmpNum % 2 == 0:
        return tmpNum

    else:
        raise ValueError

liste = [34,2,1,3,33,100,61,1800]

for fi in liste:
    try:
        print(oddNum(fi))

    except ValueError:
        pass
