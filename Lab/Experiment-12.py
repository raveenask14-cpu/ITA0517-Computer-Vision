
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
folder = os.path.join(os.path.dirname(path), "output")
os.makedirs(folder, exist_ok=True)
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    result = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    out = os.path.join(folder, "Q12_rotate_270.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Rotate 270 Degrees Clockwise", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
