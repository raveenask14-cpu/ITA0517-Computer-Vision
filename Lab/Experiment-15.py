
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
    corners = cv2.cornerHarris(np.float32(gray), 2, 3, 0.04)
    result = img.copy()
    result[corners > 0.01 * corners.max()] = [0,0,255]
    out = os.path.join(folder, "Q15_harris_corners.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Harris Corners", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
