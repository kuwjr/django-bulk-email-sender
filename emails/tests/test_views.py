import imp
from django.test import TestCase, Client
from django.urls import reverse
from emails.models import BulkEmail
from django.contrib.auth.models import User

class TestViews(TestCase):

    # view a single email
    def test_viewSingleBulkEmail_get(self):
        c = Client()
        response = c.get(reverse('single_email', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'emails/email_form.html')
    
    # create new email - get
    def test_createNewBulkEmail_get(self):
        c = Client()
        response = c.get(reverse('send_email'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'emails/email_form.html')

    # create new email - post
    def test_viewSingleBulkEmail_post(self):
        # create csv file
        test_csvFile = open('test-emails.csv','r')

        # create client user and login
        c = Client()
        test_user = User.objects.create_user(username='testusername', email='testemail@email.com', password='testpassword')
        c.login(username='testusername', password='testpassword')

        # send post request using the nwly created user
        response = c.post(reverse('send_email'), {
            'title': 'Test Title 01',
            'subject': 'Test Subject 01',
            'content': 'Test Content 01',
            'file': test_csvFile,
        })
        # check if redirected on success
        self.assertEquals(response.status_code, 302)

        # check if BulkEmail object was created by the logged in user
        self.assertEquals(BulkEmail.objects.first().user_id, test_user.id)