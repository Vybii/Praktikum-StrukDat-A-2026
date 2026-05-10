class KuraKura:
    def __init__(self, nama):
        self.nama = nama
        self._jenis = "Pipi putih"
        self.__lapar = "Lapar"

    def laparGak(self):
        return self.__lapar

    def ngasihMakan(self, kasihMakan):
        if kasihMakan > 0:
            print(f"Kasih makan ke {self.nama} sebanyak {kasihMakan} pelet.")
            print("Angga selalu lapar")
        else:
            print("Makanan habis")

peliharaanku = KuraKura("Angga")

print(peliharaanku._jenis)

peliharaanku.ngasihMakan(2)

print(peliharaanku.laparGak())

print(peliharaanku._KuraKura__lapar)

