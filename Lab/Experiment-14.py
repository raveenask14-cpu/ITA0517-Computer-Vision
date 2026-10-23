
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
    h, w = img.shape[:2]
    src = np.float32([[0,0], [w-1,0], [0,h-1], [w-1,h-1]])
    dst = np.float32([[50,50], [w-50,0], [0,h-50], [w-1,h-1]])
    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (w,h))
    out = os.path.join(folder, "Q14_perspective.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Perspective Transformation", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
