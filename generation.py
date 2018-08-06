# 生成器
def odd():
      print("step 1")
      yield 1
      print("step 2")
      yield 2
      print("step 3")
      yield 3


# odd()是调用生成器，每次调用都会调用新的生成器
one = next(odd())
print(one)

# g调用生成器，并记住状态
g = odd()
# two=next(odd())
# print(two)
one = next(g)
print(one)
two = next(g)
print(two)


# 协程

def simple_coroutine():
      print("- > Start ")
      x = yield  # 遇到关键字 yield 放回  ，x接受下一次调用send的值
      print("- > recived", x)
      y = yield
      print("- > receive", x, y)
      z = yield
      print(x, z, y)


sc = simple_coroutine()

print("------------")
sc.send(None)
# next(sc)

print("************")
sc.send('cty')

print("^^^^^^^")
sc.send('jf')
sc.send('love')
# 输出自带空格

##yeild from
