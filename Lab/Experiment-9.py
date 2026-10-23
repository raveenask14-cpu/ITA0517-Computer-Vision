
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
folder = os.path.join(os.path.dirname(path), "output")
os.makedirs(folder, exist_ok=True)
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    bigger = cv2.resize(img, None, fx=1.5, fy=1.5)
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

    p1 = os.path.join(folder, "Q9_bigger.jpg")
    p2 = os.path.join(folder, "Q9_smaller.jpg")
    cv2.imwrite(p1, bigger)
    cv2.imwrite(p2, smaller)

    cv2.imshow("Bigger", bigger)
    cv2.imshow("Smaller", smaller)
    print("Outputs saved:", p1, p2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
