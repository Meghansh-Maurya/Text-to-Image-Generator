import matplotlib.pyplot as plt
from diffusers import StableDiffusionPipeline
import torch    

from huggingface_hub import login
login("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")

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True
)
pipe =pipe.to("cpu")

user_prompt = input("Enter your prompt: ")
image = pipe(user_prompt).images[0]
plt.imshow(image)
plt.axis("off")
plt.title("Genrated Image")
plt.show()

