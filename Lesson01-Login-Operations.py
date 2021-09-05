print("""
****************************
Kullanıcı Girişi Programı
****************************
""")

sys_member_name = "mryayla"
sys_member_pass = "yayla4128"
try_chance = 3

while True:
    member_name = input("Kullanıcı adını giriniz: ")
    member_pass = input("Şifrenizi giriniz: ")
    if ( member_name != sys_member_name and member_pass == sys_member_pass):
        print("Kullanıcı adını yanlış girdiniz...")
        try_chance -= 1
    elif ( member_name == sys_member_name and member_pass != sys_member_pass):
        print("Şifrenizi yanlış girdiniz...")
        try_chance -= 1
    elif ( member_name != sys_member_name and member_pass != sys_member_pass):
        print("Kullanıcı adınızı ve şifrenizi yanlış girdiniz...")
        try_chance -= 1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı...")
        print("Siteye yönlendiriliyorsunuz...")
        break
    if try_chance == 0:
        print("Giriş hakkınız bitti...")
        print("Siteden çıkılıyor...")
        break