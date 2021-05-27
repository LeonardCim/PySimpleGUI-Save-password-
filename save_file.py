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