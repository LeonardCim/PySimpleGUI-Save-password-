from PySimpleGUI.PySimpleGUI import Button, ToolTip, WIN_CLOSED, popup, theme_text_color
import PySimpleGUI as sg
import pandas as pd
import csv



def delete():
    '''Function that allows you to delete a password inside the csv file'''

    sg.set_options(auto_size_buttons=True)
    csv_filename = r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv'

    data = []
    header_list = []

    df = pd.read_csv(csv_filename, sep=',', engine='python', header=None)
    data = df.values.tolist()               
                    
    header_list = df.iloc[0].tolist()
    data = df[1:].values.tolist()

    layout = [
        [sg.Text('Enter the name of the password you want to delete.', pad=((15, 0), (10, 5)))],
        [sg.Text('Enter the password name:', pad=((15, 0), (5, 0))), sg.Input(key='-D-',tooltip='Enter the password you want to delete', text_color='White', pad=((5, 0), (5, 0))), 
        sg.Button('Ok', pad=((10, 0), (5, 0)), size=(2, 0))],
        [sg.Text('The victim:', pad=((15, 0), (15, 0))), sg.Text(key='-E-', size=(40, 0), pad=((5, 0), (15, 0)), text_color='white')],
        [sg.Button('Close', pad=((17, 0), (20, 0)), tooltip='Press "Close" to finish and save the data.', size=(4, 0))],
        [sg.Text('_' * 75, pad=((15, 0), (0, 0)), text_color='White')],
        [sg.Table(values=data,
                  headings=header_list,
                  key='_TABLE_',
                  justification='left',
                  display_row_numbers=True,
                  auto_size_columns=True,
                  num_rows=min(100, len(data)), pad=((15, 0), (10, 0)))]
        
    ]

    window = sg.Window(resizable=True, 
        title="Password and app table",
        layout=layout,
        margins=(1, 1),
        size=(560, 300),
        finalize=True
    )

    window['_TABLE_'].expand(True, True)
    window['_TABLE_'].table_frame.pack(expand=True, fill='both')

    while True:

        event, values = window.read()
        
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == WIN_CLOSED):
            break

        elif event == 'Ok':
            window.refresh()
            window['-E-'].update(values['-D-'], text_color = 'white')

        elif event == 'Close' and sg.popup_yes_no('Do you really want to exit?', title=' ') == 'Yes':      
                
            lines = list()

            password = values['-D-']

            window.refresh()

            with open(csv_filename, 'r', newline='') as readFile:
                reader = csv.reader(readFile)

                for row in reader:
                    if row:
                        lines.append(row)

                    for field in row:
                        if field == password:
                            lines.remove(row)
                        
            with open(csv_filename, 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                for row in lines:
                    writer.writerow(row)
                writeFile.close()
            

            break 

    window.close()
