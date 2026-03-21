# GG_band_oft_sd1.5
A customized AI image generation training project based on the Stable Diffusion v1.5 diffusion model, combined with the DreamBooth fine-tuning framework and BOFT (OFT) lightweight fine-tuning technology. The core objective is to enable the AI to generate cartoon images of GG Bond with specified styles and visual characteristics.

## 📂 Project Structure

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



## 环境准备

   ```bash
   # 克隆项目
git clone https://github.com/your-username/GG_band_oft_sd1.5.git
cd GG_band_oft_sd1.5

# 安装依赖
pip install -r requirements.txt
