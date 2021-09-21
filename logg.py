import logging
import os

class Logger:
    def __init__(self):
        self.base = os.path.join(os.path.dirname(os.path.abspath(__file__)),'')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setFormatter(formatter)
        self.logger.addHandler(self.streamHandler)
        self.fileHandler = logging.FileHandler(self.base + 'bot.log', mode='a')
        self.fileHandler.setFormatter(formatter)
        self.logger.addHandler(self.fileHandler)
    
    def critical(self, l, *args):
        s = str()
        for a in args:
            if type(a) == list or type(a) == tuple:
                s += ' '.join(a)
            elif type(a) == str:
                 s += ' ' + a
        if type(l)==list or type(l)==tuple:
            self.logger.critical(' '.join([l, s]))
        elif type(l)==str:
            self.logger.critical(' '.join([l, s]))

    def error(self, l, *args):
        s = str()
        for a in args:
            if type(a) == list or type(a) == tuple:
                s += ' '.join(a)
            elif type(a) == str:
                 s += ' ' + a
        if type(l)==list or type(l)==tuple:
            self.logger.error(' '.join([l, s]))
        elif type(l)==str:
            self.logger.error(' '.join([l, s]))

    def warning(self, l, *args):
        s = str()
        for a in args:
            if type(a) == list or type(a) == tuple:
                s += ' '.join(a)
            elif type(a) == str:
                 s += ' ' + a
        if type(l)==list or type(l)==tuple:
            self.logger.warning(' '.join([l, s]))
        elif type(l)==str:
            self.logger.warning(' '.join([l, s]))

    def info(self, l, *args):
        s = str()
        for a in args:
            if type(a) == list or type(a) == tuple:
                s += ' '.join(a)
            elif type(a) == str:
                 s += ' ' + a
        if type(l)==list or type(l)==tuple:
            self.logger.info(' '.join([l, s]))
        elif type(l)==str:
            self.logger.info(' '.join([l, s]))

    def debug(self, l, *args):
        s = str()
        for a in args:
            if type(a) == list or type(a) == tuple:
                s += ' '.join(a)
            elif type(a) == str:
                 s += ' ' + a
        if type(l)==list or type(l)==tuple:
            self.logger.debug(' '.join([l, s]))
        elif type(l)==str:
            self.logger.debug(' '.join([l, s]))

logger = Logger()
