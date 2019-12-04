# coding=utf-8

'''
 daemon 守护进程方式执行
'''
import os
import sys
import atexit
import time

class Daemon:
    _option = {}

    """
        参数 dir, pidFile, mask
    """
    def __init__(self, **kwargs):
        self._option = kwargs

    def conf(self, name, default):
        if name in self._option:
            return self._option[name]
        else:
            return default

    def start(self):
        daemon = self.conf('daemon', False)

        if not daemon:
            return self

        pidFile = self.conf('pidFile', "/tmp/pid-daemon-1.pid")
        dir = self.conf('dir', "/tmp")
        mask = self.conf('mask', 755)
        # 从父进程fork一个子进程出来

        pid = os.fork()
        # 子进程的pid一定为0，父进程大于0
        if pid:
            # 退出父进程，sys.exit()方法比os._exit()方法会多执行一些刷新缓冲工作
            sys.exit(0)

        # 子进程默认继承父进程的工作目录，最好是变更到根目录，否则回影响文件系统的卸载
        os.chdir(dir)
        # 子进程默认继承父进程的umask（文件权限掩码），重设为0（完全控制），以免影响程序读写文件
        os.umask(mask)
        # 让子进程成为新的会话组长和进程组长
        os.setsid()

        # 注意了，这里是第2次fork，也就是子进程的子进程，我们把它叫为孙子进程
        _pid = os.fork()
        if _pid:
            # 退出子进程
            sys.exit(0)

        # 刷新缓冲区先，小心使得万年船
        sys.stdout.flush()
        sys.stderr.flush()

        # dup2函数原子化地关闭和复制文件描述符，重定向到/dev/nul，即丢弃所有输入输出
        with open('/dev/null') as readNull, open('/dev/null', 'w') as writeNull:
            os.dup2(readNull.fileno(), sys.stdin.fileno())
            os.dup2(writeNull.fileno(), sys.stdout.fileno())
            os.dup2(writeNull.fileno(), sys.stderr.fileno())

        # 写入pid文件
        if pidFile:
            with open(pidFile, 'w+') as f:
                f.write(str(os.getpid()))

        # 注册退出函数，进程异常退出时移除pid文件
        atexit.register(os.remove, pidFile)

    def test(self):
        # 执行逻辑
        while True:
            time.sleep(1)
            with open("/tmp/t.log", 'a+') as f:
                f.write(str(os.getpid()) + time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())  + "\n")

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
pass


with Daemon(daemon = True) as d:
    d.test()