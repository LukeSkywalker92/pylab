from pylab.devices.keysight import KeysightB2962A
import numpy as np
import time

keysight = KeysightB2962A('USB0::0x0957::0xD218::MY52351110::0::INSTR')
keysight.set_channel_mode(1, 'voltage')
keysight.set_voltage_output(1, 0)
keysight.enable_channel(1)
time.sleep(0.1)
for voltage in np.arange(0, 105e-3, 5e-3):
    keysight.set_voltage_output(1, voltage)
    time.sleep(0.1)
keysight.disable_channel(1)
