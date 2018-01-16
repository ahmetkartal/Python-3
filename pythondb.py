import sqlite3

con=sqlite3.connect("dersler.db")

cursor=con.cursor()

def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(ad TEXT,soyad TEXT,numara INT,notu INT)")
    con.commit()
   
def addvalue():
    cursor.execute("INSERT INTO ogrenciler VALUES('Emre','Kartal',1112,1)")
    con.commit()
    

def show():
    cursor.execute("SELECT *FROM ogrenciler ")
    con.commit()
    satırlar=cursor.fetchall()
    for i in satırlar:
        print(i)
    
    
def update():
    cursor.execute("SELECT *FROM ogrenciler ")
    con.commit()
    satırlar=cursor.fetchall()
    print("------------ilk kayıtlar------------------")
    for i in satırlar:
        print(i)
    cursor.execute("UPDATE ogrenciler SET notu=14 where notu=15")
    cursor.execute("SELECT * From ogrenciler")
    con.commit()
    satırlar=cursor.fetchall()
    
    print("------------updateden sonra kayıtlar------------------")
    for i in satırlar:
        print(i)
    
def delete():
    cursor.execute("DELETE From ogrenciler where ad='Emre'")
    con.commit()
    
    
delete()
con.close()
