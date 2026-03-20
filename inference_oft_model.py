from diffusers import StableDiffusionPipeline
from peft import PeftModel
import torch

# --------------------- 路径直接填你的 ---------------------
base_model_path = "autodl-tmp"
boft_path = "outputs/unet/1500/ggbond_v1_run"  # 你的路径
# --------------------------------------------------------

# 加载基础模型
pipe = StableDiffusionPipeline.from_pretrained(
    base_model_path,
    torch_dtype=torch.float16,
    safety_checker=None
)

# 关键：用 PeftModel 加载 BOFT
pipe.unet = PeftModel.from_pretrained(
    pipe.unet,
    boft_path,
    torch_dtype=torch.float16
)

pipe.to("cuda")

# 生成
prompt = "a photo of sks GG Bond pig, 2d cartoon, dressed in a red jumpsuit, red headgear with yellow glasses, iconic pig snout"
image = pipe(prompt, num_inference_steps=50, guidance_scale=7).images[0]
image.save("ggbond_boft_1500_1.png")

print("✅ 生成成功！")
