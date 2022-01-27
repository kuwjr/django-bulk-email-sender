from django.test import SimpleTestCase
from emails.forms import SendEmailForm
from django.core.files.uploadedfile import SimpleUploadedFile

class TestForms(SimpleTestCase):

    def test_SendEmailForm(self):
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

        self.assertTrue(form.is_valid())