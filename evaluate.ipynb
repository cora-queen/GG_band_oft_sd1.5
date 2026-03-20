import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import os
device = "cuda" if torch.cuda.is_available() else "cpu"

# 加载预训练的 CLIP 模型和处理器（会自动从缓存读取，通常 SD 环境里都有）
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# 你的提示词 [cite: 10]
prompt = "a photo of sks GG Bond pig, 2d cartoon, dressed in a red jumpsuit, red headgear with yellow glasses, iconic pig snout, yellow snout pattern on chest"

# 图片路径
image_paths = ["ggbond_boft_1500_1.png"]

for path in image_paths:
    if not os.path.exists(path):
        print(f"不存在: {path}")
        continue

    image = Image.open(path)
    
    # 预处理
    inputs = processor(text=[prompt], images=image, return_tensors="pt", padding=True).to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        
    # 获取相似度得分 (logits_per_image 是余弦相似度 * 100)
    # 我们将其还原回 0-1 之间的数值
    logits_per_image = outputs.logits_per_image 
    similarity = logits_per_image.item() / 100.0

    print(f"图片: {path}")
    print(f"CLIP Score: {similarity:.4f}\n")
