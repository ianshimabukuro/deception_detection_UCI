import os
import shutil
import random

input_dirs = {
    "frames_true": "frames_true",
    "frames_false": "frames_false",
    "frames_neutral": "frames_neutral"
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