n = int(input("nhap so phan tu: "))
print("nhap mang")
arr = [float(input()) for _ in range(n)]

# ghi nd vao file
with open("text_a.txt", "w" ) as f:
    f.write("{}\n".format(n))
    for i in range(n):
        f.write("{}\n".format(arr[i]))
    f.close()

#doc nd file
with open("text_a.txt", "r" ) as f:
    print(f.read())
    f.close()

#sap xep
arr = sorted(arr)

#luu vao file
with open("text_b.txt", "w" ) as f:
    f.write("{}\n".format(n))
    for i in range(n):
        f.write("{}\n".format(arr[i]))
    f.close()

