import cv2
import random

img = cv2.imread('assets/image1.png', cv2.IMREAD_COLOR)

print(f"Height: {img.shape[0]}")
print(f"Width: {img.shape[1]}")

for i in range(540):
    for j in range(540):
        #[blue, green, red]
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        img[i+540][j] = img[i][j+540]
        img[i][j+540] = img[i+540][j+540]

cv2.imshow("Window title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
