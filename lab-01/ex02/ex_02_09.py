def kiem_tra_soNT(n):
    if n <= 1:
     return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i ==0 :
            return False
    return True
number = int(input("Nhap vao so cna kiem tra :"))
if kiem_tra_soNT(number):
    print(numer,"la so nguyen to")
else:
    print(number,"khong la so nguyen to") 