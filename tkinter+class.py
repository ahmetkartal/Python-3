from tkinter import *
class sayfa:
    def __init__(self,pencere):
      
        self.button=Button(text="9",fg="Blue",command=self.mesaj(9))
        self.button.pack()
        self.button2=Button(text="Çıkış",fg="Red",command=self.kapat)
        self.button2.pack()
    def mesaj(self,a):
        print(a)
    def kapat(self):
        pencere.after(2000,pencere.destroy)
pencere=Tk()
c=sayfa(pencere)
pencere.mainloop()
