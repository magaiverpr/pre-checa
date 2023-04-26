import os
import platform
import subprocess
import socket
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QTabWidget

class CheckInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the tab widget and tabs
        tabs = QTabWidget()
        sys_tab = QWidget()
        net_tab = QWidget()
        tabs.addTab(sys_tab, "Principal")
        tabs.addTab(net_tab, "Network")

    
        # Create labels to display the check results
        desktop_label = QLabel(sys_tab)
        user_label = QLabel(sys_tab)
        ip_label = QLabel(sys_tab)
        ping_label_dns_conf = QLabel(sys_tab)
        ping_label_central = QLabel(sys_tab)
        ping_label_uad = QLabel(sys_tab)
        ping_label_confederacao = QLabel(sys_tab)
        ping_label_internet = QLabel(sys_tab)
        ips_label = QLabel(net_tab)
        interface_label = QLabel(net_tab)
        
        
        # Get the desktop name
        desktop = platform.node()
        desktop_label.setText(f"Nome do computador: {desktop}\n")

        # Get the logged in user name
        user = psutil.Process().username()
        user_label.setText(f"Usuário logado: {user}\n")

        # Get the IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        ip_label.setText(f"IP do computador: {ip_address}\n")
        
        
         # pegar todos os IPs e nomes de interfaces
        ip_addresses = []
        interface_names = []
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ip_addresses.append(addr.address)
                    interface_names.append(interface)
        ips_label.setText(f"IPs do computador:\n {', '.join(ip_addresses)}")
        ips_label.setWordWrap(True)
        interface_label.setText(f"Interfaces de rede:\n {', '.join(interface_names)}")
        interface_label.setWordWrap(True)
        
        
        # Teste de DNS
        ping_result = subprocess.run(['ping', '-n', '1', 'sisbr.coop.br'], stdout=subprocess.PIPE)
        if "Resposta de 172.16.1.140: bytes=" in str(ping_result.stdout):
            ping_label_dns_conf.setText("\n Teste de DNS - Confederação: OK\n")
            ping_label_dns_conf.setStyleSheet("color: white;"
                        "background-color: green;"
                        "selection-color: green;"
                        "selection-background-color: white;")
        else:
            ping_label_dns_conf.setText("\nTeste de DNS - Confederação: FALHA\n")
            ping_label_dns_conf.setStyleSheet("color: black;"
                        "background-color: red;"
                        "selection-color: red;"
                        "selection-background-color: white;")

        # Ping the IP 10.209.4.10 and display the result
        ping_result = subprocess.run(['ping', '-n', '1', '10.209.4.10'], stdout=subprocess.PIPE)
        if "Resposta de 10.209.4.10: bytes=" in str(ping_result.stdout):
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
        ping_result = subprocess.run(['ping', '-n', '1', '131.108.146.241'], stdout=subprocess.PIPE)
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
                        
        # Ping para UAD
        ping_result = subprocess.run(['ping', '-n', '1', '10.210.137.246'], stdout=subprocess.PIPE)
        if "Resposta de" in str(ping_result.stdout):
            ping_label_uad.setText("\nComunicação com UAD: OK\n")
            ping_label_uad.setStyleSheet("color: white;"
                        "background-color: green;"
                        "selection-color: green;"
                        "selection-background-color: white;")
        else:
            ping_label_uad.setText("\nComunicação com UAD: FALHA\n")
            ping_label_uad.setStyleSheet("color: black;"
                        "background-color: red;"
                        "selection-color: red;"
                        "selection-background-color: white;")
            

            # Create a button to run gpupdate /force
        button_gpupdate = QPushButton(net_tab)
        button_gpupdate.setText("Atualizar políticas de grupo (gpupdate /force)")   
        button_gpupdate.clicked.connect(self.run_gpupdate)


 #aba principal
        sys_layout = QVBoxLayout(sys_tab)
        sys_layout.addWidget(desktop_label)
        sys_layout.addWidget(user_label)
        sys_layout.addWidget(ip_label)
        sys_layout.addWidget(ping_label_dns_conf)
        sys_layout.addWidget(ping_label_central)
        sys_layout.addWidget(ping_label_uad)
        sys_layout.addWidget(ping_label_confederacao)
        sys_layout.addWidget(ping_label_internet)
        sys_layout.addWidget(button_gpupdate)

#aba Network
        net_layout = QVBoxLayout(net_tab)
        net_layout.addWidget(ips_label)
        net_layout.addWidget(interface_label)

        # Set the layout and window properties
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        self.setLayout(vbox)
        self.setWindowTitle("Pré-checa Unicoob - 4351")
        self.setGeometry(100, 100, 300, 150)
        self.show()
        
    def run_gpupdate(self):
        subprocess.run(['gpupdate', '/force'])

        
if __name__ == '__main__':
    app = QApplication([])
    window = CheckInfo()
    app.exec_()
