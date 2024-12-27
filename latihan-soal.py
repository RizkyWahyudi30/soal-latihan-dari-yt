#  LATIHAN KONVERSI SATUAN TEMPERATURE

'''
##  satuan ## =    Celcius    =   Reamur     =    Fahrenheit       =    Kelvin  
Celcius       =      -         =   4/5 C      =    9/5 C + 32      =   C + 273
Reamur        =    5/4 R      =      -        =    9/4 R + 32      =   5/4 K + 273
Fahrenheit    =   5/9 (f-32)  =  4/9 (F-32)  =         -           =   5/9 (F-32) + 273
Kelvin        =   K - 273     =  4/5 (K-273) =  9/5 (K-273) + 32   =       -
'''

#  PROGAM KONVERSI CELCIUS KE SATUAN LAIN
print("\n====== PROGRAM KONVERSI SATUAN =======\n")

#  celcius
celcius = float(input("masukkan suhu dalam celcius : "))
print("suhu dalam celcius : ", celcius, "C")


#  reamur
reamur = (4/5) * celcius
print("suhu dari celcius ke reamur : ", reamur, "R")


#  fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dari celcius ke fahrenheit : ", fahrenheit, "F")

#  kelvin
kelvin = celcius + 273
print("suhu dari celcius ke kelvin : ", kelvin, "K")

#  PR DARI KELAS TERBUKA
# soal 1
print("\n====== PROGRAM FAHRENHEIT KE KELVIN ======\n")
fahrenheit_to_kelvin = (5/9 * (fahrenheit-32)) + 32
print("hasilnya adalah : ", fahrenheit_to_kelvin, "K")

# soal 2
print("\n====== PROGRAM KELVIN KE FAHRENHEIT ======\n")
kelvin_to_fahrenheit = (9/5 * (kelvin-273)) + 32
print("hasilnya adalah : ", kelvin_to_fahrenheit, "F")




