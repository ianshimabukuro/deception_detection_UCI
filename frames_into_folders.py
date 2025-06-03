import os
import json
import shutil

# Paths
json_path = "json_output/sneheil_uni.json"
frames_dir = "output_frames"
output_dirs = {
    "True": "frames_true",
    "False": "frames_false",
    "Neutral": "frames_neutral"
}

# Create output directories if they don't exist
for dir_path in output_dirs.values():
    os.makedirs(dir_path, exist_ok=True)

# Load labels
with open(json_path, "r") as f:
    labels = json.load(f)

# Get sorted list of frame filenames
frame_files = sorted(os.listdir(frames_dir))

print(len(labels), len(frame_files))
# Check that lengths match
assert len(labels) == len(frame_files), "Mismatch between labels and frames!"

# Move/copy frames to corresponding folders
for label, frame_file in zip(labels, frame_files):
    src = os.path.join(frames_dir, frame_file)
    dst = os.path.join(output_dirs[label], frame_file)
    shutil.copy2(src, dst)  # Use copy2 to preserve metadata

print("Frames sorted into folders by label.")