from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8n model
model = YOLO(r"C:\Users\FERNANDO\Downloads\Backup WOTR\salvo3.pt")

# Run inference on the webcam
results = model(source='0', conf=0.6, show=True)  # generator of Results objects

print(results)