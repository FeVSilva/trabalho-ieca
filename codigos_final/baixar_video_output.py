if __name__ == '__main__':
    from ultralytics import YOLO
    import cv2

    model = YOLO(r"C:\Users\FERNANDO\Downloads\WOTR\salvo1.pt")

    results = model(r'C:\Users\FERNANDO\Downloads\Testes\videos\video1.mp4', save=False, conf=0.5, show=True)