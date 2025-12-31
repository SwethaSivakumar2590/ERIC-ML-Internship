# Object Detection + Distance Estimation for Robotics Navigation- Swetha Sivakumar

## Project Overview
This project focuses on detecting navigation-relevant objects (cones, barriers, stop signs) and estimating their distance from the robot using a camera.  
The goal is to support robotics navigation by providing real-time perception of objects and their distances.  
Additionally, the project explores techniques to optimize the model for running efficiently on edge devices.

## Objectives
- Detect navigation-relevant objects: cones, barriers, stop signs.  
- Estimate distance from the robot (camera perspective) for each detected object.  
- Annotate results on the images/videos, e.g.:
  - `Cone, 1.5m`
  - `Stop Sign, 3.2m`  
- Explore optimization techniques (quantization, pruning, lightweight backbones) for edge deployment.


## Dataset
- **BDD100K dataset** (primary recommendation)  
- Optional: you may use any other relevant dataset for fine-tuning.  
- Use **transfer learning** with a pretrained model (YOLOv8 recommended) for object detection.


## Project Structure
```

PythonProject4/
│
├─ detect.py          # Object detection and distance estimation script
├─ train.py           # Training/fine-tuning object detection model
├─ optimize.py        # Scripts for quantization/pruning and FPS evaluation
├─ utils/             # Helper functions
│   ├─ distance.py
│   ├─ fps.py
│   ├─ visualization.py
│
├─ yolov8n.pt         # Pretrained YOLOv8 model
├─ requirements.txt   # Python dependencies
└─ README.md          # Project information (this file)

````

---

## How to Run
1. **Activate virtual environment:**
```powershell
.venv\Scripts\activate
````

2. **Install required packages:**

```powershell
pip install -r requirements.txt
```

3. **Run object detection and distance estimation:**

```powershell
python detect.py
```

4. **For training the model (optional/fine-tuning):**

```powershell
python train.py
```

5. **For optimization and FPS evaluation:**

```powershell
python optimize.py
```

---

## Optimization for Edge Devices

* Techniques explored:

  * Quantization
  * Pruning
  * Lightweight backbone networks
* FPS recorded on CPU and GPU for comparison.
* Optional Extra Credit:

  * Epipolar Geometry: derive disparity-depth relation.
  * Homography / Perspective Transform: bird’s-eye view.
  * Optical Flow: track moving objects across frames.

---

## Notes

* Transfer learning reduces training time.
* Distance estimation is based on geometric calculations (focal length, pixel size).
* Annotate bounding boxes with both object type and estimated distance.
* “Before vs. After” results shown for any optimizations (if applied).

---

## Author

Swetha Sivakumar

## Contact Info

* Email: swethasivakumar2590@gmail.com
* Phone: +91-8675732590
* GitHub: [https://github.com/SwethaSivakumar2590/ERIC-ML-Internship](https://github.com/SwethaSivakumar2590/ERIC-ML-Internship)

Do you want me to do that?
```
