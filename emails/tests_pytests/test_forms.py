from emails.forms import SendEmailForm
from django.core.files.uploadedfile import SimpleUploadedFile
import pytest


@pytest.mark.django_db
def test_SendEmailForm():
    form = SendEmailForm(
        data={
            'title': 'TEST',
            'subject': 'TEST',
            'content': 'TEST',
        },
        files={
            'file': SimpleUploadedFile(name='test-emails.csv', content=b'kuwjr@outlook.com,a@a.lk', content_type='text/csv')
        }
    )

    assert form.is_valid() == True, "Form validation failed!"