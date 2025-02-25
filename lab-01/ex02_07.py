#Nhập các dòng từ người dùng 
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
#chuyển các dòng thành chữ in hoa va in ra màn hình 
print("\n Các dòng đã nhập sau khi chuyển thành in hoa: ")
for line in lines:
    print(line.upper())