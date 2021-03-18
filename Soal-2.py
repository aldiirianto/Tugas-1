print("---------------------------\n")
print("       SELAMAT DATANG      \n")
print("---------------------------\n")
#Inputan phi, jari - jari lingkaran, luas
phi = 22 / 7
jari_jari = int(input("Masukkan jari - jari lingkaran (cm) : "))
Luas = float(phi * jari_jari * jari_jari)

#Output
print("\n")
print("Hasil : \n")
print("Luas lingkaran dengan jari - jari %d cm adalah %0.2f cm\u00b2"%(jari_jari,Luas))