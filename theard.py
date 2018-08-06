import threading
from time import sleep, ctime

# 时间循环1：开始到结束4秒
def loop(i):
      print("Start loop ", i, ", time: ", ctime())
      sleep(i)
      print("End Loop ", i, " , time: ", ctime())

#时间循环2：开始到结束3秒


print("Start time:", ctime())
t1 = threading.Thread(target=loop, args=(3,))
t1.start()
t2 = threading.Thread(target=loop, args=(2,))
# t2.setDaemon(True)
t2.start()
print()
print("All done at ", ctime())

# 设置loop2为守护线程，loop(1)线程和主线程都结束，Loop（2)线程才会被结束

print("Start time:", ctime())
t1 = threading.Thread(target=loop, args=(1,))
t1.start()
t2 = threading.Thread(target=loop, args=(2,))
t2.setDaemon(True)
t2.start()
print()
print("All done at ", ctime())
