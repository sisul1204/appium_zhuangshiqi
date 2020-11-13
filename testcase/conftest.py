# * coding:utf-8 *
# Author:sisul
#创建时间：2020/11/13 10:44
import os
import shlex
import signal
import subprocess

import pytest

@pytest.fixture(scope="module", autouse=True)
def record():
    cmd = shlex.split("scrcpy --record tmp.mp4")
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
