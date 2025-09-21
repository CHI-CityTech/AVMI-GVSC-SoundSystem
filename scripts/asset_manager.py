#!/usr/bin/env python3
"""
Audio Asset Manager for AVMI-GVSC-SoundSystem

This script manages audio assets stored in a shared Dropbox folder that syncs locally.
The repository only tracks metadata and references, while actual audio files
live in the synced Dropbox folder.

Usage:
    python scripts/asset_manager.py verify
    python scripts/asset_manager.py list --category samples
    python scripts/asset_manager.py register /path/to/audio/file.wav --category samples
    python scripts/asset_manager.py scan --category samples
    python scripts/asset_manager.py validate
"""

import os
import sys
import yaml
import hashlib
import argparse
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

class AudioAssetManager:
    def __init__(self, config_path: str = "config/assets.yaml"):
        self.config_path = config_path
        self.manifest_path = "assets/manifest.yaml"
        self.load_config()
        self.load_manifest()
        self.dropbox_path = self.find_dropbox_path()
    
    def load_config(self):
        """Load asset management configuration"""
        with open(self.config_path, 'r') as f:
            self.config = yaml.safe_load(f)
    
    def load_manifest(self):
        """Load asset manifest"""
        try:
            with open(self.manifest_path, 'r') as f:
                self.manifest = yaml.safe_load(f)
        except FileNotFoundError:
            self.manifest = {
                'version': '1.0',
                'last_updated': datetime.now().isoformat(),
                'dropbox_folder': 'AVMI-GVSC-Audio-Assets',
                'categories': {}
            }
    
    def save_manifest(self):
        """Save updated manifest"""
        self.manifest['last_updated'] = datetime.now().isoformat()
        with open(self.manifest_path, 'w') as f:
            yaml.dump(self.manifest, f, default_flow_style=False, indent=2)
    
    def find_dropbox_path(self) -> Optional[str]:
        """Find the Dropbox audio assets folder"""
        possible_paths = [
            "~/Dropbox (Personal)/AVMI-GVSC-Audio-Assets",
            "~/Dropbox/AVMI-GVSC-Audio-Assets",
            "~/Dropbox (Work)/AVMI-GVSC-Audio-Assets"
        ]
        
        # Also check config for custom paths
        if 'asset_storage' in self.config and 'dropbox_shared' in self.config['asset_storage']:
            config_paths = [self.config['asset_storage']['dropbox_shared']['base_path']]
            config_paths.extend(self.config['asset_storage']['dropbox_shared'].get('alternative_paths', []))
            possible_paths = config_paths + possible_paths
        
        for path in possible_paths:
            expanded_path = os.path.expanduser(path)
            if os.path.exists(expanded_path):
                return expanded_path
        
        return None
    
    def verify_dropbox_setup(self) -> bool:
        """Verify that Dropbox folder is available and properly structured"""
        if not self.dropbox_path:
            print("❌ Dropbox audio assets folder not found!")
            print("Expected locations:")
            print("  - ~/Dropbox (Personal)/AVMI-GVSC-Audio-Assets")
            print("  - ~/Dropbox/AVMI-GVSC-Audio-Assets")
            print("  - ~/Dropbox (Work)/AVMI-GVSC-Audio-Assets")
            print("\n💡 To fix:")
            print("  1. Create shared Dropbox folder: AVMI-GVSC-Audio-Assets")
            print("  2. Invite team members to the folder")
            print("  3. Wait for Dropbox to sync locally")
            return False
        
        print(f"✅ Found Dropbox audio assets folder: {self.dropbox_path}")
        
        # Check/create subfolder structure
        subfolders = self.config.get('asset_storage', {}).get('dropbox_shared', {}).get('subfolders', {})
        default_subfolders = ['samples', 'presets', 'templates', 'evaluation_data', 'raw_recordings', 'processed']
        
        folders_to_create = list(subfolders.values()) if subfolders else default_subfolders
        
        for folder in folders_to_create:
            folder_path = os.path.join(self.dropbox_path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                print(f"📁 Created subfolder: {folder}")
            else:
                print(f"📁 Found subfolder: {folder}")
        
        return True
    
    def get_asset_path(self, category: str, filename: str) -> str:
        """Get the full path to an asset in the Dropbox folder"""
        if not self.dropbox_path:
            raise FileNotFoundError("Dropbox audio assets folder not found")
        
        return os.path.join(self.dropbox_path, category, filename)
    
    def calculate_checksum(self, file_path: str) -> str:
        """Calculate SHA256 checksum of a file"""
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    
    def register_asset(self, source_path: str, category: str, filename: str = None, metadata: Dict = None):
        """Register an asset by copying it to the Dropbox folder and updating manifest"""
        if not self.verify_dropbox_setup():
            return False
        
        if not os.path.exists(source_path):
            print(f"❌ Source file not found: {source_path}")
            return False
        
        # Use original filename if not specified
        if not filename:
            filename = os.path.basename(source_path)
        
        # Copy file to Dropbox folder
        dest_path = self.get_asset_path(category, filename)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        
        print(f"📁 Copying {filename} to Dropbox folder...")
        shutil.copy2(source_path, dest_path)
        
        # Update manifest
        if category not in self.manifest['categories']:
            self.manifest['categories'][category] = {
                'description': f'{category} assets',
                'count': 0,
                'assets': {}
            }
        
        file_size = os.path.getsize(dest_path)
        asset_info = {
            'dropbox_path': f"{category}/{filename}",
            'size_bytes': file_size,
            'size_human': self.human_readable_size(file_size),
            'checksum': self.calculate_checksum(dest_path),
            'created': datetime.now().isoformat(),
            'metadata': metadata or {}
        }
        
        self.manifest['categories'][category]['assets'][filename] = asset_info
        self.manifest['categories'][category]['count'] = len(self.manifest['categories'][category]['assets'])
        self.save_manifest()
        
        print(f"✅ Registered asset: {filename} in category '{category}'")
        print(f"📍 Location: {dest_path}")
        return True
    
    def list_assets(self, category: str = None):
        """List assets in repository"""
        if not self.verify_dropbox_setup():
            return
        
        if category:
            if category in self.manifest['categories']:
                self._list_category_assets(category)
            else:
                print(f"❌ Category '{category}' not found in manifest")
                # Check if folder exists in Dropbox
                category_path = os.path.join(self.dropbox_path, category)
                if os.path.exists(category_path):
                    print(f"💡 Found untracked files in Dropbox folder: {category_path}")
                    files = [f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))]
                    if files:
                        print("Untracked files:")
                        for file in files:
                            print(f"  📄 {file}")
                        print(f"\n💡 Run: python scripts/asset_manager.py scan --category {category}")
        else:
            print(f"📁 Dropbox Folder: {self.dropbox_path}")
            print(f"🗂  All Categories:")
            for cat_name, cat_data in self.manifest['categories'].items():
                count = cat_data.get('count', 0)
                print(f"  📂 {cat_name}: {count} tracked assets")
            
            # Check for untracked categories
            if os.path.exists(self.dropbox_path):
                existing_folders = [d for d in os.listdir(self.dropbox_path) 
                                 if os.path.isdir(os.path.join(self.dropbox_path, d))]
                untracked = [f for f in existing_folders if f not in self.manifest['categories']]
                if untracked:
                    print(f"\n💡 Untracked folders found: {', '.join(untracked)}")
                    print("Run: python scripts/asset_manager.py scan --all")
    
    def _list_category_assets(self, category: str):
        """List assets in a specific category"""
        cat_data = self.manifest['categories'][category]
        print(f"\n📂 Category: {category}")
        print(f"Description: {cat_data.get('description', 'No description')}")
        print(f"Tracked assets: {cat_data.get('count', 0)}")
        
        category_path = os.path.join(self.dropbox_path, category)
        if os.path.exists(category_path):
            actual_files = set(f for f in os.listdir(category_path) 
                              if os.path.isfile(os.path.join(category_path, f)))
            tracked_files = set(cat_data.get('assets', {}).keys())
            
            print(f"Actual files in Dropbox: {len(actual_files)}")
            
            print("\n📄 Assets:")
            for name, info in cat_data.get('assets', {}).items():
                file_path = os.path.join(category_path, name)
                status = "✅ Synced" if os.path.exists(file_path) else "⚠️ Missing locally"
                print(f"  {name} ({info.get('size_human', 'Unknown size')}) - {status}")
            
            # Show untracked files
            untracked = actual_files - tracked_files
            if untracked:
                print(f"\n💡 Untracked files ({len(untracked)}):")
                for file in sorted(untracked):
                    file_path = os.path.join(category_path, file)
                    size = self.human_readable_size(os.path.getsize(file_path))
                    print(f"  📄 {file} ({size}) - Not in manifest")
    
    def scan_assets(self, category: str = None):
        """Scan Dropbox folder and add untracked assets to manifest"""
        if not self.verify_dropbox_setup():
            return
        
        categories_to_scan = [category] if category else []
        if not categories_to_scan:
            # Scan all existing folders
            categories_to_scan = [d for d in os.listdir(self.dropbox_path) 
                                if os.path.isdir(os.path.join(self.dropbox_path, d))]
        
        for cat in categories_to_scan:
            category_path = os.path.join(self.dropbox_path, cat)
            if not os.path.exists(category_path):
                continue
                
            print(f"🔍 Scanning category: {cat}")
            
            # Initialize category in manifest if needed
            if cat not in self.manifest['categories']:
                self.manifest['categories'][cat] = {
                    'description': f'{cat} assets',
                    'count': 0,
                    'assets': {}
                }
            
            tracked_files = set(self.manifest['categories'][cat].get('assets', {}).keys())
            actual_files = set(f for f in os.listdir(category_path) 
                             if os.path.isfile(os.path.join(category_path, f)))
            
            untracked = actual_files - tracked_files
            
            for filename in untracked:
                file_path = os.path.join(category_path, filename)
                file_size = os.path.getsize(file_path)
                
                asset_info = {
                    'dropbox_path': f"{cat}/{filename}",
                    'size_bytes': file_size,
                    'size_human': self.human_readable_size(file_size),
                    'checksum': self.calculate_checksum(file_path),
                    'created': datetime.now().isoformat(),
                    'metadata': {'scanned': True}
                }
                
                self.manifest['categories'][cat]['assets'][filename] = asset_info
                print(f"  ✅ Added to manifest: {filename}")
            
            # Update count
            self.manifest['categories'][cat]['count'] = len(self.manifest['categories'][cat]['assets'])
            
            if untracked:
                print(f"✅ Added {len(untracked)} assets to manifest for category '{cat}'")
            else:
                print(f"✅ All assets in '{cat}' already tracked")
        
        self.save_manifest()
    
    @staticmethod
    def human_readable_size(size_bytes: int) -> str:
        """Convert bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f}{unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f}TB"
    
    def validate_assets(self):
        """Validate assets in Dropbox folder against manifest"""
        if not self.verify_dropbox_setup():
            return
        
        print("🔍 Validating assets...")
        issues = []
        missing_files = []
        
        for category, cat_data in self.manifest['categories'].items():
            category_path = os.path.join(self.dropbox_path, category)
            
            for filename, asset in cat_data.get('assets', {}).items():
                file_path = os.path.join(category_path, filename)
                
                if not os.path.exists(file_path):
                    missing_files.append(f"{category}/{filename}")
                    continue
                
                # Check file size
                actual_size = os.path.getsize(file_path)
                expected_size = asset.get('size_bytes', 0)
                
                if actual_size != expected_size:
                    issues.append(f"Size mismatch: {category}/{filename} (expected {expected_size}, got {actual_size})")
                
                # Check checksum if available
                if asset.get('checksum'):
                    actual_checksum = self.calculate_checksum(file_path)
                    if actual_checksum != asset['checksum']:
                        issues.append(f"Checksum mismatch: {category}/{filename}")
        
        # Report results
        if missing_files:
            print("❌ Missing files (not synced or deleted):")
            for file in missing_files:
                print(f"  - {file}")
            print("💡 These files may still be syncing from Dropbox")
        
        if issues:
            print("⚠️ Validation issues found:")
            for issue in issues:
                print(f"  - {issue}")
        
        if not missing_files and not issues:
            print("✅ All assets validated successfully")

def main():
    parser = argparse.ArgumentParser(description="Audio Asset Manager for Dropbox-synced assets")
    parser.add_argument('action', choices=['verify', 'list', 'register', 'scan', 'validate'])
    parser.add_argument('--category', help='Asset category')
    parser.add_argument('--file', help='File path to register')
    parser.add_argument('--filename', help='Custom filename for registered asset')
    parser.add_argument('--all', action='store_true', help='Apply to all categories')
    
    args = parser.parse_args()
    
    manager = AudioAssetManager()
    
    if args.action == 'verify':
        manager.verify_dropbox_setup()
    
    elif args.action == 'list':
        manager.list_assets(args.category)
    
    elif args.action == 'register':
        if not args.file:
            print("❌ Please specify --file to register")
            return
        if not args.category:
            print("❌ Please specify --category")
            return
        manager.register_asset(args.file, args.category, args.filename)
    
    elif args.action == 'scan':
        if args.all:
            manager.scan_assets()
        elif args.category:
            manager.scan_assets(args.category)
        else:
            print("❌ Please specify --category or --all")
    
    elif args.action == 'validate':
        manager.validate_assets()

if __name__ == "__main__":
    main()