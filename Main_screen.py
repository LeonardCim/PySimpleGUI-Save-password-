from PySimpleGUI.PySimpleGUI import Button, ToolTip, WIN_CLOSED, popup, theme_text_color
from configparser import ConfigParser
import table_passwordApp as tp
import password_creator as pc
import uncertainWindow as uw
import PySimpleGUI as sg
import file_delete as fd
import insert_file as fi
import save_file as sf
import encrypt as ey
import decrypt as dy
import one_time
import pandas




if __name__=="__main__":
    
    while True:

        config = ConfigParser()
        config.read(r'C:\Users\Utente\Desktop\Save password\Matrix file.ini')
        user_name = config.get('SETTINGS', 'name')


        def select_window():
            '''Function with the main screen'''

            menu_def = [['Menu', ['Help', '---', 'Report bugs', '---', 'Info', '---','Exit']]]

            layout = [
                [sg.Menu(menu_def)],
                [sg.Text('Hello', font='Any 15', pad=((0, 5), (0, 5))), sg.Text(user_name, font='Any 15', pad=((0, 20), (0, 5)))],
                [sg.Frame(layout=[
                [sg.Text('This program has four functions:', text_color='White')],
                [sg.Text('The first allows you to save passwords in a file (you will receive more information by clicking on "Hide").', text_color='White')],
                [sg.Text('The second allows you to see the passwords you have saved (by clicking on "Reveal"). The saved passwords can be viewed only and exclusively through this application.', 
                size=(65, 2), text_color='White')],
                [sg.Text("So that anyone can't read your passwords by opening the file normally.", text_color='White')],
                [sg.Text('The third option ("Delete") allows you to delete a line of the file with passwords and apps.', text_color='White')],
                [sg.Text('The fourth option allows you to save passwords in a file that is visible (to all).', text_color='White')],
                [sg.Text('Warning -', text_color='Red', pad=((5, 0), (0, 16))), sg.Text('Inside the folder there are two files called "Matrix file" and "key" which absolutely must not be MODIFIED !!! - For more information go to "Info" in the menu.', 
                size=(60, 2), text_color='White')]],
                title='Introduction', pad=((0, 0), (10, 0)) ,relief=sg.RELIEF_SUNKEN)],
                [sg.Button('Hide', pad=((0, 25), (20, 0)), tooltip='Enter a new password and app'), sg.Button('Reveal', pad=((0, 25), (20, 0)), tooltip='Show passwords'), sg.Button('Delete', pad=((0, 25), (20, 0))),
                sg.Button('Save', tooltip='Save passwords in a visible file', pad=((0, 25), (20, 0))), sg.Button('Exit', pad=((257, 0), (20, 0)), size=(10, 0))]
            ]

            window = sg.Window('Introductory note', layout, enable_close_attempted_event=True, 
            margins=(20, 20), resizable=True)
            
            while True:
                
                event, values = window.read() 

                if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == WIN_CLOSED) and sg.popup_yes_no('Do you really want to exit?', title=' ') == 'Yes':
                    exit()
                
                elif event == 'Hide':

                    window.close()
                    try:
                        if config.get('SETTINGS', 'Second count') == '0':
                            uw.uncertain_window()
                        
                        elif config.get('SETTINGS', 'Second count') == '1':
                            pass

                    except Exception:
                        uw.uncertain_window()
                        pass

                    pc.password_creator()

                    try:
                        dy.decrypt()
                    except Exception:
                        pass

                    fi.insert()
                    ey.crypt(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv')
                    
                    break


                elif event == 'Reveal':
                    window.close()

                    try:

                        try:
                            dy.decrypt()
                        except Exception:
                            pass

                        tp.table_passwordApp()
                        ey.crypt(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv')

                    except Exception:
                        sg.popup("I can't show anything if the file is empty... :-(", title='Note')
                        pass
                    
                    break
                
                elif event == 'Delete':
                    window.close()

                    try:
                        dy.decrypt()
                        fd.delete()
                        ey.crypt(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv')

                    except Exception:
                        sg.popup("I can't delete anything if the file is empty.", title='Note')
                        pass

                    break

                elif event == 'Save':

                    dy.decrypt()
                    sf.save()
                    ey.crypt(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv')
                    exit()

                elif event == 'Help':

                    sg.popup('''Hi, in this window you have four options:
click on "Hide" to save a new password; click on "Reveal" to see the passwords; click on "Delete" to delete a password; 
or click on "Save" to save the passwords in another file (always csv) but visible to all.''', title='Help note')

                elif event == 'Report bugs':
                    
                    sg.popup('In case there are any problems or bugs, I invite you to write them on my Git hub profile -> "https://github.com/LeonardCim"', title='Need help?')
                
                elif event == 'Info':

                    sg.popup('''"Matrix file" and "Key" are very important files because they allow the program to work correctly and modifying them would lead to many errors. 
Specifically, the "Key" file is used to encrypt and decrypt files. While the "Master File" manages the creation of the folder and files.
For safety the files are hidden, but in case you want to take a look at them here I show you the instructions to find the two files ->
Open the "Save password" folder and at the top you should see the following options: "File"; "Home"; "Share" and "View". 
Click on "View" and go to "Hidden items" on the right. After you click on it you should see the two hidden files.
''', title='Info')
                
                elif event == 'Exit' and sg.popup_yes_no('Do you really want to exit?', title=' ') == 'Yes':
                    exit()
                
                
            window.close()

        select_window()


