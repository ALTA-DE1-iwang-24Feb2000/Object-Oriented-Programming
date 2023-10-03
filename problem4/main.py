# tulis solusi code disini
class Barang():
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat
    
    def dimensi(self):
        return self.panjang * self.lebar * self.tinggi
    
class Hitung(Barang):
    def __init__(self, panjang, lebar, tinggi, berat, ongkir):
        super().__init__(panjang, lebar, tinggi, berat)
        self.harga = ongkir

    def ongkir(self):
        if self.dimensi() <= 50 and self.berat <= 1:
            self.harga = 5000
        return self.harga

laptop = Hitung(5, 2, 4, 1, 0)
print(laptop.ongkir())