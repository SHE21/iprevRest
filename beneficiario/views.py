from django.contrib.auth.models import Group
from .models import Beneficiario, Documento, Contato, Solicitacao
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, BeneficiarioSerializer, ContatoSerializer, SolicitacaoSerializer, DocumentoSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = Beneficiario.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permissions_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permissions_classes = [permissions.IsAuthenticated]


class SolicitacaoViewSet(viewsets.ModelViewSet):
	queryset = Solicitacao.objects.all()
	serializer_class = SolicitacaoSerializer


class BeneficiarioViewSet(viewsets.ModelViewSet):
	queryset = Beneficiario.objects.all()
	serializer_class = BeneficiarioSerializer
	#permissions_classes = [permissions.IsAuthenticated]


	def list(self, request):
		queryset = self.get_queryset()
		serializer = BeneficiarioSerializer(queryset, many=True)
		return Response(serializer.data)
