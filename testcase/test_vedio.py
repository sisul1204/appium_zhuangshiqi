# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/13 10:45
import os
import shlex
import signal
import subprocess
from time import sleep


def test_vedio():
    cmd = shlex.split("scrcpy --record tmp.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    sleep(10)
    os.kill(p.pid, signal.CTRL_C_EVENT)