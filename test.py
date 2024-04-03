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

# Test case 1: a là số nguyên âm
kiem_tra_ket_qua("khong the tinh do so luong ve khong hop le")

# Test case 2: s1 là "thuong", s2 là "khac"
kiem_tra_ket_qua(1, "thuong", "khac", 500000)

# Test case 3: s1 là "vip", s2 là "momo"
kiem_tra_ket_qua(1, "vip", "momo", 650000)

# Test case 4: s1 là "vip", s2 là "vnpay"
kiem_tra_ket_qua(1, "vip", "vnpay", 630000)

# Test case 5: s1 là "thuong", s2 là "momo"
kiem_tra_ket_qua(1, "thuong", "momo", 450000)

# Test case 6: s1 là "vip", s2 là "khac"
kiem_tra_ket_qua(1, "vip", "khac", 630000)

# Test case 7: s1 là "thuong", s2 là "vnpay"
kiem_tra_ket_qua(1, "thuong", "vnpay", 700000)
