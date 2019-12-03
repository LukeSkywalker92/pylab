import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from threading import Thread
import time

class MPLLivePlot(Thread):
    def __init__(self, columns):
        self.columns = columns
        self.stopped = False
        Thread.__init__(self)

    def stop(self):
        self.stopped = True

    def run(self):
        self.root = tk.Tk()

        self.autoscale = tk.BooleanVar()
        self.autoscale.set(True)
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax2 = self.ax.twinx()
        self.line, = self.ax.plot(0, 0, color="tab:blue")
        self.line2, = self.ax2.plot(0, 0, color="tab:red")
        self.ax.autoscale(self.autoscale.get(),self.autoscale.get(),self.autoscale.get())
        self.ax2.autoscale(self.autoscale.get(),self.autoscale.get(),self.autoscale.get())
        self.ax.tick_params(axis='y', labelcolor="tab:blue")
        self.ax2.tick_params(axis='y', labelcolor="tab:red")

        self.canvas = FigureCanvasTkAgg(self.fig,master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1,column=0,columnspan=4,rowspan=20)
        self.toolbarFrame = tk.Frame(master=self.root)
        self.toolbarFrame.grid(row=22,column=0, columnspan=4)
        toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        self.buttonFrame = tk.Frame(master=self.root)
        self.buttonFrame.grid(row=23,column=0, rowspan=len(self.columns), columnspan=5, pady=30)
        tk.Checkbutton(self.buttonFrame, variable=self.autoscale, text='Autoscale', onvalue=True, offvalue=False).grid(row=0, column=0, columnspan=4)
        tk.Label(self.buttonFrame, text="Name").grid(row=1, column=0, columnspan=2)
        tk.Label(self.buttonFrame, text="X").grid(row=1, column=2, columnspan=1)
        tk.Label(self.buttonFrame, text="Y1").grid(row=1, column=3, columnspan=1)
        tk.Label(self.buttonFrame, text="Y2").grid(row=1, column=4, columnspan=1)

        ttk.Separator(self.buttonFrame, orient='horizontal').grid(row=2, columnspan=5, sticky="ew")

        self.xaxis = tk.IntVar(0)
        self.yaxis1 = tk.IntVar(0)
        self.yaxis2 = tk.IntVar(0)

        i=0
        for column in self.columns:
            tk.Label(self.buttonFrame, text=column.name).grid(row=i+3, column=0, columnspan=2, padx=30)
            tk.Radiobutton(self.buttonFrame, variable=self.xaxis, value=i).grid(row=i+3, column=2, columnspan=1, padx=30)
            tk.Radiobutton(self.buttonFrame, variable=self.yaxis1, value=i).grid(row=i+3, column=3, columnspan=1, padx=30)
            tk.Radiobutton(self.buttonFrame, variable=self.yaxis2, value=i).grid(row=i+3, column=4, columnspan=1, padx=30)
            i+=1


        self.root.after(100, self.update)
        self.root.mainloop()

    def choose_column(self, axis, index):
        print(axis, index)

    def update(self):
        if self.stopped is False:
            self.ax.autoscale(self.autoscale.get(),self.autoscale.get(),self.autoscale.get())
            self.ax2.autoscale(self.autoscale.get(),self.autoscale.get(),self.autoscale.get())
            self.line.set_xdata(self.columns[self.xaxis.get()].values)
            self.line.set_ydata(self.columns[self.yaxis1.get()].values)
            self.line2.set_xdata(self.columns[self.xaxis.get()].values)
            self.line2.set_ydata(self.columns[self.yaxis2.get()].values)
            self.ax.set_xlabel(self.columns[self.xaxis.get()].generate_header())
            self.ax.set_ylabel(self.columns[self.yaxis1.get()].generate_header(), color="tab:blue")
            self.ax.autoscale(self.autoscale.get())
            self.ax2.autoscale(self.autoscale.get())
            self.ax.relim()
            self.ax2.set_xlabel(self.columns[self.xaxis.get()].generate_header())
            self.ax2.set_ylabel(self.columns[self.yaxis2.get()].generate_header(), color="tab:red")
            self.ax2.relim()
            self.canvas.draw()
            self.root.after(100, self.update)
