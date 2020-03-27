# X % Y
# => Z = X - (Y * (X / Y))

# Sử dụng phép chia nguyên trong slide để tính (X / Y) sau đó gán vào A
A = def PhepChia(X,Y)

# Sử dụng phép nhân để tính (Y * (X / Y)) sau đó lưu vào B
B = def PhepNhan(Y,A)

# Sywr dụng phép trừ tính X - (Y * (X / Y)) sau đó gán vào biến Z
Z = def PhepTru(X,B)

