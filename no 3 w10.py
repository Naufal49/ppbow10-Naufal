from abc import ABC, abstractmethod

# Kelas abstrak untuk kendaraan
class Kendaraan(ABC):
    @abstractmethod
    def jenis(self):
        pass

# Kelas konkret untuk mobil
class Mobil(Kendaraan):
    def jenis(self):
        return "Ini adalah Mobil."

# Kelas konkret untuk motor
class Motor(Kendaraan):
    def jenis(self):
        return "Ini adalah Motor."

# Factory class untuk membuat objek kendaraan
class KendaraanFactory:
    @staticmethod
    def buat_kendaraan(tipe):
        if tipe == "mobil":
            return Mobil()
        elif tipe == "motor":
            return Motor()
        else:
            return None

# Program utama
print("=== Program Pabrik Kendaraan ===")
tipe_kendaraan = input("Masukkan tipe kendaraan (mobil/motor): ").lower()
kendaraan = KendaraanFactory.buat_kendaraan(tipe_kendaraan)

if kendaraan:
    print(kendaraan.jenis())
else:
    print("Tipe kendaraan tidak dikenali.")
