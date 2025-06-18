x1 = 1
y1 = 2
x2 = 2
y2 = 4
m = 1
c = 1
lr = 0.1
epoch = 20

def dL_dm(m, c):
  return m*(x1**2 + x2**2) + c*(x1 + x2) - x1*y1 - x2*y2

def dL_dc(m, c):
  return m*(x1 + x2) + 2*c - y1 -y2

for i in range(epoch):
  m = m - lr*dL_dm(m, c)
  c = c - lr*dL_dc(m, c)
  print(m, c)