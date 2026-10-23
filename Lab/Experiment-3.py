
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cv2.Canny(gray, 100, 200)
    out = os.path.join(os.path.dirname(path), "Q3_canny.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Canny Edges", result)
    print("Saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
