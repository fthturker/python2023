# STRING UYGULAMALARI
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course) # 65
lenght=len(course) # 65

# 2- 'website' içinden www karakterlerini alın.
result=website[7:10] # www

# 3- 'website' içinden com karakterlerini alın.
result=website[22:25] # com
result=website[lenght-3:lenght]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
result=course[0:15]
result=course[:15]
result=course[-15:] # riniz (40 saat)

#5- 'course' ifadesindeki karakterleri tersten yazdırın.

print(result)