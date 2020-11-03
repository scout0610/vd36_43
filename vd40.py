#Sao chep noi dung tu file nguon sang file dich
link_source = input("Nhap duong dan file nguon:  ")
link_target = input("Nhap duong dan file dich:  ")

with open(link_source, "r" ) as f:
    content = f.read()
    f.close()

with open(link_target, "w" ) as f:
    for line in content:
        f.write(line)
    f.close()