# tulis solusi code disini
class Kalkulator():
    def __init__(self, x, y):
        self.x = x  
        self.y = y
    
class Penjumlahan(Kalkulator):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def jumlah(self):
        return int(self.x + self.y)
    
class Pengurangan(Kalkulator):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def kurang(self):
        return int(self.x - self.y)

class Perkalian(Kalkulator):
    def __init__(self, x, y):
        super().__init__(x, y)

    def kali(self):
        return int(self.x*self.y)

class Pembagian(Kalkulator):
    def __init__(self, x, y):
        super().__init__(x, y)

    def bagi(self):
        return int(self.x/self.y)
    
penjumlahan = Penjumlahan(3,4)
print (penjumlahan.jumlah())

pengurangan = Pengurangan(15,4)
print (pengurangan.kurang())

perkalian = Perkalian(10,10)
print (perkalian.kali())

pembagian = Pembagian(12,3)
print (pembagian.bagi())