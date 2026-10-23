
import cv2
import os

# Input video path
input_path = r"C:\Users\Senthil kumar\OneDrive\Desktop\animal_video.mp4.mp4"

# Output folder path
output_folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(output_folder, exist_ok=True)

# Output video path
output_path = os.path.join(output_folder, "Q7_animal_video.mp4")

# Open input video
video = cv2.VideoCapture(input_path)

if not video.isOpened():
    print("Error: Cannot open video!")
else:
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps <= 0:
        fps = 25

    # Create output video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(
        output_path, fourcc, fps, (width, height)
    )

    if not writer.isOpened():
        print("Error: Cannot create output video!")
    else:
        print("Playing video and saving output...")
        print("Press Q to stop.")

        while True:
            ret, frame = video.read()

            if not ret:
                break

            # Save each frame
            writer.write(frame)

            # Display video
            cv2.imshow("Animal Video", frame)

            if cv2.waitKey(max(1, int(1000 / fps))) & 0xFF == ord('q'):
                break

        writer.release()
        print("Output video saved:", output_path)

    video.release()
    cv2.destroyAllWindows()

