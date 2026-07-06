#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

MODE="create"

if [[ "${1-}" == "--check" ]]; then
  MODE="check"
elif [[ -n "${1-}" ]]; then
  echo "Usage: $(basename "$0") [--check]" >&2
  exit 1
fi

required_dirs=(
  "assets/images"
  "assets/instrument_definitions"
  "assets/manifest.yaml"
  "assets/presets"
  "assets/sample_mappings"
  "assets/samples"
  "assets/templates"
  "assets_meta"
  "data/audio_samples"
  "data/simulation_data"
  "data/evaluation_results"
  "docs/Moradi Documents"
  "docs/reports"
  "notebooks/analysis"
  "requirements"
  "results/sound_objects"
  "results/models"
  "results/reports"
  "results/measurements"
  "src/dsp_algorithms"
  "src/sound_synthesis"
  "src/spatialization"
  "src/integration"
)

missing_dirs=()

for relative_dir in "${required_dirs[@]}"; do
  target_dir="$REPO_ROOT/$relative_dir"
  if [[ ! -e "$target_dir" ]]; then
    missing_dirs+=("$relative_dir")
    if [[ "$MODE" == "create" ]]; then
      if [[ "$relative_dir" == *.* ]]; then
        mkdir -p "$(dirname "$target_dir")"
        touch "$target_dir"
      else
        mkdir -p "$target_dir"
      fi
      echo "Created: $relative_dir"
    fi
  fi
done

if [[ "$MODE" == "check" ]]; then
  if [[ ${#missing_dirs[@]} -eq 0 ]]; then
    echo "Repository structure is complete."
  else
    echo "Missing directories:"
    printf ' - %s\n' "${missing_dirs[@]}"
    exit 1
  fi
else
  if [[ ${#missing_dirs[@]} -eq 0 ]]; then
    echo "Repository structure already matched the expected layout."
  else
    echo "Repository structure updated."
  fi
fi