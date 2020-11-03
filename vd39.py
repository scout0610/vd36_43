# So sanh noi dung 2 file
with open("text_a.txt", "r") as f:
    content_a = f.read()
    f.close()

with open("text_b.txt", "r" ) as f:
    content_b = f.read()
    f.close()

if content_a == content_b:
    print("Hai file co noi dung giong nhau.")
else:
    print("Hai file co noi dung khac nhau.")