#!/usr/bin/env python3

import tenma.module as tenma
import argparse
import signal
import sys

parser = argparse.ArgumentParser(description='Setup control for Tenma Power Supply')
parser.add_argument('-v', '--voltage', help='set voltage', required=True, type=float)
parser.add_argument('-c', '--current', help='set current', required=True, type=float)
parser.add_argument('-d', '--device', default='/dev/ttyACM0', help='set device')

def signal_handler(sig, frame):
    print('Terminate Tenma control')
signal.signal(signal.SIGINT, signal_handler)

def confirmSetup(voltage_new, voltage_old, current_new, current_old):
    if (current_old != current_new or voltage_old != voltage_new):
        answer = input(f'Setup {voltage_new:2.5} V {current_new:2.5} A correct? [yN]').lower()
        if (answer != 'y'):
            sys.exit()

def main():
    args = vars(parser.parse_args())
    power_supply = tenma.Tenma(args['device'])
    confirmSetup(args['voltage'], power_supply.getVoltage(),
                 args['current'], power_supply.getCurrent())
    power_supply.setVoltage(args['voltage'])
    power_supply.setCurrent(args['current'])
    power_supply.printInfo()
    power_supply.start()
    print('Press Ctrl+C to stop')
    signal.pause()
    power_supply.stop()

if __name__ == "__main__":
    main()
