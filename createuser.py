from login.models import CustomUser
from django.conf import settings

username = raw_input("Username: ")
password = raw_input("Password: ")
emailadd = raw_input("Email Address: ")
user_privileges = raw_input("User Privileges[1 for Super Admin, 2 for Admin, 3 for Faculty, 4 for Student]: ")

def create_user(self, username, password, emailadd, user_privileges):
    	if not username: # Check if there is a user
            raise ValueError('User must have username')
        user = self.model(
            username = username,
            emailadd = CustomUserManager.normalize_email(emailadd), # Normalizes the email address
            user_privileges = user_privileges,
            is_staff = True,
            is_admin = True,
            is_superuser = False
            )
        user.set_password(password)
        user.save(using = self._db)
        return user

create_user(username = username, password = password, emailadd = emailadd, user_privileges = user_privileges)