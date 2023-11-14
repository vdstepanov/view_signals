import sys

from random import randint

import numpy as np
import matplotlib.pyplot as plt

import csv

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QListWidget,\
     QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QAction,\
     QFileDialog, QAbstractItemView, QPlainTextEdit, QTextEdit, QScrollArea,\
     QGridLayout, QTabWidget

width = 1200
height = 880

class TabGraph:
    def __init__(self, text):
        self.graph_widget = QWidget()
        # self.graph_widget.setStyleSheet('background-color: grey')
        self.graph_widget_layout = QHBoxLayout()

        # устанавливаем размер graph_widget
        self.graph_widget.setFixedSize(1050, 460)

        self.left_graph_widget = QTabWidget()

        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout()
        self.tab1_label = QLabel("Tab1 label " + text)
        self.tab1_layout.addWidget(self.tab1_label)
        self.tab1.setLayout(self.tab1_layout)

        self.left_graph_widget.addTab(self.tab1, "Tab 1")





        self.right_graph_widget = QWidget()

        self.right_graph_widget_layout = QVBoxLayout()
        self.right_graph_widget.setLayout(self.right_graph_widget_layout)

        self.graph_button_add_signal = QPushButton(text="Add signal")
        self.right_graph_widget_layout.addWidget(self.graph_button_add_signal)

        self.graph_button_set_axes = QPushButton(text="Set axes")
        self.right_graph_widget_layout.addWidget(self.graph_button_set_axes)

        self.graph_button_add_tab = QPushButton(text="Add tab")
        self.right_graph_widget_layout.addWidget(self.graph_button_add_tab)
        self.graph_button_add_tab.clicked.connect(self.add_new_tab)

        self.right_graph_widget_layout.addStretch()


        self.graph_widget_layout.addWidget(self.left_graph_widget)
        self.graph_widget_layout.addWidget(self.right_graph_widget)


        self.graph_widget.setLayout(self.graph_widget_layout)

    def add_new_tab(self):
        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout()
        self.tab2_label = QLabel("Tab2 label " + str(randint(0, 100)))
        self.tab2_layout.addWidget(self.tab2_label)
        self.tab2.setLayout(self.tab2_layout)
        self.left_graph_widget.addTab(self.tab2, "Tab 2")




class MainWindow(QMainWindow):



    def __init__(self):
        super().__init__()
        self.lst_graphs = []
        self.initUI()


    def initUI(self):

        self.setGeometry(10, 40, width, height)
        self.setMaximumWidth(width)
        self.setMaximumHeight(height)

        # Устанавливаем центральный виджет-контейнер
        self.centralwidget = QWidget()
        self.main_layout = QHBoxLayout()


        # Устанавливаем левый и правый виджеты центрального виджета
        self.right_widget = QWidget()
        self.left_widget = QScrollArea()
        self.main_layout.addWidget(self.left_widget)
        self.main_layout.addWidget(self.right_widget)



        self.scroll_widget = QWidget()

        self.scroll_widget_layout = QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_widget_layout)

        self.right_widget_layout = QVBoxLayout()
        self.right_widget.setLayout(self.right_widget_layout)






        self.button_open_shot = QPushButton(text="Open shot")
        self.right_widget_layout.addWidget(self.button_open_shot)

        self.button_add_graph = QPushButton(text="Add graph")
        self.right_widget_layout.addWidget(self.button_add_graph)
        self.button_add_graph.clicked.connect(self.add_new_graph)

        self.right_widget_layout.addStretch()


        w1 = TabGraph("1111")

        self.lst_graphs.append(w1)

        self.scroll_widget_layout.addWidget(w1.graph_widget)

        self.scroll_widget_layout.addStretch()


        self.left_widget.setWidgetResizable(True)
        # left_widget.resize(200, 200)


        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        self.left_widget.setWidget(self.scroll_widget)



        self.centralwidget.setLayout(self.main_layout)
        self.setCentralWidget(self.centralwidget)

    def add_new_graph(self):



        w1 = TabGraph(str(randint(0, 100)))

        self.lst_graphs.append(w1)

        self.scroll_widget_layout.addWidget(w1.graph_widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
