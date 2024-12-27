# #   Membuat gabungan area rentang dari sebuah angka

# #  awalan
# #  gambaran
# #  +++++++3----------10++++++++
# #  dibawah angka 3 bernilai TRUE dan juga diatas angka 10 bernilai TRUE
# inputUser = float(input("masukkan angka yang bernilai KURANG DARI 3 atau LEBIH DARI 10 : "))
# #  untuk kurang dari 3
# isKurangDari = ( inputUser < 3)
# print("Kurang dari 3 bernilai : ", isKurangDari)
# #  untuk lebih dari 10
# isLebihDari = (inputUser > 10)
# print("Lebih dari 10 bernilai : ", isLebihDari)

# #  mengukurnya menggunakan operasi komperasi OR
# isCorrect = isKurangDari or isLebihDari
# print("angka yang anda masukkan", inputUser, " bernilai : ", isCorrect)

# #  ///  KEY nya adalah di bagian inputUser yaitu kata "ATAU"


# print("\n", 10*"=","\n")
# #  Kasus Irisan
# #  Jika kita tadi menggabungkan, maka kita akan mengiris nya
# #  ------3+++++++++++10----------
# inputUser = float(input("masukkan angka yang bernilai LEBIH DARI 3 dan KURANG DARI 10 : "))
# # untuk lebih dari 3
# isLebihDari = (inputUser > 3)
# print("Lebih dari 3 bernilai : ", isLebihDari)
# #  untuk kurang dari 10
# isKurangDari = (inputUser < 10)
# print("Kurang dari 10 bernilai :", isKurangDari)

# #  mengukurnya menggunakan operasi komperasi AND
# isCorrect = isLebihDari and isKurangDari
# print("angka yang anda masukkan", inputUser, " bernilai : ", isCorrect)

#  ///  KEY nya adalah di bagian inputUser yaitu kata "DAN"



#  TUGAS NYA

#  soal 1
#  ---- 0 +++++ 5 ----- 8 ++++++ 11-------

#  soal 2
#  ++++ 0 ----- 5 +++++ 8 ------ 11 ++++++

#  soal 1
#  ---- 0 +++++ 5 ----- 8 ++++++ 11-------
inputUser = float(input("masukkan angka : "))
#  untuk 0
isNilaiNol = (inputUser > 0)
print("Nilai 0 : ", isNilaiNol) 
#  untuk 5
isNilaiLima = (inputUser < 5)
print("Nilai 5 : ", isNilaiLima) 
#  untuk 8
isNilaiDelapan = (inputUser > 8)
print("Nilai 8 : ", isNilaiDelapan) 
#  untuk 11
isNilaiSebelas = (inputUser < 11)
print("Nilai 11 : ", isNilaiSebelas) 
#  penggabungan
isCorrect = isNilaiNol or isNilaiLima or isNilaiDelapan or isNilaiSebelas
print("angka yang anda masukkan", inputUser, " bernilai : ", isCorrect)

#  soal 2
#  ++++ 0 ----- 5 +++++ 8 ------ 11 ++++++
inputUser = float(input("masukkan angka : "))
#  untuk 0
isNilaiNol = (inputUser < 0)
print("Nilai 0 : ", isNilaiNol) 
#  untuk 5
isNilaiLima = (inputUser < 5)
print("Nilai 5 : ", isNilaiLima) 
#  untuk 8
isNilaiDelapan = (inputUser < 8)
print("Nilai 8 : ", isNilaiDelapan) 
#  untuk 11
isNilaiSebelas = (inputUser > 11)
print("Nilai 11 : ", isNilaiSebelas) 
#  penggabungan
isCorrect = isNilaiNol and isNilaiLima and isNilaiDelapan and isNilaiSebelas
print("angka yang anda masukkan", inputUser, " bernilai : ", isCorrect)
