from psutil import process_iter
from PySide6 import QtCore
from time import sleep



class ProcessesInfo(QtCore.QThread):
    ProcessesInfoReceived = QtCore.Signal(list)

    def __init__(self, timeout: int = 15, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = None

    def run(self):
        self.status = True

        while self.status:
            processesInfo = []
            for process in process_iter():
                if process.is_running():
                    with process.oneshot():
                        process_name = process.name()
                        process_status = process.status()
                        process_memory = str(process.memory_info().rss)
                        processesInfo.append ([process_name, process_status, process_memory])
            self.ProcessesInfoReceived.emit(processesInfo)
            sleep(self.timeout)