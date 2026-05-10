class Hero:
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp

    def status(self):
        print(f"{self.nama} punya hp sebanyak {self.hp}")

class roamerNoSatuDumai(Hero):
    def __init__(self, nama, hp, mana, damage):
        super().__init__(nama, hp)
        self.mana = mana
        self.damage = damage

    def pakaiSpell(self):
        print(f"{self.nama} pakai skill dan damage skillnya {self.damage}")

    def manaRegen(self):
        self.mana += 0
        print(f"Mana nambah, mana sisa: {self.mana}")

Grock = roamerNoSatuDumai("Grock", 4200, 0, 200)
Grock.status()
Grock.pakaiSpell()
Grock.manaRegen()