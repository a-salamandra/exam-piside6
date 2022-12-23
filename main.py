from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem

from threads.task_scheduler_thread import TaskSchedulerInfo
from threads.cpu_disk_ram_thread import CPUInfo
from threads.processes_thread import ProcessesInfo
from threads.serveces_thread import ServecesInfo

from ui.tm import Ui_TaskManager

class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initThreads()
        self.ui = Ui_TaskManager()
        self.ui.setupUi(self)
        self.initSignals()

    def initThreads(self):
        self.task_scheduler_info = TaskSchedulerInfo()
        self.task_scheduler_info.start()

        self.cpu_info = CPUInfo()
        self.cpu_info.start()

        self.processes_info = ProcessesInfo()
        self.processes_info.start()

        self.serveses_info = ServecesInfo()
        self.serveses_info.start()

    def initSignals(self):
        self.cpu_info.CPUInfoReceived.connect(self.onCPUInfoReceived)
        self.processes_info.ProcessesInfoReceived.connect(self.onProcessesInfoReceived)
        self.serveses_info.ServecesInfoReceived.connect(self.onServecesInfoReceived)
        self.task_scheduler_info.taskSchedulerInfoReceived.connect(self.onTaskSchedulerInfoReceived)

        self.ui.horizontalSliderUpdateRate.sliderReleased.connect(self.changeUpdateRate)
        self.ui.horizontalSliderUpdateRate.valueChanged.connect(lambda v: self.ui.plainTextEdit_updaterate.setPlainText(str(v)))

    def changeUpdateRate(self):
        self.cpu_info.timeout = self.ui.horizontalSliderUpdateRate.value()

    def onCPUInfoReceived(self, info: dict):
        cpu_name, cpu_number, cpu_load = info['cpu']
        self.ui.lcdNumber_cpuload.display(cpu_load)
        self.ui.textEdit_cpubrand.setText(cpu_name)
        self.ui.lcdNumber_cpunumber.display(cpu_number)

        ram_total, ram_used = info['ram']
        self.ui.lcdNumber_ramtotal.display(ram_total)
        self.ui.lcdNumber_ramused.display(ram_used)

        self.ui.tableWidget_disks.setRowCount(len(info['disks']))
        for i, disk in enumerate(info['disks']):
            disk_filesystem, total_space, used_space = info['disks'][disk]
            self.ui.tableWidget_disks.setItem(i, 0, QTableWidgetItem(disk))
            self.ui.tableWidget_disks.setItem(i, 1, QTableWidgetItem(disk_filesystem))
            self.ui.tableWidget_disks.setItem(i, 2, QTableWidgetItem(f"{total_space} GB"))
            self.ui.tableWidget_disks.setItem(i, 3, QTableWidgetItem(f"{used_space} GB"))

    def onProcessesInfoReceived(self, list_processes: list):
        self.ui.tableWidget_processes.setRowCount(len(list_processes))
        for i, process in enumerate(list_processes):
            process_name, process_memory, process_status = process
            self.ui.tableWidget_processes.setItem(i, 0, QTableWidgetItem(process_name))
            self.ui.tableWidget_processes.setItem(i, 1, QTableWidgetItem(process_memory))
            self.ui.tableWidget_processes.setItem(i, 2, QTableWidgetItem(process_status))

    def onServecesInfoReceived(self, list_serveces: list):
        self.ui.tableWidget_services.setRowCount(len(list_serveces))
        for i, service in enumerate(list_serveces):
            service_name, service_state = service
            self.ui.tableWidget_services.setItem(i, 0, QTableWidgetItem(service_name))
            self.ui.tableWidget_services.setItem(i, 1, QTableWidgetItem(service_state))

    def onTaskSchedulerInfoReceived(self, list_tasks: list):
        self.ui.tableWidget_scheduler.setRowCount(len(list_tasks))
        for i, task in enumerate(list_tasks):
            task_name, task_path, task_state, task_next_run_time = task
            self.ui.tableWidget_scheduler.setItem(i, 0, QTableWidgetItem(task_name))
            self.ui.tableWidget_scheduler.setItem(i, 1, QTableWidgetItem(task_next_run_time))
            self.ui.tableWidget_scheduler.setItem(i, 2, QTableWidgetItem(task_state))
            self.ui.tableWidget_scheduler.setItem(i, 3, QTableWidgetItem(task_path))

    def closeEvent(self, e):
        self.task_scheduler_info.terminate()
        self.cpu_info.terminate()
        self.processes_info.terminate()
        self.serveses_info.terminate()


if __name__ == "__main__":

    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()


