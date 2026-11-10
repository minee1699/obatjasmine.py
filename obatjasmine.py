print("=== DATA STOK OBAT APOTEK ===")

print("1. Paramex - Sakit kepala")
print("2. Paracetamol - Demam")
print("3. Bodrex - Flu dan batuk")
print("4. Promag - Maag")
print("5. Laserin - Pereda tenggorokan")
print("6. Amoxicillin - Antibiotik")
print("7. Antasida - Asam lambung")
print("8. Mefenamic - Pereda radang")
print("9. Cataflam - Sakit gigi")
print("10. Cetirizine - Alergi")

pilihan = int(input("\nPilih nomor obat: "))
stok = 20

if pilihan >= 1 and pilihan <= 10:
    jumlah = int(input("Jumlah obat yang dibeli: "))

    if jumlah <= stok and jumlah > 0:
        sisa = stok - jumlah
        print("Obat tersedia")
        print("Stok awal:", stok)
        print("Jumlah dibeli:", jumlah)
        print("Sisa stok:", sisa)

    elif jumlah > stok:
        print("Stok obat tidak mencukupi")
        print("Stok tersedia:", stok)

    else:
        print("Jumlah pembelian tidak valid")

else:
    print("Nomor obat tidak tersedia")