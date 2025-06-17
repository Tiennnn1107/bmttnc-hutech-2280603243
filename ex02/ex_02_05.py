sogiolam= float(input("Nhap so gio lam moi tuan"))
luonggio = float(input("Nhap so tien nhan duoc cho moi gio lam viec"))
giotieuchuan=  44 
giovuotchuan=max(0,sogiolam - giotieuchuan)
luong=giotieuchuan*luonggio+giovuotchuan*luonggio*1.5
print("luong cua ban la = ",luong)