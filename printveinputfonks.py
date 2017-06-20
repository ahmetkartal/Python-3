a=input("Bir şey yazın: ") # python 3'de kullanıcadan veri almak için input() fonksiyonu kullanılır.bu fonksiyon aksi belirtilmedikçe string değer alır.
print(a) # input fonksiyonu ile aldığımız a değişkenini ekrana bastırıyoruz.
#eğer sayı türünde bir değişken girecekseniz cast dönüşümü ile bunu çözebilirsiniz.
b=int(input("Bir sayi girin: ")) #değişkenimizin int(tamsayı) olmasını istediğimizden bu şekilde cast dönüşümü yaptık.eğer gireceğiniz değer float olsaydı int yerine float yazmanız yeterli olacaktır.
print("Girdiğiniz sayi: %d"%(b)) #bu şekilde yaparak print fonksiyonuna girdiğimiz metinin yanına girilen sayı yazaktır.
print("Girdiniz yazi :{},Girdiğiniz sayi: {}".format(a,b)) #bu şekildede formatlı yazımı görmüş oluyoruz.ilk köşeli parantezlerin olduğu yere a,ikincisinin olduğu yere ise b gelecektir.
print("Girdiğiniz yazi: %s,Girdiğiniz sayi: %d"%(a,b)) #buda yukarıdaki ile aynı işi yapacaktır.fakat syntax farklıdır.
