
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
folder = os.path.join(os.path.dirname(path), "output")
os.makedirs(folder, exist_ok=True)
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    h, w = img.shape[:2]
    roi = img[h//4:3*h//4, w//4:3*w//4].copy()
    result = img.copy()
    rh, rw = roi.shape[:2]
    result[0:rh, 0:rw] = roi
    out = os.path.join(folder, "Q18_roi.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("ROI Copy Paste", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
