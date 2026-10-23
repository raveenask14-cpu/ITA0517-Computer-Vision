
import cv2
import os
import numpy as np

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg")
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    h, w = img.shape[:2]
    matrix = np.float32([[1, 0, 50], [0, 1, 30]])
    result = cv2.warpAffine(img, matrix, (w, h))

    cv2.imwrite(os.path.join(folder, "Q35_translation.jpg"), result)
    cv2.imshow("Image Translation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
