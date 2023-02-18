print(2 + 2)  # 4
print(2 + 1.5)  # 3.5
print(2.0 + 5)  # 7.0
print(type(2))  # <class 'int'>
# 2 nin türünü bize gösteriyor
print(type(2.0))  # <class 'float'>
print(10 % 2)  # 0
print(10 // 2)  # 5

maasAhmet = 5000
maasAli = 4000
vergi = 0.27

print(maasAhmet - (maasAhmet * vergi))  # 3650.0
print(maasAli - (maasAli * vergi))  # 2920.0

# Değişken tanımlama kuralları
# rakam ile baslayamaz
number1 = 10
number1 += 30
print(number1)  # 40
# Büyük küçük harf duyrlılığı
age = 20
AGE = 30
print(age)  # 20
print(AGE)  # 30

# Türkçe karakterkullanmayalım
# yaş=20
yas = 20
_age = 20

x = 1  # int
y = 2.3  # float
name = 'Çınar'  # string
isStudent = True  # bool

# yukarıdaki 4 tane değişkeni tek satırda ifade edelim
# x, y, name, isStudent = (1, 2.3, 'Çınar', True)

a = 10
b = 20
print(a + b)  # 30

a = '10'
b = '20'
print(a + b)  # 1020

firstName = 'Sadık'
lastName = ' Turan'
print(firstName + lastName)  # Sadık Turan
