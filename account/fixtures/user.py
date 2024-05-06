import pytest
from account.models import CustomUser

user_data={
            "email":"fagbemi65@gmail.com",
            "first_name":"fagbemi",
            "last_name":"Joseph",
            "password":"test"
        }

@pytest.fixture
def user():
    user=CustomUser.objects.create(**user_data)
    user.set_password(user_data['password'])
    user.save()
    return user