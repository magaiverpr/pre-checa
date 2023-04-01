import os
import platform
import subprocess
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class CheckInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create labels to display the check results
        desktop_label = QLabel()
        user_label = QLabel()
        ip_label = QLabel()
        ping_label_central = QLabel()
        ping_label_confederacao = QLabel()
        ping_label_internet = QLabel()
        
        # Get the desktop name
        desktop = platform.node()
        desktop_label.setText(f"Nome do computador: {desktop}\n")

        # Get the logged in user name
        user = os.getlogin()
        user_label.setText(f"Usuário logado: {user}\n")

        # Get the IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        ip_label.setText(f"IP do computador: {ip_address}\n")

        # Ping the IP 10.209.4.10 and display the result
        ping_result = subprocess.run(['ping', '-n', '1', '10.209.4.10'], stdout=subprocess.PIPE)
        if "Resposta de" in str(ping_result.stdout):
            ping_label_central.setText("\n Comunicação com UNICOOB: OK\n")
            ping_label_central.setStyleSheet("color: white;"
                        "background-color: green;"
                        "selection-color: green;"
                        "selection-background-color: white;")
        else:
            ping_label_central.setText("\nComunicação com UNICOOB: FALHA\n")
            ping_label_central.setStyleSheet("color: black;"
                        "background-color: red;"
                        "selection-color: red;"
                        "selection-background-color: white;")
            
         # Ping the IP 172.16.2.188 and display the result
        ping_result = subprocess.run(['ping', '-n', '1', '172.16.2.188'], stdout=subprocess.PIPE)
        if "Resposta de" in str(ping_result.stdout):
            ping_label_confederacao.setText("\nComunicação com Confederação: OK\n")
            ping_label_confederacao.setStyleSheet("color: white;"
                        "background-color: green;"
                        "selection-color: green;"
                        "selection-background-color: white;")
        else:
            ping_label_confederacao.setText("\nComunicação com Confederação: FALHA\n")
            ping_label_confederacao.setStyleSheet("color: black;"
                        "background-color: red;"
                        "selection-color: red;"
                        "selection-background-color: white;")

         # Ping the IP 131.108.146.241 and display the result
        ping_result = subprocess.run(['ping', '131.108.146.241'], stdout=subprocess.PIPE)
        if "Resposta de" in str(ping_result.stdout):
            ping_label_internet.setText("\nComunicação com Internet: OK\n")
            ping_label_internet.setStyleSheet("color: white;"
                        "background-color: green;"
                        "selection-color: green;"
                        "selection-background-color: white;")
        else:
            ping_label_internet.setText("\nComunicação com Internet: FALHA\n")
            ping_label_internet.setStyleSheet("color: black;"
                        "background-color: red;"
                        "selection-color: red;"
                        "selection-background-color: white;")
            

            # Create a button to run gpupdate /force
        button_gpupdate = QPushButton("Atualizar políticas de grupo (gpupdate /force)")
        button_gpupdate.clicked.connect(self.run_gpupdate)

        # Add the labels to the layout
        vbox = QVBoxLayout()
        vbox.addWidget(desktop_label)
        vbox.addWidget(user_label)
        vbox.addWidget(ip_label)
        vbox.addWidget(ping_label_central)
        vbox.addWidget(ping_label_confederacao)
        vbox.addWidget( ping_label_internet)
        vbox.addWidget(button_gpupdate)

        # Set the layout and window properties
        self.setLayout(vbox)
        self.setWindowTitle("Pré-checa Unicoob")
        self.setGeometry(100, 100, 300, 150)
        self.show()
        
    def run_gpupdate(self):
        subprocess.run(['gpupdate', '/force'])

        
if __name__ == '__main__':
    app = QApplication([])
    window = CheckInfo()
    app.exec_()
