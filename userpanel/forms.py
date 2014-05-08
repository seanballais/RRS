from django import forms
from userpanel.models import Room, Equipment, ReserveInfo

class ReserveInfoForm(forms.ModelForm):

	class Meta:
		model = ReserveInfo
		fields = '__all__'