from PySimpleGUI.PySimpleGUI import Button, ToolTip, WIN_CLOSED, popup, popup_error, theme_text_color
from cryptography.fernet import Fernet
from configparser import ConfigParser
import win32con, win32api
import PySimpleGUI as sg
from typing import Text
import csv
import os



#This script will only run once when the program starts

sg.theme('DarkAmber')

count = 0
se_count = 0
th_count = 0


while True:

    def folder_creator(folder_name):
        '''Creation function of the folder that contains the files'''

        global folder 

        desktop_path = r'C:\Users\Utente\Desktop'
        folder = os.path.join(desktop_path, folder_name)
        
        try:
            make_folder = os.mkdir(folder)
            
        except FileExistsError:
            sg.popup('''Careful, it seems that another folder has the same name as this one --> "Save password"
To make the program work correctly you have to change the name of the folder that already exists.''', title='ERROR-001', button_color='Red')
            exit()
        
        return make_folder, folder

    
    def create_csv(file_name):
        '''Creator function of the CSV file'''

        folder_path = r'C:\Users\Utente\Desktop\Save password'
        
        with open(os.path.join(folder_path, file_name + '.csv'), 'w+', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerow(['PASSWORD', 'SIGNAL', 'APP'])
            csv_file.close()

    
    def create_key():
        '''Function generates key'''

        global key

        key = Fernet.generate_key()
        return key


    def create_file_key():
        '''Folder generating function with key'''

        with open(r'C:\Users\Utente\Desktop\Save password\key.key', 'wb') as key_file:
            key_file.write(key)
            key_file.close()
        

    def userName():
        '''Function where to insert the name'''

        global user_name

        layout = [
            [sg.Text('Welcome!', font='Any 15', pad=((4, 0), (0, 15)), justification='center')],
            [sg.Text('Enter your name:'), sg.InputText('your name', text_color='white')],
            [sg.Button('Submit', pad=((7, 0), (15, 0)), size=(5, 0))]
        ]
        
        window = sg.Window('Introductory note', layout, enable_close_attempted_event=True, margins=(20, 20), resizable=False)
            
        while True:
            
            event, values = window.read()

            if event == 'Submit' and sg.popup_yes_no('Are you sure of the name you entered?', title='Note') == 'Yes':
                user_name = values[0]

                if user_name == 'your name':
                    popup_error('Enter a name :-)', title='Note')

                elif user_name == '':
                    popup_error('Enter a name :-)', title='Note')
                else:
                    break

        window.close()

        return user_name


    count += 1


    def ini():
        '''Ini file creation function'''

        config = ConfigParser()

        config['SETTINGS'] = {
            'count': count,
            'Second count' : se_count,
            'third count': th_count,
            'name': user_name
        }

        with open(os.path.join(folder, 'Matrix file.ini'), 'w+') as ini_file:
            config.write(ini_file)

    break



try:
    config = ConfigParser()
    config.read(r'C:\Users\Utente\Desktop\Save password\Matrix file.ini')
    
    if config.get('SETTINGS', 'count') == '1':
        pass

except Exception:
    folder_creator('Save password')
    create_csv('Your_password_file')
    create_key()
    create_file_key()
    userName()
    ini()




while True:

    def hidden_files():
        '''Function that hides the "key file" and the "Matrix file"'''

        key_file = r'C:\Users\Utente\Desktop\Save password\key.key'
        matrix_file = r'C:\Users\Utente\Desktop\Save password\Matrix file.ini'

        win32api.SetFileAttributes(key_file, win32con.FILE_ATTRIBUTE_HIDDEN)
        win32api.SetFileAttributes(matrix_file, win32con.FILE_ATTRIBUTE_HIDDEN)
    
    th_count += 1

    def ini_2():
        '''Second function for the ini file which will be executed only once. 
        Specifically, the "Key" and "Matrix file" are hidden'''

        config = ConfigParser()

        config['SETTINGS'] = {
            'count': count,
            'Second count' : se_count,
            'third count' : th_count,
            'name': user_name
        }

        with open(r'C:\Users\Utente\Desktop\Save password\Matrix file.ini', 'r+') as file_ini:
            config.write(file_ini)

    break 


config = ConfigParser()
config.read(r'C:\Users\Utente\Desktop\Save password\Matrix file.ini')

if config.get('SETTINGS', 'third count') == '1':
    pass

elif config.get('SETTINGS', 'third count') == '0':
    hidden_files()
    ini_2()



