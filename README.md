# Room Reservation System

## Department of Computer Science Room Reservation System

### How to Create A New User in RRS (temporarily)    
1.  Go the directory of the project through the terminal.
2.  Type `python manage.py shell` to enter the Django shell.
3.  Type `from login.models import CustomUser` to import the `CustomUser` class defined in a model.
4.  Then, type `CustomUser.objects.create_user(username=yourusername, password=yourpassword, emailadd=youremail@address, user_privileges=[1(for superadmin), 2(for admin), 3(for faculty), 4(for student)])`    
       
Now you can login to the site with the user you created.
