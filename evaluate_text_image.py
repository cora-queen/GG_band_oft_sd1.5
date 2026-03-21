import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel

# ===================== 核心配置=====================
YOUR_PROMPT = "a photo of sks GG Bond pig, 2d cartoon, dressed in a red jumpsuit, red headgear with yellow glasses, iconic pig snout"
# 你的图片路径（支持单张/多张，本地路径/网络链接都可以）
IMAGE_PATHS = [
    "your_image_1.png",  # 替换成你的第一张图路径
    "your_image_2.png",  # 替换成你的第二张图路径
    # 可以继续加更多图片
]
# CLIP模型
MODEL_NAME = "openai/clip-vit-large-patch14"
# =====================================================================

# 加载模型和处理器
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained(MODEL_NAME).to(device)
processor = CLIPProcessor.from_pretrained(MODEL_NAME)

# 计算CLIP Score函数
def calculate_clip_score(image_path, text):
    # 加载图片
    image = Image.open(image_path).convert("RGB")
    # 预处理
    inputs = processor(
        text=[text],
        images=image,
        return_tensors="pt",
        padding=True
    ).to(device)
    
    # 推理
    with torch.no_grad():
        outputs = model(**inputs)
    
    # 提取CLIP Score（标量值，越大匹配度越高）
    logits_per_image = outputs.logits_per_image
    clip_score = logits_per_image.cpu().numpy()[0][0]
    return round(clip_score, 4)

# 批量计算并打印结果
print("="*60)
print(f"参考提示词：\n{YOUR_PROMPT}")
print("="*60)
print("CLIP Score 计算结果（数值越高，图片与提示词匹配度越高）：\n")

for idx, img_path in enumerate(IMAGE_PATHS, 1):
    try:
        score = calculate_clip_score(img_path, YOUR_PROMPT)
        print(f"第{idx}张图 | {img_path} | CLIP Score: {score}")
    except Exception as e:
        print(f"第{idx}张图 | {img_path} | 加载失败：{str(e)}")

print("\n✅ 计算完成！")
