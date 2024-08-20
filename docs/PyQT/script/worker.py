# workers.py
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject

class WorkerSignals(QObject):
    progress = pyqtSignal(int)
    message = pyqtSignal(str)
    finished = pyqtSignal(str)
    result = pyqtSignal()
    error = pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func 
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
    
    def run(self):
        try:
            self.signals.message.emit("Task started")
            self.func(self.signals, *self.args, **self.kwargs)
        except Exception as e:
            self.signals.error.emit(str(e))
        finally:
            self.signals.finished.emit("Task finished")

def task_decorator(func):
    def wrapper(*args, **kwargs):
        worker = Worker(func, *args, **kwargs)
        QThreadPool.globalInstance().start(worker)
        return worker
    return wrapper
