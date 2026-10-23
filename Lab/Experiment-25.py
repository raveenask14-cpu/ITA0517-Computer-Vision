
import cv2
import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
folder = os.path.join(os.path.dirname(path), "output")
os.makedirs(folder, exist_ok=True)

img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    result = img.copy()
    count = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)
            if 0.5 < w / float(h) < 2.0:
                cv2.rectangle(result, (x, y), (x+w, y+h),
                              (0, 255, 0), 2)
                cv2.putText(result, "Possible Watch", (x, max(20, y-5)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)
                count += 1

    out = os.path.join(folder, "Q25_watch_detection.jpg")
    cv2.imwrite(out, result)

    print("Possible objects detected:", count)
    print("Output saved:", out)

    cv2.imshow("Watch-like Object Detection", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
