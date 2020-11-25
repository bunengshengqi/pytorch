# tensor的属性
import torch
# 每一个tensor都有
# torch.dtype
# torch.layout   内存中的张量排布,对应到内存中的矩阵排布
# torch.device   识别存储设备,CPU  GPU CUDA的名称
# 三种属性

# tensor的属性---稀疏张量
#
# torch.sparse_coo_tensor()
# coo类型非0元素的坐标形式

# indices = torch.tensor([[0, 1, 1], [2, 0, 2]])
# values = torch.tensor([3, 4, 5], dtype=torch.float32)
# x = torch.sparse_coo_tensor(i, v, [2,4])

dev = torch.device('cpu')
# dev = torch.device('cuda')
a = torch.tensor([2, 2], device=dev, dtype=torch.float32)
print(a)


# 稀疏的张量必须指定
i = torch.tensor([[0, 1, 2], [0, 1, 2]])  # 坐标
v = torch.tensor([1, 2, 3])  # 数值
b = torch.sparse_coo_tensor(i, v, (4, 4))
print(b)



i = torch.tensor([[0, 1, 2], [0, 1, 2]])  # 坐标
v = torch.tensor([1, 2, 3])  # 数值
c = torch.sparse_coo_tensor(i, v, (4, 4), dtype=torch.float32, device=dev).to_dense()  # 将稀疏转为稠密
print(c)
