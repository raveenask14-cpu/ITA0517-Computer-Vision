
import cv2
import os

input_path = r"C:\Users\Senthil kumar\OneDrive\Desktop\traffic_video.mp4.mp4"

output_folder = r"C:\Users\Senthil kumar\OneDrive\Desktop\output"
os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(output_folder, "Q28_vehicle_detection.mp4")

video = cv2.VideoCapture(input_path)

if not video.isOpened():
    print("Cannot open video. Check the file path.")
else:
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if fps <= 0:
        fps = 25

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width, height)
    )

    subtractor = cv2.createBackgroundSubtractorMOG2(
        history=300, varThreshold=40, detectShadows=False
    )

    print("Processing traffic video...")

    while True:
        ret, frame = video.read()
        if not ret:
            break

        mask = subtractor.apply(frame)
        mask = cv2.medianBlur(mask, 5)

        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        result = frame.copy()

        for contour in contours:
            if cv2.contourArea(contour) > 800:
                x, y, w, h = cv2.boundingRect(contour)

                cv2.rectangle(
                    result, (x, y), (x+w, y+h), (0, 255, 0), 2
                )

                cv2.putText(
                    result, "Moving Object", (x, max(y-10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2
                )

        writer.write(result)
        cv2.imshow("Q28 - Moving Object Detection", result)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    writer.release()
    cv2.destroyAllWindows()

    print("Output saved:", output_path)
