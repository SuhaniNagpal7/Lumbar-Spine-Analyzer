# Lumbar Spine Analyzer

A deep learning pipeline for automated analysis of degenerative conditions in lumbar spine MRI scans. Detects vertebrae and classifies spinal conditions with severity assessment.

## What it does

- **Vertebra Detection**: Automatically identifies L1-L5 and S1 vertebral levels
- **Condition Classification**: Analyzes 5 degenerative conditions:
  - Spinal Canal Stenosis
  - Left/Right Subarticular Stenosis  
  - Left/Right Neural Foraminal Narrowing
- **Severity Assessment**: Predicts normal/mild, moderate, or severe for each condition

## Quick Start

### Install
```bash
git clone https://github.com/yourusername/lumbar-spine-analyzer.git
cd lumbar-spine-analyzer
pip install -r requirements.txt
```

### Run Analysis
```python
from src.inference.pipeline import LumbarSpineAnalyzer

# Initialize analyzer
analyzer = LumbarSpineAnalyzer()

# Analyze MRI scan
results = analyzer.analyze_scan("path/to/mri/scan.dcm")

# Get predictions
print(results.get_predictions())
```

### Command Line
```bash
# Single scan
python scripts/inference.py --input scan.dcm --output results/

# Batch processing
python scripts/batch_inference.py --input-dir scans/ --output-dir results/
```

## Output Format

**CSV Predictions:**
```csv
row_id,condition,level,normal_mild,moderate,severe
patient_001,spinal_canal_stenosis,l1_l2,0.85,0.12,0.03
```

**JSON Report:**
```json
{
  "patient_id": "patient_001",
  "vertebrae_detected": ["L1", "L2", "L3", "L4", "L5", "S1"],
  "conditions": {
    "spinal_canal_stenosis": {
      "l1_l2": {"severity": "normal", "confidence": 0.85}
    }
  }
}
```

## Requirements

- Python 3.8+
- CUDA GPU (recommended)
- 16GB+ RAM
- PyTorch, Open3D, timm_3d, spacecutter

## Project Structure
```
lumbar-spine-analyzer/
├── src/                    # Core code
├── notebooks/              # Jupyter notebooks
├── scripts/                # Command line tools
├── configs/                # Configuration files
├── models/pretrained/      # Pre-trained models
└── data/                   # MRI data
```

## Medical Disclaimer

This software is for research purposes only. Not intended to replace professional medical diagnosis. Always consult healthcare professionals for medical decisions.

## License

MIT License - see LICENSE file for details. 
