import torch
from ultralytics import YOLO

model = YOLO(r"caminho_do_last")
torch.save(model, "salvo2.pt")
model2 = torch.load("salvo2.pt")