from django.test import Client
from django.urls import reverse
import pytest
from emails.models import BulkEmail
from django.contrib.auth.models import User

@pytest.fixture
def client():
    yield Client()

# view a single email
def test_viewSingleBulkEmail_get(client):
    response = client.get(reverse('single_email', args=[1]))
    assert response.status_code == 200, "Response failed!"

# create new email - get

def test_createNewBulkEmail_get(client):
    response = client.get(reverse('send_email'))
    assert response.status_code == 200, "Response failed!"

# create new email - post
@pytest.mark.django_db
def test_viewSingleBulkEmail_post(client):

    # create csv file
    test_csvFile = open('test-emails.csv','r')

    # create client user and login
    test_user = User.objects.create_user(username='testusername', email='testemail@email.com', password='testpassword')
    client.login(username='testusername', password='testpassword')

    # send post request using the nwly created user
    response = client.post(reverse('send_email'), {
        'title': 'Test Title 01',
        'subject': 'Test Subject 01',
        'content': 'Test Content 01',
        'file': test_csvFile,
    })
    # check if redirected on success
    assert response.status_code == 302, "Page didn't redirect!"

    # check if BulkEmail object was created by the logged in user
    assert BulkEmail.objects.first().user_id == test_user.id, "BulkEmail object not created in db!"