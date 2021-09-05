import random
import time

class controller():

    def __init__(self,tvStatus = "Kapalı", tvVolume = 0, tvList = ["TRT"], tvChannel = "TRT"):

        self.tvStatus = tvStatus
        self.tvVolume = tvVolume
        self.tvList = tvList
        self.tvChannel = tvChannel

    def tvTurnOn(self):

        if(self.tvStatus == "Açık"):
            print("Televizyon Zaten Açık...")
        else:
            print("Televizyon Açılıyor...")
            self.tvStatus = "Açık"

    def tvTurnOff(self):

        if (self.tvStatus == "Kapalı"):
            print("Televizyon Zaten Kapalı...")
        else:
            print("Televizyon Kapatılıyor...")
            self.tvStatus = "Kapalı"

    def setVolume(self):

        while True:
            reply = input("Sesi Azalt: '+'\nSesi Artır: '-'\nÇıkış: 'q'\nİşlem: ")

            if reply == "-":
                if self.tvVolume != 0:
                    self.tvVolume -= 1
                    print("Ses:", self.tvVolume)

            elif reply == "+":
                if self.tvVolume != 32:
                    self.tvVolume += 1
                    print("Ses:", self.tvVolume)

            else:
                print("Ses güncellendi:",self.tvVolume)
                break

    def addChannel(self,newChannel):
        print("Kanal Ekleniyor...")
        time.sleep(1)  # PROGRAM 1 SN BEKLİYECEK

        self.tvList.append(newChannel)
        time.sleep(1)  # PROGRAM 1 SN BEKLİYECEK
        print("Kanal Eklendi")

    def rndChannel(self):

        rnd = random.randint(0,len(self.tvList)-1)
        self.tvChannel = self.tvList[rnd]
        print("Şu Anki Kanal:",self.tvChannel)

    def __len__(self):

        return len(self.tvList)

    def __str__(self):

        return "Tv Durumu:{}\nTv Ses: {}\nKanal Listesi{}\nŞu Anki Kanal: {}\n".format(self.tvStatus,self.tvVolume,self.tvList,self.tvChannel)

remoteController = controller()

print("""

    Televizyon Uygulaması:

    1. Tv Aç

    2. Tv Kapat

    3.Ses Ayarları

    4.Kanal Ekleme

    5.Kanal Sayısını Öğrenme

    6.Rastgele Kanala Geçme

    7.Televizyon Bilgileri

    ÇIKMAK İÇİN "q" YA BASINIZ

    """)

while True:
    oprt = input("İşlem seçiniz: ")
    if oprt == "q":
        print("Program Sonlandırılıyor...")
        break

    elif oprt == "1":
        remoteController.tvTurnOn()

    elif oprt == "2":
        remoteController.tvTurnOff()

    elif oprt == "3":
        remoteController.setVolume()

    elif oprt == "4":
        nameChannel = input("Kanal İsimlerini ',' ile ayırarak giriniz:")

        channelList = nameChannel.split(",")   # ayırma yaptık

        for add_ch in channelList:
            remoteController.addChannel(add_ch)

    elif oprt == "5":
        print("Kanal Sayısı:",len(remoteController))

    elif oprt == "6":
        remoteController.rndChannel()

    elif oprt == "7":
        print(remoteController)

    else:
        print("Geçerisiz İşlem")