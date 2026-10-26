import torch

if torch.backends.mps.is_available():
    device = torch.device("mps")

    x = torch.ones(3, 3, device=device)
    print("Success! Tensor created on Apple GPU:", x)
else:
    print("MPS device not found. Defaulting to CPU.")
