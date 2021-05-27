from PySimpleGUI.PySimpleGUI import Button, ToolTip, WIN_CLOSED, popup, theme_text_color
from configparser import ConfigParser
import PySimpleGUI as sg
from typing import Text



pass_list = []
app_list = []


def password_creator():
    '''Creator function of the window with the options to enter the password and the app'''


    menu_def = [['Menu', ['Help', '---', 'Report bugs', '---','Exit']]]


    layout = [
                [sg.Menu(menu_def)],
                [sg.Text('Enter your password and app', size=(30, 1), pad=((110, 1), (5, 10)), justification="center", font='Any 15')],
                [sg.Text('Password', tooltip='Enter your password')],
                [sg.Input(key='-IN-', tooltip='Enter your password', text_color='white')],
                [sg.Text('App', tooltip='Enter the App', pad=((5, 0), (15, 2)))],
                [sg.Input(key='-2IN-', tooltip='Enter the App', text_color='white')],
                [sg.Text('Your password:', pad=((5, 1), (15, 0))), sg.Text(size=(35, 1), pad=((1, 1), (15, 0)), key='-OUT-')],
                [sg.Text('Your app:', pad=((5, 1), (15, 0))), sg.Text(size=(35, 1), pad=((1, 1), (15, 0)), key='-2OUT-')],
                [sg.Text('_' * 70)],
                [sg.Frame(layout=[
                [sg.Text('Press "Continue" to move forward. Or "Rewrite" to start over. Then click "ok"', text_color='white', justification="center",  size=(60, 1))],
                [sg.Checkbox('Continue', size=(10, 1), key='-v-'),  sg.Checkbox('Rewrite', key='-x-')]], 
                title='Options', relief=sg.RELIEF_SUNKEN, pad=((5, 0), (15, 0)))],

                [sg.Button('Ok', pad=((5, 20), (25, 0)), tooltip='Confirm the options entered'), 
                sg.Button('Close', pad=((0, 20), (25, 0)), tooltip='Continue with the program'), sg.Button('Exit', pad=((1, 1), (25, 0)), tooltip='Close the program'), 
                sg.Text('Click "Close" to continue or "Exit" to close the program.', pad=((25, 0),(25, 0)), size=(45, 1), justification="center", text_color='white')] ]

    window = sg.Window('Save Password', layout, enable_close_attempted_event=True, margins=(20, 20), resizable=True)


    while True:

        event, values = window.read()
        
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit' or event == WIN_CLOSED) and sg.popup_yes_no('Do you really want to exit?', title=' ') == 'Yes':
            exit()

        elif values['-x-'] and values['-v-'] and event == 'Ok':
            sg.popup('You cannot fill in two fields at the same time', title='ERROR-003', button_color='Red')
            window.refresh()
        
        elif values['-x-'] and values['-v-'] and event == "Close":
            sg.popup('You cannot fill in two fields at the same time', title='ERROR-003', button_color='Red')
            window.refresh()

        elif  values['-v-'] and event == 'Ok':
            window['-OUT-'].update(values['-IN-'], text_color = 'white')
            window['-2OUT-'].update(values['-2IN-'], text_color = 'white')

        elif event == 'Close' and sg.popup_yes_no('Do you really want to continue?') == 'Yes':
            pass_list.append(values['-IN-'])
            app_list.append(values['-2IN-'])
            window.refresh()
            break

        elif values['-x-'] and event == 'Ok':
            window['-OUT-'].update(values['-IN-'], text_color = 'white')
            window['-2OUT-'].update(values['-2IN-'], text_color = 'white')
            window.FindElement('-IN-').Update('')
            window.FindElement('-2IN-').Update('')
        
        elif event == 'Report bugs':

            sg.popup('In case there are any problems or bugs, I invite you to write them on my Git hub profile -> "https://github.com/LeonardCim"', title='Need help?')
        
        elif event == 'Help':

            sg.popup('''Hello, here you will find all the instructions: Once you have entered the password and the app go to "Options" and choose the parameter ("Continue" or "Rewrite") 
then click "Ok" to confirm. Once this is done click "Close" to continue the program, or "Exit" to exit. If you want to skip the "options" point, press "Close" to enter the data immediately. 
Careful, clicking "Exit" the data will not be saved.''', title='Help note')


    window.close()

    return pass_list, app_list
