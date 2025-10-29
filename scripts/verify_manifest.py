#!/usr/bin/env python3
"""Simple manifest validator for assets_meta/manifest.yaml

This script is intentionally dependency-light: it will try to import yaml (PyYAML)
and use it if available. If not available, it will attempt a very small JSON-like
fallback that supports minimal checks (not full YAML parsing).

Usage: python3 scripts/verify_manifest.py
"""

import sys
from pathlib import Path

MANIFEST = Path(__file__).resolve().parents[1] / 'assets_meta' / 'manifest.yaml'


def check_with_pyyaml(path: Path) -> int:
    try:
        import yaml
    except Exception as e:
        print('PyYAML import failed:', e)
        return 2
    try:
        with path.open('r', encoding='utf8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print('Failed to parse YAML with PyYAML:', e)
        return 3

    if not isinstance(data, dict) or 'assets' not in data:
        print("Manifest missing top-level 'assets' key or wrong type.")
        return 4
    if not isinstance(data['assets'], list):
        print("Manifest 'assets' must be a list.")
        return 5

    print('✅ manifest parsed successfully (PyYAML). assets count =', len(data['assets']))
    return 0


def minimal_yaml_check(path: Path) -> int:
    # Very small heuristic: ensure file contains a top-level 'assets:' line
    s = path.read_text(encoding='utf8')
    first_lines = s.splitlines()[:10]
    if not any('assets:' in line for line in first_lines):
        print("Basic check failed: 'assets:' not found in the first 10 lines.")
        return 6
    print("⚠️ PyYAML not available — performed minimal heuristic check. Please install PyYAML for full validation: pip install pyyaml")
    return 0


def main():
    if not MANIFEST.exists():
        print('Manifest not found at', MANIFEST)
        sys.exit(1)

    # Try PyYAML path first
    try:
        import yaml  # type: ignore
        ret = check_with_pyyaml(MANIFEST)
        sys.exit(ret)
    except Exception:
        # PyYAML unavailable; run minimal heuristic
        ret = minimal_yaml_check(MANIFEST)
        sys.exit(ret)


if __name__ == '__main__':
    main()
