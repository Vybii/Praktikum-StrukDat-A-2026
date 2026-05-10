class luar:
    def __init__(self, nama):
        self.nama = nama

    class dalam:
        def __init__(self, panggilluar):
            self.keluar = panggilluar

        def panggilClassLuar(self):
            print("Class luar diakses dari dalam")

classLuar = luar("Devin suka mie minas nasi goreng")

classDalam = luar.dalam(classLuar) 
classDalam.panggilClassLuar()

