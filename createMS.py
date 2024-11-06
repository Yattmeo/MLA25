import os
import librosa
import matplotlib.pyplot as plt
import numpy as np

# Directory containing the .wav files
input_dir = 'Data/gen_jazz'
# Directory to save the .png files
output_dir = 'Mel_Spectrograms3'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to create and save Mel spectrogram
def save_mel_spectrogram(y, sr, output_path):
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_dB = librosa.power_to_db(S, ref=np.max)

    plt.figure(figsize=(5, 5))
    plt.axis('off')  # Remove axes
    plt.imshow(S_dB, aspect='auto', origin='lower', cmap='viridis')
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
    plt.close()

# Process each .wav file in the input directory and its subdirectories
for root, _, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith('.wav'):
            wav_path = os.path.join(root, filename)
            print(f"Processing file: {wav_path}")
            y, sr = librosa.load(wav_path, sr=None)
            duration = librosa.get_duration(y=y, sr=sr)
            segment_length = 3  # 3 seconds
            num_segments = int(duration // segment_length)

            for i in range(num_segments):
                start_sample = i * segment_length * sr
                end_sample = start_sample + segment_length * sr
                y_segment = y[start_sample:end_sample]

                relative_path = os.path.relpath(wav_path, input_dir)
                segment_output_path = os.path.join(output_dir, f"{os.path.splitext(relative_path)[0]}_segment_{i}.png")
                os.makedirs(os.path.dirname(segment_output_path), exist_ok=True)
                save_mel_spectrogram(y_segment, sr, segment_output_path)
                print(f"Saved segment {i} to {segment_output_path}")

print("Processing complete.")