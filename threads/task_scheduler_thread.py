import pythoncom
import win32com.client
from PySide6 import QtCore
from time import sleep
from re import search

class TaskSchedulerInfo(QtCore.QThread):
    taskSchedulerInfoReceived = QtCore.Signal(list)
    TASK_STATE = {0: 'Unknown',
                  1: 'Disabled',
                  2: 'Queued',
                  3: 'Ready',
                  4: 'Running'}

    def __init__(self, timeout: int = 100, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = None

    def run(self):
        self.status = True

        while self.status:
            pythoncom.CoInitialize()
            taskSchedulerInfo = []
            scheduler = win32com.client.Dispatch('Schedule.Service')
            scheduler.Connect()
            folders = [scheduler.GetFolder('\\')]
            while folders:
                folder = folders.pop(0)
                folders += list(folder.GetFolders(0))
                for task in folder.GetTasks(0):
                    task_name = search(r".*\\{1}(.+$)", task.Path).group(1)
                    task_path = task.Path
                    task_state = TaskSchedulerInfo.TASK_STATE[task.State]
                    task_run_time = str(task.NextRunTime)
                    taskSchedulerInfo.append([task_name, task_path, task_state, task_run_time])
            self.taskSchedulerInfoReceived.emit(taskSchedulerInfo)
            sleep(self.timeout)
