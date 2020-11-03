import cv2

link_image = input("Nhap duong dan file: ")
im = cv2.imread(link_image)

print("kich thuoc anh la : {}".format(im.shape))


