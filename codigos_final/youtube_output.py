from vidgear.gears import CamGear
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO(r"C:\Users\FERNANDO\Downloads\WOTR\runs\detect\train11\weights\last.pt")

options = {
    "STREAM_RESOLUTION": "720p",
}

stream = CamGear(source='https://www.youtube.com/watch?v=DcxKsF-Dv8o', stream_mode=True, logging=True, **options).start()

while True:
    frame = stream.read()

    if frame is None:
        break

    # Run YOLOv8 inference on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLOv8 Inference", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
stream.stop()