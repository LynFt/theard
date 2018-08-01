import threading
import time

# 时间循环1：开始到结束4秒
def loop1():
    print("Start loop1, time: ", time.ctime())
    time.sleep(2)
    print("End Loop1,time: ", time.ctime())

#时间循环2：开始到结束3秒
def loop2():
    print("Start Loop2,time ",time.ctime())
    time.sleep(3)
    print("End Loop2,time: ",time.ctime())

#设置loop2为守护线程，loop1线程和主线程都结束，Loop2线程才会被结束

print("Start time:", time.ctime())
t1=threading.Thread(target=loop1)
t1.start()
t2=threading.Thread(target=loop2)
t2.setDaemon(True)
t2.start()
print()
print("All done at ",time.ctime())



