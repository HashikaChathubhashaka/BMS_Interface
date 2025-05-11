# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_MainWindow
from SerialReader import SerialReader
from DataRecorder import Recorder
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
from PySide6.QtCore import QStringListModel
from serial.tools import list_ports



class MainWindow(QMainWindow):
    def __init__(self,app, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        with open("style.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.app = app
        # Create SerialReader object to read data from Serial
        self.reader = SerialReader(self.ui.debug_lable)

        self.cell_voltage_recorder = Recorder(self.reader)


        # Get data Button for getting constant data
        self.ui.GetConstantData.clicked.connect(self.read_device_info)

        self.user_logs_model = QStringListModel()
        self.ui.listView_users.setModel(self.user_logs_model)



        # Connect buttons for real time data
        self.ui.startButton.clicked.connect(self.connect_for_RT_data)
        self.ui.stopButton.clicked.connect(self.disconnect_for_RT_data)
        self.ui.stopButton.setEnabled(False)

        #Connect Buttons for Record Cell voltages
        self.ui.StartRecordCellVoltages.clicked.connect(self.start_recording_cell_voltages)
        self.ui.StopRecordCellVoltages.clicked.connect(self.stop_recording_cell_voltages)

        self.ui.StartRecordCellVoltages.setEnabled(False)
        self.ui.StopRecordCellVoltages.setEnabled(False)

        # update UI text live
        self.reader.timer.timeout.connect(self.update_ui)

##################################################################
        # Refreshing threshold Values using 'Refresh' button
        self.ui.Refresh_configuration_button.clicked.connect(self.refresh_threshold_values)

        # Set Temp Warning threshold button
        self.ui.SetTempWarn.clicked.connect(self.update_TWT)

        self.ui.SetTempDisconnect.clicked.connect(self.update_TDT)

        self.ui.SetMaxVoltage.clicked.connect(self.update_VHT)

        self.ui.SetMinVoltage.clicked.connect(self.update_VLT)

        self.ui.SetVoltageDiff.clicked.connect(self.update_VDT)

        self.ui.SetMaxCurrent.clicked.connect(self.update_CHT)

        self.ui.SetMinSOC.clicked.connect(self.update_SLT)

        self.ui.SetBatterCapacity.clicked.connect(self.update_SBCT)
#######################################################################


        # Fill the port list
        self.fill_port_list()

        # Connect the 'Connect' button
        self.ui.ConnectSerial.clicked.connect(self.connect_serial)

        #Refresh COM ports
        self.ui.refreshCOMports.clicked.connect(self.refresh_com_ports)


        # Connect radio buttons
        self.ui.radioButton_light.toggled.connect(self.apply_light_theme)
        self.ui.radioButton_dark.toggled.connect(self.apply_dark_theme)

        # Set default selection
        self.ui.radioButton_light.setChecked(True)

    def connect_for_RT_data(self):

        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)
        self.ui.StartRecordCellVoltages.setEnabled(True)
        self.reader.start_reading();




    def disconnect_for_RT_data(self):
        if not self.ui.StopRecordCellVoltages.isEnabled():
            self.ui.startButton.setEnabled(True)
            self.ui.stopButton.setEnabled(False)
            self.ui.StartRecordCellVoltages.setEnabled(False)
            self.reader.stop_reading();



    def start_recording_cell_voltages(self):

        self.ui.StopRecordCellVoltages.setEnabled(True)
        self.ui.StartRecordCellVoltages.setEnabled(False)

        if self.reader.cell_voltages_1_to_8 and self.reader.cell_voltages_9_to_16:
            # Combine both lists and convert all values to float
            all_cell_voltages_str = self.reader.cell_voltages_1_to_8 + self.reader.cell_voltages_9_to_16
            all_cell_voltages = [float(v) for v in all_cell_voltages_str if v]  # Skip empty strings if any

        self.cell_voltage_recorder.start();





    def stop_recording_cell_voltages(self):
        self.ui.StopRecordCellVoltages.setEnabled(False)
        self.ui.StartRecordCellVoltages.setEnabled(True)

        self.cell_voltage_recorder.stop();

    def fill_port_list(self):
        ports = [port.device for port in list_ports.comports()]
        self.ui.comboBox_serial_list.addItems(ports)

    def refresh_com_ports(self):
        ports = list_ports.comports()
        self.ui.comboBox_serial_list.clear()
        for port in ports:
            self.ui.comboBox_serial_list.addItem(port.device)


    def connect_serial(self):
        selected_port = self.ui.comboBox_serial_list.currentText()

        self.reader.set_port(selected_port)
        # Get data Button for getting constant data
        self.ui.GetConstantData.clicked.connect(self.read_device_info)



        # Connect buttons for real time data
        self.ui.startButton.clicked.connect(self.reader.start_reading)
        self.ui.stopButton.clicked.connect(self.reader.stop_reading)


        # update UI text live
        self.reader.timer.timeout.connect(self.update_ui)

        if (self.reader.ser):
            self.ui.COMConnectionFeedback.setText(f"Connected to {selected_port}.")
        print(f"Connected to {selected_port}")
        self.ui.debug_lable.setText(f"Connected to {selected_port}")


    def update_ui(self):

        if self.reader.total_voltage:
            self.ui.Total_Voltage.setText(f"{self.reader.total_voltage}")

        if self.reader.total_current:
            self.ui.Total_Current.setText(f"{self.reader.total_current}")

        if self.reader.Avg_cell_voltage:
            self.ui.AveCellVoltLabel.setText(f"{self.reader.Avg_cell_voltage}")

        if self.reader.cell_voltage_different:
            self.ui.CellVoltDiffLabel.setText(f"{self.reader.cell_voltage_different}")


        # Set C1 to C8 labels
        if self.reader.cell_voltages_1_to_8:
            for cell_number in range(1, 9):
                label_name = f"C{cell_number}_label"
                cell_value = self.reader.cell_voltages_1_to_8[cell_number - 1]
                label_widget = getattr(self.ui, label_name, None)
                if label_widget:
                    label_widget.setText(f"{cell_value}")

        # Set C9 to C16 labels
        if self.reader.cell_voltages_9_to_16:
            for cell_number in range(9, 17):
                label_name = f"C{cell_number}_label"
                cell_value = self.reader.cell_voltages_9_to_16[cell_number - 9]
                label_widget = getattr(self.ui, label_name, None)
                if label_widget:
                    label_widget.setText(f"{cell_value}")

        # Temp probs values
        if self.reader.temps:
            for temp_probs in range(1,7):
                label_name = f"BT{temp_probs}label"
                temp_value = self.reader.temps[temp_probs-1]
                label_widget = getattr(self.ui, label_name, None)
                if label_widget:
                    label_widget.setText(f"{temp_value}")


        if self.reader.remain_battery_capacity:
            self.ui.RemainBatteryLabel.setText(f"{self.reader.remain_battery_capacity}")

        if self.reader.battery_capacity:
            self.ui.BatteryCapacityLabel.setText(f"{self.reader.battery_capacity}")


        # if self.reader.battery_power: # dont have a label
        #         # self.ui.RemainBatteryLabel.setText(f"{self.reader.remain_battery_capacity}")




    def update_user_logs_listview(self, users_logs):
        numbered_logs = [f"{i}. {log}" for i, log in enumerate(users_logs)]
        model = QStringListModel()
        model.setStringList(numbered_logs)
        self.ui.listView_users.setModel(model)



    def read_device_info(self): # for device info tab ( statics data)


        fm_version, bms_ID, cell_type , balance_state , charge_state , discharge_state , users_logs,log_index = self.reader.get_constant_data()

        if bms_ID:
            self.ui.BMSID_label.setText(f"{bms_ID}")

        if fm_version:
            self.ui.FirmwareVersion_Label.setText(f"{fm_version}")

        if cell_type:
            self.ui.CellType_label.setText(f"{cell_type}")

        if balance_state:
            self.ui.BalanceStateLabel.setText(f"{balance_state}")

        if charge_state:
            self.ui.ChargeStateLabel.setText(f"{charge_state}")

        if discharge_state:
            self.ui.DischargeStateLabel.setText(f"{discharge_state}")

        if users_logs:
            ordered_logs = []
            count = len(users_logs)
            print(log_index)
            for i in range(count):
                # Calculate the correct index in circular fashion
                index = (int(log_index) - 1 - i) % count
                ordered_logs.append(f"{i+1}.) {users_logs[index]}")

            self.user_logs_model.setStringList(ordered_logs)




        if not (fm_version or bms_ID): # in case of no data reciving -> just for debugging
            self.ui.GetDataStatus.setText("No data received")
### Configurations - custom functions ###################
    def refresh_threshold_values(self):
        (
            temp_warning_threshold,
            temp_disconnecting_threshold,
            voltage_higher_threshold,
            voltage_lower_threshold,
            current_higher_threshold,
            soc_lower_threshold,
            voltage_different_threshold,
            battery_capacity
        ) = self.reader.get_threshould_values()

        if temp_warning_threshold:
            self.ui.TempWarnBox.setValue(float(temp_warning_threshold))
        if temp_disconnecting_threshold:
            self.ui.TempDisconnectBox.setValue(float(temp_disconnecting_threshold))
        if voltage_higher_threshold:
            self.ui.MaxVoltageBox.setValue(float(voltage_higher_threshold))
        if voltage_lower_threshold:
            self.ui.MinVoltageBox.setValue(float(voltage_lower_threshold))
        if current_higher_threshold:
            self.ui.MaxCurrentBox.setValue(float(current_higher_threshold))
        if soc_lower_threshold:
            self.ui.MinSOCBox.setValue(float(soc_lower_threshold))
        if voltage_different_threshold:
            self.ui.VoltageDiffBox.setValue(float(voltage_different_threshold))
        if battery_capacity:
            self.ui.BatterCapacityBox.setValue(float(battery_capacity))

    def update_TWT(self):
        value = self.ui.TempWarnBox.value()
        self.reader.set_temp_warning_threshold(value)

    def update_TDT(self):
        value = self.ui.TempDisconnectBox.value()
        self.reader.set_temp_disconnecting_threshold(value)

    def update_VHT(self):
        value = self.ui.MaxVoltageBox.value()
        self.reader.set_voltage_higher_threshold(value)

    def update_VLT(self):
        value = self.ui.MinVoltageBox.value()
        self.reader.set_voltage_lower_threshold(value)

    def update_VDT(self):
        value = self.ui.VoltageDiffBox.value()
        self.reader.set_voltage_different_threshold(value)

    def update_CHT(self):
        value = self.ui.MaxCurrentBox.value()
        self.reader.set_current_higher_threshold(value)

    def update_SLT(self):
        value = self.ui.MinSOCBox.value()
        self.reader.set_soc_lower_threshold(value)

    def update_SBCT(self):
        value = self.ui.BatterCapacityBox.value()
        self.reader.set_battery_capacity(value)


################################


#### Settings-> Custom functions

    def apply_light_theme(self):
        if self.ui.radioButton_light.isChecked():
            self.setStyleSheet("")  # Clear QSS



    def apply_dark_theme(self):
        if self.ui.radioButton_dark.isChecked():
            with open("style_dark.qss", "r") as file:
                self.setStyleSheet(file.read())

#################

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Start with light palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor("#FAFAFA"))
    palette.setColor(QPalette.WindowText, QColor("#000000"))
    palette.setColor(QPalette.Base, QColor("#f5f5f5"))
    palette.setColor(QPalette.Text, QColor("#000000"))
    palette.setColor(QPalette.Button, QColor("#E1E1E1"))
    palette.setColor(QPalette.ButtonText, QColor("#000000"))
    palette.setColor(QPalette.Highlight, QColor("#0078d7"))
    palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))

    app.setStyle("Fusion")
    app.setPalette(palette)

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

        window = MainWindow(app)
    window.show()
    sys.exit(app.exec())

