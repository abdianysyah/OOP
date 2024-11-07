# Kelas Induk
class Kendaraan:
    jenis_kendaraan = "Motor"

    def __init__(self, merk, kecepatan):
        # public
        self.merk = merk
        # Protected
        self._kecepatan = kecepatan
        # Private
        self.__bahan_bakar = "Pertalite"

    # get
    def get_bahan_bakar(self):
        return self.__bahan_bakar
    
    # set
    def set_bahan_bakar(self, bahan_bakar):
        self.__bahan_bakar = bahan_bakar
    
    # tampilkan informasi
    def description(self):
        return f"{self.merk} bergerak dengan kecepatan {self._kecepatan} km/jam"

# Kelas Turunan (inheritance)
class Motor(Kendaraan):
    def __init__(self, merk, kecepatan, warna):
        # inheritance/pewarisan
        super().__init__(merk, kecepatan)
        # tambahan
        self.warna = warna

    def desc(self):
        return f"{self.merk} berwarna {self.warna} dan mampu mencapai kecepatan {self._kecepatan} km/jam"
    
motor_gua = Motor("CB Teyeng", 120, "Coklat")

# print(motor_gua.jenis_kendaraan)
# print(motor_gua.merk)

# print(motor_gua._kecepatan)

# print(motor_gua.get_bahan_bakar())
motor_gua.set_bahan_bakar("Pertamax")
print(motor_gua.get_bahan_bakar())
#
# print(motor_gua.description())
# print(motor_gua.desc())