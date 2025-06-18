x = 10
y = 10
lr = 0.1
epoch = 20

def f(x,y):
  return x**2 + y**2

def diff_fx(x,y):
  return 2*x

def diff_fy(x,y):
  return 2*y

for i in range(epoch):
  x = x - lr*diff_fx(x,y)
  y = y - lr*diff_fy(x,y)
  print(x, y,"\n")

print("value:", f(x,y))
