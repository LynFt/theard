# def fib(max):
#       n,a,b=0,0,1
#       while n<max:
#             print(b)
#             a,b=b,a+b
#             n+=1
#       return "done"
#
# g=fib(5)

def fib_g(max):
      n, a, b = 0, 0, 1
      while n < max:
            yield b
            a, b = b, a + b
            n += 1
      # return 'Done'


g = fib_g(5)

for i in range(6):
      rst = next(g)
      print(rst)

# 输出异常
