# Results Directory Structure

This directory contains outputs and generated content from the AVMI-GVSC Sound System project.

## 📁 Folder Organization

### `measurements/`
**Purpose:** Objective measurements and test data
**Contents:**
- Latency measurements
- Frequency response data
- Performance benchmarks
- Hardware-in-the-loop test results
- Audio quality metrics (THD, SNR, etc.)

**File formats:** `.csv`, `.json`, `.h5`, `.mat`

### `models/`
**Purpose:** Trained models and saved algorithm states
**Contents:**
- Machine learning models for sound synthesis
- Calibrated acoustic models
- DSP algorithm parameters
- Neural network weights and configurations

**File formats:** `.pkl`, `.h5`, `.pth`, `.onnx`, `.pb`

### `reports/`
**Purpose:** Generated reports and documentation
**Contents:**
- **`interim/`** - Progress reports, weekly updates
- **`final/`** - Final research reports, papers
- **`presentations/`** - Slides, poster files
- **`technical/`** - Technical documentation, specs

**File formats:** `.pdf`, `.docx`, `.html`, `.md`, `.pptx`

### `sound_objects/`
**Purpose:** Generated audio assets and sound objects
**Contents:**
- Synthesized audio samples
- Processed sound objects
- Generated audio libraries
- Hybrid synthesis outputs

**File formats:** `.wav`, `.flac`, `.aiff` (stored here temporarily before moving to external Dropbox)

## 🔄 Workflow Guidelines

### Adding Results:
1. **Save outputs** to appropriate subfolder
2. **Use descriptive filenames** with timestamps
3. **Add metadata** files (`.json` or `.yaml`) describing the results
4. **Move large audio files** to external Dropbox storage if > 5MB

### File Naming Convention:
```
{category}_{experiment}_{date}_{version}.{ext}

Examples:
- measurements_latency_test_20250922_v1.csv
- models_engine_synthesis_20250922_final.pkl
- reports_interim_progress_week3.pdf
- sound_objects_ev_engine_idle_20250922.wav
```

### Metadata Files:
Each significant result should have an accompanying metadata file:
```yaml
# measurements_latency_test_20250922_v1.meta.yaml
experiment: "Real-time latency measurement"
date: "2025-09-22"
description: "Audio processing latency under different buffer sizes"
parameters:
  buffer_sizes: [128, 256, 512, 1024]
  sample_rate: 48000
  duration: 300  # seconds
methodology: "Hardware-in-the-loop testing"
results_summary: "Average latency: 12.3ms"
related_files:
  - "measurements_latency_test_20250922_v1.csv"
```

## 📊 Integration with External Assets

- **Large audio files** (> 5MB) should be moved to external Dropbox storage
- **Keep references** in the repository using the asset management system
- **Small result files** (< 5MB) can stay in Git for easy access

## 🔍 Finding Results

Use the project search tools:
```bash
# Find all results from a specific date
find results/ -name "*20250922*"

# Find all model files
find results/models/ -name "*.pkl" -o -name "*.h5"

# Find reports containing specific keywords
grep -r "latency" results/reports/
```

## 📋 Maintenance

- **Regular cleanup** of temporary files
- **Archive old experiments** to compressed formats
- **Update metadata** when results are moved or modified
- **Backup critical results** to external storage