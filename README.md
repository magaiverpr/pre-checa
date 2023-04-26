# pré-checa
Aplicativo em python para fazer checagens num PC. 


O objetivo primário é trazer as informações que um técnico de suporte precisa para fazer um diagnóstico rápido em alguns problemas na máquina alvo. Ele traz o hostname da máquina, qual o usuário que está logado no momento, o IP da máquina e faz testes de PING para IPs pertinentes ao nosso ambiente. Ele retorna se deu problema de ping em algum host. Também conseguimos rodar o GPUPDATE /FORCE ao clicar no botão da tela.


O objetivo secundário é usar o máximo possível do chatGPT pra gerar os códigos, com umas pitadas de buscas no Google quando ele dá aquela engasgada.


Para instalar os pacotes pips, siga o exemplo:

pip install auto-py-to-exe --trusted-host files.pythonhosted.org --trusted-host pypi.org --trusted-host pypi.python.org

Estou usando o auto-py-to-exe para converter para EXE.
