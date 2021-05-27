import password_creator as pc
import csv 


signal_list = ['-------->']
totalitems = zip(pc.pass_list, signal_list, pc.app_list)

def insert():
    '''Function to insert the password and the app inside the csv file'''

    with open(r'C:\Users\Utente\Desktop\Save password\Your_password_file.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        for row in totalitems:
            writer.writerow(row)
        csv_file.close()