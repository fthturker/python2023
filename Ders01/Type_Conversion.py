"""
x = input("1.sayi : ")
y = input("2.sayi : ")

print(type(x)) # <class 'str'>
print(type(y)) # <class 'str'>

toplam = int(x) + int(y)

print(toplam) # 10
"""

x = 5  # int
y = 2.5  # float
name = "Çınar"  # string
isOnline = True  # bool

#print(type(x))
#print(type(y))
#print(type(name))
#print(type(isOnline))
"""
#Type Conversion

# int to float
x= float(x)
print(x) # 5.0

# float to int
y= int(y)
print(y) #2
print(type(y))

result=str(x)+str(y)
print(result) #7.0 # 5.02
print(type(result))  # <class 'str'>

#bool to str
isOnline=str(isOnline)
print(isOnline) # True
print(type(isOnline)) # <class 'str'>
"""
#bool to int
isOnline=int(isOnline)
print(isOnline) # 1
print(type(isOnline)) # <class 'int'>