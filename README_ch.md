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

# 克隆项目
git clone https://github.com/your-username/GG_band_oft_sd1.5.git
cd GG_band_oft_sd1.5
# 安装依赖
pip install -r requirements.txt

## 数据预处理
将猪猪侠原始图像素材放入 data/GG_band_raw/ 目录；
运行 data/data_process.ipynb 笔记本，完成数据清洗、裁剪、归一化等预处理；
预处理后的标准化数据会自动保存至 data/GG_band_processed/。

## 模型微调
# 进入训练模块目录
cd boft_dreambooth

# 一键启动训练（可根据需求修改sh脚本中的参数）
bash train_dreambooth.sh

## 推理生成
基于 SD1.5 基础模型生成：
python inference_base_model.py --prompt "猪猪侠 卡通 高清" --output_dir comparison/oft_before

基于 OFT 微调后模型生成：
python inference_oft_model.py --prompt "猪猪侠 卡通 高清" --output_dir comparison/oft_after

## 效果评估

# 量化评估模型生成效果（PSNR/SSIM等指标）
python evaluate.py --before_dir comparison/oft_before --after_dir comparison/oft_after
