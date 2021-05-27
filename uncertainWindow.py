from PySimpleGUI.PySimpleGUI import Button, ToolTip, WIN_CLOSED, popup, theme_text_color
from configparser import ConfigParser
import PySimpleGUI as sg
import one_time



config = ConfigParser()
config.read(r'C:\Users\Utente\Desktop\Save password\Matrix file.ini')
user_name = config.get('SETTINGS', 'name')

se_count = 0

def uncertain_window():
    '''Uncertain window creator function'''

    global se_count
    global user_name
    

    layout = [
        [sg.Text(user_name, pad=((4 ,0), (0, 5)), font='Any 15')],
        [sg.Text('This program allows you to save your passwords in a csv sheet next to the respective apps where they will be used.', size=(55, 2))],
        [sg.Text('The file will be placed in an encrypted folder called "Save Password" on the desktop.', pad=((5, 0), (0, 0)))],
        [sg.Text('I recommend that you protect the app by hiding it. Since through the app you can read the passwords and possibly copy them.', 
        pad=((7, 0), (0, 0)), size=(60, 2))],
        [sg.Text('_' * 65, text_color='White')],
        [sg.Text('If you want to remove the window forever click ---> Once this is done click "Submit" to confirm.', size=(36, 2), pad=((5, 0), (18, 5))), 
        sg.Checkbox('Remove it', pad=((5, 0), (10, 10)), text_color='White', key='-R-')],
        [sg.Text('If you want to continue keeping the window just press "Submit".', pad=((5, 0), (5, 0)))],
        [sg.Button('Submit', tooltip='Confirm your settings', pad=((7, 0), (15, 0)))]
    ]
    
    window = sg.Window('Note', layout, enable_close_attempted_event=True, margins=(20, 20), resizable=False)
    
    while True:
        
        event, values = window.read()

        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == WIN_CLOSED) and sg.popup_yes_no('Do you really want to exit?', title=' ')== 'Yes':
            break

        elif values['-R-'] and event == 'Submit':

            se_count += 1

            config = ConfigParser()

            config['SETTINGS'] = {
                'count': one_time.count,
                'Second count' : se_count,
                'third count': one_time.th_count,
                'name': user_name
            }

            with open(r'C:\Users\Utente\Desktop\Save password\Matrix file.ini', 'r+') as file_ini:
                config.write(file_ini)

            break
        
        elif event == 'Submit':
            break

    window.close()
