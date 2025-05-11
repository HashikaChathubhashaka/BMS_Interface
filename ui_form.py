# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QListView, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1035, 609)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(10)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.LiveStatus = QWidget()
        self.LiveStatus.setObjectName(u"LiveStatus")
        self.verticalLayout = QVBoxLayout(self.LiveStatus)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.LiveStatus)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.Tab1Details = QHBoxLayout()
        self.Tab1Details.setObjectName(u"Tab1Details")
        self.Temperature = QGroupBox(self.LiveStatus)
        self.Temperature.setObjectName(u"Temperature")
        self.BatteryTemp = QVBoxLayout(self.Temperature)
        self.BatteryTemp.setObjectName(u"BatteryTemp")
        self.TemperatureHeader = QLabel(self.Temperature)
        self.TemperatureHeader.setObjectName(u"TemperatureHeader")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.TemperatureHeader.setFont(font)
        self.TemperatureHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BatteryTemp.addWidget(self.TemperatureHeader)

        self.line_3 = QFrame(self.Temperature)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Shadow.Plain)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.BatteryTemp.addWidget(self.line_3)

        self.BT1 = QHBoxLayout()
        self.BT1.setObjectName(u"BT1")
        self.BT1text = QLabel(self.Temperature)
        self.BT1text.setObjectName(u"BT1text")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.BT1text.setFont(font1)
        self.BT1text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BT1.addWidget(self.BT1text)

        self.BT1label = QLabel(self.Temperature)
        self.BT1label.setObjectName(u"BT1label")
        font2 = QFont()
        font2.setPointSize(12)
        self.BT1label.setFont(font2)
        self.BT1label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BT1.addWidget(self.BT1label)


        self.BatteryTemp.addLayout(self.BT1)

        self.BT2 = QHBoxLayout()
        self.BT2.setObjectName(u"BT2")
        self.BT2text = QLabel(self.Temperature)
        self.BT2text.setObjectName(u"BT2text")
        self.BT2text.setFont(font1)
        self.BT2text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BT2.addWidget(self.BT2text)

        self.BT2label = QLabel(self.Temperature)
        self.BT2label.setObjectName(u"BT2label")
        self.BT2label.setFont(font2)
        self.BT2label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BT2.addWidget(self.BT2label)


        self.BatteryTemp.addLayout(self.BT2)

        self.BT3 = QHBoxLayout()
        self.BT3.setObjectName(u"BT3")
        self.BT3text = QLabel(self.Temperature)
        self.BT3text.setObjectName(u"BT3text")
        self.BT3text.setFont(font1)
        self.BT3text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BT3.addWidget(self.BT3text)

        self.BT3label = QLabel(self.Temperature)
        self.BT3label.setObjectName(u"BT3label")
        self.BT3label.setFont(font2)
        self.BT3label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BT3.addWidget(self.BT3label)


        self.BatteryTemp.addLayout(self.BT3)

        self.BT4 = QHBoxLayout()
        self.BT4.setObjectName(u"BT4")
        self.BT4text = QLabel(self.Temperature)
        self.BT4text.setObjectName(u"BT4text")
        self.BT4text.setFont(font1)
        self.BT4text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BT4.addWidget(self.BT4text)

        self.BT4label = QLabel(self.Temperature)
        self.BT4label.setObjectName(u"BT4label")
        self.BT4label.setFont(font2)
        self.BT4label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BT4.addWidget(self.BT4label)


        self.BatteryTemp.addLayout(self.BT4)

        self.BT5 = QHBoxLayout()
        self.BT5.setObjectName(u"BT5")
        self.BT5text = QLabel(self.Temperature)
        self.BT5text.setObjectName(u"BT5text")
        self.BT5text.setFont(font1)
        self.BT5text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BT5.addWidget(self.BT5text)

        self.BT5label = QLabel(self.Temperature)
        self.BT5label.setObjectName(u"BT5label")
        self.BT5label.setFont(font2)
        self.BT5label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BT5.addWidget(self.BT5label)


        self.BatteryTemp.addLayout(self.BT5)

        self.BT6 = QHBoxLayout()
        self.BT6.setObjectName(u"BT6")
        self.BT6text = QLabel(self.Temperature)
        self.BT6text.setObjectName(u"BT6text")
        self.BT6text.setFont(font1)
        self.BT6text.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BT6.addWidget(self.BT6text)

        self.BT6label = QLabel(self.Temperature)
        self.BT6label.setObjectName(u"BT6label")
        self.BT6label.setFont(font2)
        self.BT6label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BT6.addWidget(self.BT6label)


        self.BatteryTemp.addLayout(self.BT6)

        self.BatteryTemp.setStretch(1, 2)
        self.BatteryTemp.setStretch(2, 2)
        self.BatteryTemp.setStretch(3, 2)
        self.BatteryTemp.setStretch(4, 2)
        self.BatteryTemp.setStretch(5, 2)
        self.BatteryTemp.setStretch(6, 2)
        self.BatteryTemp.setStretch(7, 2)

        self.Tab1Details.addWidget(self.Temperature)

        self.Main = QGridLayout()
        self.Main.setObjectName(u"Main")
        self.BatteryHealthLevel = QFrame(self.LiveStatus)
        self.BatteryHealthLevel.setObjectName(u"BatteryHealthLevel")
        self.BatteryHealthLevel.setFrameShape(QFrame.Shape.Box)
        self.HealthLevel = QVBoxLayout(self.BatteryHealthLevel)
        self.HealthLevel.setObjectName(u"HealthLevel")
        self.HealthLevel.setContentsMargins(10, -1, 10, -1)
        self.HealthBar = QProgressBar(self.BatteryHealthLevel)
        self.HealthBar.setObjectName(u"HealthBar")
        self.HealthBar.setValue(24)
        self.HealthBar.setTextVisible(False)

        self.HealthLevel.addWidget(self.HealthBar)

        self.BatteryHealth = QHBoxLayout()
        self.BatteryHealth.setObjectName(u"BatteryHealth")
        self.BatteryHealthText = QLabel(self.BatteryHealthLevel)
        self.BatteryHealthText.setObjectName(u"BatteryHealthText")
        self.BatteryHealthText.setFont(font1)
        self.BatteryHealthText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BatteryHealth.addWidget(self.BatteryHealthText)

        self.BatteryHealthLabel = QLabel(self.BatteryHealthLevel)
        self.BatteryHealthLabel.setObjectName(u"BatteryHealthLabel")
        self.BatteryHealthLabel.setFont(font2)
        self.BatteryHealthLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.BatteryHealth.addWidget(self.BatteryHealthLabel)

        self.BatteryHealth.setStretch(0, 2)
        self.BatteryHealth.setStretch(1, 1)

        self.HealthLevel.addLayout(self.BatteryHealth)


        self.Main.addWidget(self.BatteryHealthLevel, 2, 0, 1, 1)

        self.RemainCapacity = QHBoxLayout()
        self.RemainCapacity.setObjectName(u"RemainCapacity")
        self.RemainCapacityText = QLabel(self.LiveStatus)
        self.RemainCapacityText.setObjectName(u"RemainCapacityText")
        self.RemainCapacityText.setFont(font1)
        self.RemainCapacityText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.RemainCapacity.addWidget(self.RemainCapacityText)

        self.RemainCapacityLabel = QLabel(self.LiveStatus)
        self.RemainCapacityLabel.setObjectName(u"RemainCapacityLabel")
        self.RemainCapacityLabel.setFont(font2)
        self.RemainCapacityLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.RemainCapacity.addWidget(self.RemainCapacityLabel)

        self.RemainCapacity.setStretch(0, 3)
        self.RemainCapacity.setStretch(1, 1)

        self.Main.addLayout(self.RemainCapacity, 4, 1, 1, 1)

        self.stopButton = QPushButton(self.LiveStatus)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.stopButton.setFont(font3)

        self.Main.addWidget(self.stopButton, 0, 1, 1, 1)

        self.AveCellVolt = QHBoxLayout()
        self.AveCellVolt.setObjectName(u"AveCellVolt")
        self.AveCellVoltText = QLabel(self.LiveStatus)
        self.AveCellVoltText.setObjectName(u"AveCellVoltText")
        self.AveCellVoltText.setFont(font1)
        self.AveCellVoltText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.AveCellVolt.addWidget(self.AveCellVoltText)

        self.AveCellVoltLabel = QLabel(self.LiveStatus)
        self.AveCellVoltLabel.setObjectName(u"AveCellVoltLabel")
        self.AveCellVoltLabel.setFont(font2)
        self.AveCellVoltLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.AveCellVolt.addWidget(self.AveCellVoltLabel)

        self.AveCellVolt.setStretch(0, 2)
        self.AveCellVolt.setStretch(1, 1)

        self.Main.addLayout(self.AveCellVolt, 3, 0, 1, 1)

        self.BatteryChargeLevel = QFrame(self.LiveStatus)
        self.BatteryChargeLevel.setObjectName(u"BatteryChargeLevel")
        self.BatteryChargeLevel.setFrameShape(QFrame.Shape.Box)
        self.BatteryLevel = QVBoxLayout(self.BatteryChargeLevel)
        self.BatteryLevel.setObjectName(u"BatteryLevel")
        self.BatteryLevel.setContentsMargins(10, -1, 10, -1)
        self.BatteryLevelBar = QProgressBar(self.BatteryChargeLevel)
        self.BatteryLevelBar.setObjectName(u"BatteryLevelBar")
        self.BatteryLevelBar.setValue(24)
        self.BatteryLevelBar.setTextVisible(False)

        self.BatteryLevel.addWidget(self.BatteryLevelBar)

        self.RemainBattery = QHBoxLayout()
        self.RemainBattery.setObjectName(u"RemainBattery")
        self.RemainBatteryText = QLabel(self.BatteryChargeLevel)
        self.RemainBatteryText.setObjectName(u"RemainBatteryText")
        self.RemainBatteryText.setFont(font1)
        self.RemainBatteryText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.RemainBattery.addWidget(self.RemainBatteryText)

        self.RemainBatteryLabel = QLabel(self.BatteryChargeLevel)
        self.RemainBatteryLabel.setObjectName(u"RemainBatteryLabel")
        self.RemainBatteryLabel.setFont(font2)
        self.RemainBatteryLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.RemainBattery.addWidget(self.RemainBatteryLabel)

        self.RemainBattery.setStretch(0, 2)
        self.RemainBattery.setStretch(1, 1)

        self.BatteryLevel.addLayout(self.RemainBattery)


        self.Main.addWidget(self.BatteryChargeLevel, 2, 1, 1, 1)

        self.TotalC = QFrame(self.LiveStatus)
        self.TotalC.setObjectName(u"TotalC")
        self.TotalC.setFrameShape(QFrame.Shape.Box)
        self.TotalCurrent = QVBoxLayout(self.TotalC)
        self.TotalCurrent.setObjectName(u"TotalCurrent")
        self.Total_Current_Text = QLabel(self.TotalC)
        self.Total_Current_Text.setObjectName(u"Total_Current_Text")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.Total_Current_Text.setFont(font4)
        self.Total_Current_Text.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.TotalCurrent.addWidget(self.Total_Current_Text)

        self.Total_Current = QLabel(self.TotalC)
        self.Total_Current.setObjectName(u"Total_Current")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Total_Current.sizePolicy().hasHeightForWidth())
        self.Total_Current.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(16)
        self.Total_Current.setFont(font5)
        self.Total_Current.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.TotalCurrent.addWidget(self.Total_Current)


        self.Main.addWidget(self.TotalC, 1, 1, 1, 1)

        self.TotalV = QFrame(self.LiveStatus)
        self.TotalV.setObjectName(u"TotalV")
        self.TotalV.setFrameShape(QFrame.Shape.Box)
        self.TotalVoltage = QVBoxLayout(self.TotalV)
        self.TotalVoltage.setObjectName(u"TotalVoltage")
        self.Total_Voltage_Text = QLabel(self.TotalV)
        self.Total_Voltage_Text.setObjectName(u"Total_Voltage_Text")
        self.Total_Voltage_Text.setFont(font4)
        self.Total_Voltage_Text.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Total_Voltage_Text.setAutoFillBackground(False)
        self.Total_Voltage_Text.setTextFormat(Qt.TextFormat.AutoText)
        self.Total_Voltage_Text.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.TotalVoltage.addWidget(self.Total_Voltage_Text)

        self.Total_Voltage = QLabel(self.TotalV)
        self.Total_Voltage.setObjectName(u"Total_Voltage")
        self.Total_Voltage.setFont(font5)
        self.Total_Voltage.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.TotalVoltage.addWidget(self.Total_Voltage)


        self.Main.addWidget(self.TotalV, 1, 0, 1, 1)

        self.startButton = QPushButton(self.LiveStatus)
        self.startButton.setObjectName(u"startButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy2)
        self.startButton.setMinimumSize(QSize(0, 50))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(13)
        font6.setBold(True)
        font6.setItalic(False)
        self.startButton.setFont(font6)

        self.Main.addWidget(self.startButton, 0, 0, 1, 1)

        self.BatteryCapacity = QHBoxLayout()
        self.BatteryCapacity.setObjectName(u"BatteryCapacity")
        self.BatteryCapacityText = QLabel(self.LiveStatus)
        self.BatteryCapacityText.setObjectName(u"BatteryCapacityText")
        self.BatteryCapacityText.setFont(font1)
        self.BatteryCapacityText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BatteryCapacity.addWidget(self.BatteryCapacityText)

        self.BatteryCapacityLabel = QLabel(self.LiveStatus)
        self.BatteryCapacityLabel.setObjectName(u"BatteryCapacityLabel")
        self.BatteryCapacityLabel.setFont(font2)
        self.BatteryCapacityLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.BatteryCapacity.addWidget(self.BatteryCapacityLabel)

        self.BatteryCapacity.setStretch(0, 3)
        self.BatteryCapacity.setStretch(1, 1)

        self.Main.addLayout(self.BatteryCapacity, 4, 0, 1, 1)

        self.CellVoltDiff = QHBoxLayout()
        self.CellVoltDiff.setObjectName(u"CellVoltDiff")
        self.CellVoltDiffText = QLabel(self.LiveStatus)
        self.CellVoltDiffText.setObjectName(u"CellVoltDiffText")
        self.CellVoltDiffText.setFont(font1)
        self.CellVoltDiffText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.CellVoltDiff.addWidget(self.CellVoltDiffText)

        self.CellVoltDiffLabel = QLabel(self.LiveStatus)
        self.CellVoltDiffLabel.setObjectName(u"CellVoltDiffLabel")
        self.CellVoltDiffLabel.setFont(font2)
        self.CellVoltDiffLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.CellVoltDiff.addWidget(self.CellVoltDiffLabel)

        self.CellVoltDiff.setStretch(0, 2)
        self.CellVoltDiff.setStretch(1, 1)

        self.Main.addLayout(self.CellVoltDiff, 3, 1, 1, 1)

        self.Main.setRowStretch(0, 3)

        self.Tab1Details.addLayout(self.Main)

        self.CellVoltage = QFrame(self.LiveStatus)
        self.CellVoltage.setObjectName(u"CellVoltage")
        self.CellVoltage.setFrameShape(QFrame.Shape.Panel)
        self.CellVoltage.setFrameShadow(QFrame.Shadow.Sunken)
        self.CellVoltages = QVBoxLayout(self.CellVoltage)
        self.CellVoltages.setObjectName(u"CellVoltages")
        self.CellVoltageHeader = QLabel(self.CellVoltage)
        self.CellVoltageHeader.setObjectName(u"CellVoltageHeader")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setWeight(QFont.ExtraBold)
        font7.setItalic(False)
        font7.setUnderline(False)
        self.CellVoltageHeader.setFont(font7)
        self.CellVoltageHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.CellVoltages.addWidget(self.CellVoltageHeader)

        self.LineBetweeCellVHedaer = QFrame(self.CellVoltage)
        self.LineBetweeCellVHedaer.setObjectName(u"LineBetweeCellVHedaer")
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(False)
        self.LineBetweeCellVHedaer.setFont(font8)
        self.LineBetweeCellVHedaer.setFrameShadow(QFrame.Shadow.Plain)
        self.LineBetweeCellVHedaer.setLineWidth(1)
        self.LineBetweeCellVHedaer.setFrameShape(QFrame.Shape.HLine)

        self.CellVoltages.addWidget(self.LineBetweeCellVHedaer)

        self.CellVoltageValues = QHBoxLayout()
        self.CellVoltageValues.setObjectName(u"CellVoltageValues")
        self.C1toC8 = QVBoxLayout()
        self.C1toC8.setObjectName(u"C1toC8")
        self.C1 = QHBoxLayout()
        self.C1.setObjectName(u"C1")
        self.C1_text = QLabel(self.CellVoltage)
        self.C1_text.setObjectName(u"C1_text")
        font9 = QFont()
        font9.setPointSize(11)
        font9.setBold(True)
        self.C1_text.setFont(font9)
        self.C1_text.setFrameShape(QFrame.Shape.NoFrame)
        self.C1_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C1.addWidget(self.C1_text)

        self.C1_label = QLabel(self.CellVoltage)
        self.C1_label.setObjectName(u"C1_label")
        font10 = QFont()
        font10.setPointSize(11)
        self.C1_label.setFont(font10)

        self.C1.addWidget(self.C1_label)


        self.C1toC8.addLayout(self.C1)

        self.C2 = QHBoxLayout()
        self.C2.setObjectName(u"C2")
        self.C2_text = QLabel(self.CellVoltage)
        self.C2_text.setObjectName(u"C2_text")
        self.C2_text.setFont(font9)
        self.C2_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C2.addWidget(self.C2_text)

        self.C2_label = QLabel(self.CellVoltage)
        self.C2_label.setObjectName(u"C2_label")
        self.C2_label.setFont(font10)

        self.C2.addWidget(self.C2_label)


        self.C1toC8.addLayout(self.C2)

        self.C3 = QHBoxLayout()
        self.C3.setObjectName(u"C3")
        self.C3_text = QLabel(self.CellVoltage)
        self.C3_text.setObjectName(u"C3_text")
        self.C3_text.setFont(font9)
        self.C3_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C3.addWidget(self.C3_text)

        self.C3_label = QLabel(self.CellVoltage)
        self.C3_label.setObjectName(u"C3_label")
        self.C3_label.setFont(font10)

        self.C3.addWidget(self.C3_label)


        self.C1toC8.addLayout(self.C3)

        self.C4 = QHBoxLayout()
        self.C4.setObjectName(u"C4")
        self.C4_text = QLabel(self.CellVoltage)
        self.C4_text.setObjectName(u"C4_text")
        self.C4_text.setFont(font9)
        self.C4_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C4.addWidget(self.C4_text)

        self.C4_label = QLabel(self.CellVoltage)
        self.C4_label.setObjectName(u"C4_label")
        self.C4_label.setFont(font10)

        self.C4.addWidget(self.C4_label)


        self.C1toC8.addLayout(self.C4)

        self.C5 = QHBoxLayout()
        self.C5.setObjectName(u"C5")
        self.C5_text = QLabel(self.CellVoltage)
        self.C5_text.setObjectName(u"C5_text")
        self.C5_text.setFont(font9)
        self.C5_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C5.addWidget(self.C5_text)

        self.C5_label = QLabel(self.CellVoltage)
        self.C5_label.setObjectName(u"C5_label")
        self.C5_label.setFont(font10)

        self.C5.addWidget(self.C5_label)


        self.C1toC8.addLayout(self.C5)

        self.C6 = QHBoxLayout()
        self.C6.setObjectName(u"C6")
        self.C6_text = QLabel(self.CellVoltage)
        self.C6_text.setObjectName(u"C6_text")
        self.C6_text.setFont(font9)
        self.C6_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C6.addWidget(self.C6_text)

        self.C6_label = QLabel(self.CellVoltage)
        self.C6_label.setObjectName(u"C6_label")
        self.C6_label.setFont(font10)

        self.C6.addWidget(self.C6_label)


        self.C1toC8.addLayout(self.C6)

        self.C7 = QHBoxLayout()
        self.C7.setObjectName(u"C7")
        self.C7_text = QLabel(self.CellVoltage)
        self.C7_text.setObjectName(u"C7_text")
        self.C7_text.setFont(font9)
        self.C7_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C7.addWidget(self.C7_text)

        self.C7_label = QLabel(self.CellVoltage)
        self.C7_label.setObjectName(u"C7_label")
        self.C7_label.setFont(font10)

        self.C7.addWidget(self.C7_label)


        self.C1toC8.addLayout(self.C7)

        self.C8 = QHBoxLayout()
        self.C8.setObjectName(u"C8")
        self.C8_text = QLabel(self.CellVoltage)
        self.C8_text.setObjectName(u"C8_text")
        self.C8_text.setFont(font9)
        self.C8_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C8.addWidget(self.C8_text)

        self.C8_label = QLabel(self.CellVoltage)
        self.C8_label.setObjectName(u"C8_label")
        self.C8_label.setFont(font10)

        self.C8.addWidget(self.C8_label)


        self.C1toC8.addLayout(self.C8)


        self.CellVoltageValues.addLayout(self.C1toC8)

        self.C9toC16 = QVBoxLayout()
        self.C9toC16.setObjectName(u"C9toC16")
        self.C9 = QHBoxLayout()
        self.C9.setObjectName(u"C9")
        self.C9_text = QLabel(self.CellVoltage)
        self.C9_text.setObjectName(u"C9_text")
        self.C9_text.setFont(font9)
        self.C9_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C9.addWidget(self.C9_text)

        self.C9_label = QLabel(self.CellVoltage)
        self.C9_label.setObjectName(u"C9_label")
        self.C9_label.setFont(font10)

        self.C9.addWidget(self.C9_label)


        self.C9toC16.addLayout(self.C9)

        self.C10 = QHBoxLayout()
        self.C10.setObjectName(u"C10")
        self.C10_text = QLabel(self.CellVoltage)
        self.C10_text.setObjectName(u"C10_text")
        self.C10_text.setFont(font9)
        self.C10_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C10.addWidget(self.C10_text)

        self.C10_label = QLabel(self.CellVoltage)
        self.C10_label.setObjectName(u"C10_label")
        self.C10_label.setFont(font10)

        self.C10.addWidget(self.C10_label)


        self.C9toC16.addLayout(self.C10)

        self.C11 = QHBoxLayout()
        self.C11.setObjectName(u"C11")
        self.C11_text = QLabel(self.CellVoltage)
        self.C11_text.setObjectName(u"C11_text")
        self.C11_text.setFont(font9)
        self.C11_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C11.addWidget(self.C11_text)

        self.C11_label = QLabel(self.CellVoltage)
        self.C11_label.setObjectName(u"C11_label")
        self.C11_label.setFont(font10)

        self.C11.addWidget(self.C11_label)


        self.C9toC16.addLayout(self.C11)

        self.C12 = QHBoxLayout()
        self.C12.setObjectName(u"C12")
        self.C12_text = QLabel(self.CellVoltage)
        self.C12_text.setObjectName(u"C12_text")
        self.C12_text.setFont(font9)
        self.C12_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C12.addWidget(self.C12_text)

        self.C12_label = QLabel(self.CellVoltage)
        self.C12_label.setObjectName(u"C12_label")
        self.C12_label.setFont(font2)

        self.C12.addWidget(self.C12_label)


        self.C9toC16.addLayout(self.C12)

        self.C13 = QHBoxLayout()
        self.C13.setObjectName(u"C13")
        self.C13_text = QLabel(self.CellVoltage)
        self.C13_text.setObjectName(u"C13_text")
        self.C13_text.setFont(font9)
        self.C13_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C13.addWidget(self.C13_text)

        self.C13_label = QLabel(self.CellVoltage)
        self.C13_label.setObjectName(u"C13_label")
        self.C13_label.setFont(font10)

        self.C13.addWidget(self.C13_label)


        self.C9toC16.addLayout(self.C13)

        self.C14 = QHBoxLayout()
        self.C14.setObjectName(u"C14")
        self.C14_text = QLabel(self.CellVoltage)
        self.C14_text.setObjectName(u"C14_text")
        self.C14_text.setFont(font9)
        self.C14_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C14.addWidget(self.C14_text)

        self.C14_label = QLabel(self.CellVoltage)
        self.C14_label.setObjectName(u"C14_label")
        self.C14_label.setFont(font10)

        self.C14.addWidget(self.C14_label)


        self.C9toC16.addLayout(self.C14)

        self.C15 = QHBoxLayout()
        self.C15.setObjectName(u"C15")
        self.C15_text = QLabel(self.CellVoltage)
        self.C15_text.setObjectName(u"C15_text")
        self.C15_text.setFont(font9)
        self.C15_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C15.addWidget(self.C15_text)

        self.C15_label = QLabel(self.CellVoltage)
        self.C15_label.setObjectName(u"C15_label")
        self.C15_label.setFont(font10)

        self.C15.addWidget(self.C15_label)


        self.C9toC16.addLayout(self.C15)

        self.C16 = QHBoxLayout()
        self.C16.setObjectName(u"C16")
        self.C16_text = QLabel(self.CellVoltage)
        self.C16_text.setObjectName(u"C16_text")
        self.C16_text.setFont(font9)
        self.C16_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.C16.addWidget(self.C16_text)

        self.C16_label = QLabel(self.CellVoltage)
        self.C16_label.setObjectName(u"C16_label")
        self.C16_label.setFont(font10)

        self.C16.addWidget(self.C16_label)


        self.C9toC16.addLayout(self.C16)


        self.CellVoltageValues.addLayout(self.C9toC16)


        self.CellVoltages.addLayout(self.CellVoltageValues)

        self.StartRecordCellVoltages = QPushButton(self.CellVoltage)
        self.StartRecordCellVoltages.setObjectName(u"StartRecordCellVoltages")
        self.StartRecordCellVoltages.setEnabled(True)

        self.CellVoltages.addWidget(self.StartRecordCellVoltages)

        self.StopRecordCellVoltages = QPushButton(self.CellVoltage)
        self.StopRecordCellVoltages.setObjectName(u"StopRecordCellVoltages")

        self.CellVoltages.addWidget(self.StopRecordCellVoltages)

        self.CellVoltages.setStretch(0, 1)
        self.CellVoltages.setStretch(2, 15)

        self.Tab1Details.addWidget(self.CellVoltage)

        self.Tab1Details.setStretch(0, 1)
        self.Tab1Details.setStretch(1, 3)
        self.Tab1Details.setStretch(2, 2)

        self.verticalLayout.addLayout(self.Tab1Details)

        self.tabWidget.addTab(self.LiveStatus, "")
        self.DeviceInfo = QWidget()
        self.DeviceInfo.setObjectName(u"DeviceInfo")
        self.horizontalLayout = QHBoxLayout(self.DeviceInfo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MainDetails = QVBoxLayout()
        self.MainDetails.setObjectName(u"MainDetails")
        self.GetData = QVBoxLayout()
        self.GetData.setSpacing(4)
        self.GetData.setObjectName(u"GetData")
        self.GetData.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.GetDataStatus = QLabel(self.DeviceInfo)
        self.GetDataStatus.setObjectName(u"GetDataStatus")
        self.GetDataStatus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.GetData.addWidget(self.GetDataStatus)

        self.GetConstantData = QPushButton(self.DeviceInfo)
        self.GetConstantData.setObjectName(u"GetConstantData")
        self.GetConstantData.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.GetConstantData.sizePolicy().hasHeightForWidth())
        self.GetConstantData.setSizePolicy(sizePolicy3)
        self.GetConstantData.setMinimumSize(QSize(0, 10))
        self.GetConstantData.setMaximumSize(QSize(16777215, 24))
        font11 = QFont()
        font11.setWeight(QFont.Medium)
        self.GetConstantData.setFont(font11)
        self.GetConstantData.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.GetConstantData.setAcceptDrops(False)
        self.GetConstantData.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.GetData.addWidget(self.GetConstantData, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.MainDetails.addLayout(self.GetData)

        self.line_4 = QFrame(self.DeviceInfo)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.MainDetails.addWidget(self.line_4)

        self.BMSVersion = QHBoxLayout()
        self.BMSVersion.setObjectName(u"BMSVersion")
        self.BMSIDtext = QLabel(self.DeviceInfo)
        self.BMSIDtext.setObjectName(u"BMSIDtext")
        font12 = QFont()
        font12.setPointSize(10)
        font12.setBold(True)
        self.BMSIDtext.setFont(font12)
        self.BMSIDtext.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BMSVersion.addWidget(self.BMSIDtext)

        self.BMSID_label = QLabel(self.DeviceInfo)
        self.BMSID_label.setObjectName(u"BMSID_label")
        font13 = QFont()
        font13.setPointSize(10)
        self.BMSID_label.setFont(font13)
        self.BMSID_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.BMSVersion.addWidget(self.BMSID_label)


        self.MainDetails.addLayout(self.BMSVersion)

        self.FirmwareVersion = QHBoxLayout()
        self.FirmwareVersion.setObjectName(u"FirmwareVersion")
        self.FirmwareVersionText = QLabel(self.DeviceInfo)
        self.FirmwareVersionText.setObjectName(u"FirmwareVersionText")
        self.FirmwareVersionText.setFont(font12)
        self.FirmwareVersionText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.FirmwareVersion.addWidget(self.FirmwareVersionText)

        self.FirmwareVersion_Label = QLabel(self.DeviceInfo)
        self.FirmwareVersion_Label.setObjectName(u"FirmwareVersion_Label")
        self.FirmwareVersion_Label.setFont(font13)
        self.FirmwareVersion_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.FirmwareVersion.addWidget(self.FirmwareVersion_Label)


        self.MainDetails.addLayout(self.FirmwareVersion)

        self.CellType = QHBoxLayout()
        self.CellType.setObjectName(u"CellType")
        self.CellTypeText = QLabel(self.DeviceInfo)
        self.CellTypeText.setObjectName(u"CellTypeText")
        self.CellTypeText.setFont(font12)
        self.CellTypeText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.CellType.addWidget(self.CellTypeText)

        self.CellType_label = QLabel(self.DeviceInfo)
        self.CellType_label.setObjectName(u"CellType_label")
        self.CellType_label.setFont(font13)
        self.CellType_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.CellType.addWidget(self.CellType_label)


        self.MainDetails.addLayout(self.CellType)

        self.BMSStates = QHBoxLayout()
        self.BMSStates.setSpacing(10)
        self.BMSStates.setObjectName(u"BMSStates")
        self.BMSStates.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.BMSStates.setContentsMargins(0, -1, -1, -1)
        self.BalanceState = QHBoxLayout()
        self.BalanceState.setObjectName(u"BalanceState")
        self.BalanceStateText = QLabel(self.DeviceInfo)
        self.BalanceStateText.setObjectName(u"BalanceStateText")
        font14 = QFont()
        font14.setBold(True)
        self.BalanceStateText.setFont(font14)
        self.BalanceStateText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.BalanceState.addWidget(self.BalanceStateText)

        self.BalanceStateLabel = QLabel(self.DeviceInfo)
        self.BalanceStateLabel.setObjectName(u"BalanceStateLabel")
        self.BalanceStateLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.BalanceState.addWidget(self.BalanceStateLabel)


        self.BMSStates.addLayout(self.BalanceState)

        self.ChargeState = QHBoxLayout()
        self.ChargeState.setObjectName(u"ChargeState")
        self.ChargeStateText = QLabel(self.DeviceInfo)
        self.ChargeStateText.setObjectName(u"ChargeStateText")
        self.ChargeStateText.setFont(font14)
        self.ChargeStateText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.ChargeState.addWidget(self.ChargeStateText)

        self.ChargeStateLabel = QLabel(self.DeviceInfo)
        self.ChargeStateLabel.setObjectName(u"ChargeStateLabel")
        self.ChargeStateLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.ChargeState.addWidget(self.ChargeStateLabel)


        self.BMSStates.addLayout(self.ChargeState)

        self.DischargeState = QHBoxLayout()
        self.DischargeState.setObjectName(u"DischargeState")
        self.DischargeStateText = QLabel(self.DeviceInfo)
        self.DischargeStateText.setObjectName(u"DischargeStateText")
        self.DischargeStateText.setFont(font14)
        self.DischargeStateText.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.DischargeState.addWidget(self.DischargeStateText)

        self.DischargeStateLabel = QLabel(self.DeviceInfo)
        self.DischargeStateLabel.setObjectName(u"DischargeStateLabel")
        self.DischargeStateLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.DischargeState.addWidget(self.DischargeStateLabel)


        self.BMSStates.addLayout(self.DischargeState)


        self.MainDetails.addLayout(self.BMSStates)

        self.MainDetails.setStretch(0, 1)
        self.MainDetails.setStretch(2, 2)
        self.MainDetails.setStretch(3, 2)
        self.MainDetails.setStretch(4, 2)
        self.MainDetails.setStretch(5, 2)

        self.horizontalLayout.addLayout(self.MainDetails)

        self.verticalFrame = QFrame(self.DeviceInfo)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setFrameShape(QFrame.Shape.Box)
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.UsersLogsText = QLabel(self.verticalFrame)
        self.UsersLogsText.setObjectName(u"UsersLogsText")
        self.UsersLogsText.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.UsersLogsText)

        self.listView_users = QListView(self.verticalFrame)
        self.listView_users.setObjectName(u"listView_users")
        self.listView_users.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.listView_users)


        self.horizontalLayout.addWidget(self.verticalFrame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.tabWidget.addTab(self.DeviceInfo, "")
        self.Configuration = QWidget()
        self.Configuration.setObjectName(u"Configuration")
        self.verticalLayout_8 = QVBoxLayout(self.Configuration)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Refresh_configuration_button = QPushButton(self.Configuration)
        self.Refresh_configuration_button.setObjectName(u"Refresh_configuration_button")
        sizePolicy3.setHeightForWidth(self.Refresh_configuration_button.sizePolicy().hasHeightForWidth())
        self.Refresh_configuration_button.setSizePolicy(sizePolicy3)
        self.Refresh_configuration_button.setAutoDefault(False)

        self.verticalLayout_8.addWidget(self.Refresh_configuration_button, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(200, -1, 200, 100)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.MaxVoltageDiff = QVBoxLayout()
        self.MaxVoltageDiff.setObjectName(u"MaxVoltageDiff")
        self.VoltageDiffLabel = QLabel(self.Configuration)
        self.VoltageDiffLabel.setObjectName(u"VoltageDiffLabel")
        self.VoltageDiffLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.MaxVoltageDiff.addWidget(self.VoltageDiffLabel)

        self.VoltageDiffSetter = QHBoxLayout()
        self.VoltageDiffSetter.setObjectName(u"VoltageDiffSetter")
        self.VoltageDiffBox = QDoubleSpinBox(self.Configuration)
        self.VoltageDiffBox.setObjectName(u"VoltageDiffBox")
        sizePolicy3.setHeightForWidth(self.VoltageDiffBox.sizePolicy().hasHeightForWidth())
        self.VoltageDiffBox.setSizePolicy(sizePolicy3)
        self.VoltageDiffBox.setSingleStep(0.010000000000000)

        self.VoltageDiffSetter.addWidget(self.VoltageDiffBox)

        self.SetVoltageDiff = QPushButton(self.Configuration)
        self.SetVoltageDiff.setObjectName(u"SetVoltageDiff")
        sizePolicy2.setHeightForWidth(self.SetVoltageDiff.sizePolicy().hasHeightForWidth())
        self.SetVoltageDiff.setSizePolicy(sizePolicy2)

        self.VoltageDiffSetter.addWidget(self.SetVoltageDiff)


        self.MaxVoltageDiff.addLayout(self.VoltageDiffSetter)


        self.verticalLayout_6.addLayout(self.MaxVoltageDiff)

        self.MaxVoltage = QVBoxLayout()
        self.MaxVoltage.setObjectName(u"MaxVoltage")
        self.MaxVoltageLabel = QLabel(self.Configuration)
        self.MaxVoltageLabel.setObjectName(u"MaxVoltageLabel")
        self.MaxVoltageLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.MaxVoltage.addWidget(self.MaxVoltageLabel)

        self.MaxVoltageSetter = QHBoxLayout()
        self.MaxVoltageSetter.setObjectName(u"MaxVoltageSetter")
        self.MaxVoltageBox = QDoubleSpinBox(self.Configuration)
        self.MaxVoltageBox.setObjectName(u"MaxVoltageBox")
        sizePolicy3.setHeightForWidth(self.MaxVoltageBox.sizePolicy().hasHeightForWidth())
        self.MaxVoltageBox.setSizePolicy(sizePolicy3)
        self.MaxVoltageBox.setSingleStep(0.010000000000000)

        self.MaxVoltageSetter.addWidget(self.MaxVoltageBox)

        self.SetMaxVoltage = QPushButton(self.Configuration)
        self.SetMaxVoltage.setObjectName(u"SetMaxVoltage")
        sizePolicy2.setHeightForWidth(self.SetMaxVoltage.sizePolicy().hasHeightForWidth())
        self.SetMaxVoltage.setSizePolicy(sizePolicy2)

        self.MaxVoltageSetter.addWidget(self.SetMaxVoltage)


        self.MaxVoltage.addLayout(self.MaxVoltageSetter)


        self.verticalLayout_6.addLayout(self.MaxVoltage)

        self.MinVoltage = QVBoxLayout()
        self.MinVoltage.setObjectName(u"MinVoltage")
        self.MinVoltageLabel = QLabel(self.Configuration)
        self.MinVoltageLabel.setObjectName(u"MinVoltageLabel")
        self.MinVoltageLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.MinVoltage.addWidget(self.MinVoltageLabel)

        self.MinVoltageSetter = QHBoxLayout()
        self.MinVoltageSetter.setObjectName(u"MinVoltageSetter")
        self.MinVoltageBox = QDoubleSpinBox(self.Configuration)
        self.MinVoltageBox.setObjectName(u"MinVoltageBox")
        sizePolicy3.setHeightForWidth(self.MinVoltageBox.sizePolicy().hasHeightForWidth())
        self.MinVoltageBox.setSizePolicy(sizePolicy3)
        self.MinVoltageBox.setSingleStep(0.010000000000000)

        self.MinVoltageSetter.addWidget(self.MinVoltageBox)

        self.SetMinVoltage = QPushButton(self.Configuration)
        self.SetMinVoltage.setObjectName(u"SetMinVoltage")
        sizePolicy2.setHeightForWidth(self.SetMinVoltage.sizePolicy().hasHeightForWidth())
        self.SetMinVoltage.setSizePolicy(sizePolicy2)

        self.MinVoltageSetter.addWidget(self.SetMinVoltage)


        self.MinVoltage.addLayout(self.MinVoltageSetter)


        self.verticalLayout_6.addLayout(self.MinVoltage)

        self.TempWarn = QVBoxLayout()
        self.TempWarn.setObjectName(u"TempWarn")
        self.TempWarnSetterLabel = QLabel(self.Configuration)
        self.TempWarnSetterLabel.setObjectName(u"TempWarnSetterLabel")
        self.TempWarnSetterLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.TempWarn.addWidget(self.TempWarnSetterLabel)

        self.TempWarnSetter = QHBoxLayout()
        self.TempWarnSetter.setObjectName(u"TempWarnSetter")
        self.TempWarnBox = QDoubleSpinBox(self.Configuration)
        self.TempWarnBox.setObjectName(u"TempWarnBox")
        sizePolicy3.setHeightForWidth(self.TempWarnBox.sizePolicy().hasHeightForWidth())
        self.TempWarnBox.setSizePolicy(sizePolicy3)
        self.TempWarnBox.setSingleStep(0.010000000000000)

        self.TempWarnSetter.addWidget(self.TempWarnBox)

        self.SetTempWarn = QPushButton(self.Configuration)
        self.SetTempWarn.setObjectName(u"SetTempWarn")
        sizePolicy2.setHeightForWidth(self.SetTempWarn.sizePolicy().hasHeightForWidth())
        self.SetTempWarn.setSizePolicy(sizePolicy2)

        self.TempWarnSetter.addWidget(self.SetTempWarn)


        self.TempWarn.addLayout(self.TempWarnSetter)


        self.verticalLayout_6.addLayout(self.TempWarn)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(40, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.horizontalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.MinSOC = QVBoxLayout()
        self.MinSOC.setObjectName(u"MinSOC")
        self.MinSOCLabel = QLabel(self.Configuration)
        self.MinSOCLabel.setObjectName(u"MinSOCLabel")
        self.MinSOCLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.MinSOC.addWidget(self.MinSOCLabel)

        self.MinSOCSetter = QHBoxLayout()
        self.MinSOCSetter.setObjectName(u"MinSOCSetter")
        self.MinSOCBox = QDoubleSpinBox(self.Configuration)
        self.MinSOCBox.setObjectName(u"MinSOCBox")
        sizePolicy3.setHeightForWidth(self.MinSOCBox.sizePolicy().hasHeightForWidth())
        self.MinSOCBox.setSizePolicy(sizePolicy3)
        self.MinSOCBox.setSingleStep(0.010000000000000)

        self.MinSOCSetter.addWidget(self.MinSOCBox)

        self.SetMinSOC = QPushButton(self.Configuration)
        self.SetMinSOC.setObjectName(u"SetMinSOC")
        sizePolicy2.setHeightForWidth(self.SetMinSOC.sizePolicy().hasHeightForWidth())
        self.SetMinSOC.setSizePolicy(sizePolicy2)

        self.MinSOCSetter.addWidget(self.SetMinSOC)


        self.MinSOC.addLayout(self.MinSOCSetter)


        self.verticalLayout_7.addLayout(self.MinSOC)

        self.MaxCurrent = QVBoxLayout()
        self.MaxCurrent.setObjectName(u"MaxCurrent")
        self.MaxCurrentLabel = QLabel(self.Configuration)
        self.MaxCurrentLabel.setObjectName(u"MaxCurrentLabel")
        self.MaxCurrentLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.MaxCurrent.addWidget(self.MaxCurrentLabel)

        self.MaxCurrentSetter = QHBoxLayout()
        self.MaxCurrentSetter.setObjectName(u"MaxCurrentSetter")
        self.MaxCurrentBox = QDoubleSpinBox(self.Configuration)
        self.MaxCurrentBox.setObjectName(u"MaxCurrentBox")
        sizePolicy3.setHeightForWidth(self.MaxCurrentBox.sizePolicy().hasHeightForWidth())
        self.MaxCurrentBox.setSizePolicy(sizePolicy3)
        self.MaxCurrentBox.setSingleStep(0.010000000000000)

        self.MaxCurrentSetter.addWidget(self.MaxCurrentBox)

        self.SetMaxCurrent = QPushButton(self.Configuration)
        self.SetMaxCurrent.setObjectName(u"SetMaxCurrent")
        sizePolicy2.setHeightForWidth(self.SetMaxCurrent.sizePolicy().hasHeightForWidth())
        self.SetMaxCurrent.setSizePolicy(sizePolicy2)

        self.MaxCurrentSetter.addWidget(self.SetMaxCurrent)


        self.MaxCurrent.addLayout(self.MaxCurrentSetter)


        self.verticalLayout_7.addLayout(self.MaxCurrent)

        self.TempDisconnect = QVBoxLayout()
        self.TempDisconnect.setObjectName(u"TempDisconnect")
        self.TempDisconnectLabel = QLabel(self.Configuration)
        self.TempDisconnectLabel.setObjectName(u"TempDisconnectLabel")
        self.TempDisconnectLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.TempDisconnect.addWidget(self.TempDisconnectLabel)

        self.TempDisconnectSetter = QHBoxLayout()
        self.TempDisconnectSetter.setObjectName(u"TempDisconnectSetter")
        self.TempDisconnectBox = QDoubleSpinBox(self.Configuration)
        self.TempDisconnectBox.setObjectName(u"TempDisconnectBox")
        sizePolicy3.setHeightForWidth(self.TempDisconnectBox.sizePolicy().hasHeightForWidth())
        self.TempDisconnectBox.setSizePolicy(sizePolicy3)
        self.TempDisconnectBox.setSingleStep(0.010000000000000)

        self.TempDisconnectSetter.addWidget(self.TempDisconnectBox)

        self.SetTempDisconnect = QPushButton(self.Configuration)
        self.SetTempDisconnect.setObjectName(u"SetTempDisconnect")
        sizePolicy2.setHeightForWidth(self.SetTempDisconnect.sizePolicy().hasHeightForWidth())
        self.SetTempDisconnect.setSizePolicy(sizePolicy2)

        self.TempDisconnectSetter.addWidget(self.SetTempDisconnect)


        self.TempDisconnect.addLayout(self.TempDisconnectSetter)


        self.verticalLayout_7.addLayout(self.TempDisconnect)

        self.BatterCapacity = QVBoxLayout()
        self.BatterCapacity.setObjectName(u"BatterCapacity")
        self.BatterCapacityLabel = QLabel(self.Configuration)
        self.BatterCapacityLabel.setObjectName(u"BatterCapacityLabel")
        self.BatterCapacityLabel.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.BatterCapacity.addWidget(self.BatterCapacityLabel)

        self.BatterCapacitySetter = QHBoxLayout()
        self.BatterCapacitySetter.setObjectName(u"BatterCapacitySetter")
        self.BatterCapacityBox = QDoubleSpinBox(self.Configuration)
        self.BatterCapacityBox.setObjectName(u"BatterCapacityBox")
        sizePolicy3.setHeightForWidth(self.BatterCapacityBox.sizePolicy().hasHeightForWidth())
        self.BatterCapacityBox.setSizePolicy(sizePolicy3)
        self.BatterCapacityBox.setSingleStep(0.010000000000000)

        self.BatterCapacitySetter.addWidget(self.BatterCapacityBox)

        self.SetBatterCapacity = QPushButton(self.Configuration)
        self.SetBatterCapacity.setObjectName(u"SetBatterCapacity")
        sizePolicy2.setHeightForWidth(self.SetBatterCapacity.sizePolicy().hasHeightForWidth())
        self.SetBatterCapacity.setSizePolicy(sizePolicy2)

        self.BatterCapacitySetter.addWidget(self.SetBatterCapacity)


        self.BatterCapacity.addLayout(self.BatterCapacitySetter)


        self.verticalLayout_7.addLayout(self.BatterCapacity)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(2, 5)

        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.Configuration, "")
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.COMConnectionFeedback = QLabel(self.Settings)
        self.COMConnectionFeedback.setObjectName(u"COMConnectionFeedback")
        self.COMConnectionFeedback.setGeometry(QRect(360, 210, 271, 31))
        self.verticalLayoutWidget_9 = QWidget(self.Settings)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(70, 240, 191, 111))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_9)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.radioButton_light = QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_light.setObjectName(u"radioButton_light")

        self.verticalLayout_4.addWidget(self.radioButton_light)

        self.radioButton_dark = QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_dark.setObjectName(u"radioButton_dark")

        self.verticalLayout_4.addWidget(self.radioButton_dark)

        self.verticalLayoutWidget_10 = QWidget(self.Settings)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(70, 100, 191, 101))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget_10)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox_serial_list = QComboBox(self.verticalLayoutWidget_10)
        self.comboBox_serial_list.setObjectName(u"comboBox_serial_list")

        self.horizontalLayout_3.addWidget(self.comboBox_serial_list)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ConnectSerial = QPushButton(self.verticalLayoutWidget_10)
        self.ConnectSerial.setObjectName(u"ConnectSerial")

        self.horizontalLayout_2.addWidget(self.ConnectSerial)

        self.refreshCOMports = QPushButton(self.verticalLayoutWidget_10)
        self.refreshCOMports.setObjectName(u"refreshCOMports")

        self.horizontalLayout_2.addWidget(self.refreshCOMports)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.Settings, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.debug_lable = QLabel(self.centralwidget)
        self.debug_lable.setObjectName(u"debug_lable")

        self.horizontalLayout_8.addWidget(self.debug_lable)

        self.horizontalLayout_8.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1035, 21))
        self.menuPort = QMenu(self.menubar)
        self.menuPort.setObjectName(u"menuPort")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPort.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"**Please Disconnect Before Closing the Window", None))
        self.TemperatureHeader.setText(QCoreApplication.translate("MainWindow", u"Tempareture (\u00b0C)", None))
        self.BT1text.setText(QCoreApplication.translate("MainWindow", u"Battery T1:", None))
        self.BT1label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BT2text.setText(QCoreApplication.translate("MainWindow", u"Battery T2:", None))
        self.BT2label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BT3text.setText(QCoreApplication.translate("MainWindow", u"Battery T3:", None))
        self.BT3label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BT4text.setText(QCoreApplication.translate("MainWindow", u"Battery T4:", None))
        self.BT4label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BT5text.setText(QCoreApplication.translate("MainWindow", u"Battery T5:", None))
        self.BT5label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BT6text.setText(QCoreApplication.translate("MainWindow", u"Battery T6:", None))
        self.BT6label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.BatteryHealthText.setText(QCoreApplication.translate("MainWindow", u"Battery Health(%):", None))
        self.BatteryHealthLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RemainCapacityText.setText(QCoreApplication.translate("MainWindow", u"Remain Capacity:", None))
        self.RemainCapacityLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.AveCellVoltText.setText(QCoreApplication.translate("MainWindow", u"Avg.Cell Volt:", None))
        self.AveCellVoltLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.RemainBatteryText.setText(QCoreApplication.translate("MainWindow", u"Remain Battery(%):", None))
        self.RemainBatteryLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Total_Current_Text.setText(QCoreApplication.translate("MainWindow", u"Current (A)", None))
        self.Total_Current.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Total_Voltage_Text.setText(QCoreApplication.translate("MainWindow", u"Voltage (V)", None))
        self.Total_Voltage.setText(QCoreApplication.translate("MainWindow", u"0 ", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.BatteryCapacityText.setText(QCoreApplication.translate("MainWindow", u"Battery Capacity:", None))
        self.BatteryCapacityLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CellVoltDiffText.setText(QCoreApplication.translate("MainWindow", u"Cell Volt. Diff:", None))
        self.CellVoltDiffLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CellVoltageHeader.setText(QCoreApplication.translate("MainWindow", u"Cell Voltage(V)", None))
        self.C1_text.setText(QCoreApplication.translate("MainWindow", u"C1:", None))
        self.C1_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C2_text.setText(QCoreApplication.translate("MainWindow", u"C2:", None))
        self.C2_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C3_text.setText(QCoreApplication.translate("MainWindow", u"C3:", None))
        self.C3_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C4_text.setText(QCoreApplication.translate("MainWindow", u"C4:", None))
        self.C4_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C5_text.setText(QCoreApplication.translate("MainWindow", u"C5:", None))
        self.C5_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C6_text.setText(QCoreApplication.translate("MainWindow", u"C6:", None))
        self.C6_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C7_text.setText(QCoreApplication.translate("MainWindow", u"C7:", None))
        self.C7_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C8_text.setText(QCoreApplication.translate("MainWindow", u"C8:", None))
        self.C8_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C9_text.setText(QCoreApplication.translate("MainWindow", u"C9:", None))
        self.C9_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C10_text.setText(QCoreApplication.translate("MainWindow", u"C10:", None))
        self.C10_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C11_text.setText(QCoreApplication.translate("MainWindow", u"C11:", None))
        self.C11_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C12_text.setText(QCoreApplication.translate("MainWindow", u"C12:", None))
        self.C12_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C13_text.setText(QCoreApplication.translate("MainWindow", u"C13:", None))
        self.C13_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C14_text.setText(QCoreApplication.translate("MainWindow", u"C14:", None))
        self.C14_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C15_text.setText(QCoreApplication.translate("MainWindow", u"C15:", None))
        self.C15_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.C16_text.setText(QCoreApplication.translate("MainWindow", u"C16:", None))
        self.C16_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.StartRecordCellVoltages.setText(QCoreApplication.translate("MainWindow", u"Start Cell Voltage Recording ", None))
        self.StopRecordCellVoltages.setText(QCoreApplication.translate("MainWindow", u"Stop Cell Voltage Recording", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LiveStatus), QCoreApplication.translate("MainWindow", u"Live Status", None))
        self.GetDataStatus.setText("")
        self.GetConstantData.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.BMSIDtext.setText(QCoreApplication.translate("MainWindow", u"BMS ID: ", None))
        self.BMSID_label.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.FirmwareVersionText.setText(QCoreApplication.translate("MainWindow", u"Firmware Version:", None))
        self.FirmwareVersion_Label.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.CellTypeText.setText(QCoreApplication.translate("MainWindow", u"Cell type: ", None))
        self.CellType_label.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.BalanceStateText.setText(QCoreApplication.translate("MainWindow", u"Balancer:", None))
        self.BalanceStateLabel.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.ChargeStateText.setText(QCoreApplication.translate("MainWindow", u"Charge:", None))
        self.ChargeStateLabel.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.DischargeStateText.setText(QCoreApplication.translate("MainWindow", u"Discharge:", None))
        self.DischargeStateLabel.setText(QCoreApplication.translate("MainWindow", u"NONE", None))
        self.UsersLogsText.setText(QCoreApplication.translate("MainWindow", u"Users Logs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DeviceInfo), QCoreApplication.translate("MainWindow", u"Device Info", None))
        self.Refresh_configuration_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.VoltageDiffLabel.setText(QCoreApplication.translate("MainWindow", u"Max Voltage Difference (V)", None))
        self.SetVoltageDiff.setText(QCoreApplication.translate("MainWindow", u"Set Max Voltage Diff.", None))
        self.MaxVoltageLabel.setText(QCoreApplication.translate("MainWindow", u"Max Voltage (V)", None))
        self.SetMaxVoltage.setText(QCoreApplication.translate("MainWindow", u"Set Max Voltage", None))
        self.MinVoltageLabel.setText(QCoreApplication.translate("MainWindow", u"Min Voltage (V)", None))
        self.SetMinVoltage.setText(QCoreApplication.translate("MainWindow", u"Set Min Voltage", None))
        self.TempWarnSetterLabel.setText(QCoreApplication.translate("MainWindow", u"High Temperature Warning TH (\u00b0C)", None))
        self.SetTempWarn.setText(QCoreApplication.translate("MainWindow", u"Set Temp Warning TH", None))
        self.MinSOCLabel.setText(QCoreApplication.translate("MainWindow", u"Min SOC (%)", None))
        self.SetMinSOC.setText(QCoreApplication.translate("MainWindow", u"Set Min SOC", None))
        self.MaxCurrentLabel.setText(QCoreApplication.translate("MainWindow", u"Max Current (A)", None))
        self.SetMaxCurrent.setText(QCoreApplication.translate("MainWindow", u"Set Max Current", None))
        self.TempDisconnectLabel.setText(QCoreApplication.translate("MainWindow", u"High Temperature Disconnect TH (\u00b0C)", None))
        self.SetTempDisconnect.setText(QCoreApplication.translate("MainWindow", u"Set Temp Disconnect TH", None))
        self.BatterCapacityLabel.setText(QCoreApplication.translate("MainWindow", u"Battery Capacity (AH)", None))
        self.SetBatterCapacity.setText(QCoreApplication.translate("MainWindow", u"Set Battery Capacity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Configuration), QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.COMConnectionFeedback.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Theme", None))
        self.radioButton_light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.radioButton_dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select COM port", None))
        self.ConnectSerial.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.refreshCOMports.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Last Status:", None))
        self.debug_lable.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"BMS Dashboard v1.0 | FYP-Group21  | \u00a9 2025", None))
        self.menuPort.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

