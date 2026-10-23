
import cv2
import os

img = cv2.imread(r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg")
folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(folder, exist_ok=True)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    result = img.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

    cv2.imwrite(os.path.join(folder, "Q38_contours.jpg"), result)
    cv2.imshow("Contour Detection", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found!")
