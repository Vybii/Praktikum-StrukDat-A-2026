class person:
    def __init__(self, nama, jk, umur):
        self.nama = nama
        self.umur = umur
        self.jk = jk

class karyawan(person):
    def __init__(self, nama, jk, umur, gaji):
        super().__init__(nama, jk, umur)
        self._gaji = gaji

    def getGaji(self):
        return self._gaji
    
    def setGaji(self, gaji):
        self._gaji = gaji

class rekening:
    def __init__(self, norekening, pin):
        self.norekening = norekening
        self.__pin = pin
    
    def getpin(self):
        return self.__pin
    
    def setpin(self, pinbaru):
        self__pin = pinbaru

devin = person("Devin", "Lakik", 18)
angga = karyawan("Amgga", "Lakik", 18, 1000000000)
norek = rekening(829374, 88888)

print(devin.nama)
print(angga.getGaji())
print(norek.getpin())