import os
import shutil
import random

# Define the paths
original_dataset_dir = 'mel_spectrograms3'
base_dir = 'mel_spectrograms_split3'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

# Create directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Define the split ratios
train_ratio = 0.8
validation_ratio = 0.1
test_ratio = 0.1

# Get the list of all files in the original dataset directory
all_files = []
for root, dirs, files in os.walk(original_dataset_dir):
    for file in files:
        if file.endswith(('.png', '.jpg', '.jpeg')):  # Adjust the file extensions as needed
            all_files.append(os.path.join(root, file))

# Shuffle the files
random.shuffle(all_files)

# Calculate the number of files for each split
total_files = len(all_files)
train_count = int(total_files * train_ratio)
validation_count = int(total_files * validation_ratio)
test_count = total_files - train_count - validation_count

# Split the files
train_files = all_files[:train_count]
validation_files = all_files[train_count:train_count + validation_count]
test_files = all_files[train_count + validation_count:]

# Function to copy files to the respective directories
def copy_files(files, target_dir):
    for file in files:
        class_name = os.path.basename(os.path.dirname(file))
        class_dir = os.path.join(target_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)
        shutil.copy(file, class_dir)

# Copy the files to the respective directories
copy_files(train_files, train_dir)
copy_files(validation_files, validation_dir)
copy_files(test_files, test_dir)

print(f'Total files: {total_files}')
print(f'Training files: {len(train_files)}')
print(f'Validation files: {len(validation_files)}')
print(f'Test files: {len(test_files)}')