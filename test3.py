#  tensor的四则运算
# 加法 add  减法 sub  乘法(哈达玛积) mul  除法div
# 二维矩阵的运算   torch.mm()   torch.matmul()   @ 一共三种
# 高维的tensor   只支持  torch.matmul()
# tensor 的幂运算
# torch.pow()
# e的n次方  torch.exp()
# 开方运算 sqrt()
# 对数运算  torch.log2()   torch.log10()

# add

import torch
a = torch.rand(2, 3)
b = torch.rand(2, 3)
print(a)
print(b)

# 加法的几种形式
print(a+b)
print(a.add(b))
print(torch.add(a, b))
print('------')
print(a.add_(b))
print('------')
print(a)