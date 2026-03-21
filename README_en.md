# GG_band_oft_sd1.5
A customized AI image generation training project based on the Stable Diffusion v1.5 diffusion model, combined with the DreamBooth fine-tuning framework and BOFT (OFT) lightweight fine-tuning technology. The core objective is to enable the AI to generate cartoon images of GG Bond with specified styles and visual characteristics.

## Project Structure

```bash
GG_band_oft_sd1.5/
├── boft_dreambooth/           # BOFT+DreamBooth training module
│   ├── train_dreambooth.py    # DreamBooth training core logic
│   ├── train_dreambooth.sh    # DreamBooth training execution script
│   └── utils/                 # Training utility toolkit
├── comparison/                # Performance comparison
│   ├── oft_after/             # Generated images after OFT fine-tuning
│   └── oft_before/            # Base model generated images (pre-fine-tuning)
├── data/                      # Dataset management
│   ├── GG_band_processed/     # Standardized/Pre-processed dataset
│   ├── GG_band_raw/           # Raw image dataset
│   └── data_process.ipynb     # Data cleaning and processing script
├── outputs/                   # Training outputs
│   ├── ggbond_oft_project/    # GG Bond OFT training logs
│   ├── readme.md              # Output directory documentation
│   ├── unet/                  # UNet weights: Fine-tuned SD1.5 core modules
│   └── validation/            # Validation results during training
├── README.md                  # Project core documentation
├── evaluate.py                # Model evaluation script
├── inference_base_model.py    # Base model inference (Original SD1.5 testing)
├── inference_oft_model.py     # OFT model inference (Using fine-tuned weights)
└── requirements.txt           # Project environment dependencies
```

## 🚀 Getting Started

### 1. Environment Preparation
```bash
# Clone the repository
git clone [https://github.com/your-username/GG_band_oft_sd1.5.git](https://github.com/your-username/GG_band_oft_sd1.5.git)
cd GG_band_oft_sd1.5

# Install required dependencies
pip install -r requirements.txt
```

##  Data Preprocessing
-Place the raw GG Bond (猪猪侠) image assets into the data/GG_band_raw/ directory.

-Run the data/data_process.ipynb notebook to perform data cleaning, cropping, and normalization.

-The preprocessed standardized data will be automatically saved to data/GG_band_processed/.

## Model Fine-tuning
```bash
# Navigate to the training module directory
cd boft_dreambooth

# One-click start for training (Modify parameters in the .sh script as needed)
bash train_dreambooth.sh
```

## Inference & Generation
```bash
# Generate images using the base SD1.5 model
python inference_base_model.py --prompt "GG Bond, cartoon, high quality" --output_dir comparison/oft_before

# Generate images using the fine-tuned OFT model
python inference_oft_model.py --prompt "GG Bond, cartoon, high quality" --output_dir comparison/oft_after
```

## Performance Evaluation
```bash
# Quantitatively evaluate the generation results (PSNR, SSIM, etc.)
python evaluate.py --before_dir comparison/oft_before --after_dir comparison/oft_after
```
