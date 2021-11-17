from cryptography.fernet import Fernet
import PySimpleGUI as sg

### seta as configuracoes da tela ###
sg.theme('Dark Blue 3')  

layout = [[sg.Text('Busque o arquivo para Desencriptar')],
      [sg.Text('Navegar', size=(15, 3)), sg.InputText(), sg.FileBrowse()],
      [sg.Submit("Decode"), sg.Cancel()]]

window = sg.Window('Desencriptador', layout)


### Inicia o loopgin da tela###
while True:
    event, values = window.read()
    if event == "Desencriptar":
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        fernet = Fernet(key)
        ### Inicia o Desencriptar tratando o erro de enviar vazio ####
        if values[0] == "":
            sg.popup("Voce não Colocou nenhum arquivo.", "Feche o programa e execute de novo!")
            break
        else:
            with open(values[0], 'rb') as enc_file:
                encrypted = enc_file.read()
            
            decrypted = fernet.decrypt(encrypted)
            
            with open(values[0], 'wb') as dec_file:
                dec_file.write(decrypted)
                sg.popup("decode feito com sucesso!", "Obrigado por utilizar!")
                break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

