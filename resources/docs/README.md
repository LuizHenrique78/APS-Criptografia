# APS Criptografia
 Programa que Criptograda e descriptografa um arquivo.
 
Bibliotecas ultilizadas.
 
pip install pysimplegui https://pysimplegui.readthedocs.io/en/latest/ 
pip install cryptography https://cryptography.io/en/latest/
 
 
Ultilização Encriptador

Execute o arquivo criptografar.py em alguma IDE, ou pelo prompt (vou deixar uma pasta dist com os arquivos em executavel).
Após executado abriraá uma tela do PYSimpleGUI com um INPUT, BrowserButton, EncriptButton e CaancelarButton.
BrowserButton: Busque um arquivo no seu computador;
EncriptButton: Faz a criptografia do arquivo escolhido e gera um arquivo KEY no diretorio chamado "filekey.key" (A cada execução essa chave é alterada)
Por fim gera o arquivo encriptado 
 
Ultilizaçao Desencriptar

Execute o arquivo descriptografar.py em alguma IDE, ou pelo prompt.(vou deixar uma pasta dist com os arquivos em executavel).
Após executado abriraá uma tela do PYSimpleGUI com um INPUT, BrowserButton, DecripttButton e CaancelarButton.
BrowserButton: Busque um arquivo (CRIPTOGRAFADO pelo criptografar.py) no seu computador;
DecriptButton: Faz a decriptografia do arquivo escolhido ultilizando o arquivo "filekey.key" gerado pelo encriptador.py
Por fim gera o arquivo desencriptografado.


 
