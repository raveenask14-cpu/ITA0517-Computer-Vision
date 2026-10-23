
import cv2
import os

# Input image path
image_path = r"C:\Users\Senthil kumar\OneDrive\Desktop\human face.jpg"

# Face detection XML model path
model_path = r"C:\Users\Senthil kumar\OneDrive\Desktop\haarcascade_frontalface_default.xml"

# Output folder path
output_folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(output_folder, exist_ok=True)

# Read the input image
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
else:
    # Load the face detection model
    face_cascade = cv2.CascadeClassifier(model_path)

    if face_cascade.empty():
        print("Error: XML model not loaded! Check the file name and path.")
    else:
        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw rectangles around detected faces
        result = img.copy()

        for (x, y, w, h) in faces:
            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        # Save the output image
        output_path = os.path.join(
            output_folder, "Q27_face_detection.jpg"
        )
        cv2.imwrite(output_path, result)

        print("Number of faces detected:", len(faces))
        print("Output saved at:", output_path)

        # Display the result
        cv2.imshow("Q27 - Face Detection", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
