from pylab.devices.keysight import KeysightB2962A
import numpy as np
import time

keysight = KeysightB2962A('USB0::0x0957::0xD218::MY52351110::0::INSTR')
keysight.set_channel_mode(1, 'voltage')

keysight.enable_channel(1)
for voltage in np.arange(0, 105e-2, 5e-2):
    keysight.voltage_pulse(1, voltage, 100e-3)
    time.sleep(0.5)
keysight.disable_channel(1)
