from ast import Not
from django.shortcuts import redirect, render
import os.path
from . import models
from .forms import SendEmailForm
from .my_own_utils.handle_csv_file import get_emails_from_csv
from .my_own_utils.send_emails import sendEmails
from django.contrib import messages, auth
from .models import BulkEmail

def createNewBulkEmail(request):
    context = {
        'form': SendEmailForm()
    }
    if request.method == 'POST':
        # process form
        form = SendEmailForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # get form data
            title = form.cleaned_data['title'] 
            subject = form.cleaned_data['subject'] 
            content = form.cleaned_data['content'] 
            file = form.cleaned_data['file']
            
            # check if extension is .csv
            extension = os.path.splitext(file.name)[1]
            if extension != '.csv':
                messages.error(request, 'File is not a CSV file!')
                return render(request, "emails/email_form.html", context)
            
            # check if emails are valid
            allEmails = get_emails_from_csv(request.FILES['file'])
            if len(allEmails) is 0:
                messages.error(request, 'No valid emails in CSV file!')
                return render(request, "emails/email_form.html", context)

            # create BulkEmail object
            be = BulkEmail.objects.create(user=request.user, title=title, subject=subject, content=content, recipients=allEmails, activated=False)
            
            # send emails
            res = sendEmails(be)
            if res is not True:
                messages.error(request, 'There was an error while sending emails!')
                return render(request, "emails/email_form.html", context)

            # everything is successfull
            be.save()
            messages.success(request, 'All emails were sent successfully!')
        else:
            messages.error(request, 'Form is not valid!')
            return render(request, "emails/email_form.html", context)
        return redirect('send_email')
    else:
        return render(request, "emails/email_form.html", context)

def viewSingleBulkEmail(request, id):
    sent_email = models.BulkEmail.objects.get(id=id, user_id=request.user.id)
    context = {
        'sent_email': sent_email
    }
    return render(request, "emails/email_form.html", context)