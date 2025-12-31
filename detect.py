import cv2
from ultralytics import YOLO
from utils.distance import estimate_distance
from utils.visualization import draw_annotation

# YOLO model load (first time automatic-ah download aagum)
model = YOLO("yolov8n.pt")

# Webcam open
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Webcam open aagala")
        break

    # Object detection
    results = model(frame)[0]

    # Loop through detections
    for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
        label = model.names[int(cls)]
        bbox_height = box[3] - box[1]

        distance = estimate_distance(label, bbox_height)
        if distance is not None:
            frame = draw_annotation(frame, box, label, distance)

    cv2.imshow("Robot Vision", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
