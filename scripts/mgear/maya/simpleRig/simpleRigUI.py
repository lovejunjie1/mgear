# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/repo/mgear/scripts/mgear/maya/simpleRig/simpleRigUI.ui'
#
# Created: Tue Feb 20 11:48:35 2018
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.createRoot_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createRoot_pushButton.sizePolicy().hasHeightForWidth())
        self.createRoot_pushButton.setSizePolicy(sizePolicy)
        self.createRoot_pushButton.setObjectName("createRoot_pushButton")
        self.gridLayout_6.addWidget(self.createRoot_pushButton, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.createCtl_lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createCtl_lineEdit.sizePolicy().hasHeightForWidth())
        self.createCtl_lineEdit.setSizePolicy(sizePolicy)
        self.createCtl_lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.createCtl_lineEdit.setObjectName("createCtl_lineEdit")
        self.gridLayout_2.addWidget(self.createCtl_lineEdit, 1, 0, 1, 1)
        self.createCtl_pushButton = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.createCtl_pushButton.sizePolicy().hasHeightForWidth())
        self.createCtl_pushButton.setSizePolicy(sizePolicy)
        self.createCtl_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.createCtl_pushButton.setObjectName("createCtl_pushButton")
        self.gridLayout_2.addWidget(self.createCtl_pushButton, 3, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.side_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_comboBox.sizePolicy().hasHeightForWidth())
        self.side_comboBox.setSizePolicy(sizePolicy)
        self.side_comboBox.setObjectName("side_comboBox")
        self.side_comboBox.addItem("")
        self.side_comboBox.addItem("")
        self.side_comboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.side_comboBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.position_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_comboBox.sizePolicy().hasHeightForWidth())
        self.position_comboBox.setSizePolicy(sizePolicy)
        self.position_comboBox.setObjectName("position_comboBox")
        self.position_comboBox.addItem("")
        self.position_comboBox.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.position_comboBox)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.shape_comboBox = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shape_comboBox.sizePolicy().hasHeightForWidth())
        self.shape_comboBox.setSizePolicy(sizePolicy)
        self.shape_comboBox.setObjectName("shape_comboBox")
        self.shape_comboBox.addItem("")
        self.shape_comboBox.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.shape_comboBox)
        self.gridLayout_2.addLayout(self.formLayout_2, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.remove_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.remove_pushButton.setMinimumSize(QtCore.QSize(45, 50))
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.horizontalLayout.addWidget(self.remove_pushButton)
        self.add_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.add_pushButton.setMinimumSize(QtCore.QSize(45, 50))
        self.add_pushButton.setObjectName("add_pushButton")
        self.horizontalLayout.addWidget(self.add_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.selectAffected_pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.selectAffected_pushButton.setObjectName("selectAffected_pushButton")
        self.verticalLayout_2.addWidget(self.selectAffected_pushButton)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.editPivot_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.editPivot_pushButton.setObjectName("editPivot_pushButton")
        self.verticalLayout.addWidget(self.editPivot_pushButton)
        self.setPivot_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.setPivot_pushButton.setObjectName("setPivot_pushButton")
        self.verticalLayout.addWidget(self.setPivot_pushButton)
        self.reParentPivot_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.reParentPivot_pushButton.setObjectName("reParentPivot_pushButton")
        self.verticalLayout.addWidget(self.reParentPivot_pushButton)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.suffix_label = QtWidgets.QLabel(self.groupBox_5)
        self.suffix_label.setObjectName("suffix_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.suffix_label)
        self.autoBuild_lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.autoBuild_lineEdit.setObjectName("autoBuild_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.autoBuild_lineEdit)
        self.gridLayout_5.addLayout(self.formLayout, 0, 0, 1, 1)
        self.autoRig_pushButton = QtWidgets.QPushButton(self.groupBox_5)
        self.autoRig_pushButton.setObjectName("autoRig_pushButton")
        self.gridLayout_5.addWidget(self.autoRig_pushButton, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 282, 21))
        self.menubar.setObjectName("menubar")
        self.menuIO = QtWidgets.QMenu(self.menubar)
        self.menuIO.setObjectName("menuIO")
        self.menuConvert = QtWidgets.QMenu(self.menubar)
        self.menuConvert.setObjectName("menuConvert")
        self.menuDelete = QtWidgets.QMenu(self.menubar)
        self.menuDelete.setObjectName("menuDelete")
        MainWindow.setMenuBar(self.menubar)
        self.export_action = QtWidgets.QAction(MainWindow)
        self.export_action.setObjectName("export_action")
        self.import_action = QtWidgets.QAction(MainWindow)
        self.import_action.setObjectName("import_action")
        self.convertToShifterRig_action = QtWidgets.QAction(MainWindow)
        self.convertToShifterRig_action.setObjectName("convertToShifterRig_action")
        self.createShifterGuide_action = QtWidgets.QAction(MainWindow)
        self.createShifterGuide_action.setObjectName("createShifterGuide_action")
        self.deleteRig_action = QtWidgets.QAction(MainWindow)
        self.deleteRig_action.setObjectName("deleteRig_action")
        self.deletePivot_action = QtWidgets.QAction(MainWindow)
        self.deletePivot_action.setObjectName("deletePivot_action")
        self.menuIO.addAction(self.export_action)
        self.menuIO.addAction(self.import_action)
        self.menuIO.addSeparator()
        self.menuConvert.addAction(self.convertToShifterRig_action)
        self.menuConvert.addAction(self.createShifterGuide_action)
        self.menuDelete.addAction(self.deletePivot_action)
        self.menuDelete.addSeparator()
        self.menuDelete.addAction(self.deleteRig_action)
        self.menubar.addAction(self.menuIO.menuAction())
        self.menubar.addAction(self.menuConvert.menuAction())
        self.menubar.addAction(self.menuDelete.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.createRoot_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create Root", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Create Control", None, -1))
        self.createCtl_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Create CTL", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Side Label", None, -1))
        self.side_comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Center", None, -1))
        self.side_comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Left", None, -1))
        self.side_comboBox.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Right", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Position", None, -1))
        self.position_comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Center of Geometry", None, -1))
        self.position_comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Base of Geometry (Y axis =0 )", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Ctl Shape", None, -1))
        self.shape_comboBox.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Circle", None, -1))
        self.shape_comboBox.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Cube", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Elements", None, -1))
        self.remove_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.add_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.selectAffected_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Select Affected", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Pivot", None, -1))
        self.editPivot_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Edit Pivot", None, -1))
        self.setPivot_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Set Pivot", None, -1))
        self.reParentPivot_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Re-Parent Pivot", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("MainWindow", "Auto Rig", None, -1))
        self.suffix_label.setText(QtWidgets.QApplication.translate("MainWindow", "Suffix Rule", None, -1))
        self.autoBuild_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "geoRoot", None, -1))
        self.autoRig_pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Auto Build", None, -1))
        self.menuIO.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuConvert.setTitle(QtWidgets.QApplication.translate("MainWindow", "Convert", None, -1))
        self.menuDelete.setTitle(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.export_action.setText(QtWidgets.QApplication.translate("MainWindow", "Export Config", None, -1))
        self.import_action.setText(QtWidgets.QApplication.translate("MainWindow", "Import Config", None, -1))
        self.convertToShifterRig_action.setText(QtWidgets.QApplication.translate("MainWindow", "Convert to Shifter Rig", None, -1))
        self.createShifterGuide_action.setText(QtWidgets.QApplication.translate("MainWindow", "Create Shifter Guide", None, -1))
        self.deleteRig_action.setText(QtWidgets.QApplication.translate("MainWindow", "Delete Rig", None, -1))
        self.deletePivot_action.setText(QtWidgets.QApplication.translate("MainWindow", "Delete Pivot", None, -1))

