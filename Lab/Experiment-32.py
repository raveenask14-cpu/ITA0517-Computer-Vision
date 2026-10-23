
import cv2
import os

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg", 0)
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    result = cv2.Canny(img, 100, 200)
    cv2.imwrite(os.path.join(folder, "Q32_canny_edges.jpg"), result)
    cv2.imshow("Canny Edge Detection", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
