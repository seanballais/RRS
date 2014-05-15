Room Reservation System
===

Department of Computer Science Room Reservation System

How to Create A New User in RRS (temporarily)
1. Go the directory of the project through the terminal.
2. Type 'python manage.py shell' to enter the Django shell.
3. Type 'from login.models import CustomUser' to import the CustomUser class defined in a model
4. Then, type 'CustomUser.objects.create_user(username = username, password = password, emailadd = emailadd, user_privileges = user_privileges)'
Replace the second username with a username in quotations, password with a different password with quotations, emailadd with an email address with quotations, and user privileges with a number from 1 to 4. 1 for super admin, 2 for admin, 3 for faculty, and 4 for student.

Now you can login to the site with the user you created.