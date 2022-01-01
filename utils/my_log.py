"""
自定义日志
"""
import logging
import os
from logging import handlers

if not os.path.exists('./logs'):
    os.mkdir('./logs')
log_file = 'logs/web.log'

logger = logging.getLogger("web")
logger.setLevel(logging.INFO)
fh = handlers.TimedRotatingFileHandler(filename=log_file, when="midnight")
logger.addHandler(fh)
file_formatter = logging.Formatter(fmt='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(file_formatter)
