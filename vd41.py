#Ghep noi dung file nguon vao cuoi file dich
arr = []

link_source = input("Nhap duong dan file nguon:  ")
link_target = input("Nhap duong dan file dich:  ")

with open(link_target, "r" ) as f:
    content_target = f.read()
    for line in content_target:
        arr.append(line)
    f.close()

with open(link_source, "r" ) as f:
    content_source = f.read()
    for line in content_source:
        arr.append(line)
    f.close()

with open(link_target, "w" ) as f:
    for i in arr:
        f.write(i)
    f.close()