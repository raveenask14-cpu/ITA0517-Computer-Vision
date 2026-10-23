
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
    result = cv2.erode(gray, np.ones((5,5), np.uint8), iterations=1)
    out = os.path.join(folder, "Q6_erosion.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Erosion", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
