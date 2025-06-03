from ultralytics import YOLO
import os
model = YOLO('yolov8n-cls.pt')  # You can use yolov8s-cls.pt for a larger model

# Train the model
model.train(
    data="dataset",
    epochs=10,
    imgsz=224,
    batch=32,
    project="runs/classify",
    name="deception_yolov8"
)

# Evaluate the model on the test set (if available)
model.val(data="dataset", imgsz=224, batch=32)
