import sys

import numpy as np
import matplotlib.pyplot as plt

import csv

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QListWidget,\
     QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QAction,\
     QFileDialog, QAbstractItemView, QPlainTextEdit, QTextEdit


class Signal:
    def __init__(self, name, xdata, ydata):
        self.name = name
        self.xmin = min(xdata)
        self.xmax = max(xdata)
        self.ymin = min(ydata)
        self.ymax = max(ydata)
        self.npoints = len(xdata)
        self.x = np.array(xdata)
        self.y = np.array(ydata)


def read_csv_data(filename, delimiter=',', before_pass=0, after_pass=0, encoding='utf-8'):
    lst_signals = []
    try:
        with open(filename, encoding=encoding) as r_file:
            file_reader = csv.reader(r_file, delimiter=delimiter)

            # пропускаем строки вначале файла
            while before_pass > 0:
                before_pass -= 1
                file_reader.__next__()

            # считываем именна сигналов
            lst_name_signals = file_reader.__next__()
            # print(f"сигналы : {lst_name_signals}")

            # пропускаем строки после считывание строки с названиями сигналов
            while after_pass > 0:
                after_pass -= 1
                file_reader.__next__()

            # инициализируем массивы для данных
            lst_ydata = [[] for i in range(len(lst_name_signals)-1)]
            xdata = []

            # считываем данные в массивы из файла (при конвертации в число заменяем "," на ".")
            for data in file_reader:
                xdata.append(float(data[0].replace(',','.')))
                for idx in range(len(lst_name_signals)-1):
                    lst_ydata[idx].append(float(data[idx + 1].replace(',', '.')))

            # на основе массивов данных создаем экземпляры сигналов (класс Signal) и помещаем их в список сигналов lst_signals
            for i, name in enumerate(lst_name_signals):
                if i != 0:
                    signal = Signal(name, xdata, lst_ydata[i - 1])
                    lst_signals.append(signal)

            signal1 = lst_signals[3]
            print(signal1.name)
            # print(signal1.x)
            # print(signal1.y)
            print(f" xmin - {signal1.xmin}")
            print(f" xmax - {signal1.xmax}")
            print(f" ymin = {signal1.ymin}")
            print(f" ymax = {signal1.ymax}")
            print(f" npoints = {signal1.npoints}")
    except:
        print(f"Ошибка при считывании данных из файла {filename}")

    return lst_signals


lst_signals = read_csv_data("geter.8066", delimiter='\t', before_pass=0, after_pass=1)



