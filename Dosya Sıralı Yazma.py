import os
os.chdir("D:/")
isimler=open("isimler.txt","w")
sırala=open("sırala.txt","w")
liste=[]
for i in range(5):
    veri=input("İsmi giriniz: ")
    isimler.writelines(veri+ "\n")
    liste.append(veri)
 
isimler.close()
liste.sort()
print(liste) 
for j in range(5):
    sırala.write(liste[j]+ "\n")
sırala.close()
