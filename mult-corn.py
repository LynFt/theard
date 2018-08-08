from concurrent.futures import ThreadPoolExecutor
from time import sleep


def return_msg(msg):
      print(msg)
      sleep(2)
      return msg


# 创建线程池
pool = ThreadPoolExecutor(max_workers=2)
# 线程分配任务
f1 = pool.submit(return_msg, 'Hello')
f2 = pool.submit(return_msg, "Hi")
# 线程池包含2个线程，创建3个任务，等一个任务完成 第三任务才会执行
# f3=pool.submit(return_msg,"Bye")

print(f1.done())
sleep(3)
print(f2.done())
print(f1.done())

print(f1.result())
print(f2.result())
# print(f3.result())
