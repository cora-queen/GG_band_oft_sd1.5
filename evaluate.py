import torch
import clip
from PIL import Image
import torch.nn.functional as F



# 加载模型
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# 你的配置
# 文本提示词（用于 Text-to-Image）
PROMPT = "a photo of sks GG Bond pig, 2d cartoon, dressed in a red jumpsuit, red headgear with yellow glasses, iconic pig snout"

# 图片A
IMAGE_PATH = "base_model_result3.png"

# 图片B
IMAGE_PATH_2 = "data/GG_band_processed/014.jpg"
# ====================================================
# 加载图片
image = Image.open(IMAGE_PATH).convert("RGB")
image2 = Image.open(IMAGE_PATH_2).convert("RGB")

# 编码图片
@torch.no_grad()
def encode_img(img):
    img = preprocess(img).unsqueeze(0).to(device)
    feat = model.encode_image(img)
    return F.normalize(feat, p=2, dim=-1)

# 编码文本
@torch.no_grad()
def encode_txt(text):
    txt = clip.tokenize([text]).to(device)
    feat = model.encode_text(txt)
    return F.normalize(feat, p=2, dim=-1)

# ===================== 1. Text-to-Image 分数 =====================
img_feat = encode_img(image)
txt_feat = encode_txt(PROMPT)
score_t2i = torch.matmul(img_feat, txt_feat.T).item()

# ===================== 2. Image-to-Image 分数 =====================
img_feat2 = encode_img(image2)
score_i2i = torch.matmul(img_feat, img_feat2.T).item()

# ===================== 输出结果 =====================
print("="*70)
print("📊 CLIP 分数计算（Text-to-Image + Image-to-Image）")
print("="*70)
print(f"提示词：{PROMPT}")
print(f"图片1路径：{IMAGE_PATH}")
print(f"图片2路径：{IMAGE_PATH_2}")
print("\n--- 1. Text-to-Image 分数（文本 ↔ 图片1）---")
print(f"CLIP Score = {score_t2i:.4f}")
print("\n--- 2. Image-to-Image 分数（图片1 ↔ 图片2）---")
print(f"CLIP Score = {score_i2i:.4f}")
print("="*70)
