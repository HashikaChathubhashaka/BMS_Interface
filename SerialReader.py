# SerialReader.py
# use to communicate with Serial


import time
import serial
from PySide6.QtCore import QTimer



class SerialReader:

    def __init__(self, debug_label , port='COM0', baudrate=115200):

        #variables for holding UI real-time values

        self.total_voltage = None
        self.total_current = None

        self.cell_voltages_1_to_8 = []  # each cell voltages from 1 to 8
        self.cell_voltages_9_to_16 = []  # each cell voltages from 9 to 16
        self.temps = [] # temperature probs readings

        self.battery_power = None  # find by calculation or from IC?
        self.battery_capacity = None # Full capacity -> ( we need to define or find by IC)
        self.remain_battery_capacity = None

        self.Avg_cell_voltage = None
        self.cell_voltage_different = None # calculate inside the UI ( also need to calculate inside STM)
        self.Avg_temp = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.read_line)  # This runs every interval

        self.port = port
        self.baudrate = baudrate

        self.debuging = debug_label


        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            self.ser = None  # handle it later in main GUI


    def set_port(self,new_port):
        self.port = new_port
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        except serial.SerialException as e:
            print(f"Serial error: {e}")
            self.debuging("Serial error: {e}")
            self.ser = None  # handle it later in main GUI


    def get_available_ports():
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]


    def write_to_uart(self,data):
        if self.ser:
            if self.ser.is_open:
                self.ser.write((data + '\n').encode('utf-8'))
                print(f"Sent: {data}")
            else:
                print("Serial port not open")
                self.debuging.setText("Serial port not open")

        else:
            print("port not found")
            self.debuging.setText("port not found")


    def get_constant_data(self, duration=5):

        fm_version = None
        bms_id = None
        cell_type = None
        users_logs = []
        log_index = 0


        balance_state = None
        charge_state = None
        discharge_state = None

        self.write_to_uart("DINFO\n")

        start_time = time.time()
        while time.time() - start_time < duration:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line.startswith("FMVERSION:"):
                    fm_version = line.split(":", 1)[1] #string.split(separator, maxsplit)
                elif line.startswith("BMSID:"):
                    bms_id = line.split(":", 1)[1]
                elif line.startswith("CELLTYPE:"):
                    cell_type = line.split(":", 1)[1]

                # data should send as -> USERLOGS:U1=Log1;U2=Log2;U3=Log3;...;U10=Log10
                elif line.startswith("USERLOGS:"):
                    print("user details coms")
                    logs_str = line.split(":", 1)[1]  # U1=..., U2=...
                    entries = logs_str.split(";")     # ['U1=...', 'U2=...', ...]
                    for entry in entries:
                        if '=' in entry:
                            key, value = entry.split("=", 1)
                            users_logs.append(value)


                elif line.startswith("BALANCESTATE:"):
                    balance_state = line.split(":", 1)[1]

                elif line.startswith("CHARGESTATE:"):
                    charge_state = line.split(":", 1)[1]

                elif line.startswith("DISCHARGESTATE:"):
                    discharge_state = line.split(":", 1)[1]

                elif line.startswith("LOGINDEX:"):
                    log_index = line.split(":", 1)[1]

            except UnicodeDecodeError:
                continue
            except AttributeError:
                continue

        return fm_version, bms_id,cell_type , balance_state , charge_state , discharge_state , users_logs,log_index

    def get_threshould_values(self, duration=5):


        temp_warning_threshold = None
        temp_disconnecting_threshold = None
        voltage_higher_threshold = None
        voltage_lower_threshold = None
        current_higher_threshold = None
        soc_lower_threshold = None
        voltage_different_threshold = None
        battery_capacity = None

        self.write_to_uart("GCONFIG\n")

        start_time = time.time()
        while time.time() - start_time < duration:
            try:
                line = self.ser.readline().decode('utf-8').strip()
                if line.startswith("TWT:"): # data should send as TWT:65.6
                    temp_warning_threshold = line.split(":", 1)[1] #string.split(separator, maxsplit)
                elif line.startswith("TDT:"): # TDT:101.1
                    temp_disconnecting_threshold = line.split(":", 1)[1]
                elif line.startswith("VHT:"):
                    voltage_higher_threshold = line.split(":", 1)[1]
                elif line.startswith("VLT:"):
                    voltage_lower_threshold = line.split(":", 1)[1]
                elif line.startswith("CHT:"):
                    current_higher_threshold = line.split(":", 1)[1]
                elif line.startswith("SLT:"):
                    soc_lower_threshold = line.split(":", 1)[1]
                elif line.startswith("VDT:"):
                    voltage_different_threshold = line.split(":", 1)[1]
                elif line.startswith("BCT:"):
                    battery_capacity = line.split(":", 1)[1]


            except UnicodeDecodeError:
                continue
            except AttributeError:
                continue

        return temp_warning_threshold, temp_disconnecting_threshold,voltage_higher_threshold , voltage_lower_threshold , current_higher_threshold , soc_lower_threshold,voltage_different_threshold,battery_capacity


    # setting up the values
    def set_temp_warning_threshold(self, value):
        self.write_to_uart(f"STWT:{value:.2f}\n")

    def set_temp_disconnecting_threshold(self, value):
        self.write_to_uart(f"STDT:{value:.2f}\n")

    def set_voltage_higher_threshold(self, value):
        self.write_to_uart(f"SVHT:{value:.2f}\n")

    def set_voltage_lower_threshold(self, value):
        self.write_to_uart(f"SVLT:{value:.2f}\n")

    def set_current_higher_threshold(self, value):
        self.write_to_uart(f"SCHT:{value:.2f}\n")

    def set_soc_lower_threshold(self, value):
        self.write_to_uart(f"SSLT:{value:.2f}\n")

    def set_voltage_different_threshold(self, value):
        self.write_to_uart(f"SVDT:{value:.2f}\n")

    def set_battery_capacity(self,value):
        self.write_to_uart(f"SBCT:{value:.2f}\n")


    def start_reading(self, interval_ms=200):
        # send data reading request
        self.write_to_uart("RDATASTART\n")
        self.timer.start(interval_ms)  # Start polling

    def stop_reading(self):
        self.timer.stop()
        #send stop data sending request
        self.write_to_uart("RDATASTOP\n")


    def read_line(self): # for real time data
        if self.ser and self.ser.in_waiting:
            try:

                line = self.ser.readline().decode('utf-8').strip()

                if line.startswith("TV:"): # total Voltage
                    self.total_voltage = line.split(":", 1)[1]
                    print("Total Voltage:", self.total_voltage)  # for debugging

                if line.startswith("TC:"): # Total Current
                    self.total_current = line.split(":", 1)[1]

                if line.startswith("BCP:"): # Battery Capacity ( this is a constant value for that battery,
                                                                # anyways, it is good to show in main Dashboard)
                    self.battery_capacity = line.split(":", 1)[1]

                if line.startswith("RBC:"): # Remaining battery capacity
                    self.remain_battery_capacity = line.split(":", 1)[1]

                # data should send as -> BTS:T1=100;T2=200, ...,T6=200
                if line.startswith("BTS:"): # Battery Temps
                    temps_str = line.split(":", 1)[1]  # Get everything after "BTS:"
                    entries = temps_str.split(",")     # Split into ['T1=100', 'T2=200', ..., 'T6=100']

                    # Initialize a dictionary temporarily to make it easier
                    temps = {}
                    for entry in entries:
                        if '=' in entry:
                            key, value = entry.split("=", 1)
                            temps[key.strip()] = value.strip()

                    self.temps = [temps.get(f"T{i}", None) for i in range(1, 7)]

                # data should send as -> CV1:C1=2.45;C2=4.45, ...,C8=1.00
                if line.startswith("CV1:"): # Cell Voltage Cell-1 to Cell-8
                    voltages_str = line.split(":", 1)[1]
                    entries = voltages_str.split(",")     # Split into ['C1=2.45', 'C2=4.45', ..., 'C6=1.00']

                    voltages = {}
                    for entry in entries:
                        if '=' in entry:
                            key, value = entry.split("=", 1)
                            voltages[key.strip()] = value.strip()

                    self.cell_voltages_1_to_8 = [voltages.get(f"C{i}", None) for i in range(1, 9)]

                # data should send as -> CV2:C9=4.45, ...,C16=1.00
                if line.startswith("CV2:"): # Cell Voltage Cell-9 to Cell-16
                    voltages_str = line.split(":", 1)[1]
                    entries = voltages_str.split(",")     # Split into ['C9=4.45', ..., 'C16=1.00']

                    voltages = {}
                    for entry in entries:
                        if '=' in entry:
                            key, value = entry.split("=", 1)
                            voltages[key.strip()] = value.strip()

                    self.cell_voltages_9_to_16 = [voltages.get(f"C{i}", None) for i in range(9, 17)]





            except UnicodeDecodeError:
                pass



            if self.cell_voltages_1_to_8 and self.cell_voltages_9_to_16:
                # Combine both lists and convert all values to float
                all_voltages_str = self.cell_voltages_1_to_8 + self.cell_voltages_9_to_16
                all_voltages = [float(v) for v in all_voltages_str if v]  # Skip empty strings if any

                # Calculate average and difference between max and min
                if all_voltages:
                    # make these two have limited decimal points
                    self.Avg_cell_voltage = round(sum(all_voltages) / len(all_voltages), 4)
                    self.cell_voltage_different = round(max(all_voltages) - min(all_voltages), 4)


            #calculating Avarage Temperature
            if self.temps:
                temp_floats = [float(v) for v in self.temps if v]
                self.Avg_temp = round(sum(temp_floats) / len(temp_folats) , 4)







