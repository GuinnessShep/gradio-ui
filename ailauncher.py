Model = "Pygmalion 6B Experimental" #@param ["Pygmalion 350M", "Pygmalion 1.3B", "Pygmalion 2.7B", "Pygmalion 6B", "Pygmalion 6B Experimental"] {allow-input: true}

pretty_model_name_to_hf_name = {
    "Pygmalion 350M": "PygmalionAI/pygmalion-350m",
    "Pygmalion 1.3B": "PygmalionAI/pygmalion-1.3b",
    "Pygmalion 2.7B": "PygmalionAI/pygmalion-2.7b",
    "Pygmalion 6B": "PygmalionAI/pygmalion-6b",
    "Pygmalion 6B Experimental": "PygmalionAI/pygmalion-6b"
}

model_name = pretty_model_name_to_hf_name[Model]
branch_name = "main" if Model != "Pygmalion 6B Experimental" else "dev" 

import os
if not os.path.exists("/content/drive"):
  os.mkdir("/content/drive")
if not os.path.exists("/content/drive/MyDrive/"):
  os.mkdir("/content/drive/MyDrive/")

!wget https://koboldai.org/ckds -O - | bash /dev/stdin --init only

!git clone --depth=1 \
  "https://github.com/PygmalionAI/gradio-ui.git" \
  && cd gradio-ui && pip3 install -r requirements.txt

print("\n\n\n")
print("* The model is about to be downloaded and loaded into the GPU.")
print("* This takes several minutes, sit tight.")
print("* A link will show up when this step is completed, keep checking back every couple minutes or so.")
print("\n\n\n")
os.system(f"cd /content/KoboldAI-Client && python3 aiserver.py --noaimenu --host --port 80808 --model {model_name} --revision {branch_name} --nobreakmodel --lowmem --quiet &")

!python3 gradio-ui/src/app.py \
  --koboldai-url "http://localhost:80808" \
  --share