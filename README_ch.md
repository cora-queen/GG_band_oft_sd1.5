# 项目简介
一个基于 Stable Diffusion v1.5 扩散模型的定制化 AI 图像生成训练项目，整合了 DreamBooth 微调框架与 BOFT（OFT）轻量化微调技术。核心目标是使 AI 能够生成具备指定风格与视觉特征的猪猪侠（GG Bond）卡通形象。

## 📂 项目结构 (Project Structure)

```bash
GG_band_oft_sd1.5/
├── boft_dreambooth/           # BOFT+DreamBooth训练模块
│   ├── train_dreambooth.py    # DreamBooth训练核心代码
│   ├── train_dreambooth.sh    # DreamBooth训练启动脚本
│   └── utils/                 # 训练工具包
├── comparison/                # 效果对比
│   ├── oft_after/             # OFT微调后的生成图像结果
│   └── oft_before/            # OFT微调前的基模生成图像结果
├── data/                      # 数据
│   ├── GG_band_processed/     # 处理后的标准化数据集
│   ├── GG_band_raw/           # 原始数据集
│   └── data_process.ipynb     # 数据处理脚本
├── outputs/                   # 输出
│   ├── ggbond_oft_project/    # 猪猪侠OFT训练日志
│   ├── readme.md              # 输出目录说明
│   ├── unet/                  # UNet模块输出：存放微调后的UNet模型权重
│   └── validation/            # 验证结果目录
├── README.md                  # 项目核心说明文档
├── evaluate.py                # 模型评估脚本
├── inference_base_model.py    # 基模推理脚本：加载SD1.5基模进行猪猪侠图像生成推理
├── inference_oft_model.py     # OFT模型推理脚本：加载微调后的OFT模型进行猪猪侠图像生成推理
└── requirements.txt           # 项目依赖


## 环境准备

```bash
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

```bash
# 进入训练模块目录
cd boft_dreambooth
# 一键启动训练（可根据需求修改sh脚本中的参数）
bash train_dreambooth.sh

## 推理生成

```bash
基于 SD1.5 基础模型生成：
python inference_base_model.py --prompt "猪猪侠 卡通 高清" --output_dir comparison/oft_before
基于 OFT 微调后模型生成：
python inference_oft_model.py --prompt "猪猪侠 卡通 高清" --output_dir comparison/oft_after

## 效果评估

```bash
# 量化评估模型生成效果（PSNR/SSIM等指标）
python evaluate.py --before_dir comparison/oft_before --after_dir comparison/oft_after
