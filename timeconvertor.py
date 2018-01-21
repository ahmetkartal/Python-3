import sys

def timeConversion(s):
    # Complete this function
    kontrol=int(s[:2])
    zaman=s[8:10]
    s=s[2:8]
  
    if(zaman=="PM" and kontrol!=12):
        saat=kontrol+12
        return str(saat)+s
    
    if(zaman=="AM" and kontrol==12):
        kontrol=0
        return str(kontrol)+"0"+s 
    if(kontrol==12):
         return str(kontrol)+s
    else:
        return "0"+str(kontrol)+s

s = input().strip()
result = timeConversion(s)
print(result)
