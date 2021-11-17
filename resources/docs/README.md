# APS Criptografia

Alunos - 

Henry Yujra Espejo – RA: 21309076

Luiz Henrique da Silva Rodrigues – RA: 21438729

Rodrigo Loterio Silva – RA: 21300031

Vinicius Marques Gallichio – RA: 21502361


# Programa que Criptograda e descriptografa um arquivo.
 
# Bibliotecas ultilizadas.
 
pip install pysimplegui  https://pysimplegui.readthedocs.io/en/latest/ 
pip install cryptography https://cryptography.io/en/latest/
 
 
# Ultilização Encriptador

    Execute o arquivo criptografar.py em alguma IDE, ou pelo prompt (vou deixar uma pasta dist com os arquivos em executavel).
    Após executado abriraá uma tela do PYSimpleGUI com um INPUT, BrowserButton, CodeButton e ExitButton.
    BrowserButton: Busque um arquivo no seu computador;
    CodeButton: Faz a criptografia do arquivo escolhido e gera um arquivo KEY no diretorio chamado "filekey.key" (A cada execução essa chave é alterada), portanto salvar essa chave a cada encriptação!!
    Por fim gera o arquivo encriptado.
 
# Ultilizaçao Desencriptar

    Execute o arquivo descriptografar.py em alguma IDE, ou pelo prompt.(vou deixar uma pasta dist com os arquivos em executavel).
    Após executado abriraá uma tela do PYSimpleGUI com um INPUT, BrowserButton, DecodeButton e CaancelarButton.
    BrowserButton: Busque um arquivo (CRIPTOGRAFADO pelo criptografar.py) no seu computador;
    DecodeButton: Faz a decriptografia do arquivo escolhido ultilizando o arquivo "filekey.key" gerado pelo encriptador.py, ou ultilizando uma key salva para determinado documento.
    Por fim gera o arquivo desencriptografado.


 
