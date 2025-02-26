# Wav2Lip - Lip-Sync Model

This repository implements the Wav2Lip model to generate realistic lip-sync videos from an image and audio file.

## 📁 Project Structure

```
Wav2Lip/
├── README.md                  # Project Documentation
├── checkpoints/               # Model weights directory
│    ├── README.md             # Model weights info
│    ├── face_sync.pth         # SyncNet model weight (for lip-sync evaluation)
│    └── wav2lip_gan.pth       # Wav2Lip GAN model weight
├── inputs/                    # Input media directory
│    ├── image.jpg             # Input face image
│    └── input_audio.mp3       # Input audio file
├── outputs/                   # Output media directory
│    └── result.mp4            # Lip-synced output video
├── inference.py               # Main script for inference
├── requirements.txt           # Python dependencies
└── ...                        # Other training and evaluation scripts
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Wav2Lip.git
cd Wav2Lip
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv wav2lip_env
source wav2lip_env/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download Pre-trained Models

Ensure the following weights exist under the `checkpoints/` folder:

- [wav2lip_gan.pth](https://github.com/Rudrabha/Wav2Lip/releases/download/v1.0/wav2lip_gan.pth)
- [face_sync.pth](https://github.com/Rudrabha/Wav2Lip/releases/download/v1.0/face_sync.pth)

Download and place them in `checkpoints/` folder:

```bash
wget "https://github.com/Rudrabha/Wav2Lip/releases/download/v1.0/wav2lip_gan.pth" -P checkpoints/
wget "https://github.com/Rudrabha/Wav2Lip/releases/download/v1.0/face_sync.pth" -P checkpoints/
```

## ▶️ Running the Model

Ensure you have an image and audio file in the `inputs/` folder.

```bash
python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth \
    --face inputs/image.jpg --audio inputs/input_audio.mp3 \
    --outfile outputs/result.mp4
```

### Example Input Files:
- `inputs/image.jpg`: Image to animate.
- `inputs/input_audio.mp3`: Audio for lip-sync.

### Output:
- `outputs/result.mp4`: Generated lip-synced video.f

## 📚 References

- [Wav2Lip Paper](https://arxiv.org/abs/2008.10010)
- [Original Wav2Lip Repository](https://github.com/Rudrabha/Wav2Lip)


