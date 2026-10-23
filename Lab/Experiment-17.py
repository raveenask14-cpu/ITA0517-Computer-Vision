
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
folder = os.path.join(os.path.dirname(path), "output")
os.makedirs(folder, exist_ok=True)
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    result = img.copy()
    h, w = result.shape[:2]
    cv2.putText(result, "WATERMARK", (20, h-20),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    out = os.path.join(folder, "Q17_watermark.jpg")
    cv2.imwrite(out, result)
    cv2.imshow("Watermark", result)
    print("Output saved:", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
