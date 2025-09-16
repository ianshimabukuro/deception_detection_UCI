# Deception Detection using Frame Level Classification

This repository contains code for a video-based deception detection pipeline using **YOLOv8 classification**. The system processes videos into frames, annotates them with human input, organizes them into train/val/test datasets, and trains a YOLOv8 classifier to detect truth, deception, or neutral expressions.  

---

## Features

- Frame extraction from raw videos  
- Human annotation via keyboard-based clicker tool  
- Automatic organization of annotated frames into train/val/test splits  
- Training a YOLOv8 classifier on the processed dataset  
- Live inference using a webcam feed with top-2 predictions displayed in real-time  

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ianshimabukuro/deception_detection_UCI.git
   cd deception_detection_UCI
2. Install dependencies:
   ```bash
   pip install ultralytics opencv-python keyboard
## Workflow

### 1. Frame Extraction
Extract frames from a video:
```bash
python annotation_vid_2_tvt_folders.py
```

### 2. Annotation
Run the clicker tool to label frames:
```bash
python clicker.py
```

### 3. Dataset Preparation
`annotation_vid_2_tvt_folders.py` also:  
- Reads the JSON annotation file  
- Copies frames into `true/`, `false/`, and `neutral/` folders  
- Splits data into `train/`, `val/`, and `test/` sets

### 4. Training
Train a YOLOv8 classifier:
```bash
python train.py
```

### 5. Inference
Run webcam inference with trained weights:
```bash
python inference.py
```


## Example Data Flow

1. Raw video → extracted frames  
2. Annotate frames with `clicker.py`  
3. Frames split into `train/val/test` by label  
4. Train YOLOv8 on dataset  
5. Run `inference.py` for live predictions  
