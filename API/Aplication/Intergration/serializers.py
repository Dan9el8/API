# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import UseModel
 
# Create a model serializer
class UseSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = UseModel
        fields = ('client_ip', 'location', 'greetings')