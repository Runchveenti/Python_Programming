for i in range(1, 101):
    print(i)
    if i % 10 == 0:
        print()

# Nhap 1 nam duong lich, in ra nam am lich
# 2024 -> Giap Thin
can = ['Canh', 'Tan', 'Nham', 'Quy', 'Giap', 'At', 'Binh', 'Dinh', 'Mau', 'Ky']
chi = ['Than', 'Dau', 'Tuat', 'Hoi', 'Ty', 'Suu', 'Dan', 'Meo', 'Thin', 'Ty', 'Ngo', 'Mui']
# Nhap nam duong lich
namDL = int(input("Nhap nam duong lich:"))
# Tinh can
can1 = namDL % 10
# Tinh chi
chi1 = namDL % 12
# Doi nam AL
namAL = can[can1] + " " + chi[chi1]
print(namAL)
