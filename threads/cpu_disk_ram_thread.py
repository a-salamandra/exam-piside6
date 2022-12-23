
from PySide6 import QtCore
from time import sleep
from cpuinfo import get_cpu_info
from psutil import cpu_count, cpu_percent, virtual_memory, disk_partitions, disk_usage


class CPUInfo(QtCore.QThread):
    CPUInfoReceived = QtCore.Signal(dict)

    def __init__(self, timeout:int = 5, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = None

    def run(self):
        self.status = True
        cpu_name = get_cpu_info()["brand_raw"]
        cpu_number = str(cpu_count())

        while self.status:
            info = {}
            cpu_load = cpu_percent()

            info['cpu'] = [cpu_name, cpu_number, cpu_load]

            ram_total = virtual_memory().total // 1024 ** 2
            ram_used = virtual_memory().used // 1024 ** 2
            info['ram'] = [ram_total, ram_used]

            info['disks'] = {}
            for disk in disk_partitions(all=False):
                disk_name = disk.device
                disk_ftype = disk.fstype
                disk_total = round (disk_usage(disk_name).total / 1024**3, 2)
                disk_used = round (disk_usage(disk_name).used / 1024**3, 2)
                info['disks'][disk_name] = [disk_ftype, disk_total, disk_used]
            self.CPUInfoReceived.emit(info)
            sleep(self.timeout)