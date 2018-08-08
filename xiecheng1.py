# 引入异步IO包和多线程包
import asyncio
import threading
from time import ctime


@asyncio.coroutine
def hello():
      print("Start>>>(%s)(%s)" % (threading.current_thread(), ctime()))
      yield from asyncio.sleep(3)
      print("Done>>>(%s)(%s)" % (threading.current_thread(), ctime()))


@asyncio.coroutine
def hi():
      print("hi>>>(%s)" % threading.current_thread())
      yield from asyncio.sleep(5)
      print("bye>>(%s)" % threading.current_thread())


# 启动消息循环
loop = asyncio.get_event_loop()
# 定义任务
tasks = [hello(), hi()]
# asyncio使用wait等待tasks执行完毕
loop.run_until_complete(asyncio.wait(tasks))
# 关闭
loop.close()
