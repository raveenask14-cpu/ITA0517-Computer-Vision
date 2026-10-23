
import cv2
import os

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg")
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sharpened = cv2.convertScaleAbs(laplacian)
    result = cv2.addWeighted(img, 1.5, sharpened, -0.5, 0)

    cv2.imwrite(os.path.join(folder, "Q29_sharpening.jpg"), result)
    cv2.imshow("Image Sharpening", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
