print("---------------------------\n")
print("       SELAMAT DATANG      \n")
print("---------------------------\n")
#Inputan ujian teori dan praktek
ujian_teori = int(input("Masukkan Nilai Ujian Teori : "))
ujian_praktek = int(input("Masukkan Nilai Ujian Praktek : "))

#Output
print("\n")
print("Hasil : \n")
if(ujian_teori >= 70 and ujian_praktek >= 70):
	print("Selamat, Anda lulus!")
elif(ujian_teori >= 70 and ujian_praktek < 70):
	print("Anda harus mengulang ujian praktek.")
elif(ujian_teori < 70 and ujian_praktek >= 70):
	print("Anda harus mengulang ujian teori.")
elif(ujian_teori and ujian_praktek < 70):
	print("Anda harus mengulang ujian teori dan praktek.")