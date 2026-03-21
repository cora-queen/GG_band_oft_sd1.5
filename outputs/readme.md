# 目录结构
---

```text
outputs/ggbond_oft/
├── unet/                # UNet 模型的 BOFT 微调权重
│   └── {step}/          # 按训练步数保存的权重文件（500/1000/1500）
├── text_encoder/        # 文本编码器的 BOFT 微调权重
│   └── {step}/          # 与 unet 步数对应的权重文件
├── validation/          # 训练过程中自动生成的验证图像
│   └── {step}/          # 每 300 步生成的验证结果
│       └── ggbond_v1_run/  # 对应训练 run 的验证图片
└── README.md            # 目录说明文档
