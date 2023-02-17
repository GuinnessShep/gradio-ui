Model = "Pygmalion 6B Experimental"

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
import subprocess

subprocess.run(["wget", "https://koboldai.org/ckds", "-O", "-", "|", "bash", "/dev/stdin", "--init", "only"])

subprocess.run(["git", "clone", "--depth=1", "https://github.com/PygmalionAI/gradio-ui.git"])
subprocess.run(["cd", "gradio-ui", "&&", "pip3", "install", "-r", "requirements.txt"])

print("\n\n\n")
print("* The model is about to be downloaded and loaded.")
print("* This takes several minutes, sit tight.")
print("* A link will show up when this step is completed, keep checking back every couple minutes or so.")
print("\n\n\n")

subprocess.Popen(f"python3 /content/KoboldAI-Client/aiserver.py --noaimenu --host --port 80808 --model {model_name} --revision {branch_name} --nobreakmodel --lowmem --quiet", shell=True)

subprocess.run(["python3", "gradio-ui/src/app.py", "--koboldai-url", "http://localhost:80808", "--share"])
