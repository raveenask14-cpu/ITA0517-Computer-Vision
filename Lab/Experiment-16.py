
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
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    result = cv2.convertScaleAbs(cv2.magnitude(sx, sy))
    out = os.path.join(folder, "Q16_sobel.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Sobel Edges", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
