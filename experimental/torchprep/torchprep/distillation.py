import torch
from pathlib import Path 
from typing import List 
from .main import app, Device
 
@app.command()
def distill(model_path : Path, device : Device = Device.cpu, parameter_scaling : int = 2, layer_scaling : int = None, profile : List[int] = None) -> torch.nn.Module:
    """
    [Coming soon]: Create a smaller student model by setting a distillation ratio and teach it how to behave exactly like your existing model
    """
    print(f"Coming soon")
    print("See this notebook for more information https://colab.research.google.com/drive/1RzQtprrHx8PokLQsFiQPAKzfn_DiTpDN?usp=sharing")