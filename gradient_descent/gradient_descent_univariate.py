x = 10
lr = 0.1
epoch = 20

def f(x):
  return x**2

def diff_f(x):
  return 2*x

for i in range(epoch):
  x = x - lr*diff_f(x)
  print(x)

print("value:", f(x))