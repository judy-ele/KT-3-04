def tinh_tien(a, s1, s2):
    if a<1: 
        return "khong the tinh do so luong ve khong hop le"
    if s1 == "thuong":
        c = a * 500000
    else:
        c = a * 700000

    if s2 == "momo":
        c -= 50000
    elif s2 == "vnpay" and s1 == "vip":
        c *= 0.9

    return c

# Nhập giá trị từ người dùng
a = int(input("Nhập số lượng: "))
s1 = input("Nhập loại khách hàng (thuong hoặc vip): ")
s2 = input("Nhập hình thức thanh toán (momo, vnpay hoặc khac): ")

print(tinh_tien(a, s1, s2))
