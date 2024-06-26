if __name__ == '__main__':
    from ultralytics import YOLO

# Load a model
    model = YOLO(r'caminho_do_salvo1')

# Use the model
    model.train(data='config.yaml', epochs=300,  batch=-1, conf=0.6)  # train the model