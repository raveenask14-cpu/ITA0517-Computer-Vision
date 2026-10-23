
import cv2
import os
import numpy as np

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg", 0)
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    result = cv2.dilate(binary, kernel, iterations=1)

    cv2.imwrite(os.path.join(folder, "Q37_dilation.jpg"), result)
    cv2.imshow("Image Dilation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
