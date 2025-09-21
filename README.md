# AVMI–GVSC Sound System Project

## Overview
This repository supports the **AVMI–GVSC10-2024 Project: Sound System Modeling, Simulation, and Integration in the AVMI Autonomous Systems Laboratory (ASL) Digital Engineering Ecosystem Simulator**.

The project seeks to transform sound design in simulators for **human–machine integrated formations** by addressing the critical need for **high-fidelity, dynamic, and immersive real-time audio environments**. Realistic soundscapes are essential for effective training, as they directly impact immersion, situational awareness, and preparedness in complex operational environments.

## Research Scope
Our research combines **theoretical analysis**, **technical development**, and **applied testing** across the following areas:

- **Sampling vs. Acoustical Modeling**
  - Comparative analysis of existing sound design methodologies.
  - Development of hybrid synthesis approaches that integrate sampling precision with acoustical modeling flexibility.
  - Creation of a modular, controllable **sound object library**.

- **Real-Time Audio Processing and Spatialization**
  - Design and optimization of DSP algorithms for **real-time performance**.
  - Dynamic placement and movement of sound sources in **multi-channel immersive environments** (cockpit, external, and environmental perspectives).
  - Integration of sound with **vibration and haptic systems** to align physical and auditory cues.

- **Validation and Evaluation**
  - Iterative testing through **subjective perceptual assessments** and **objective technical measurements**.
  - Integration with the VI-Grade **SimSound** and NVH platforms.
  - Hardware-in-the-loop and simulation-based trials to measure fidelity, latency, and trainee performance outcomes.

## Repository Structure

```
├── docs/                          # Documentation and research papers
│   ├── research/                  # Research documentation and findings
│   ├── technical/                 # Technical specifications and designs
│   └── evaluation/                # Evaluation methodologies and results
├── data/                          # Data storage
│   ├── audio_samples/             # Raw and processed audio samples
│   ├── simulation_data/           # Simulation parameters and outputs
│   └── evaluation_results/        # Test results and measurements
├── src/                           # Source code
│   ├── dsp_algorithms/            # Digital signal processing algorithms
│   ├── sound_synthesis/           # Hybrid synthesis models
│   ├── spatialization/            # Multi-channel audio spatialization
│   └── integration/               # System integration modules
├── notebooks/                     # Jupyter notebooks
│   ├── analysis/                  # Data analysis notebooks
│   ├── modeling/                  # Sound modeling experiments
│   └── evaluation/                # Performance evaluation notebooks
├── tests/                         # Test files
│   ├── unit/                      # Unit tests
│   ├── integration/               # Integration tests
│   └── performance/               # Performance benchmarks
├── config/                        # Configuration files
│   ├── simulation/                # Simulation configurations
│   └── audio_engine/              # Audio engine settings
├── results/                       # Generated results
│   ├── sound_objects/             # Generated sound object library
│   ├── models/                    # Trained/calibrated models
│   ├── reports/                   # Generated reports
│   └── measurements/              # Objective measurements
├── scripts/                       # Utility scripts
│   ├── preprocessing/             # Audio preprocessing scripts
│   ├── simulation/                # Simulation execution scripts
│   └── evaluation/                # Evaluation and testing scripts
├── assets/                        # Project assets
│   ├── samples/                   # Sample audio files
│   ├── templates/                 # Template configurations
│   └── presets/                   # Predefined settings
├── validation/                    # Validation frameworks
│   ├── subjective/                # Subjective evaluation tools
│   ├── objective/                 # Objective measurement tools
│   └── hardware_in_loop/          # Hardware-in-the-loop testing
└── requirements/                  # Dependency specifications
```

## Deliverables
- Hybrid synthesis models (sample + modeled).
- Real-time, multi-channel audio engine.
- Modular sound object library matched to simulation parameters.
- Evaluation reports and integration documentation.
- Contributions to the AVMI **Digital Engineering Ecosystem** via the DE Simulator.

## Broader Impacts
While designed for **military vehicle simulation**, the project's outcomes will influence:
- **Blended reality environments** (concert halls, museums, training facilities).
- **Entertainment & gaming industries** through high-fidelity immersive audio.
- **Automotive and acoustic design** for next-generation vehicle systems.
- **STEM education and training**, involving graduate and undergraduate researchers in cutting-edge DSP and acoustics work.

## Project Leadership
- **PI**: Dr. Frederick W. Bianchi (WPI)  
- **Co-PI**: Dr. David B. Smith (CUNY)  
- **Co-PI**: Dr. Lee Moradi (WPI)  
- **Project Participant**: Dr. Vladimir Vantsevich (WPI)
- **Research Associate** srikar gorantla <srikar.gorantla@gmail.com>  

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Audio processing libraries (NumPy, SciPy, librosa)
- Real-time audio frameworks (PyAudio, JUCE, etc.)
- Simulation platforms (VI-Grade SimSound integration)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CHI-CityTech/AVMI-GVSC-SoundSystem.git
   cd AVMI-GVSC-SoundSystem
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements/requirements.txt
   ```

## Usage

### Sound Synthesis
[Add usage instructions for sound synthesis modules]

### Real-Time Processing
[Add usage instructions for real-time audio processing]

### Evaluation Framework
[Add usage instructions for validation and evaluation tools]

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/sound-enhancement`)
3. Commit your changes (`git commit -m 'Add sound spatialization feature'`)
4. Push to the branch (`git push origin feature/sound-enhancement`)
5. Open a Pull Request

## Research Team

[Add current team member information here]

## License

[Add license information here]

## Citation

If you use this work in your research, please cite:

```
AVMI–GVSC10-2024 Project: Sound System Modeling, Simulation, and Integration 
in the AVMI Autonomous Systems Laboratory (ASL) Digital Engineering Ecosystem Simulator.
Principal Investigators: F.W. Bianchi, D.B. Smith, L. Moradi, V. Vantsevich.
```

## Contact

- Dr. David B. Smith (CUNY) - [contact information]
- Dr. Frederick W. Bianchi (WPI) - [contact information]

## Repository Usage
This repository serves as:
- A **documentation hub** for research findings, code, and simulation assets.
- A **version-controlled environment** for collaborative development.
- A record of **sound object libraries, DSP algorithms, and evaluation reports** generated during the project.
