from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import time,sys,traceback

class Worker(QRunnable):
    
    def __init__(self,fn, *args, **kwargs) -> None:
        super(Worker,self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        
    
    @pyqtSlot()
    def run(self) -> None:
        self.fn(*self.args,**self.kwargs)
        
















