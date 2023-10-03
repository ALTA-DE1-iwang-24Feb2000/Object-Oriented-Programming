# tulis solusi code disini
class Persegi():
    def __init__(self, sisi):
        self.sisi = sisi
    
    def luas(self):
        return self.sisi * self.sisi
    
    def keliling(self):
        return 4 * self.sisi

class Segitiga():
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
    def keliling(self):
        return 3 * self.alas

class PersegiPanjang():
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    
persegi = Persegi(4)
print("luas persegi :", persegi.luas())
print("keliling persegi: ", persegi.keliling())

segitiga = Segitiga(4,3)
print ("luas segitiga: ", segitiga.luas())
print ("keliling segitiga: ", segitiga.keliling())

persegipanjang = PersegiPanjang(7,8)
print("luas pp: " ,persegipanjang.luas())
print("keliling pp: " , persegipanjang.keliling())