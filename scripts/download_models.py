#!/usr/bin/env python3
"""
Script to download pre-trained models for lumbar spine analysis.
"""

import os
import requests
import zipfile
from pathlib import Path
import argparse
from tqdm import tqdm

def download_file(url, filename, chunk_size=8192):
    """Download a file with progress bar."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(filename, 'wb') as f, tqdm(
        desc=filename,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for data in response.iter_content(chunk_size=chunk_size):
            size = f.write(data)
            pbar.update(size)

def setup_model_directory():
    """Create model directory structure."""
    model_dir = Path("models/pretrained")
    model_dir.mkdir(parents=True, exist_ok=True)
    return model_dir

def download_models():
    """Download all required pre-trained models."""
    print("Setting up model directory...")
    model_dir = setup_model_directory()
    
    # Model URLs (replace with actual URLs when available)
    models = {
        "spinenet.pt": "https://example.com/models/spinenet.pt",
        "coatnet.pt": "https://example.com/models/coatnet.pt", 
        "maxvit_fallback.pt": "https://example.com/models/maxvit_fallback.pt"
    }
    
    print("Downloading pre-trained models...")
    for model_name, url in models.items():
        model_path = model_dir / model_name
        
        if model_path.exists():
            print(f"Model {model_name} already exists, skipping...")
            continue
            
        print(f"Downloading {model_name}...")
        try:
            download_file(url, model_path)
            print(f"Successfully downloaded {model_name}")
        except Exception as e:
            print(f"Failed to download {model_name}: {e}")
            print("Please download manually from the provided URL")

def main():
    parser = argparse.ArgumentParser(description="Download pre-trained models")
    parser.add_argument("--force", action="store_true", help="Force re-download existing models")
    
    args = parser.parse_args()
    
    if args.force:
        # Remove existing models
        model_dir = Path("models/pretrained")
        if model_dir.exists():
            for model_file in model_dir.glob("*.pt"):
                model_file.unlink()
    
    download_models()
    print("Model download complete!")

if __name__ == "__main__":
    main() 