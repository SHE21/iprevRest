from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Beneficiario, Solicitacao, Endereco, Contato, Documento, Cargo


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']


class ContatoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Contato
		fields = [
		'telefone',
		'celular',
		'email'
		]


class EnderecoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Endereco
		fields = [
		'cidade',
		'numero',
		'rua',
		'bairro',
		'cep'
		]


class CargoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cargo
		fields = '__all__'


class DocumentoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Documento
		fields = [
			#'beneficiario',
			'filePath',
			'fileNome',
			'categoria',
			'formato'
		]


class SolicitacaoSerializer(serializers.ModelSerializer):
	documento = DocumentoSerializer(required=True, many=True)

	class Meta:
		model = Solicitacao
		fields = [
		'tipoSolicitacao',
		'documento',
		'data',
		'status',
		'deferida'
		]

	def create(self, validated_data):
		documentos_data = validated_data.pop('documento')
		solicitacao = Solicitacao.objects.create(**validated_data)

		for documento_data in documentos_data:
			Documento.objects.create()

class BeneficiarioSerializer(serializers.ModelSerializer):

	documento = DocumentoSerializer(required=True, many=True)
	endereco = EnderecoSerializer(required=True)
	contato = ContatoSerializer(required=True)
	#solicitacao = SolicitacaoSerializer(required=False, many=True)

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
			#'solicitacao'
		]
		read_only_fields = ('nome',)

	def create(self, validated_data):
		documentos_data = validated_data.pop('documento')
		endereco_data = validated_data.pop('endereco')
		contato_data = validated_data.pop('contato')

		validated_data['foto'] = "teste"
		beneficiario = Beneficiario.objects.create(**validated_data)
		Endereco.objects.create(beneficiario=beneficiario, **endereco_data)
		Contato.objects.create(beneficiario=beneficiario, **contato_data)

		for documento_data in documentos_data:
			Documento.objects.create(beneficiario=beneficiario, **documento_data)

		return beneficiario

class UserSerializer(serializers.ModelSerializer):
	documento = DocumentoSerializer(required=True, many=True)

	class Meta:
		model = Beneficiario
		fields = [
			'username',
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
			'foto',
			'documento'
		]