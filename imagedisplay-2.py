import cv2

image = cv2.imread("test.png")

if image is not None:
    cv2.imshow("image showing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("error: image not loaded")
