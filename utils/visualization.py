import cv2

def draw_annotation(img, box, label, distance):
    x1, y1, x2, y2 = map(int, box)
    text = f"{label}, {distance}m"

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(
        img,
        text,
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )
    return img
