from utils import extract_frames
import os
import json
import shutil
import random


"""
1. First we extract all frames from the video
"""

extract_frames('sneheil.mov', 'output_frames') #Path to the video file  

"""
2. Then we separate each frame into neutral, true or false folders
"""


json_path = "json_output/sneheil_uni.json" #Path to the clicker result json file
frames_dir = "output_frames"
output_dirs = {
    "True": "true",
    "False": "false",
    "Neutral": "neutral"
}

for dir_path in output_dirs.values():
    os.makedirs(dir_path, exist_ok=True)

# Load the json file into a python list
with open(json_path, "r") as f:
    labels = json.load(f)

# Get sorted list of frame filenames, kinda pointless kinda they are already sorted 
frame_files = sorted(os.listdir(frames_dir))


# Check that lengths match for the JSON and Number of Frames
assert len(labels) == len(frame_files), "Mismatch between labels and frames!"

# Move/copy frames to corresponding folders
for label, frame_file in zip(labels, frame_files):
    src = os.path.join(frames_dir, frame_file)
    dst = os.path.join(output_dirs[label], frame_file)
    shutil.copy2(src, dst)  # Use copy2 to preserve metadata

print("Frames sorted into folders by label.")

"""
3. We split the dataset into train, validation and test sets
"""

input_dirs = {
    "true": "true",
    "false": "false",
    "neutral": "neutral"
}
output_base = "dataset"
splits = ["train", "val", "test"]
val_ratio = 0.2   # 20% for validation
test_ratio = 0.1  # 10% for test

os.makedirs(output_base, exist_ok=True)

for class_dir, src_dir in input_dirs.items():
    images = os.listdir(src_dir)
    random.shuffle(images)
    n = len(images)
    n_test = int(n * test_ratio)
    n_val = int(n * val_ratio)
    n_train = n - n_val - n_test
    split_files = {
        "train": images[:n_train],
        "val": images[n_train:n_train + n_val],
        "test": images[n_train + n_val:]
    }
    for split in splits:
        out_dir = os.path.join(output_base, split, class_dir)
        os.makedirs(out_dir, exist_ok=True)
        for img in split_files[split]:
            shutil.copy2(os.path.join(src_dir, img), os.path.join(out_dir, img))