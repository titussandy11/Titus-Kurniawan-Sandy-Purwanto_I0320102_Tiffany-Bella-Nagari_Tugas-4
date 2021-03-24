print("Kursus Online 'Gajah Operation'")
masukkan_usia_siswa = int(input('Masukkan usia anda :'))
print(masukkan_usia_siswa >= 21)
ujian_kualifikasi = input("Apakah anda lulus ujian kualifikasi (lulus/tidak ?")
if masukkan_usia_siswa >= 21 and ujian_kualifikasi == "lulus":
    print("Anda dapat mendaftar di kursus")
else:
    print("Maaf, anda tidak dapat mendaftar di kursus")