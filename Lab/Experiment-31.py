
import cv2
import os

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg", 0)
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    result = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    cv2.imwrite(os.path.join(folder, "Q31_adaptive_threshold.jpg"), result)
    cv2.imshow("Adaptive Thresholding", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
