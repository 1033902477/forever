import os
import time

REPORT_TIME = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))


# 定义项目的根路径
base_path = os.path.dirname(os.path.dirname(__file__))

# 定义文件夹所在位置
OUTPUT = os.path.join(base_path, 'OutPut')


# 定义日志文件的位置
LOGLOG = os.path.join(OUTPUT, "LogLog")
REPORT = os.path.join(OUTPUT, 'Report')


# 定义日志文件
LOG_PATH = os.path.join(LOGLOG, 'log.log')
REPORT_PATH = os.path.join(REPORT, 'report_%s.html' % (REPORT_TIME))