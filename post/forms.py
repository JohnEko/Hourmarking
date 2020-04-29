from django import forms
from .models import Userhour


class Userform(forms.ModelForm):
	class Meta:
		model = Userhour
		fields = [
				"first_name",
				"last_name",
				"email",
				"userId",
				"workTargetId",
				"phoneNumber"

		]




