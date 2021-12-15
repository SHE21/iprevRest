from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Beneficiario, Documento

class BeneficiarioCreateForm(UserCreationForm):

	class Meta:
		model = Beneficiario
		fields = (
			'email',
			'password',
			'nome',
			'genero',
			'cpf',
			'rg',
			'cnh',
			'pis_pasep',
			'dataNascimento',
			'eleitorNumero',
			'nomeMae',
			'nomePai',
			'naturalidade',
			'cargo',
			'foto'
		)
		labels = {'username': 'Username/Email'}

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data["username"]

		if commit:
			user.save()
		return user


class BeneficiarioChangeForm(UserChangeForm):
	class Meta:
		model = Beneficiario
		fields = (
			'email',
			'nome', 
			'genero', 
			'cpf', 
			'rg', 
			'cnh', 
			'pis_pasep', 
			'dataNascimento', 
			'eleitorNumero', 
			'nomeMae',
			'nomePai',
			'naturalidade',
			'cargo',
			'foto'
		)