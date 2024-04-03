def tinh_tien(a, s1, s2):
    if s1 == "thuong":
        c = a * 500000
    elif s1 == "vip":
        c = a * 700000

    if s2 == "momo":
        c -= 50000
    elif s2 == "vnpay" and s1 == "vip":
        c *= 0.9

    return c

def kiem_tra_ket_qua(a, s1, s2, ket_qua_du_kien):
    ket_qua_thuc_te = tinh_tien(a, s1, s2)
    if ket_qua_thuc_te == ket_qua_du_kien:
        print("Test case passed!")
    else:
        print("Test case failed! Kết quả thực tế:", ket_qua_thuc_te, "Kết quả kỳ vọng:", ket_qua_du_kien)

# Test case 1: s1 là "thuong", s2 là "momo"
kiem_tra_ket_qua(3, "thuong", "momo", 1500000)

# Test case 2: s1 là "vip", s2 là "momo"
kiem_tra_ket_qua(2, "vip", "momo", 1300000)

# Test case 3: s1 là "vip", s2 là "vnpay"
kiem_tra_ket_qua(4, "vip", "vnpay", 2520000)

# Test case 4: s1 là "thuong", s2 là "vnpay"
kiem_tra_ket_qua(5, "thuong", "vnpay", 2500000)
