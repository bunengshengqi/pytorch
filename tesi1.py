import torch

b = torch.Tensor(2, 3)


b = torch.zeros_like(b)
print(b)
print(b.type())
