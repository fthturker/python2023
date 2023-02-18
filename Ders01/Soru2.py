"""
    Daire Alanı     :
    Daire Çevresi   :

    * Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    (r: 3.14)
"""
pi = 3.14
yariCap = float(input("yarı çapı :"))

alan = pi * (yariCap ** 2)
print("Daire Alanı : ", alan)

cevre = 2 * pi * yariCap
print("Daire Cevre : ", cevre)
