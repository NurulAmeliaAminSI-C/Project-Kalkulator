import os
import math
os.system('cls')

def kalkulator():
    while True:
        print("\nPROGRAM KALKULATOR\n")
        print("Pilihan:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Perpangkatan")
        print("6. Akar Pangkat Dua")
        print("7. Akar Pangkat n")
        print("8. Logaritma")

        operator = int(input("\nMasukkan Operator: "))

        if operator in [1, 2, 3, 4, 5, 6, 7, 8]:
            if operator == 1:
                angka1 = float(input("Masukkan Angka 1: "))
                angka2 = float(input("Masukkan Angka 2: "))
                hasil = angka1 + angka2
                print(f"Hasil Perhitungan {angka1} + {angka2} = {hasil}")

            elif operator == 2:
                angka1 = float(input("Masukkan Angka 1: "))
                angka2 = float(input("Masukkan Angka 2: "))
                hasil = angka1 - angka2
                print(f"Hasil Perhitungan {angka1} - {angka2} = {hasil}")

            elif operator == 3:
                angka1 = float(input("Masukkan Angka 1: "))
                angka2 = float(input("Masukkan Angka 2: "))
                hasil = angka1 * angka2
                print(f"Hasil Perhitungan {angka1} x {angka2} = {hasil}")

            elif operator == 4:
                angka1 = float(input("Masukkan Angka 1: "))
                angka2 = float(input("Masukkan Angka 2: "))
                hasil = angka1 / angka2
                print(f"Hasil Perhitungan {angka1} / {angka2} = {hasil}")

            elif operator == 5:
                angka1 = float(input("Masukkan Angka: "))
                pangkat = float(input("Masukkan Pangkat: "))
                hasil = angka1 ** pangkat
                print(f"Hasil Perhitungan {angka1} ^ {pangkat} = {hasil}")

            elif operator == 6:
                angka = float(input("Masukkan Angka: "))
                hasil = math.sqrt(angka)
                print(f"Akar Pangkat Dua dari {angka} = {hasil}")

            elif operator == 7:
                angka = float(input("Masukkan Angka: "))
                pangkat = float(input("Masukkan Pangkat: "))
                hasil = angka ** (1 / pangkat)
                print(f"Akar Pangkat {pangkat} dari {angka} = {hasil}")

            elif operator == 8:
                basis = float(input("Masukkan Basis: "))
                nilai = float(input("Masukkan Nilai: "))
                hasil = math.log(nilai, basis)
                print(f"Logaritma Basis {basis} dari {nilai} = {hasil}")

            lanjutkan = input("\nIngin Lanjutkan? [y/n] ").lower()
            if lanjutkan != 'y':
                print("\nTerima Kasih Telah Menggunakan Kalkulator ini :)")
                break
        else:
            print("\nOperator tidak valid. Silakan pilih operator yang benar")

if __name__ == "__main__":
    kalkulator()
