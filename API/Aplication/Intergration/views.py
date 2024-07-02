# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import UseSerializer
from .models import UseModel

# create a viewset


class UseViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = UseModel.objects.all()

	# specify serializer to be used
	serializer_class = UseSerializer

