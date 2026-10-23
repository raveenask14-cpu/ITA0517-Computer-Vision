
import cv2
import os

# Input video
input_path = r"C:\Users\Senthil kumar\OneDrive\Desktop\animal_video.mp4.mp4"

# Output folder
output_folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(
    output_folder, "Q39_reverse_slow_motion.mp4"
)

video = cv2.VideoCapture(input_path)

if not video.isOpened():
    print("Error: Cannot open video!")
else:
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps <= 0:
        fps = 25

    # Read all frames
    frames = []

    while True:
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)

    video.release()

    if not frames:
        print("Error: No frames found!")
    else:
        # Half-speed playback
        slow_fps = max(1, fps / 2)

        writer = cv2.VideoWriter(
            output_path,
            cv2.VideoWriter_fourcc(*"mp4v"),
            slow_fps,
            (width, height)
        )

        if not writer.isOpened():
            print("Error: Cannot create output video!")
        else:
            # Write frames in reverse order
            for frame in reversed(frames):
                writer.write(frame)

            writer.release()
            print("Output saved:", output_path)

            # Play the result
            result = cv2.VideoCapture(output_path)

            while True:
                ret, frame = result.read()
                if not ret:
                    break

                cv2.imshow("Q39 - Reverse Slow Motion", frame)

                if cv2.waitKey(30) & 0xFF == ord("q"):
                    break

            result.release()
            cv2.destroyAllWindows()
