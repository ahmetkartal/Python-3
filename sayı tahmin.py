import random
a=random.randrange(0,100)
sayi=-1
sayac=0
while(sayi!=a):
    sayac=sayac+1
    sayi=int(input("Tahmin ettiğiniz sayıyı giriniz: "))
    print(a)
    if(sayi<a):
        print("daha yüksek bi sayı girmen lazım")
    elif(sayi>a):
        print(" daha küçük sayı girmen lazım")
    else:
        print(sayac," denemede buldun")
    if(sayac==10):
        print("bulamadın")
        break
