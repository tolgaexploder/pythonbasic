sys_username = "Exploder"
sys_password = "123"

kullanici_adi = input("Kullanici adi giriniz: ")
sifre = input("Sifre giriniz: ")

if(kullanici_adi == sys_username and (sifre != sys_password)):
   print("Sifre yanlis")

elif(kullanici_adi != sys_username and (sifre == sys_password)):
   print("Kullanici adi yanlis")

elif(kullanici_adi != sys_username)and (sifre == sys_password):
   print("Kullanici adi yanlis")
elif(kullanici_adi != sys_username) and (sifre != sys_password):
    print("Kullanici adi ve sifre yanlis")
else:
    print("Giris yapildi")


