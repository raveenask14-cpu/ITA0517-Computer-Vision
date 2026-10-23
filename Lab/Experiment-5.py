
import cv2
import os
import matplotlib.pyplot as plt

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\image.jpg"
folder = os.path.join(os.path.dirname(path), "output")
os.makedirs(folder, exist_ok=True)
img = cv2.imread(path)

if img is None:
    print("Image not found!")
else:
    for i, color in enumerate(("b", "g", "r")):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)

    plt.title("Colour Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])
    out = os.path.join(folder, "Q5_colour_histogram.png")
    plt.savefig(out)
    print("Output saved:", out)
    plt.show()
