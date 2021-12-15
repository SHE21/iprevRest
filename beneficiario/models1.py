from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Beneficiario, Solicitacao, Endereco, Contato, Documento, Cargo


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']


class ContatoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contato
		fields = '__all__'


class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Endereco
		fields = '__all__'


class DocumentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Documento
		fields = '__all__'

class SolicitacaoSerializer(serializers.HyperlinkedModelSerializer):
	documento = DocumentoSerializer()
	class Meta:
		model = Solicitacao
		fields = '__all__'


class CargoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cargo
		fields = '__all__'


class BeneficiarioSerializer(serializers.HyperlinkedModelSerializer):
	contato = ContatoSerializer()
	endereco = EnderecoSerializer()
	documento = DocumentoSerializer()
	solicitacao = SolicitacaoSerializer()
	cargo = CargoSerializer()

	class Meta:
		model = Beneficiario
		fields = [
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
		'endereco',
		'contato',
		'documento',
		'foto',
		'solicitacao']
