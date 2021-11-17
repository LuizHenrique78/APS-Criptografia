from cryptography.fernet import Fernet
import PySimpleGUI as sg

### Seta as configs da tela ###
sg.theme('Dark Blue 3')  

layout = [[sg.Text('Busque o arquivo para Encriptar')],
      [sg.Text('Navegar', size=(15, 3)), sg.InputText(), sg.FileBrowse()],
      [sg.Submit("Code"), sg.Cancel()]]

window = sg.Window('Encriptador', layout)
###  inicina o looping da tela ####
while True:
    event, values = window.read()
    print(event, values)
    
    if event == "Encriptar":
        key = Fernet.generate_key()
        
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)

        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        fernet = Fernet(key)
        ### inicia a cao encriptar tratando o erro dce enviar vazio ###
        if values[0] ==  '':
            sg.popup("Voce não Colocou nenhum arquivo.", "Feche o programa e execute de novo!")
            break
        else:
            with open(values[0], 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)

            with open(values[0], 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
                sg.popup("code feito com sucesso!", "Obrigado por utilizar!")
                break
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

window.close()



