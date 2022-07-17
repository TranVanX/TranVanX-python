print("Tính giờ phút giây")
n=int(input("Nhập vào số giây: "))
hour=(n//3600)
minus=(n%3600)//60
second=(n%3600)%60
print(hour,":",minus,":",second)