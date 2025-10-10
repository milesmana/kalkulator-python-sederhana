# Program Kalkulator menggunakan Python Sederhana

def tambah(x,y):
    return x + y

def kurang(x,y):
    return x - y

def kali(x,y):
    return x * y

def bagi(x,y):
    if y == 0:
        return "Error! Tidak bisa membagi dengan nol."
    else:
        return x / y
    
    

print("=== Kalkulator Sederhana ===")
print("Pilih Operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukan pilihan (1/2/3/4):")

if pilihan in('1','2','3','4'):
    angka1 = float(input("Masukan angka pertama: "))
    angka2 = float(input("Masukan angka kedua: "))

if pilihan == '1':
    print(f"Hasil: {angka1} + {angka2} = {tambah(angka1, angka2)}")
elif pilihan == '2':
    print(f"Hasil: {angka1} - {angka2} = {kurang(angka1, angka2)}")
elif pilihan == '3':
    print(f"Hasil: {angka1} * {angka2} = {kali(angka1, angka2)}")
elif pilihan == '4':
    print(f"Hasil: {angka1} / {angka2} = {bagi(angka1, angka2)}")
else:
    print("Pilihan tidak tidak tersedia")