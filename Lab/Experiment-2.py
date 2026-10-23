
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    result = cv2.GaussianBlur(img, (7, 7), 0)
    out = os.path.join(os.path.dirname(path), "Q2_blur.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Gaussian Blur", result)
    print("Saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
