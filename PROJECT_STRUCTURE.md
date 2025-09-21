# AVMI-GVSC Project Structure Setup

## ✅ What We've Created

### 1. Separate Asset Storage Structure
```
~/Dropbox (Personal)/
├── GitHub/                                    # All Git repositories
│   └── AVMI-GVSC-SoundSystem/                # This repository (lightweight)
└── AVMI-GVSC-Audio-Assets/                   # Shared assets (separate)
    ├── samples/
    ├── presets/
    ├── templates/
    ├── evaluation_data/
    ├── raw_recordings/
    └── processed/
```

### 2. Updated Configuration
- `config/assets.yaml` - Points to separate Dropbox folder
- `assets/manifest.yaml` - Tracks metadata only
- `.gitignore` - Excludes large audio files

### 3. Management Tools
- `scripts/asset_manager.py` - Full-featured asset management
- `scripts/audio_asset_helper.py` - Simple path resolution

### 4. Documentation
- `docs/AUDIO_ASSET_MANAGEMENT.md` - Complete setup guide
- Asset folder has its own README

## 🎯 Benefits Achieved

✅ **Repository stays fast** - No large files in Git  
✅ **Cross-project sharing** - Assets can be used by multiple repos  
✅ **Team collaboration** - Dropbox handles file distribution  
✅ **Scalable structure** - Easy to add new repositories  
✅ **Local access** - Files available offline once synced  

## 🚀 Next Steps

### For You:
1. **Share the Dropbox folder** with team members
2. **Add your first audio assets** to test the system
3. **Update your audio processing code** to use the asset helper

### For Team Members:
1. **Accept Dropbox folder invitation**
2. **Wait for sync** to complete
3. **Run verification**: `python3 scripts/audio_asset_helper.py`
4. **Start using assets** in their code

### For Future Repositories:
When creating new AVMI-GVSC repositories:
1. **Add similar asset management scripts**
2. **Reference the same shared Dropbox folder**
3. **Keep repositories lightweight**

## 📋 Usage Examples

### Simple Usage:
```python
from scripts.audio_asset_helper import get_audio_asset_path

# Load an audio sample
sample_path = get_audio_asset_path('samples', 'engine_recording.wav')

# Use in your audio processing
import librosa
audio, sr = librosa.load(sample_path)
```

### Advanced Management:
```bash
# Add new asset
python3 scripts/asset_manager.py register \
  --file /path/to/audio.wav \
  --category samples

# List all assets  
python3 scripts/asset_manager.py list

# Validate assets
python3 scripts/asset_manager.py validate
```

This structure is ready for production use and follows industry best practices! 🎉