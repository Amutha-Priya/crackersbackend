from rest_framework import serializers
from .models import *

class ProducttableSerializer(serializers.ModelSerializer):
        class Meta:
            model = Producttable
            fields = '__all__'