from django.contrib.auth.models import (UserManager, AbstractUser)

# UserManager class code here
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name', 'email']

    objects=UserManager()
    def __str__(self):
        return self.email

  