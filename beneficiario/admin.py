from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import BeneficiarioCreateForm, BeneficiarioChangeForm
from .models import Beneficiario

# Register your models here.
@admin.register(Beneficiario)
class BeneficiarioAdmin(UserAdmin):
	add_form = BeneficiarioCreateForm
	form = BeneficiarioChangeForm
	model = Beneficiario

	list_display = (
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
			'foto',
			'is_staff'
			)

	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Informações Pessoais', {'fields': ('nome', 'genero', 'cpf', 'rg', 'cnh', 'pis_pasep', 'dataNascimento', 'eleitorNumero', 'nomeMae', 'nomePai', 'naturalidade', 'cargo', 'foto')}),
		('Permissoes', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Datas', {'fields': ('last_login', 'date_joined')}),
	)