# GG_band_oft_sd1.5
A customized AI image generation training project based on the Stable Diffusion v1.5 diffusion model, combined with the DreamBooth fine-tuning framework and BOFT (OFT) lightweight fine-tuning technology. The core objective is to enable the AI to generate cartoon images of GG Bond with specified styles and visual characteristics.

GG_band_oft_sd1.5/
├── README.md                # 项目核心说明文档
├── evaluate.py              # 模型评估脚本
├── inference_base_model.py  # 基模推理脚本：加载SD1.5基模进行猪猪侠图像生成推理
├── inference_oft_model.py   # OFT模型推理脚本：加载微调后的OFT模型进行猪猪侠图像生成推理
├── requirements.txt         # 项目依赖
├── comparison/              # 效果对比
│   ├── oft_after/           # OFT微调后的生成图像结果
│   └── oft_before/          # OFT微调前的基模生成图像结果
├── boft_dreambooth/         # BOFT+DreamBooth训练模块
│   ├── train_dreambooth.py  # DreamBooth训练核心代码
│   ├── train_dreambooth.sh  # DreamBooth训练启动脚本
│   └── utils/               # 训练工具包
├── data/                    # 数据
│   ├── GG_band_processed/   # 处理后的标准化数据集
│   ├── GG_band_raw/         # 原始数据集
│   └── data_process.ipynb   # 数据处理脚本
├── outputs/                 # 输出
│   ├── ggbond_oft_project/  # 猪猪侠OFT训练日志
│   ├── readme.md            # 输出目录说明
│   ├── unet/                # UNet模块输出：存放微调后的UNet模型权重（SD1.5核心生成模块）
│   └── validation/          # 验证结果目录
## 环境要求
列出项目运行所需的系统环境、编程语言版本、依赖库/软件等。
示例：
- 操作系统：Windows 10+/macOS 10.15+/Linux
- 编程语言：Python 3.8+
- 依赖库：
  - requests 2.28.1
  - pandas 1.5.3
  - openpyxl 3.1.2

## 安装步骤
详细说明如何安装和配置项目环境，包括依赖安装命令。
示例：
1. 克隆本项目到本地
   ```bash
   git clone https://github.com/你的用户名/项目仓库名.git
   cd 项目仓库名
