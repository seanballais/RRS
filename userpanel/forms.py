from django import forms
from userpanel.models import Room, Equipment, ReserveInfo, UseInfo

class ReserveInfoForm(forms.ModelForm):

	class Meta:
		model = ReserveInfo
		fields = '__all__'

class UseInfoForm(forms.ModelForm):

	class Meta:
		model = UseInfo
		fields = '__all__'