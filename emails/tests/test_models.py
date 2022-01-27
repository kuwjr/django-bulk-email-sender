from turtle import title
from django.test import TestCase, Client
from emails.models import BulkEmail
from django.contrib.auth.models import User

class TestModls(TestCase):
    def setUp(self):
        # create user
        self.user1 = User.objects.create_user(
            username='testusername', 
            email='testemail@email.com', 
            password='testpassword',
        )

        # create BulkEmail
        self.be1 = BulkEmail.objects.create(
            user=self.user1,
            title="TEST TITLE",
            subject="TEST SUBJECT",
            content="TEST CONTENT",
            recipients=['kuwjr@outlook.com'],
            activated=False,
        )
    

    # check if user is created
    def test_if_user_created(self):
        self.assertEquals(User.objects.first().username, 'testusername')

    # check if BulkEmail is created
    def test_if_user_created(self):
        self.assertEquals(BulkEmail.objects.first().title, 'TEST TITLE')
    
    # couldn't think of anything else to test