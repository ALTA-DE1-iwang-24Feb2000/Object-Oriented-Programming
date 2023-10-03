# tulis solusi code disini
class Kubus():
  def __init__(self, sisi):
    self.sisi = sisi

  def menghitung_volume(self):
    return self.sisi * self.sisi * self.sisi

class Balok():
  def __init__(self, panjang, lebar, tinggi):
    self.panjang = panjang
    self.lebar = lebar
    self.tinggi = tinggi

  def menghitung_volume(self):
    return self.panjang * self.lebar * self.tinggi

class Tabung():
  def __init__(self, jari_jari, tinggi):
    self.phi = 3.14285714286
    self.jari_jari = jari_jari
    self.tinggi = tinggi

  def menghitung_volume(self):
    return int(self.phi * pow(self.jari_jari, 2) * self.tinggi)
  
kubus = Kubus(10)
print("volume kubus: " ,kubus.menghitung_volume())

balok = Balok(3,6,10)
print("volume balok: " ,balok.menghitung_volume())

tabung = Tabung( 7, 10)
print("volume tabung : " ,tabung.menghitung_volume())
