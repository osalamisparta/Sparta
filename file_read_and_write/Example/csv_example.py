import csv

def open_csv(csv_filename):
    try:
        csvfile = open(csv_filename, newline='')
        return csvfile

    except FileNotFoundError:
        print('File not found')
        #raise


def transform_user_details(csv_file_name):
    new_user_data = []
    csvfile = open_csv(csv_file_name)
    user_details = csv.reader(csvfile, delimiter=',')
    for user in user_details:
        transform=[]
        transform.append(user[1])
        transform.append(user[2])
        transform.append(user[-1])
        new_user_data.append(transform)
    csvfile.close()
    return new_user_data

def create_new_csv(old_data, new_file_name):
    new_user_data = transform_user_details(old_data)
    with open(new_file_name,'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_csv('user_details.csv','new_user_file.csv')