x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
n = len(x)
m = 1
c = 1
lr = 0.1
epoch = 50

def dL_dm(m, c):
  return m*sum([i**2 for i in x]) + c*sum(x) - sum([i*j for i in x for j in y])

def dL_dc(m, c):
  return m*sum(x) + n*c - sum(y)

for i in range(epoch):
  m = m - lr*dL_dm(m, c)
  c = c - lr*dL_dc(m, c)
  print(m, c)