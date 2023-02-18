"""
1- bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
"""
musteriAdi="Fatih"
musteriSoyadi="Türker"
musteriAdSoyad=musteriAdi +' '+musteriSoyadi
musteriCinsiyet= True # Erkek
musteriTcKimlik="10684554676"
musteriDogumYili= 1981
musteriAdresi="İstanbul Kadikoy"
musteriYasi=2022-musteriDogumYili
print(musteriYasi) # 41

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    Sipariş 1 => 110        TL
    Sipariş 2 => 110.5      TL
    Sipariş 3 => 356.95     TL
        
"""
print (110+110.5+356.95) # 577.45
order1=110
order2=110.5
order3=356.95

total=order1+order2+order3
print("Total : " ,total) # Total :  577.45
