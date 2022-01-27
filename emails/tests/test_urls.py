from django.test import SimpleTestCase
from django.urls import reverse, resolve
from emails.views import createNewBulkEmail, viewSingleBulkEmail

class TestUrls(SimpleTestCase):

    # test methods
    def test_createNewBulkEmail_resolves(self):
        url = reverse('send_email')
        self.assertEquals(resolve(url).func, createNewBulkEmail)

    def test_viewSingleBulkEmail_resolves(self):
        url = reverse('single_email', args=[1])
        self.assertEquals(resolve(url).func, viewSingleBulkEmail)