
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out = os.path.join(os.path.dirname(path), "Q1_grayscale.jpg")
    cv2.imwrite(out, gray)
    cv2.imshow("Grayscale Image", gray)
    print("Saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
