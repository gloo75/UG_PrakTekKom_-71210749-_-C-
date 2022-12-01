def penjumlahan(bil1, bil2):
    hasil =  bil1 + bil2
    return hasil

def pengurangan(bil1, bil2):
    hasil =  bil1 - bil2
    return hasil

def perkalian(bil1, bil2):
    hasil =  bil1 * bil2
    return hasil

def pembagian(bil1, bil2):
    hasil =  bil1 / bil2
    return hasil

print("Operasi Matematika")
print("1 Jumlah [+]")
print("2 Kurang [-]")
print("3 Kali   [x]")
print("4 Bagi   [/]")

menu = str(input("Pilih Operasi 1/2/3/4 : "))
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

if menu == '1':
    print(f"hasil operasi dari {bil1} + {bil2} = {penjumlahan(bil1, bil2)}")
elif menu == '2':
    print(f"hasil operasi dari {bil1} - {bil2} = {pengurangan(bil1, bil2)}")
elif menu == '3':
    print(f"hasil operasi dari {bil1} * {bil2} = {perkalian(bil1, bil2)}")
elif menu == '4':
    print(f"hasil operasi dari {bil1} / {bil2} = {pembagian(bil1, bil2)}")
else:
    print('Hasil operasi dari')