import os

path = r"C:\Users\Senthil kumar\OneDrive\Desktop\output\Q40_text_detection.mp4"

if os.path.exists(path):
    print("Video exists!")
    print("File size:", os.path.getsize(path), "bytes")
    os.startfile(path)
else:
    print("Video file not found!")

