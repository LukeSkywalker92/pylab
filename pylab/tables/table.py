import warnings
from tabulate import tabulate
from .column import Column
from threading import Thread

class Table():

    def __init__(self):
        self.columns = []
        self.measured = False

    def __str__(self):
        headers = [column.generate_header() for column in self.columns]
        values = list(map(list, zip(*[column.values for column in self.columns])))
        return tabulate(values, headers=headers, tablefmt="psql")

    def table_add(self, name, unit, callback):
        if self.measured:
            warnings.warn("Already measured, cannot add another column.")
        else:
            self.columns.append(Column(name, unit, callback))
            self._table_add()

    def plot(self, plot):
        self.plot = plot(self.columns)
        self.plot.start()

    def stop_plotting(self):
        self.plot.stop()
        self.plot.join()

    def tablesave(self):
        self.measured = True
        for device in self.columns:
            device.measure()
        self._tablesave()

    def _table_add(self):
        pass

    def _tablesave(self):
        pass
