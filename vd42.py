link_file = input("Nhap duong dan file :  ")

with open(link_file, "r") as f:
    content = f.read()

print("so ky tu: {}".format(len(content)))
print("so tu: {}".format(len(content.split())))

sentences = list(content)
count = 0
for i in sentences:
    if i == '.':
        count = count + 1

print("so cau: {}".format(count))

