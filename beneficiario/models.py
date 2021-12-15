from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Created by Santiago, L.C

class UserManage(BaseUserManager):
	user_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('Email obrigatorio!')
		email = self.normalize_email(email)
		user = self.model(email=email, username=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user


	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)


	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Super user precisa ser is_staff=True')

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Staff precisa ser is_staff=True')

		return self._create_user(email, password, **extra_fields)


class Beneficiario(AbstractUser):
	"""
	Um beneficiario só pode ter um Contato;
	"""
	email = models.EmailField('E-mail', unique=True)
	nome = models.CharField('Nome', max_length=50)
	genero = models.CharField('Genero', max_length=10)
	cpf = models.CharField('CPF', max_length=50, unique=True)
	rg = models.CharField('RG', max_length=50)
	cnh = models.CharField('CNH', max_length=50)
	pis_pasep = models.CharField('PIS/PASEP', max_length=100)
	dataNascimento = models.DateField('Data de Nascimento', blank=True, null=True)
	eleitorNumero = models.CharField('Número de eleitor', max_length=50)
	nomeMae = models.CharField('Nome da Mãe', max_length=100)
	nomePai = models.CharField('Nome do Pai', max_length=100)
	naturalidade = models.CharField('Naturalidade', max_length=100)
	cargo = models.CharField('Cargo', max_length=100)
	foto = models.ImageField(upload_to='user_foto', max_length=100)
	is_staff = models.BooleanField('Membro', default=True)

	class Meta:
		verbose_name = 'Beneficiário'
		verbose_name_plural = 'Beneficiários'

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [
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
	]

	def __str__(self):
		return self.nome

	objects = UserManage()


class Endereco(models.Model):
	beneficiario = models.OneToOneField(Beneficiario, related_name='endereco', on_delete=models.CASCADE)
	cidade = models.CharField('Cidade', max_length=100)
	numero = models.CharField('Número', max_length=10)
	rua = models.CharField('Rua/Avenida', max_length=100)
	bairro = models.CharField('Bairro', max_length=80)
	cep = models.CharField('CEP', max_length=15)

	class Meta:
		verbose_name = 'Endereço'


class Contato(models.Model):
	beneficiario = models.OneToOneField(Beneficiario, related_name='contato', on_delete=models.CASCADE)
	telefone = models.CharField('Telefone', max_length=50)
	celular = models.CharField('Celular', max_length=50)

	class Meta:
		verbose_name = 'Contato'
		verbose_name_plural = 'Contatos'

	def __str__(self):
		return self.email


class Cargo(models.Model):
	orgao = models.CharField('Orgão', max_length=50)
	nome = models.CharField('Nome do Cargo/Profissão', max_length=80)
	matricula = models.CharField('Matrícula', max_length=80)
	lotacao = models.CharField('Lotação/Setor', max_length=100)

	class Mata:
		verbose_name = 'Lotaçao'

	def __str__(self):
		return self.nome


class Documento(models.Model):
	beneficiario = models.ForeignKey(Beneficiario,related_name='documento', on_delete=models.CASCADE)
	filePath = models.CharField('Path', max_length=100)
	fileNome = models.CharField('Nome Documento', max_length=100)
	categoria = models.CharField('Categoria/Tipo', max_length=80)
	formato = models.CharField('Formato', max_length=10)

	class Meta:
		verbose_name = 'Documento'
		verbose_name_plural = 'Documentos'

	def __str__(self):
		return self.filePath


class Solicitacao(models.Model):
	beneficiario = models.OneToOneField(Beneficiario, related_name='solicitacao', on_delete=models.CASCADE)
	tipoSolicitacao = models.CharField('Tipo de Solicitação', max_length=120)
	documento = models.ForeignKey(Documento, on_delete=models.CASCADE)
	data = models.DateTimeField()
	status = models.BooleanField(default=True)
	deferida = models.BooleanField(default=False)

	class Meta:
		verbose_name = 'Solicitação'
		verbose_name_plural = 'Solicitações'

	def __str__(self):
		return self.tipoSolicitacao