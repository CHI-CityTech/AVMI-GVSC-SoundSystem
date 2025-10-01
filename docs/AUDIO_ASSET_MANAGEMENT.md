# Audio Asset Management Guide

## 🎯 Overview

This project uses a **Dropbox shared folder approach** for audio assets. Large audio files are stored in a shared Dropbox folder that syncs locally to all team members, while the Git repository only tracks metadata and references.

## 📋 Why This Approach?

✅ **Repository stays fast** - No large files in Git  
✅ **Automatic sync** - Dropbox handles file distribution  
✅ **Local access** - Files available offline once synced  
✅ **Team collaboration** - Everyone gets the same files  
✅ **Unlimited storage** - Use existing Dropbox space  
✅ **Version control** - Dropbox handles file versions  

## 🚀 Quick Setup

### 1. Create Shared Dropbox Folder
```bash
# Create this folder in your Dropbox (separate from repositories):
~/Dropbox (Personal)/AVMI-GVSC-Audio-Assets/
├── samples/
├── presets/
├── templates/
├── evaluation_data/
├── raw_recordings/
└── processed/
```

**Important**: This folder is **separate** from your GitHub repositories and can be shared across multiple AVMI-GVSC projects.

### 2. Share with Team
- Right-click folder → "Share" 
- Invite all team members
- Set permissions: "Can edit"

### 3. Wait for Sync
All team members will get the folder synced locally

### 4. Verify Setup
```bash
python3 scripts/audio_asset_helper.py
```

## 💻 Using Assets in Your Code

### Simple approach (no dependencies):
```python
from scripts.audio_asset_helper import get_audio_asset_path

# Load an audio sample
sample_path = get_audio_asset_path('samples', 'engine_recording.wav')

# Use in your audio processing
import librosa
audio, sr = librosa.load(sample_path)
```

### Full asset manager (requires PyYAML):
```bash
# Install dependencies
pip install pyyaml

# Register a new asset
python3 scripts/asset_manager.py register \
  --file /path/to/your/audio.wav \
  --category samples

# List all assets
python3 scripts/asset_manager.py list

# Scan Dropbox folder for new files
python3 scripts/asset_manager.py scan --all
```

## 📁 Project Structure

Your complete setup should look like this:

```
~/Dropbox (Personal)/
├── GitHub/                                    # Git repositories
│   ├── AVMI-GVSC-SoundSystem/                # This repository
│   ├── AVMI-GVSC-DataAnalysis/               # Future repository
│   └── AVMI-GVSC-VehicleControl/             # Future repository
└── AVMI-GVSC-Audio-Assets/                   # Shared assets (separate)
    ├── samples/                    # Raw audio samples
    │   ├── engine_idle_001.wav
    │   ├── road_noise_highway.wav
    │   └── vehicle_pass_by.wav
    ├── presets/                    # Audio processing presets
    │   ├── spatial_config.json
    │   └── noise_reduction.xml
    ├── templates/                  # Audio templates
    │   ├── alert_template.wav
    │   └── notification_base.wav
    ├── evaluation_data/            # Large test datasets
    │   ├── dataset_v1/
    │   └── validation_set/
    ├── raw_recordings/             # Unprocessed recordings
    │   └── field_recordings/
    └── processed/                  # Enhanced audio files
        └── cleaned_samples/
```

### 🎯 Benefits of This Structure:

✅ **Cross-project sharing** - Multiple repos can use the same assets  
✅ **Clean repositories** - Git repos stay lightweight  
✅ **Easy team onboarding** - New team members get assets automatically  
✅ **Scalable** - Add new repositories without restructuring

## 🔄 Team Workflow

Your Dropbox folder should look like:
```
AVMI-GVSC-Audio-Assets/
├── samples/                    # Raw audio samples
│   ├── engine_idle_001.wav
│   ├── road_noise_highway.wav
│   └── vehicle_pass_by.wav
├── presets/                    # Audio processing presets
│   ├── spatial_config.json
│   └── noise_reduction.xml
├── templates/                  # Audio templates
│   ├── alert_template.wav
│   └── notification_base.wav
├── evaluation_data/            # Large test datasets
│   ├── dataset_v1/
│   └── validation_set/
├── raw_recordings/             # Unprocessed recordings
│   └── field_recordings/
└── processed/                  # Enhanced audio files
    └── cleaned_samples/
```

## 🔄 Team Workflow

### Adding New Assets:
1. **Copy files** to Dropbox folder (manually or via script)
2. **Wait for sync** (automatic)
3. **Register in manifest** (optional, for tracking):
   ```bash
   python3 scripts/asset_manager.py register \
     --file ~/Dropbox/AVMI-GVSC-Audio-Assets/samples/new_file.wav \
     --category samples
   ```
4. **Commit manifest** changes to Git

### Using Assets in Development:
```python
# Your code references local Dropbox paths
import os

def load_audio_sample(filename):
    # Dropbox synced folder
    base_path = os.path.expanduser("~/Dropbox/AVMI-GVSC-Audio-Assets")
    sample_path = os.path.join(base_path, "samples", filename)
    
    if not os.path.exists(sample_path):
        raise FileNotFoundError(f"Audio sample not found: {filename}")
    
    return sample_path
```

## � Configuration

The `config/assets.yaml` file defines:
- Dropbox folder paths
- Subfolder structure  
- File organization rules

The `assets/manifest.yaml` file tracks:
- Asset metadata
- File checksums
- Creation dates
- Custom metadata

## ⚡ Benefits vs Other Approaches

| Approach | Repository Size | Setup Complexity | Team Sync | Storage Cost |
|----------|-----------------|------------------|-----------|--------------|
| **Dropbox Shared** | Small ✅ | Simple ✅ | Automatic ✅ | Existing ✅ |
| Git LFS | Medium | Medium | Manual | Expensive ❌ |
| Cloud URLs | Small | Complex ❌ | Manual | Varies |
| Direct Git | Huge ❌ | Simple | Automatic | Free |

## 🔧 Troubleshooting

### "Dropbox folder not found"
1. Check if Dropbox is installed and running
2. Verify folder name: `AVMI-GVSC-Audio-Assets`
3. Make sure folder is synced (not online-only)

### "Asset not found"
1. Check if file exists in Dropbox folder
2. Verify file is synced locally (green checkmark)
3. Check spelling of filename

### Slow sync
1. Check Dropbox sync status
2. Consider Dropbox selective sync settings
3. Large files may take time to sync

## � Next Steps

1. **Create the Dropbox folder** and share with team
2. **Test the setup** using the helper script
3. **Start adding audio assets** to appropriate folders
4. **Update your audio processing code** to reference Dropbox paths
5. **Consider installing PyYAML** for advanced asset management

This approach scales from small teams to large projects while keeping your Git repository fast and manageable!