from django.urls import reverse, resolve
from emails.views import createNewBulkEmail, viewSingleBulkEmail

def test_createNewBulkEmail_resolves():
    url = reverse('send_email')
    assert resolve(url).func == createNewBulkEmail, "Issue with createNewBulk email URL"

def test_viewSingleBulkEmail_resolves():
    url = reverse('single_email', args=[1])
    assert resolve(url).func == viewSingleBulkEmail, "Issue with createNewBulk email URL"