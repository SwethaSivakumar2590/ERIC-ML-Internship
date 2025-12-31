def estimate_distance(object_name, bbox_height_px, focal_length=800):
    heights = {
        "cone": 0.5,
        "barrier": 1.0,
        "stop_sign": 2.0
    }

    if bbox_height_px <= 0:
        return None

    if object_name not in heights:
        return None

    distance = (heights[object_name] * focal_length) / bbox_height_px
    return round(distance, 2)
