# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tm.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLCDNumber, QLabel,
    QPlainTextEdit, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_TaskManager(object):
    def setupUi(self, TaskManager):
        if not TaskManager.objectName():
            TaskManager.setObjectName(u"TaskManager")
        TaskManager.resize(762, 655)
        TaskManager.setMinimumSize(QSize(580, 0))
        self.verticalLayout = QVBoxLayout(TaskManager)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabs = QTabWidget(TaskManager)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setMinimumSize(QSize(740, 600))
        self.tabs.setMaximumSize(QSize(745, 700))
        self.tabs.setContextMenuPolicy(Qt.NoContextMenu)
        self.tab_performance = QWidget()
        self.tab_performance.setObjectName(u"tab_performance")
        self.verticalLayout_8 = QVBoxLayout(self.tab_performance)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox = QGroupBox(self.tab_performance)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(360, 180))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit_cpubrand = QTextEdit(self.groupBox)
        self.textEdit_cpubrand.setObjectName(u"textEdit_cpubrand")
        self.textEdit_cpubrand.setMaximumSize(QSize(350, 35))
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.textEdit_cpubrand.setFont(font)
        self.textEdit_cpubrand.setFrameShape(QFrame.NoFrame)
        self.textEdit_cpubrand.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit_cpubrand)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.lcdNumber_cpunumber = QLCDNumber(self.groupBox)
        self.lcdNumber_cpunumber.setObjectName(u"lcdNumber_cpunumber")
        self.lcdNumber_cpunumber.setMinimumSize(QSize(200, 40))
        self.lcdNumber_cpunumber.setFrameShape(QFrame.Panel)
        self.lcdNumber_cpunumber.setDigitCount(10)
        self.lcdNumber_cpunumber.setSegmentStyle(QLCDNumber.Filled)
        self.lcdNumber_cpunumber.setProperty("value", 0.000000000000000)
        self.lcdNumber_cpunumber.setProperty("intValue", 0)

        self.horizontalLayout_6.addWidget(self.lcdNumber_cpunumber)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 40))
        self.label_3.setFont(font1)
        self.label_3.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.lcdNumber_cpuload = QLCDNumber(self.groupBox)
        self.lcdNumber_cpuload.setObjectName(u"lcdNumber_cpuload")
        self.lcdNumber_cpuload.setMinimumSize(QSize(200, 70))
        self.lcdNumber_cpuload.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_5.addWidget(self.lcdNumber_cpuload)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tab_performance)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(340, 230))
        self.groupBox_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lcdNumber_ramused = QLCDNumber(self.groupBox_2)
        self.lcdNumber_ramused.setObjectName(u"lcdNumber_ramused")
        self.lcdNumber_ramused.setMinimumSize(QSize(0, 50))
        self.lcdNumber_ramused.setFrameShape(QFrame.Panel)
        self.lcdNumber_ramused.setSmallDecimalPoint(False)
        self.lcdNumber_ramused.setDigitCount(13)
        self.lcdNumber_ramused.setSegmentStyle(QLCDNumber.Filled)

        self.verticalLayout_6.addWidget(self.lcdNumber_ramused)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lcdNumber_ramtotal = QLCDNumber(self.groupBox_2)
        self.lcdNumber_ramtotal.setObjectName(u"lcdNumber_ramtotal")
        self.lcdNumber_ramtotal.setMinimumSize(QSize(0, 50))
        self.lcdNumber_ramtotal.setLayoutDirection(Qt.LeftToRight)
        self.lcdNumber_ramtotal.setFrameShape(QFrame.Panel)
        self.lcdNumber_ramtotal.setDigitCount(13)

        self.verticalLayout_5.addWidget(self.lcdNumber_ramtotal)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_7.addWidget(self.groupBox_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.tableWidget_disks = QTableWidget(self.tab_performance)
        if (self.tableWidget_disks.columnCount() < 4):
            self.tableWidget_disks.setColumnCount(4)
        font2 = QFont()
        font2.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget_disks.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget_disks.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget_disks.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget_disks.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_disks.setObjectName(u"tableWidget_disks")
        self.tableWidget_disks.setMinimumSize(QSize(710, 295))
        self.tableWidget_disks.setMaximumSize(QSize(750, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        self.tableWidget_disks.setFont(font3)
        self.tableWidget_disks.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_disks.horizontalHeader().setDefaultSectionSize(175)

        self.horizontalLayout_4.addWidget(self.tableWidget_disks)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label = QLabel(self.tab_performance)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.plainTextEdit_updaterate = QPlainTextEdit(self.tab_performance)
        self.plainTextEdit_updaterate.setObjectName(u"plainTextEdit_updaterate")
        self.plainTextEdit_updaterate.setMaximumSize(QSize(30, 20))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(False)
        self.plainTextEdit_updaterate.setFont(font4)
        self.plainTextEdit_updaterate.setLayoutDirection(Qt.LeftToRight)
        self.plainTextEdit_updaterate.setFrameShape(QFrame.Panel)
        self.plainTextEdit_updaterate.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_updaterate.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_updaterate.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit_updaterate.setReadOnly(True)
        self.plainTextEdit_updaterate.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.plainTextEdit_updaterate)

        self.horizontalSliderUpdateRate = QSlider(self.tab_performance)
        self.horizontalSliderUpdateRate.setObjectName(u"horizontalSliderUpdateRate")
        self.horizontalSliderUpdateRate.setMaximumSize(QSize(110, 16777215))
        self.horizontalSliderUpdateRate.setMinimum(1)
        self.horizontalSliderUpdateRate.setMaximum(60)
        self.horizontalSliderUpdateRate.setSingleStep(5)
        self.horizontalSliderUpdateRate.setValue(5)
        self.horizontalSliderUpdateRate.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.horizontalSliderUpdateRate)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.tabs.addTab(self.tab_performance, "")
        self.tab_processes = QWidget()
        self.tab_processes.setObjectName(u"tab_processes")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_processes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget_processes = QTableWidget(self.tab_processes)
        if (self.tableWidget_processes.columnCount() < 3):
            self.tableWidget_processes.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget_processes.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidget_processes.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tableWidget_processes.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tableWidget_processes.setObjectName(u"tableWidget_processes")
        self.tableWidget_processes.setFont(font1)
        self.tableWidget_processes.horizontalHeader().setDefaultSectionSize(250)

        self.horizontalLayout_2.addWidget(self.tableWidget_processes)

        self.tabs.addTab(self.tab_processes, "")
        self.tab_services = QWidget()
        self.tab_services.setObjectName(u"tab_services")
        self.verticalLayout_2 = QVBoxLayout(self.tab_services)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget_services = QTableWidget(self.tab_services)
        if (self.tableWidget_services.columnCount() < 2):
            self.tableWidget_services.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.tableWidget_services.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.tableWidget_services.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tableWidget_services.setObjectName(u"tableWidget_services")
        self.tableWidget_services.setFont(font1)
        self.tableWidget_services.horizontalHeader().setDefaultSectionSize(360)

        self.verticalLayout_2.addWidget(self.tableWidget_services)

        self.tabs.addTab(self.tab_services, "")
        self.tab_scheduler = QWidget()
        self.tab_scheduler.setObjectName(u"tab_scheduler")
        self.horizontalLayout = QHBoxLayout(self.tab_scheduler)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget_scheduler = QTableWidget(self.tab_scheduler)
        if (self.tableWidget_scheduler.columnCount() < 4):
            self.tableWidget_scheduler.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.tableWidget_scheduler.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.tableWidget_scheduler.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2);
        self.tableWidget_scheduler.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        self.tableWidget_scheduler.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        self.tableWidget_scheduler.setObjectName(u"tableWidget_scheduler")
        self.tableWidget_scheduler.setFont(font1)
        self.tableWidget_scheduler.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_scheduler.setColumnCount(4)
        self.tableWidget_scheduler.horizontalHeader().setDefaultSectionSize(250)

        self.horizontalLayout.addWidget(self.tableWidget_scheduler)

        self.tabs.addTab(self.tab_scheduler, "")

        self.verticalLayout.addWidget(self.tabs)


        self.retranslateUi(TaskManager)

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TaskManager)
    # setupUi

    def retranslateUi(self, TaskManager):
        TaskManager.setWindowTitle(QCoreApplication.translate("TaskManager", u"Task Manager", None))
        self.groupBox.setTitle(QCoreApplication.translate("TaskManager", u"CPU", None))
        self.label_2.setText(QCoreApplication.translate("TaskManager", u"number of CPUs", None))
        self.label_3.setText(QCoreApplication.translate("TaskManager", u"CPU utilization", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TaskManager", u"RAM", None))
        self.label_6.setText(QCoreApplication.translate("TaskManager", u"current RAM usage (MB)", None))
        self.label_5.setText(QCoreApplication.translate("TaskManager", u"total RAM capacity (MB)", None))
        ___qtablewidgetitem = self.tableWidget_disks.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TaskManager", u"Disk", None));
        ___qtablewidgetitem1 = self.tableWidget_disks.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TaskManager", u"File System", None));
        ___qtablewidgetitem2 = self.tableWidget_disks.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TaskManager", u"Size", None));
        ___qtablewidgetitem3 = self.tableWidget_disks.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TaskManager", u"Free Space", None));
        self.label.setText(QCoreApplication.translate("TaskManager", u"update rate (sec)", None))
        self.plainTextEdit_updaterate.setPlainText(QCoreApplication.translate("TaskManager", u"5", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_performance), QCoreApplication.translate("TaskManager", u"Performance", None))
        ___qtablewidgetitem4 = self.tableWidget_processes.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TaskManager", u"Name", None));
        ___qtablewidgetitem5 = self.tableWidget_processes.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TaskManager", u"Status", None));
        ___qtablewidgetitem6 = self.tableWidget_processes.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TaskManager", u"Memory", None));
        self.tabs.setTabText(self.tabs.indexOf(self.tab_processes), QCoreApplication.translate("TaskManager", u"Processes", None))
        ___qtablewidgetitem7 = self.tableWidget_services.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TaskManager", u"Name", None));
        ___qtablewidgetitem8 = self.tableWidget_services.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TaskManager", u"Status", None));
        self.tabs.setTabText(self.tabs.indexOf(self.tab_services), QCoreApplication.translate("TaskManager", u"Services", None))
        ___qtablewidgetitem9 = self.tableWidget_scheduler.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TaskManager", u"Name", None));
        ___qtablewidgetitem10 = self.tableWidget_scheduler.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TaskManager", u"Next Run Time", None));
        ___qtablewidgetitem11 = self.tableWidget_scheduler.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TaskManager", u"Status", None));
        ___qtablewidgetitem12 = self.tableWidget_scheduler.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TaskManager", u"Task Path", None));
        self.tabs.setTabText(self.tabs.indexOf(self.tab_scheduler), QCoreApplication.translate("TaskManager", u"Task Scheduler", None))
    # retranslateUi

