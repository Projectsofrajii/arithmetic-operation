from rest_framework import serializers
from .models import Arithmetic

class Arithseri(serializers.ModelSerializer):
    class Meta:
        model = Arithmetic
        fields = ['add','sub','mul','div']