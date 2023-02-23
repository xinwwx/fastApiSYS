# -*- coding: utf-8 -*-
import os
import pymysql
import shutil
import time
import os.path
import psutil


def kill(self):
    ret_msg = os.popen("netstat -aon | findstr %s" % (self,))
    for i in ret_msg:
        n = i.split()
        pid = n[4]
        if pid:
            # print(pid)
            try:
                os.system('taskkill /pid %s -f' % (pid,))
                # print('kill %s' % (pid,))
            except Exception as e:
                print(e)
            return 1
        else:
            return 0