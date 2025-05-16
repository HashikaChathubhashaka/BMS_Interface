import csv
import datetime
from PySide6.QtCore import QTimer


class CellRecorder:
    def __init__(self, reader, interval_ms=60000): # data saving as 1 min intervals
        self.reader = reader  # data source (must have .cell_voltages_1_to_8 and .cell_voltages_9_to_16)
        self.interval_ms = interval_ms

        # QTimer is initialize in here, but it is start when timer.start happen
        self.timer = QTimer()
        self.timer.timeout.connect(self._record)

        self.file = None
        self.writer = None

    def start(self):
        # Generate filename with timestamp
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"cell_voltages_{now}.csv"

        # Open file and set up CSV writer
        self.file = open(filename, mode='w', newline='')
        self.writer = csv.writer(self.file)

        # Write CSV header
        self.writer.writerow(["Timestamp"] + [f"Cell_{i+1}" for i in range(16)])

        # Start timer
        self.timer.start(self.interval_ms)

    def stop(self):
        self.timer.stop()
        if self.file:
            self.file.close()
            self.file = None
            self.writer = None

    def _record(self):
        # if self.reader.cell_voltages_1_to_8 and self.reader.cell_voltages_9_to_16:
        data_str = self.reader.cell_voltages_1_to_8 + self.reader.cell_voltages_9_to_16
        data = [float(v) for v in data_str if v]  # convert and filter

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.writer.writerow([timestamp] + data)



class TempRecorder:
    def __init__(self, reader, interval_ms=60000): # data saving as 1 min intervals
        self.reader = reader  # data source (must have .cell_voltages_1_to_8 and .cell_voltages_9_to_16)
        self.interval_ms = interval_ms

        # QTimer is initialize in here, but it is start when timer.start happen
        self.timer = QTimer()
        self.timer.timeout.connect(self._record)

        self.file = None
        self.writer = None

    def start(self):
        # Generate filename with timestamp
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"temperatures_{now}.csv"

        # Open file and set up CSV writer
        self.file = open(filename, mode='w', newline='')
        self.writer = csv.writer(self.file)

        # Write CSV header
        self.writer.writerow(["Timestamp"] + [f"Temp_probs_{i+1}" for i in range(6)])

        # Start timer
        self.timer.start(self.interval_ms)

    def stop(self):
        self.timer.stop()
        if self.file:
            self.file.close()
            self.file = None
            self.writer = None

    def _record(self):

        #taking the temps values
        data_str = self.reader.temps
        data = [float(v) for v in data_str if v]  # convert and filter

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.writer.writerow([timestamp] + data)


class Temp_recorder:
    def __init__(self, reader, interval_ms=60000): # data saving as 1 min intervals
        self.reader = reader  # data source (must have .cell_voltages_1_to_8 and .cell_voltages_9_to_16)
        self.interval_ms = interval_ms

        # QTimer is initialize in here, but it is start when timer.start happen
        self.timer = QTimer()
        self.timer.timeout.connect(self._record)

        self.file = None
        self.writer = None

    def start(self):
        # Generate filename with timestamp
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"temperatures_{now}.csv"

        # Open file and set up CSV writer
        self.file = open(filename, mode='w', newline='')
        self.writer = csv.writer(self.file)

        # Write CSV header
        self.writer.writerow(["Timestamp"] + [f"Temp_probs_{i+1}" for i in range(6)])

        # Start timer
        self.timer.start(self.interval_ms)

    def stop(self):
        self.timer.stop()
        if self.file:
            self.file.close()
            self.file = None
            self.writer = None

    def _record(self):

        #taking the temps values
        data_str = self.reader.temps
        data = [float(v) for v in data_str if v]  # convert and filter

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.writer.writerow([timestamp] + data)
