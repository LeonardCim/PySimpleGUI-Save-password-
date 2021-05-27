import csv


def save():
    '''Function that saves the file with the passwords in another but visible'''

    try:

        lock_csv = r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv'
        unlock_csv = r'C:\Users\Utente\Desktop\Save password\Your_visible_file.csv'

        items_list = []

        with open(lock_csv, 'r', newline='') as oldfile:
            writer = csv.reader(oldfile)
            for row in writer:
                items_list.append(row)
            oldfile.close()

        with open(unlock_csv, 'w+', newline='') as newfile:
            writer = csv.writer(newfile)
            for row in items_list:
                writer.writerow(row)
            newfile.close()

    except Exception:
        pass





# # config = ConfigParser()
# #     config.read(r'C:\Users\Utente\Desktop\Save password\Matrix file.ini')
# #     name = config.get('SETTINGS', 'name')


# #     def select_window():
# #         '''Function with the main screen'''

# #         menu_def = [['Menu', ['Help', '---', 'Report bugs', '---','Exit']]]

# #         layout = [
# #             [sg.Menu(menu_def)],
# #             [sg.Text('Hello', font='Any 15', pad=((0, 5), (0, 5))), sg.Text(name, font='Any 15', pad=((0, 20), (0, 5)))],
# #             [sg.Frame(layout=[
# #             [sg.Text('This program has three functions:', text_color='White')],
# #             [sg.Text('The first allows you to save passwords in a file (you will receive more information by clicking on "Hide").', text_color='White')],
# #             [sg.Text('The second allows you to see the passwords you have saved (by clicking on "Reveal"). The saved passwords can be viewed only and exclusively through this application.', 
# #             size=(65, 2), text_color='White')],
# #             [sg.Text("So that anyone can't read your passwords by opening the file normally.", text_color='White')],
# #             [sg.Text('The third option ("Delete") allows you to delete a line of the file with passwords and apps.', text_color='White')],
# #             [sg.Text('Warning -', text_color='Red', pad=((5, 0), (0, 16))), sg.Text('Inside the folder there are two files called "Matrix file" and "key" which absolutely must not be MODIFIED !!!', size=(60, 2), text_color='White')]],
# #             title='Introduction', pad=((0, 0), (10, 0)) ,relief=sg.RELIEF_SUNKEN)],
# #             [sg.Button('Hide', pad=((0, 25), (20, 0)), tooltip='Enter a new password and app'), sg.Button('Reveal', pad=((0, 25), (20, 0)), tooltip='Show passwords'), sg.Button('Delete', pad=((0, 25), (20, 0))),
# #             sg.Button('Save', tooltip='Save passwords in a visible file', pad=((0, 25), (20, 0))), sg.Button('Exit', pad=((257, 0), (20, 0)), size=(10, 0))]
# #         ]

# #         window = sg.Window('Introductory note', layout, enable_close_attempted_event=True, margins=(20, 20), resizable=False)
        
# #         while True:
            
# #             event, values = window.read()

# #             if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == WIN_CLOSED) and sg.popup_yes_no('Do you really want to exit?', title=' ') == 'Yes':
# #                 break

# #             elif event == 'Hide':

# #                 window.close()
# #                 try:
# #                     if config.get('SETTINGS', 'Second count') == '0':
# #                         uncertain_window()
                    
# #                     elif config.get('SETTINGS', 'Second count') == '1':
# #                         pass

# #                 except Exception:
# #                     uncertain_window()
# #                     pass

# #                 password_creator()

# #                 try:
# #                     decrypt()
# #                 except Exception:
# #                     pass

# #                 insert()
# #                 crypt(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv')
# #                 break


# #             elif event == 'Reveal':
# #                 window.close()

# #                 try:

# #                     try:
# #                         decrypt()
# #                     except Exception:
# #                         pass

# #                     table_passwordApp()
# #                     crypt(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv')

# #                 except Exception:
# #                     sg.popup_error("I can't show anything if the file is empty... :-( - Restart the program", title='ERROR-004')
# #                     exit()
# #                 break
            
# #             elif event == 'Delete':
# #                 #decrypt()
# #                 #delete()
# #                 #crypt(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv')
# #                 pass

# #             elif event == 'Save':
# #                 pass
            
# #             elif event == 'Exit' and sg.popup_yes_no('Do you really want to exit?', title=' ') == 'Yes':
# #                 exit()
            
# #             elif event == 'Report bugs':
                
# #                 sg.popup('In case there are any problems or bugs, I invite you to write them on my Git hub profile -> "https://github.com/LeonardCim"', title='Need help?')
            
# #             elif event == 'Help':

# #                 sg.popup('''Hi, in this window you have two options:
# # click on "Hide" to save a new password; or click on "Reveal" to see the passwords.''', title='Help note')
            
# #         window.close()

# #     select_window()