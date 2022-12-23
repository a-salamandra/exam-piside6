from psutil import win_service_iter, win_service_get
from PySide6 import QtCore
from time import sleep

class ServecesInfo(QtCore.QThread):
    ServecesInfoReceived = QtCore.Signal(list)

    def __init__(self, timeout: int = 20, parent=None):
        super().__init__(parent)
        self.timeout = timeout
        self.status = None

    def run(self) -> None:
        """
        Получение информации о запущенных службах, отправка из потока в виде списка
        """
        self.status = True
        servecesInfo = []

        while self.status:
            for win in win_service_iter():
                serv_info = win_service_get(win.name()).as_dict()
                service_name = serv_info['display_name']
                service_status = serv_info['status']
                servecesInfo.append([service_name, service_status])
            self.ServecesInfoReceived.emit(servecesInfo)
            sleep(self.timeout)