#!/usr/bin/env python3
"""
Simple Audio Asset Path Helper - No dependencies required
Demonstrates how to reference Dropbox assets in your code
"""

import os

def find_dropbox_audio_assets():
    """Find the Dropbox audio assets folder"""
    possible_paths = [
        "~/Dropbox (Personal)/AVMI-GVSC-Audio-Assets",
        "~/Dropbox/AVMI-GVSC-Audio-Assets",
        "~/Dropbox (Work)/AVMI-GVSC-Audio-Assets"
    ]
    
    for path in possible_paths:
        expanded_path = os.path.expanduser(path)
        if os.path.exists(expanded_path):
            return expanded_path
    
    return None

def get_audio_asset_path(category, filename):
    """Get path to an audio asset"""
    dropbox_path = find_dropbox_audio_assets()
    
    if not dropbox_path:
        raise FileNotFoundError(
            "Dropbox audio assets folder not found. "
            "Please create: ~/Dropbox/AVMI-GVSC-Audio-Assets"
        )
    
    asset_path = os.path.join(dropbox_path, category, filename)
    
    if not os.path.exists(asset_path):
        raise FileNotFoundError(f"Audio asset not found: {asset_path}")
    
    return asset_path

def verify_setup():
    """Verify Dropbox setup"""
    dropbox_path = find_dropbox_audio_assets()
    
    if dropbox_path:
        print(f"✅ Found Dropbox audio assets folder: {dropbox_path}")
        
        # Check subfolders
        expected_folders = ['samples', 'presets', 'templates', 'evaluation_data', 'raw_recordings', 'processed']
        for folder in expected_folders:
            folder_path = os.path.join(dropbox_path, folder)
            if os.path.exists(folder_path):
                print(f"📁 Found: {folder}/")
            else:
                print(f"📁 Missing: {folder}/ (will be created when needed)")
        
        return True
    else:
        print("❌ Dropbox audio assets folder not found!")
        print("\n💡 To set up:")
        print("1. Create shared Dropbox folder: AVMI-GVSC-Audio-Assets")
        print("2. Share with team members")
        print("3. Wait for local sync")
        print("4. Create subfolders: samples, presets, templates, evaluation_data, raw_recordings, processed")
        return False

# Example usage
if __name__ == "__main__":
    print("🎵 AVMI-GVSC Audio Asset Helper")
    print("=" * 40)
    
    if verify_setup():
        print("\n✅ Setup complete! You can now use audio assets in your code:")
        print()
        print("# Example Python code:")
        print("from scripts.audio_asset_helper import get_audio_asset_path")
        print()
        print("# Load an audio sample")
        print("sample_path = get_audio_asset_path('samples', 'engine_recording.wav')")
        print("# Use sample_path in your audio processing code")
    else:
        print("\n⚠️ Please complete Dropbox setup first")