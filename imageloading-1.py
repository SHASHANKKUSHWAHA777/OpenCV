import cv2

image = cv2.imread("test.png")

if image is None:
    print("error : no image found")
else:
    print("image loaded successfully")
