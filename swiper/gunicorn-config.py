# gunicorn.conf
# coding:utf-8
from multiprocessing import cpu_count

# 绑定的ip与端口
bind = ['0.0.0.0:8000']#线上环境不会开启在公网IP下，一般使用内网IP
# 是否设置守护进程,将进程交给supervisor管理
daemon = True
# 设置进程文件目录
pidfile='logs/gunicorn.pid'

# 并行工作进程数
workers = cpu_count() * 2
# 工作模式协程，默认的是sync模式，这里指定使用gevent作为异步处理的库
worker_class = 'gevent'
"""
worker_class
-k STRTING, --worker-class STRTING

要使用的工作模式，默认为sync。可引用以下常见类型“字符串”作为捆绑类：

sync
eventlet：需要下载eventlet>=0.9.7
gevent：需要下载gevent>=0.13
tornado：需要下载tornado>=0.2
gthread
gaiohttp：需要python 3.4和aiohttp>=0.21.5
————————————————
版权声明：本文为CSDN博主「玉米丛里吃过亏」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/y472360651/article/details/78538188
"""
# 设置最大并发量（每个worker处理请求的工作线程数，正整数，默认为1）
worker_connections = 65535

# 在keep-alive连接上等待请求的秒数，默认情况下值为2。一般设定在1~5秒之间。
# 服务器保持连接的时间，能够避免频繁的三次握手过程
keepalive = 60
# 设置超时时间120s，默认为30s。按自己的需求进行设置timeout = 120
# 超时时间内请求没有完成，服务器主动断开
timeout = 30
# 超时重启
graceful_timeout = 10
forward_allow_ips = '*'

# 日志处理
capture_output = True
loglevel = 'info'
errorlog = 'logs/error.log'