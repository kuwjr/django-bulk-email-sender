import csv
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# method to handle uploaded csv file
def get_emails_from_csv(f):
    # create csv file in server (will be replaced by next csv file)
    with open('media/uploads/emails.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    # loop through generated file and search for emails
    with open('media/uploads/emails.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        # create list to save emails
        allEmails = list()
        for row in csv_reader:
            # print("ROW: ", row)
            for cell in row:
                # validate email and save all emails to variable
                try:
                    validate_email(cell)
                    # save valid emails to the list
                    allEmails.append(cell)
                except ValidationError as e:
                    continue
        return allEmails