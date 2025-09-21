# Team Setup Instructions

## 📧 Email Template for Team Members

Copy and customize this email for your team:

---

**Subject:** AVMI-GVSC Audio Asset Management Setup - Action Required

**Hi Team,**

We've set up a new audio asset management system for the AVMI-GVSC project that will keep our repositories fast while managing large audio files efficiently.

### 🚀 **Quick Setup (5 minutes):**

1. **Accept Dropbox Invitation**
   - Check your email for Dropbox folder invitation: `AVMI-GVSC-Audio-Assets`
   - Click "Join folder" and wait for sync to complete

2. **Clone/Update Repository**
   ```bash
   git clone https://github.com/CHI-CityTech/AVMI-GVSC-SoundSystem.git
   cd AVMI-GVSC-SoundSystem
   ```

3. **Verify Setup**
   ```bash
   python3 scripts/audio_asset_helper.py
   ```
   You should see: ✅ Setup complete!

### 💻 **Using Audio Assets in Your Code:**

```python
from scripts.audio_asset_helper import get_audio_asset_path

# Load any audio sample
sample_path = get_audio_asset_path('samples', 'engine_recording.wav')

# Use with your preferred audio library
import librosa
audio, sr = librosa.load(sample_path)
```

### 📁 **How It Works:**
- **Large audio files** → Stored in shared Dropbox folder (synced locally)
- **Code repositories** → Stay lightweight and fast
- **Your workflow** → Reference files as if they're local (because they are!)

### 🆘 **Troubleshooting:**
- **"Dropbox folder not found"** → Make sure folder is synced (not online-only)
- **"Asset not found"** → Check file exists in Dropbox folder
- **Questions?** → See full guide: `docs/AUDIO_ASSET_MANAGEMENT.md`

### 📋 **Adding New Assets:**
1. Copy files to appropriate Dropbox subfolder:
   - `samples/` - Raw recordings
   - `presets/` - Processing configurations
   - `templates/` - Audio templates
2. Files automatically sync to team
3. Use in code immediately!

**Benefits:** Fast repository clones, automatic team sync, unlimited audio storage, local file access.

**Questions?** Reply to this email or check the documentation.

Best regards,  
[Your Name]

---

## 📖 **Alternative: Short Email with Links**

For a more concise approach:

---

**Subject:** AVMI-GVSC Audio Assets - Setup Required

**Hi Team,**

We've implemented a new audio asset management system. Please follow the setup guide here:

**📚 Setup Guide:** https://github.com/CHI-CityTech/AVMI-GVSC-SoundSystem/blob/main/docs/AUDIO_ASSET_MANAGEMENT.md

**🚀 Quick Start:** https://github.com/CHI-CityTech/AVMI-GVSC-SoundSystem/blob/main/PROJECT_STRUCTURE.md

**Action Required:**
1. Accept Dropbox folder invitation (check email)
2. Run verification: `python3 scripts/audio_asset_helper.py`
3. Start using audio assets in your code!

Questions? See documentation or reply to this email.

---

## 🔧 **For Project Managers**

### Pre-sending Checklist:
- [ ] Dropbox folder `AVMI-GVSC-Audio-Assets` created and populated
- [ ] Team members invited to Dropbox folder with "Can edit" permissions
- [ ] Repository is up to date with latest asset management tools
- [ ] Documentation is current and accessible

### After Team Setup:
- [ ] Verify each team member can run `python3 scripts/audio_asset_helper.py` successfully
- [ ] Confirm team members can access and use audio assets
- [ ] Monitor Dropbox folder for proper usage patterns
- [ ] Address any setup issues promptly

### Ongoing Maintenance:
- [ ] Regular cleanup of unused assets
- [ ] Periodic verification of asset integrity
- [ ] Update documentation as workflow evolves
- [ ] Monitor storage usage and team permissions