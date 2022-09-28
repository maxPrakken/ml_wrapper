from cProfile import label
from msilib.schema import CheckBox
from tkinter import * 
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
from turtle import width
import datetime

def main():
    curtime = datetime.datetime.now()

    # Top level window
    frame = tk.Tk()
    frame.title("pipeline tester")
    frame.geometry('400x500')
    # Function for getting Input
    # from textbox and printing it 
    # at label widget

    widgets = {}
    parameters = {}
    
    def getInput():
        #print(widgets)
        for x, y in widgets.items():
            try:
                parameters[x] = y.get(1.0, 'end-1c')
                #print(f"{x} | {y.get(1.0, 'end-1c')}")
            except:
                parameters[x] = y
                #print(f'{x} {y}')
        
        modelname = f"{parameters['project name']}_{parameters['pipeline']}_epochs{parameters['epochs']}_batches{parameters['batches']}_{curtime}"
        print(modelname)

    def getPath(name, gridindex, directory=True):
        filepath = fd.askdirectory(title='select directory') if directory else fd.askopenfilename(title='select file')
        label = tk.Label(frame, text=filepath)
        label.grid(row=gridindex, column=2)
        widgets[name] = filepath

    def getDropdownInput(name, selection):
        widgets[name] = selection

    def create_txtinput(name, default, gridindex):
        label = tk.Label(frame, text=name)
        input = tk.Text(frame,
                        height = 1,
                        width = 8)
        input.insert('1.0', default)
        input.grid(row=gridindex,column=1)
        label.grid(row=gridindex, column=0)
        widgets[name] = input

    def create_dropinput(name, values, gridindex):
        # make dropdown menu for selecting pipeline
        label = tk.Label(frame, text= 'select ' + name)
        var = StringVar()
        var.set(value=values[0])
        var.trace_add('write', lambda *args: getDropdownInput(name=name, selection=var.get()))
        input = OptionMenu(frame, var, *values)
        input.grid(row=gridindex,column=1)
        label.grid(row=gridindex, column=0)
        widgets[name] = input

    def create_openfileinput(name, gridindex):
        label = tk.Label(frame, text=name)
        Input = tk.Button(frame, text='select', command=lambda: getPath(name=name, gridindex=gridindex, directory=False))
        Input.grid(row=gridindex,column=1)
        label.grid(row=gridindex,column=0)
        widgets[name] = input

    def create_openfolderinput(name, gridindex):
        label = tk.Label(frame, text=name)
        input = tk.Button(frame, text='select', command=lambda: getPath(name=name, gridindex=gridindex, directory=True))
        input.grid(row=gridindex,column=1)
        label.grid(row=gridindex,column=0)
        widgets[name] = input

    def createWidgets():
        create_openfolderinput(name='dataset', gridindex=0)
        create_openfileinput(name='hyperparameters', gridindex=1)
        create_openfileinput(name='cfg', gridindex=2)
        create_dropinput(name='pipeline', values=['YOLOv5', 'CNet', 'efficientdet'], gridindex=3)
        create_txtinput(name='batches', default='16', gridindex=4)
        create_txtinput(name='epochs', default='100', gridindex=5)
        create_txtinput(name='image size', default='512x512', gridindex=6)
        create_dropinput(name='device', values=['cpu', '0', '1', '-1'], gridindex=7)
        create_dropinput(name='optimizer', values=['SGD', 'Adam', 'AdamW'], gridindex=8)
        create_txtinput(name='workers', default='8', gridindex=9)
        create_txtinput(name='project name', default='name', gridindex=10)
        create_txtinput(name='patience', default='100', gridindex=11)
        create_txtinput(name='layers to freeze', default='non', gridindex=12)
        create_txtinput(name='save period', default='-1', gridindex=13)
        
        # start button creation
        runButton = tk.Button(frame,
                                text = "start", 
                                command = getInput)
        runButton.grid(row=15,column=1)
    
    createWidgets()
    frame.mainloop()

if __name__ == "__main__":
    main()