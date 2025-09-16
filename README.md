# Deception Detection (UCI)

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
   
