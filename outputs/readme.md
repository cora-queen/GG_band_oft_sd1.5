# 目录结构
---

```text
outputs/
├── ggbond_oft_project/          # 项目训练日志与配置目录
│   └── events.out.tfevents.*   # TensorBoard 训练日志文件
├── unet/                       # UNet 模型的 BOFT 微调权重
│   ├── 500/ggbond_v1_run/      # 第 500 步训练权重
│   ├── 1000/ggbond_v1_run/     # 第 1000 步训练权重
│   │   ├── adapter_config.json    # BOFT 适配器配置文件
│   │   └── adapter_model.safetensors  # 微调权重参数文件
│   └── 1500/ggbond_v1_run/     # 第 1500 步训练权重
├── validation/                 # 训练过程中自动生成的验证图像
│   ├── 301/ggbond_v1_run/      # 第 301 步验证结果
│   ├── 601/ggbond_v1_run/      # 第 601 步验证结果
│   ├── 901/ggbond_v1_run/      # 第 901 步验证结果
│   └── 1201/ggbond_v1_run/     # 第 1201 步验证结果
│       └── _photo_of_sks_GG_Bond_pig,...  # 验证生成的猪猪侠图像
└── readme.md                   # 本目录说明文档
