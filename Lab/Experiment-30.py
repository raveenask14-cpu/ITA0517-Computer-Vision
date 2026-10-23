
import cv2
import os

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg", 0)
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    _, result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(folder, "Q30_thresholding.jpg"), result)
    cv2.imshow("Thresholding", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
