import PySimpleGUI as sg
from typing import Text
import pandas as pd



def table_passwordApp():
    '''Function that shows passwords and apps in a table'''

    sg.set_options(auto_size_buttons=True)
    csv_filename = r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv'

    data = []
    header_list = []

    df = pd.read_csv(csv_filename, sep=',', engine='python', header=None)
    data = df.values.tolist()               
                    
    header_list = df.iloc[0].tolist()
    data = df[1:].values.tolist()

    layout = [
        [sg.Text('Your password and apps', pad=((15, 0), (10, 10)))],
        [sg.Table(values=data,
                  justification='left',
                  key='_TABLE_',
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=True,
                  num_rows=min(100, len(data)), pad=((15, 0), (10, 0)))]
    ]

    window = sg.Window(resizable=True,
        title="Password and app table",
        layout=layout,
        margins=(1, 1),
        size=(500, 170),
        finalize=True
    )

    window['_TABLE_'].expand(True, True)
    window['_TABLE_'].table_frame.pack(expand=True, fill='both')

    while True:
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Exit'):
            window.refresh()
            break
    
    window.close()
