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


# 减法的几种形式
print(a-b)
print(a.sub(b))
print(torch.sub(a, b))
print('------')
print(a.sub_(b))
print('------')
print(a)


# 乘法 mul
print("========")
print(a * b)
print(torch.mul(a,b))
print(a.mul(b))
print(a.mul_(b))


# 除法 div

print("====div======")
print(a/b)
print(torch.div(a, b))
print(a.div(b))
print(a.div_(b))


# matmul
a = torch.ones(2, 1)
print(a)
b = torch.ones(1, 2)
print(b)
print(a @ b)
print(a.matmul(b))
print(torch.matmul(a, b))
print(torch.mm(a, b))
print(a.mm(b))


## 高维tensor

a = torch.ones(1, 2, 3, 4)
b = torch.ones(1, 2, 4, 3)
print(a.matmul(b))
print(a.matmul(b).shape)

# 指数运算
a = torch.tensor([1, 2])
print(torch.pow(a, 3))
print(a.pow(3))
print(a**3)
print(a.pow_(3))


# exp
a = torch.tensor([1, 2], dtype=torch.float32)
print(a.type())
print(torch.exp(a))
print(torch.exp_(a))
print(a.exp())
print(a.exp_())


# 对数
a = torch.tensor([10, 2], dtype=torch.float32)
print(torch.log(a))
print(torch.log_(a))
print(a.log())
print(a.log_())


# sqart
a = torch.tensor([10, 2], dtype=torch.float32)
print(torch.sqrt(a))
print(torch.sqrt_(a))
print(a.sqrt())
print(a.sqrt_())