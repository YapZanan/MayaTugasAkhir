import os
import cv2 as cv
import time
import numpy as np
from datetime import datetime
from threading import Thread
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QLineEdit
from PyQt5.uic.properties import QtGui

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('GUI_TA.ui', self)

        self.path = None
        self.path2 = None
        self.data = None
        self.image = QImage()

        self.pushButton_Load_File_Calibrate.clicked.connect(self.load_file_calibrate_to_table)
        self.pushButton_Load_File_Distorted.clicked.connect(self.load_file_distorted_to_table)
        self.tableWidget_Tabel_File.clicked.connect(self.load_image_to_label_distorsi)
        # self.tableWidget_Tabel_File_Undistortion.clicked.connect(self.load_image_to_label_undistorsi)
        self.pushButton_Delete_File.clicked.connect(self.load_image_delete)
        # self.lineEdit_Rows.clicked.connect(self.input_rows)
        # self.lineEdit_Cols.clicked.connect(self.input_cols)
        self.pushButton_Start_Undistorted.clicked.connect(self.calibration)
        # self.listWidget_Progress.clicked.connect(self.load_file_to_listWidget)
        self.pushButton_Save.clicked.connect(self.save_file)

    def select_folder(self):
        path = QFileDialog.getExistingDirectory(self, 'Load File')
        return path

    def get_selected_file_path(self):
        row = self.tableWidget_Tabel_File.currentRow()
        cola = self.tableWidget_Tabel_File.currentColumn()
        data = self.tableWidget_Tabel_File.item(row, cola)
        text = data.text()
        if cola == 0:
            path_lengkap = self.path + "/" + str(text)
            print(self.path2)
        else:
            path_lengkap = self.path2 + "/" + str(text)
        print(path_lengkap)
        return path_lengkap