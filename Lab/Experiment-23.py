
import cv2
import os
import numpy as np

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
folder = os.path.join(os.path.dirname(path), "output")
os.makedirs(folder, exist_ok=True)
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((9,9), np.uint8)
    result = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    out = os.path.join(folder, "Q23_tophat.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Top Hat", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
