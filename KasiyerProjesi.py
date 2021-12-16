#Bu kısımda ürünlerin fiyatlarını dictionary(sozluk) ile gosterdik
fiyatlar={"kola":7,"cipsi":13,"elma":7,"portakal":13,"mandalina":8,"su":2} #İçeriği çeşitlendirebilirsiniz
print("Urunlerimiz: ",fiyatlar)     #Musteri ne alabilecegini görebilsin

#Fiyatlara erişmek için print(fiyatlar["ürünün ismi"]) şeklinde yazdığımızda erişebiliriz Örneğin:
#print(fiyatlar["cipsi"])-->13 şekilinde ekrana yazdıracaktır

alinan_urunler=[] #En son aldigi ürünleri göstermek için bir liste olusturduk bu listeye aldigi ürünleri eklicez (append metodu ile)
fiyat_toplam=0    #Aldigi ürünlerin fiyat toplamını burada tutcaz


while True:    #Müşteriden sürekli ürün almasını sağlayabilmek için sonsuz döngü kullanıyoruz
    secim=input("Lutfen alicaginiz urunun ismini giriniz: ")

    if secim in fiyatlar.keys():    #Eğer kullanıcıdan aldığımız ürün ismi fiyatlar sözlüğümüzdeki keysler yani isimler ile eşleşirse
        print("{} urunu listeye basiryla eklenmistir".format(secim))    #Girdigi ürünü yazdırıyoruz
        alinan_urunler.append(secim)  #Aldigi urunleri ekliyoruz
        fiyat_toplam+=fiyatlar[secim]   #4.satırda bahsettiğim gibi ürünün adını yazarak sözlükteki degerine (fiyatına) erişip toplam fiyata ekledik
        print("Toplam hesap: {}".format(fiyat_toplam))  #Toplam hesabı yazdırıyoruz

    elif(secim=="q"): #Müşteri çıkış yapmak için q ya bassın (istediğiniz degeri veya stringi yazabilirsiniz)
        print("Cıkıs yapılıyor...")
        print("Aldiginiz urunler: {}".format(alinan_urunler)) #Liste biçimimde alinan ürünler  yazılacak
        print("Toplam Ucretiniz: {}".format(fiyat_toplam))
        break #Bu komut ile programı sonlandırıyoruz

    else:  #Eğer yukaridaki 2 durumda olmazsa (yanlis isim girimi veya  q harfine basmazsa kod buraya gelicektir
        print("Yanlis ürün girisi yapilmistir.Lutfen listeyi tekrar gozden geciriniz.")
        print(fiyatlar) #Urunleri tekrar gormesi icin ekrana yazdirdik



#Sonsuz döngüde olduğu için müsteri sadece q ya bastiğinde (bunu istediğiniz harfe atıyabilirsiniz 21.satirda yaptık) program sonlanacaktır
