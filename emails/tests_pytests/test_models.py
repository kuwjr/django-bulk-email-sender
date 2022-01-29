from emails.models import BulkEmail
from django.contrib.auth.models import User
import pytest

pytestmark = pytest.mark.django_db

@pytest.fixture
def setUp():
    # create user
    user1 = User.objects.create_user(
        username='testusername',
        email='testemail@email.com',
        password='testpassword',
    )

    # create BulkEmail
    be1 = BulkEmail.objects.create(
        user=user1,
        title="TEST TITLE",
        subject="TEST SUBJECT",
        content="TEST CONTENT",
        recipients=['kuwjr@outlook.com'],
        activated=False,
    )

    yield user1, be1

# check if user is created
def test_if_user_created(setUp):
    assert User.objects.first().username == setUp[0].username

# check if BulkEmail is created
def test_if_user_created(setUp):
    assert BulkEmail.objects.first().title == setUp[1].title

# couldn't think of anything else to test