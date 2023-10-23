def cek_kelulusan(skor):
    if skor >= 70:
        return "Lulus"
    else:
        return "Tidak Lulus"

# Meminta input skor dari pengguna
skor = float(input("Masukkan skor tes baca-tulis: "))

# Menentukan kelulusan dan menampilkan hasil
hasil = cek_kelulusan(skor)
print(f"Hasil tes: {hasil}")
