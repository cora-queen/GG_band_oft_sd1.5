import torch
from diffusers import StableDiffusionPipeline
# 1. 指向原始模型路径
model_id = "autodl-tmp" 

# 2. 加载 Pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    torch_dtype=torch.float16, 
    safety_checker=None  # 关闭安全检查员以节省显存
)
pipe = pipe.to("cuda")

# 3. 使用你设计的Prompt
prompt = "a photo of sks GG Bond pig, 2d cartoon, dressed in a red jumpsuit, red headgear with yellow glasses,  iconic pig snout, yellow snout pattern on chest, white background"
# 4. 生成图片 
seed = 42
generator = torch.Generator("cuda").manual_seed(seed)

print("正在生成原始模型对比图...")
image = pipe(prompt, num_inference_steps=50, generator=generator).images[0]

# 5. 保存结果
image.save("base_model_result.png")
print("保存成功：base_model_result.png")
