import serial
import time

class Tenma:
    def __init__(self, _port, _voltage, _current):
        self.ser = serial.Serial(port=_port,
                                 baudrate=9600,
                                 parity=serial.PARITY_NONE,
                                 stopbits=serial.STOPBITS_ONE)
        self.setVoltage(_voltage)
        self.setCurrent(_current)

    def __sendCommand(self, command):
        self.ser.write(command.encode('ascii'))
        time.sleep(0.1)

    def __receiveOutput(self):
        return self.ser.read(self.ser.in_waiting).decode('ascii')

    def getVersion(self):
        self.__sendCommand("*IDN?")
        return self.__receiveOutput()

    def setCurrent(self, current):
        self.__sendCommand(f'ISET1:{current}')

    def getCurrent(self):
        self.__sendCommand(f'ISET1?')
        return float(self.__receiveOutput())

    def setVoltage(self, voltage):
        self.__sendCommand(f'VSET1:{voltage}')

    def getVoltage(self):
        self.__sendCommand(f'VSET1?')
        return float(self.__receiveOutput())

    def start(self):
        self.__sendCommand(f'OUT1')

    def stop(self):
        self.__sendCommand(f'OUT0')

    def printInfo(self):
        print(f'Version: {self.getVersion()}')
        print(f'Current: {self.getCurrent():2.5} A')
        print(f'Voltage: {self.getVoltage():2.5} V')
