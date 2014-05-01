from django import forms

import sqlite3

class LoginForm(forms.Form):
	# Login form widgets that will be used
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput())

	# Check if username entered is in the database and matches the password
	def authenticate_form(self):
		conn = sqlite3.connect('rrs.db')
		cursor = conn.cursor()

		# Retrieve the username
		
		exec_sql = "SELECT username FROM login_userprofile WHERE username = '" + username + "'"
		cursor.execute(exec_sql)
		usernameVal = cursor.fetchone()
		if usernameVal:
			usernameVal = "%s" % (usernameVal[0]) # Let's use usernameVal later for comparison

		# Retrieve the password

		exec_sql = "SELECT password FROM login_userprofile WHERE username = '" + password + "'"
		cursor.execute(exec_sql)
		passwordVal = cursor.fetchone()
		if passwordVal:
			passwordVal = "%s" % (passwordVal[0]) # Let's user passwordVal later for comparison

		""" if username == usernameVal:
			if password == passwordVal:
				# Add redirect code to User Panel

		else:
			# Add redirect code to self

			Ray Mart and kuya Dioc, edit this part and I'll continue the template.
		""" 