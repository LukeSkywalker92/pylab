from pylab.tables import Table, Variable
from pylab.devices.generic import DummyDevice, TimeDevice
from pylab.plots import MPLLivePlot
import time

t = Table()

time_dev = TimeDevice()
t.table_add("Time", "Seconds", time_dev.elapsed_time)
dummy_dev = DummyDevice()
t.table_add("Random", "int", dummy_dev.get_value)
b_field = Variable(0)
t.table_add("BField", "Tesla", b_field)

t.plot(MPLLivePlot)

time_dev.reset_start_time()
for field in range(0,100):
    b_field.value = field
    t.tablesave()
    time.sleep(1)

print(t)
t.stop_plotting()
