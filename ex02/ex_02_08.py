def chiahetcho5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 ==0:
        return True
    else:
        return False
Chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan (Phan tach boi dau ,):")
so_nhi_phan_list = Chuoi_so_nhi_phan.split(',')
so_chia_Het_cho_5 = [so for so in so_nhi_phan_list if chiahetcho5(so)]
if len(so_chia_Het_cho_5 ) > 0:
    ket_qua= ','.join (so_chia_Het_cho_5)
    print("Cac so nhi phan  chia het cho 5 la :",ket_qua)
else:
    print("khong co so nhi phan nao chia het cho 5 trong chuoi da nhap:")