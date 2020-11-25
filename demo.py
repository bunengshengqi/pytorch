import numpy as np

# N is batch-size D_in is input dimension
# H is hidden dimension ; D_out dimension

N, D_in, H, D_out = 64, 1000, 100, 10

# create random input and output data
x = np.random.rand(N, D_in)
y = np.random.rand(N, D_out)

#randomly initialize weights

w1 = np.random.rand(D_in, H)
w2 = np.random.rand(H, D_out)







