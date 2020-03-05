import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtCore import QFile
from form import Ui_MainWindow
import serial.tools.list_ports
from escpos.printer import Serial

def listar_porta_serial():
    portas = serial.tools.list_ports.comports()
    lista_portas = []

    for porta in portas:
        lista_portas.append(str(porta.device))

    return lista_portas

class Imprimir:

    def __init__(self, porta_serial):
        self.p = Serial(porta_serial)
        self.p.charcode("MULTILINGUAL")
        self.nome_serial = porta_serial

    def imprimir_texto(self, texto):
        self.p.text(str(texto))
        self.p.cut()

    def imprimir_imagem(self, imagem):
        self.p.image(str(imagem))
        self.p.cut()

    def imprimir_qr_code(self, texto):
        self.p.qr(str(texto))
        self.p.cut()

    def retornar_impressora(self):
        return str(self.nome_serial)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cb_impressoras.addItems(listar_porta_serial())
        self.ui.btn_conectar.clicked.connect(self.clicar_btn_conectar)
        self.ui.btn_imprimir_texto.clicked.connect(self.clicar_btn_imprimir_texto)
        self.ui.btn_imprimir_qr_code.clicked.connect(self.clicar_btn_imprimir_qr_code)
        self.ui.btn_buscar_imagem.clicked.connect(self.clicar_btn_buscar_imagem)
        self.ui.btn_imprimir_imagem.clicked.connect(self.clicar_btn_imprimir_imagem)

        self.impressao = None
        self.status_impressao = False

    def clicar_btn_conectar(self):
        if(self.ui.btn_conectar.text() == "Conectar"):
            nome_serial = self.ui.cb_impressoras.currentText()
            if(nome_serial == ""):
                pass
            else:
                self.ui.btn_atualizar.setEnabled(False)
                self.ui.cb_impressoras.setEnabled(False)
                self.ui.btn_conectar.setText("Desconectar")

                self.impressao = Imprimir(nome_serial)
                self.status_impressao = True

                self.ui.statusbar.showMessage(nome_serial + " conectado.")

        elif(self.ui.btn_conectar.text() == "Desconectar"):
            self.ui.btn_atualizar.setEnabled(True)
            self.ui.cb_impressoras.setEnabled(True)
            self.ui.btn_conectar.setText("Conectar")  

            self.status_impressao = False   

            self.ui.statusbar.showMessage("Desconectado.")   

    def clicar_btn_imprimir_texto(self):
        if(self.status_impressao == True):
            self.impressao.imprimir_texto(self.ui.ed_texto.toPlainText())    
        else:
            self.ui.statusbar.showMessage("Impressora não está conectada!")

    def clicar_btn_imprimir_imagem(self):
        if(self.status_impressao == True):
            if(self.ui.ed_imagem.text() == ""):
                pass
            else:
                self.impressao.imprimir_imagem(self.ui.ed_imagem.text())
        else:
            self.ui.statusbar.showMessage("Impressora não está conectada!")

    def clicar_btn_buscar_imagem(self):
        imagem = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.gif)")
        self.ui.ed_imagem.setText(str(imagem[0]))

    def clicar_btn_imprimir_qr_code(self):
        if(self.status_impressao == True):
            self.impressao.imprimir_qr_code(self.ui.ed_qr_code.toPlainText())    
        else:
            self.ui.statusbar.showMessage("Impressora não está conectada!")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
