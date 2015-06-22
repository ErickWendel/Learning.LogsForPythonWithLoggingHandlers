## -*- coding: utf-8 -*-

import os
import time
import datetime
import logging
import logging.handlers
class Logger(object) :
    #inner class for logs
    class __Logger:
        ''' Singleton for class'''
        def __init__(self):
            self.val = None
        def __str__(self):
            return repr(self) + self.val
        
        logger = None
        def myLogger(self):
            if None == self.logger:
                self.logger=logging.getLogger('flask_app')
                self.logger.setLevel(logging.DEBUG)
                now = datetime.datetime.now()
                handler=logging.handlers.RotatingFileHandler('flask_app_'+ now.strftime("%Y-%m-%d") + '.log', maxBytes=16000000, backupCount=4)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                handler.setFormatter(formatter)
                ch = logging.StreamHandler()
                ch.setLevel(logging.DEBUG)
                ch.setFormatter(formatter)
                self.logger.addHandler(handler)
                self.logger.addHandler(ch)
            return self.logger

        def log_info(self, info_text):
            self.myLogger().info(info_text)

        def log_error(self, info_text):
            self.myLogger().error(info_text)

    instance = None
    def __new__(cls): 
        if not Logger.instance:
            Logger.instance = Logger.__Logger()
        return Logger.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)



    

a = Logger()
a.val = "new"
print(a)
b = Logger()
b.val = "new2"
print(b)
for i in range(1, 1000):
   Logger().log_error("Error%i" % i)

for i in range(1, 1000):
   Logger().log_info("Info%i" % i)