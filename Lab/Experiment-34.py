
import cv2
import os

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg")
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    result = cv2.resize(img, None, fx=0.5, fy=0.5)
    cv2.imwrite(os.path.join(folder, "Q34_resized.jpg"), result)
    cv2.imshow("Resized Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
