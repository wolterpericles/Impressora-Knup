# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(534, 588)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_impressora = QLabel(self.centralwidget)
        self.lb_impressora.setObjectName(u"lb_impressora")

        self.verticalLayout.addWidget(self.lb_impressora)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_impressoras = QComboBox(self.centralwidget)
        self.cb_impressoras.setObjectName(u"cb_impressoras")

        self.horizontalLayout.addWidget(self.cb_impressoras)

        self.btn_atualizar = QPushButton(self.centralwidget)
        self.btn_atualizar.setObjectName(u"btn_atualizar")

        self.horizontalLayout.addWidget(self.btn_atualizar)

        self.btn_conectar = QPushButton(self.centralwidget)
        self.btn_conectar.setObjectName(u"btn_conectar")

        self.horizontalLayout.addWidget(self.btn_conectar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lb_texto = QLabel(self.centralwidget)
        self.lb_texto.setObjectName(u"lb_texto")

        self.verticalLayout.addWidget(self.lb_texto)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ed_texto = QPlainTextEdit(self.centralwidget)
        self.ed_texto.setObjectName(u"ed_texto")

        self.horizontalLayout_3.addWidget(self.ed_texto)

        self.btn_imprimir_texto = QPushButton(self.centralwidget)
        self.btn_imprimir_texto.setObjectName(u"btn_imprimir_texto")

        self.horizontalLayout_3.addWidget(self.btn_imprimir_texto)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.lb_imagem = QLabel(self.centralwidget)
        self.lb_imagem.setObjectName(u"lb_imagem")

        self.verticalLayout.addWidget(self.lb_imagem)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ed_imagem = QLineEdit(self.centralwidget)
        self.ed_imagem.setObjectName(u"ed_imagem")

        self.horizontalLayout_2.addWidget(self.ed_imagem)

        self.btn_buscar_imagem = QPushButton(self.centralwidget)
        self.btn_buscar_imagem.setObjectName(u"btn_buscar_imagem")

        self.horizontalLayout_2.addWidget(self.btn_buscar_imagem)

        self.btn_imprimir_imagem = QPushButton(self.centralwidget)
        self.btn_imprimir_imagem.setObjectName(u"btn_imprimir_imagem")

        self.horizontalLayout_2.addWidget(self.btn_imprimir_imagem)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lb_qr_code = QLabel(self.centralwidget)
        self.lb_qr_code.setObjectName(u"lb_qr_code")

        self.verticalLayout.addWidget(self.lb_qr_code)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ed_qr_code = QPlainTextEdit(self.centralwidget)
        self.ed_qr_code.setObjectName(u"ed_qr_code")

        self.horizontalLayout_4.addWidget(self.ed_qr_code)

        self.btn_imprimir_qr_code = QPushButton(self.centralwidget)
        self.btn_imprimir_qr_code.setObjectName(u"btn_imprimir_qr_code")

        self.horizontalLayout_4.addWidget(self.btn_imprimir_qr_code)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Impressora Knup", None))
        self.lb_impressora.setText(QCoreApplication.translate("MainWindow", u"Impressora", None))
        self.btn_atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.btn_conectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.lb_texto.setText(QCoreApplication.translate("MainWindow", u"Texto", None))
        self.btn_imprimir_texto.setText(QCoreApplication.translate("MainWindow", u"Imprimir Texto", None))
        self.lb_imagem.setText(QCoreApplication.translate("MainWindow", u"Imagem", None))
        self.btn_buscar_imagem.setText(QCoreApplication.translate("MainWindow", u"Buscar Imagem ", None))
        self.btn_imprimir_imagem.setText(QCoreApplication.translate("MainWindow", u"Imprimir Imagem", None))
        self.lb_qr_code.setText(QCoreApplication.translate("MainWindow", u"QR Code", None))
        self.btn_imprimir_qr_code.setText(QCoreApplication.translate("MainWindow", u"Imprimir QR Code", None))
    # retranslateUi

