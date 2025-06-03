from ultralytics import YOLO
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("sneheil_best_weight.pt")

# object classes
classNames = ["neutral", "true", "false"
              ]


while True:
    success, img = cap.read()
    results = model(img, stream=False)
    r = results[0]
    probs = r.probs.data.cpu().numpy()  
    top2_idx = probs.argsort()[-2:][::-1]
 
    y_offset = 30
    for i in top2_idx:
        class_name = r.names[i]
        confidence = probs[i]
        label = f"{class_name}: {confidence:.2f}"
        cv2.putText(img, label, (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        y_offset += 30
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()